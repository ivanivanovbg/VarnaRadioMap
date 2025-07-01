from schemas.navroute import NavRoute
import os.path

def parse_route(route_file:bytes,route_file_name:str)->NavRoute|bool:
    route_file_text = route_file.decode("UTF-8")
    route_name,route_extension = os.path.splitext(route_file_name)

    match route_extension.lower():
        case '.csv':
            return NavRoute(route_file=route_file_text,route_type=0)
        case '.rt3':
            return NavRoute(route_file=route_file_text,route_type=3)
        case '.gpx':
            return NavRoute(route_file=route_file_text,route_type=2)
    return False