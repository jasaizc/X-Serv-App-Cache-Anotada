#!/usr/bin/python
import urllib


class proxyApp:
    
    def parse(self, request, rest):
        peticion = request.split()[1][1:]
        return peticion

    def process(self,parsedRequest):
        opener = urllib.FancyURLopener({})
        original = "http://" + parsedRequest
        f = opener.open(original)
        dev = f.read()
        pos1 = dev.find("<body");
        peticion1 = dev[pos1:]
        AntesDelBody = dev[:pos1]
        pos2 = peticion1.find(">");
        peticion2 = peticion1[pos2+1:]
        dev = dev[:(pos2+1+pos1)]
        peticion2 = "\n<div'><a href = '" + original + "' > Original </a> <a href = '"+ "http://localhost:1234/" + parsedRequest +"'> Recargar</a><a href = '#'> Server-side HTTP </a><a href = '#'> Client-side HTTP</a></div>" + peticion2;
        peticiones = dev + peticion2
        peticiones = ("200 OK", peticiones);          
        return (peticiones)







