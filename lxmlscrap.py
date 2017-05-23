from lxml import html
import requests
import json

trg = requests.get('http://publicinfobanjir.water.gov.my/View/OnlineFloodInfo/PublicWaterLevel.aspx?scode=TRG')
tree = html.fromstring(trg.content)
stations = tree.xpath('//span[starts-with(@id, "ContentPlaceHolder1_grdStation_lbl_StationName_")]/text()')
district = tree.xpath('//a[starts-with(@id, "ContentPlaceHolder1_grdStation_lbl_District_")]/text()')
basin = tree.xpath('//span[starts-with(@id, "ContentPlaceHolder1_grdStation_lbl_basin_")]/text()')
latest_update = tree.xpath('//span[starts-with(@id, "ContentPlaceHolder1_grdStation_lbl_LastUpdate_")]/text()')
water_level = tree.xpath('//span[starts-with(@id, "ContentPlaceHolder1_grdStation_DailyRainFall_1_")]/text()')

info = [{'station': stations, 'district': district, 'basin': basin, 'latest_update': latest_update, 'water_level': water_level} for stations, district, basin, latest_update, water_level in zip(stations, district, basin, latest_update, water_level)]

with open('infobanjir.json', 'w') as outfile:
    json.dump(info, outfile, indent=4)
