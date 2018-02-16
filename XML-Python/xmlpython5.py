from lxml import etree
doc = etree.parse('provinciasypoblaciones.xml')

provincias = doc.findall("provincia")
municipiobuscar = input("Dime un municipio a buscar: ")

for provincia in provincias:
	nombre = provincia.find("nombre")
	localidades = provincia.findall("localidades/localidad")
	for localidad in localidades:
		if localidad.text == municipiobuscar:
			print(localidad.text, nombre.text)
