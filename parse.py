from lxml import etree
xml = open("food.xml", "rb").read()
# xmlio = BytesIO(xml)
tree = etree.parse(xml)
etree.tostring(tree)

# tree = etree.XMLParser(xml)
# tree = etree.parse(xml)
tree = etree.fromstring(xml)
tree = etree.parse(xml)

# print(tree)
# print(type(tree))

# for element in tree.iter():
    # print(f"{element.tag} - {element.text}")
