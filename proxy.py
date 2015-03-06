#!/usr/bin/python
import urllib
cache = {}
cabe = {}

class proxyApp:
    
    def parse(self, request, rest):
        peticion = request.split()[1][1:]
        cabeceras = request.split("\r\n")[1:]
        cabe[peticion] = cabeceras;
        return peticion

    def process(self,parsedRequest):
        try:
            argumentos = parsedRequest.split('/')
            print argumentos
            if argumentos[0] == 'cache':          
                peticiones = ("200 OK", cache[argumentos[1]])
            elif argumentos[0] == 'cabe':
                peticiones = ("200 OK", ("<html><body>" + str(cabe[argumentos[1]]) + "</body></html>"  + "\r\n"))
            else:
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
                peticion2 = "\n<div'><a href = '" + original + "' > Original </a> <a href = '"+ "http://localhost:1234/" + parsedRequest +"'> Recargar</a><a href = '""http://localhost:1234/cache/" +  argumentos[0]  +"'> Server-side HTTP </a><a a href = '""http://localhost:1234/cabe/" +  argumentos[0]  +"'> Client-side HTTP</a></div>" + peticion2;
                peticiones = dev + peticion2
                cache[argumentos[0]] = peticiones
                peticiones = ("200 OK", peticiones)
        except IOError:
                peticiones = ("404 ERROR NOT FOUND", ("<html><body>Error en la ruta</body></html>"  + "\r\n"))
        return (peticiones)







