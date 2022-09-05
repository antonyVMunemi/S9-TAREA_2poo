class menuncio:
    def init(self):
        pass
    def menuncio(self,opciones,titulo):
        print(titulo)
        for opcion in opciones:
            print(opcion)
        opci = input("Escoja la opcion[1...{}]: ".format(len(opciones)))
        return opci
