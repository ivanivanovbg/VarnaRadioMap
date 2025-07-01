from pydantic import BaseModel,model_validator,Field
from typing import Annotated,List,Tuple
from enum import Enum
from utilities.totem_parser import parse_totem_file
from utilities.transas_parser import parse_transas_file
from utilities.gpx_parser import parse_gpx_file

class RouteType(int,Enum):
    CSV = 0
    TXT = 1
    GPX = 2
    RT3 = 3

class NavRoute(BaseModel):
    coordinates: Annotated[List[Tuple[float, float,str]], Field(default_factory=list)]
    route_file:Annotated[str,Field()]
    route_type:Annotated[RouteType,Field()]

    @model_validator(mode='after')
    def parse_rote_file(self):
        match self.route_type:
            case 0:
                totem_result = parse_totem_file(route_file=self.route_file)
                if totem_result:
                    self.coordinates = totem_result
                    return self

            case 2:
                gpx_result = parse_gpx_file(route_file=self.route_file)
                if gpx_result:
                    self.coordinates = gpx_result
                    return self

            case 3:
                transas_result = parse_transas_file(route_file=self.route_file)
                if transas_result:
                    self.coordinates = transas_result
                    return self

        return self
