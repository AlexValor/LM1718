from lxml import etree
doc = etree.parse('provinciasypoblaciones.xml')

provincias = doc.findall("provincia")

for provincia in provincias:
	nombre = provincia.find("nombre")
	municipios = provincia.findall("localidades/localidad")
	print(nombre.text, len(municipios))