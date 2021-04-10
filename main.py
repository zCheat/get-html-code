import requests

#descarga
web = input ("pagina: ")
peticion = requests.get(web)
html = peticion.text
#crear archivo
pagina = open('index.html', w)
pagina.write(html)
pagina.close()
print ("pagina descargada")
