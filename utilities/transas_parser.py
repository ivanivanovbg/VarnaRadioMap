import re

def parse_transas_file(route_file:str):
    line_regex = r"<WayPoint[^>]*WPName=\"(.*?)\".*Lat=\"([-]?\d+(?:\.\d+)?)\"\s*Lon=\"([-]?\d+(?:\.\d+)?)\""
    line_matches = re.findall(line_regex,route_file,re.MULTILINE)
    return_list = [(float(x[1])/60,float(x[2])/60,x[0]) for x in line_matches]
    if not return_list:
        return False
    return return_list
