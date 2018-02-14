from lxml import etree
doc = etree.parse('provinciasypoblaciones.xml')

# 2)Programa que lista todos los municipios
raiz=doc.getroot()
municipios=doc.findall("provincia/localidades/localidad")	
for localidad in municipios:
	print(localidad.text)