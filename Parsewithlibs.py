import json
from dicttoxml import dicttoxml
import xml.dom.minidom
from xml.dom.minidom import parseString


sfile = None
saddress = 'rasp.json'
text = None


def load_file(address):
    global sfile
    sfile = open(address, 'r')


load_file(saddress)
text = sfile.read(2000)

dict = json.loads(text)

print(dict)
xml = dicttoxml(dict, attr_type=False, root=False)

from xml.dom.minidom import parseString
dom = parseString(xml)
print(dom.toprettyxml())

f = open('rasp3.xml', 'w')
f.write(dom.toprettyxml())
f.close()
