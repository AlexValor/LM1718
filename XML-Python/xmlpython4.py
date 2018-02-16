from lxml import etree
doc = etree.parse('provinciasypoblaciones.xml')

provincias = doc.findall("provincia")
provinciabuscar = input("Dime una provincia a buscar: ")

for provincia in provincias:
	nombre = provincia.find("nombre")
	if nombre.text == provinciabuscar:
		municipios = provincia.findall("localidades/localidad")
		for localidad in municipios:
			print(localidad.text)