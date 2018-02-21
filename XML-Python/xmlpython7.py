from lxml import etree
doc = etree.parse('provinciasypoblaciones.xml')

provincias = doc.findall("provincia")
provinciabuscar = input("Dime una provincia a buscar: ")
	
for provincia in provincias:
	nombre = provincia.find("nombre")
	if nombre.text == provinciabuscar:
		for localidades in provincia.findall("localidades/localidad"):
			if localidades.attrib["c"]=="1":
				print(localidad.text)
			else:
				print("No existe la provincia")	
