from lxml import etree
xml = open("food.xml", "rb").read()

# tree = etree.parse(xml)
# tree = etree.fromstring(xml)
tree = etree.parse(xml)

print(tree)
print(type(tree))