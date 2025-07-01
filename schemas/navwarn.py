import re
from pydantic import BaseModel,model_validator,Field
from typing import List,Tuple,Annotated
from enum import Enum

class WarningType(str,Enum):
    GENERAL = "General"
    POINT = "Point"
    LINE = "Line"
    POLYGON = "Polygon"

class NavWarning(BaseModel):
    full_text:Annotated[str,Field()]
    coordinates:Annotated[List[Tuple[float,float]],Field(default_factory=list)]
    warning_type:Annotated[WarningType,Field(default_factory=str)]

    @staticmethod
    def clean_up_args(*args):
        return [a.replace(",", ".") if isinstance(a, str) else a for a in args]

    @staticmethod
    def parse_lat_long(degrees_lat:str,minutes_lat:str,sign_lat:str,degrees_lon:str,minutes_lon:str,sign_lon:str):
        if sign_lat == "N":
            yield float(degrees_lat) + (float(minutes_lat)/60)
        else:
            yield 0 - (float(degrees_lat) + (float(minutes_lat)/60))
        if sign_lon == "E" or sign_lon =="Е":
            yield float(degrees_lon) + (float(minutes_lon)/60)
        else:
            yield 0- (float(degrees_lon) + (float(minutes_lon)/60))

    @model_validator(mode="after")
    def populate_coordinates(self):
        coordinates_re = r"(\d+)\s?(\d*[,.]*\d*)\s?([NS])\s*(\d+)\s?(\d*[,.]*\d*)\s?([EWЕ])"
        coordinates_matches = re.findall(coordinates_re, self.full_text)

        coords = []
        area_sum = 0

        for i, match in enumerate(coordinates_matches):
            parsed = self.parse_lat_long(*self.clean_up_args(*match))
            coord = (next(parsed), next(parsed))

            if not coords or coords[-1] != coord:
                coords.append(coord)

            if i > 0:
                area_sum += (coords[i][0] - coords[i - 1][0]) * (coords[i][1] + coords[i - 1][1])

        self.coordinates = coords

        match len(coords):
            case 0:
                self.warning_type = WarningType.GENERAL
            case 1:
                self.warning_type = WarningType.POINT
            case 2:
                self.warning_type = WarningType.LINE
            case _:
                self.warning_type = WarningType.POLYGON
                if coords[0] != coords[-1]:
                    self.coordinates.append(coords[0])
                if area_sum < 0:
                    self.coordinates.reverse()
        return self
