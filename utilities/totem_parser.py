import re

def parse_totem_file(route_file:str):
    line_regex = r"^\d+,([^,]*),(\d+[.]?\d*),(\d+[.]?\d*).*"
    line_matches = re.findall(line_regex,route_file,re.MULTILINE)
    return_list = [(float(x[1]),float(x[2]),x[0]) for x in line_matches]
    if not return_list:
        return False
    return return_list