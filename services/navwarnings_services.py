from schemas.navwarn import NavWarning
from typing import List
import requests
import re
from bs4 import BeautifulSoup
import os

async def get_all_warnings_service()->List[NavWarning]|None:
    wx_nav_request = requests.get("https://vtmis.bg/wx/wx_eng.htm")
    if wx_nav_request.status_code == 200:
        wx_nav_html = wx_nav_request.content
        bs_parser = BeautifulSoup(wx_nav_html,"lxml")
        wx_nav_body = bs_parser.find("div")
        if wx_nav_body:
            nav_warnings = []
            wx_nav_text = wx_nav_body.get_text(separator=os.linesep,strip=True).replace("\xa0"," ")
            nav_re_block = r"NAVWARN \d+/\d+.*?(?=NAVWARN|\Z)"
            nav_matches = re.findall(nav_re_block,wx_nav_text,re.DOTALL)
            for nav_match in nav_matches:
                nav_warnings.append(NavWarning(full_text=nav_match))
            return nav_warnings
        else:
            return None