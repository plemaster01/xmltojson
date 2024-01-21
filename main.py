# Convert XML Data to JSON with Python!
from pprint import pprint

import xmltodict
import json

with open("file.xml") as xml_file:
    data_dict = xmltodict.parse(xml_file.read())

json_data = json.dumps(data_dict)

with open("data.json", "w") as json_file:
    json_file.write(json_data)
    pprint(json_data)

"""import xml.etree.ElementTree as E
tree = E.parse('file.xml')
root = tree.getroot()
dic = {}
for child in root:
    if child.tag not in dic:
        dic[child.tag] = [child.text]

pprint(dic)"""