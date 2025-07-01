import re

def parse_gpx_file(route_file:str):
    line_regex = r"<(?:wpt|rtept)[^>]*lat=\"([-]?\d+(?:\.\d+)?)\"\s*lon=\"([-]?\d+(?:\.\d+)?)\""
    line_matches = re.findall(line_regex,route_file,re.MULTILINE)
    return_list = [(float(x[0]),float(x[1]),"") for x in line_matches]
    if not return_list:
        return False
    return return_list
