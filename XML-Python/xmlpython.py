from lxml import etree
doc = etree.parse('provinciasypoblaciones.xml')

# 1)Programa que lista todas las provincias
raiz=doc.getroot()
provincias=doc.findall("provincia/nombre")
for provincia in provincias:
	print (provincia.text)

#raiz=doc.getroot()
#for x in range(len(raiz)):
	#provincia = raiz[x]
	#print(provincia[0].text)


