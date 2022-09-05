from menu import menuncio
from modulosss import *

muestreo = menuncio()
listass = ["1) Saludo","2) Variable","3) Conversiones","4) Operaciones","5) Concatenacion","6) Cadenas",
           "7) Tuplas", "8) Listas", "9) Diccionario","10) Ingreso datos","11) Condicionales","12) Funciones",
           "13) Operadores logicos","14) Operador ternario","15) Funcion range","16) Bucle for","17) If con tuplas",
           "18) Factorial de un numero","19) Bucle While","20: Break, continue, pass","21) Generadores",
           "22) Generadores 2","23) Excepciones","24) Sentencia Raise","25) Modulos","26) POO","27) Constructores",
           "28) Encapsulamiento variable","29) Encapsulamiento metodos","30) Metodo accesores","31) Metodo __str__",
           "32) Herencia","33) Sobreescritura","34) Sustitucion","35) Herencia multiple","36) Polimorfosis",
           "37) Relaciones"]

opcion = ""
while opcion != "0":
    opcion = muestreo.menuncio(listass,"****** Menu de ejercicios ******")

    if opcion == "1":
        print("Hola Mundillo")

    elif opcion == "2":
        print("*** aprender a declarar variables ***")
        nombre = "Antony"
        print("Nombre:", nombre)
        Edad = 19
        print("Edad: ", Edad)
        Edad = True
        print("valor: ", Edad)
        sueldo = 90.50
        print("Sueldo: ",sueldo)

    elif opcion == "3":
        print("*** Hacer comversiones ***")

        numero1 = "24"
        numero2 = "10"
        print(numero1 + numero2)

        num1 = int(numero1)
        num2 = int(numero2)
        print(num1 + num2)

        sueldo = 1500.50
        enterosueldo = int(sueldo)
        print(enterosueldo)

        valor = "450.65"
        decivalor = float(valor)
        print(decivalor)
        print(decivalor * 3)

        edad = 101
        print(len(str(edad)))

    elif opcion == "4":
        print("*** Operaciones basicas ***")

        num1 = 15
        num2 = 5

        print("Suma: ", (num1+num2))
        print("Resta: ", (num1 - num2))
        print("Multiplicacion: ", (num1 * num2))
        print("Division: ", (num1 / num2))
        print("DivisionExacta: ", (num1 // num2))
        print("Potencia: ", (num1 ** num2))

    elif opcion == "5":
        print("FORMAS DE CONCATENAR")

        Tex1 = "HOLA"
        Tex2 = "MUNDO"
        Texfinal = Tex1 + " " + Tex2
        print(Texfinal)

        print("EL SALUDO ES: %s %s" % (Tex1, Tex2))

        saludofinal = "saludo: {0} {1}".format(Tex1, Tex2)
        print(saludofinal)

        saludofinal2 = "Saludo: {x} {y}".format(x=Tex1, y=Tex2)
        print(saludofinal2)

    elif opcion == "6":
        print("*** Opciones de Cadenas ***")
        textop = "bienvenido A doctop"

        print(textop)
        print(textop.lower())
        print(textop.upper())
        print(textop.title())

        print(textop.find("ven"))
        print(textop.count("e"))

        textofinal = textop.replace("i", "1")
        print(textofinal)

        valor = textop.isnumeric()
        print(valor)

        cadenaseparada = textop.split(" ")
        print(cadenaseparada)

    elif opcion == "7":
        print("*** Tuplas ***")

        tupla = (1, 2, 3)
        print(tupla)

        tupla2 = (7, "ANTONY", True, 125.25, 15 + 2j, 15, "conff ese tower", False)
        print(tupla2)

        tupla3 = (9, 3, (4, 5, 6))
        print(tupla3)

        print(tupla2[1])
        print(tupla2[-1])
        print(tupla2[0:4])
        print(tupla2[-2])

        a, g, v = tupla
        print(a)
        print(g)
        print(v)

        tuplafinal = tupla +tupla3
        print(tuplafinal)

        print(tuplafinal.count((3)))
        print(tuplafinal.index(3))

    elif opcion == "8":
        print("*** lista ***")
        lista1 = ["Antony", 19, 21.7, True, "Robert", 29.4]
        print(lista1)
        print(lista1[:])
        print(lista1[3])
        print(lista1[-1])

        print(lista1[0:3])
        print(lista1[:2])
        print(lista1[3:])

        lista1.append("ANDEXXUS")
        print(lista1)

        lista1.insert(4, "val?")
        print(lista1)

        lista1.extend(["carlitos", 21, False])
        print(lista1)
        print(lista1.index("ANDEXXUS"))

        lista1.remove(21)
        print(lista1)

        lista1.pop()
        print(lista1)

        lista2 = ["DUKI", "KNEKRO","XQC"]
        lista3 = lista1 + lista2
        print(lista3)

        print(lista2 * 2)

        print("ANDEXXUS" in lista1)

    elif opcion == "9":
        print("*** Diccionario ***")
        midic = {"Ecuador":"Quito", "Peru":"Lima", "Argentina":"la plata"}
        print(midic["Argentina"])
        print(midic)

        midic["Venezuela"] = "HAMBRE"
        print(midic)

        midic["Ecuador"] = "Guayas"
        print(midic)

        del midic["Venezuela"]
        print(midic)

        mi2dic = {"Vera":"Antony",19:True, "Sueldo":"Sin laburo"}
        print(mi2dic[19])

        llaves = ("Japon", "francia", "España")
        dicpaises = {llaves[0]:"OKINAWA", llaves[1]:"paris", llaves[2]:"Mostoles"}
        print(dicpaises)

        estudio =  {"NOM":"Antony","anios":{1:2019, 2:2020, 3:2021}}
        print(estudio)
        print(estudio["anios"])

        print(estudio.get("NOMe", "andexx"))


        print(estudio.keys())
        valores = list(estudio.values())
        print(valores)

    elif opcion == "10":
        print("*** Ingreso de datos ***")
        nombre = input("Ingrese su nombre: ")
        edad = int(input("Ingrese su edad: "))

        print("Hola, "+ nombre)
        edadfut = edad + 10
        print("Tu edad es: ", edad)
        print("Tu edad en 10 años sera: ", edadfut)

    elif opcion == "11":
        print("*** Condiciones ***")
        edad = int(input("Ingrese su edad: "))
        if edad > 18:
            print("Puedes beber")
        elif edad == 18:
            print("recien complidos capo")
        else:
            print("NO PODES TOMAR!!!!")

    elif opcion == "12":
        print("*** Funciones ***")
        def saludar():
            print("ANTONY")
            print("Vera")
            print("Andexxus")
            return "Hola"
        print(saludar())

        def evaluarsueld(sueldo):
            if sueldo >= 600:
                print("sueldo goty pa")
            else:
                print("te estan explotando mijo")

        evaluarsueld(750)

    elif opcion == "13":
        print("*** Operadores Logicos ***")
        distancia = 1500
        numHermanos = 2
        salaripapa = 1500
        tienebene = False
        if (distancia > 1000 and numHermanos > 1) or salaripapa < 2000:
            tienebene = True

        print(not tienebene)

        if (5 > 3) and (8 < 15):
            print("verdad")
        else:
            print("Falso")

    elif opcion == "14":
        print("*** operador ternario ***")
        sexos = ("Hombre","mujer")

        sexo = sexos[1]
        print(sexo)
        sexo = sexos[0]
        print(sexo)

        """
        posicion = True
        sexo = sexos[posicion]
        print(sexo)
        sexo = sexos[not posicion]
        print(sexo)
        """
    elif opcion == "15":
        print("*** Funcion Range ***")

        numeros = range(5)
        print(numeros[4])

        numer1 = range(4,10)
        print(numer1[5])

        numer2 = range(10,100,8)
        print(numer2[9])

    elif opcion == "16":
        print("*** Bucle for ***")

        """for num in range(0,20,2):
            print("valor actual: {0}".format(num))"""

        for i in range (1,13):
            print("{0} x {1} es: {2}".format(i, i,(i * i)))

        for nom in ["carlos","cesar","carolina","cristian"]:
            print("cantidad de letras de {0} es: {1}".format(nom, len(nom)))

    elif opcion == "17":
        print("*** IF con tuplas ***")

        print(" cursos")
        print("Matematica - biologia - lenguaje - ciencias")

        curso = input("ingrese el curso deseado: ")

        if curso in ("Matematica - biologia - lenguaje - ciencias"):
            print("curso {0} seleccionado.".format(curso))
        else:
            print("no existe ese curso")

    elif opcion == "18":
        print("*** Factorial de un numero ***")

        numero = int(input("Ingrese un numero: "))

        factorial = 1
        for n in range(1, (numero + 1)):
            factorial = factorial * n
        print ("El factorial de {0} es: {1}".format(numero,factorial))

    elif opcion == "19":
        print("*** Bucle while ***")

        """indice = 1

        while indice < 10:
            print("valor actual: {0}".format(indice))
            indice = indice + 1

        print("Terminado el bucle")"""

        inicio = 2

        while inicio <= 20:
            print("numero par: {0}".format(inicio))
            inicio += 2
        print("Terminado el bucle")

    elif opcion == "20":
        print("*** Break, continue, pass ***")

        """****** USO DEL BREAK ******"""
        for num in range(1,6):
            if num == 3:
                break
            print("el numero es: {0}".format(num))
        print("bucle termiando")

        """****** USO DEL CONTINUE ******"""
        for num in range(1, 6):
            if numero == 3:
                continue
            print("el numero es: {0}".format(num))
        print("bucle termiando")

        """****** USO DEL PASS ******"""
        for num in range(1,6):
            if num <= 3:
                pass
            else:
                print("el siguiente valor es mayor a 3:")
            print("el numero es: {0}".format(num))
        print("bucle termiando")

        def funcionnn ():
            pass

    elif opcion == "21":
        print("*** Generadores ***")

        def genemultiplo7(limite):
            numero = 1
            listnumero = []

            while numero <= limite:
                listnumero.append(numero * 7)
                numero = numero + 1
            return listnumero

        print(genemultiplo7(10))

        def genemult7(limite):
            numre = 1

            while numre <= limite:
                yield numre * 7
                numre = numre + 1
        obtimult7 = genemult7(10)

        """for n in obtimult7:
            print(n)"""
        #next(): retorna el siguiente elemento de un objeto iterable.
        print(next(obtimult7))
        print("Acá hay 386 líneas de código...")
        print(next(obtimult7))
        print("Acá hay 188 líneas de código...")
        print(next(obtimult7))

    elif opcion == "22":
        print("*** Generadores part 2 ***")

        """
        def devlenguaje(*lenguajes):
            for leng in lenguajes:
                yield leng
        """

        def devlenguaje(*lenguajes):
            for leng in lenguajes:
                yield from leng

        lenguaobten = devlenguaje("Python", "Java", "PHP", "Ruby", "JavaScript")

        print(next(lenguaobten))
        print(next(lenguaobten))
        print(next(lenguaobten))

    elif opcion == "23":
        print("*** Excepciones ***")

        numero1 = 10
        numero2 = 0

        #print("La división de {0} entre {1} es: {2}".format(numero1, numero2, (numero1 / numero2)))

        try:
            resultado = numero1 / numero2
        # except:
        except :
            print("No se puede dividir entre 0...")
        finally:
            print("AQUI TOY X100PRE")
        print("Aquí termina mi programa.")

    elif opcion == "24":
        print("*** Sentencia Raise ***")

        def evalnota(nota):
            if nota < 0:
                raise ValueError("Valor incorrecto...")
                # raise ZeroDivisionError("Este mensaje es opcional.")
            elif nota >= 16:
                print("Excelente")
            elif nota >= 11:
                print("Aprobado")
            else:
                print("Desaprobado")

        evalnota(17)

        print("Este es el fin de mi programa.")

    elif opcion == "25":
        print("*** Modulos en python ***")

        print(sumar(5 ,6))
        print(multiplicar(5, 6))

    elif opcion == "26":
        print("*** POO ***")

        class Person():

            apellidos = ""
            nombres = ""
            edad = 0
            despierta = False

            def despertar(self):
                self.despierta = True
                print("Buen día.")


        person1 = Person()
        person1.apellidos = "vera medina"
        print(person1.apellidos)
        person1.despertar()
        print(person1.despierta)

        person2 = Person()
        person2.apellidos = "medina vera"
        print(person2.apellidos)
        # person2.despertar()
        print(person2.despierta)

    elif opcion == "27":
        print("*** Constructores ***")

        class cursosxd():

            """
            nombre = "Matematica"
            credito = 5
            profresion = "Ingeniero civil
            """

            def __init__ (self, nom, cre, pro):
                self.nombre = nom
                self.creditos = cre
                self.profesion = pro

        cursoss1 = cursosxd("matematicas",5,"ingeniero civil")
        print(cursoss1.nombre)
        print(cursoss1.profesion)

    elif opcion == "28":
        print("*** Encapsulamiento variable ***")

        class curso():

            def __init__(self, nom, cre, pro,):
                self.nombre = nom
                self.creditos = cre
                self.profesion = pro
                self.__imparticion = "presencial"

            def most(self):
                dat = "nombre: {0} / creditos: {1} / modo imparticion: {2}"
                print(dat.format(self.nombre,self.creditos,self.__imparticion))

        curso1 = curso("matematicas", 5, "ingeniero civil")
        print(curso1.nombre)
        print(curso1.profesion)
        curso1.most()

    elif opcion == "29":
        print("*** Encapsulamiento metodos ***")

        class curso():

            def __init__(self, nom, cre, pro,):
                self.nombre = nom
                self.creditos = cre
                self.profesion = pro
                self.__imparticion = "presencial"

            def most(self):
                dat = "nombre: {0} / creditos: {1} / modo imparticion: {2}"
                print(dat.format(self.nombre,self.creditos,self.__imparticion))
                docentasig = self.__verdocen()
                if docentasig:
                    print("si hay docente")
                else:
                    print("NO hay doncente :(")

            def __verdocen(self):
                print("VERIFICANDO SI EL DOCENTE ESTA ASIGNADO...")
                if self.__imparticion == "Presencial":
                    return True
                else:
                    return False

        curso1 = curso("matematicas", 5, "ingeniero civil")
        print(curso1.nombre)
        print(curso1.profesion)
        curso1.most()

    elif opcion == "30":
        print("*** Metodos Accesores ***")

        class Cuenta():

            def __init__(self, pro, sal, mon):
                self.__propie = pro
                self.__saldo = sal
                self.__moneda = mon

            """metodo get"""
            def get_Saldo(self):
                return self.__saldo

            def get_Propie(self):
                return self.__propie

            def get_Moneda(self):
                return self.__moneda

            """metodo set"""
            def set_Moneda(self, moneda):
                self.__moneda = moneda

        cuen1 = Cuenta("ANTONY VERA", 1500, "dolares")
        print(cuen1.get_Saldo())
        print(cuen1.get_Moneda())
        cuen1.set_Moneda("Euros")
        print(cuen1.get_Moneda())

    elif opcion == "31":
        print("*** Metodo __str__ ***")

        class curso():

            def __init__(self, nom, cre, pro,):
                self.nombre = nom
                self.creditos = cre
                self.profesion = pro
                self.__imparticion = "presencial"

            def most(self):
                dat = "nombre: {0} / creditos: {1} / modo imparticion: {2}"
                print(dat.format(self.nombre,self.creditos,self.__imparticion))
                docentasig = self.__verdocen()
                if docentasig:
                    print("si hay docente")
                else:
                    print("NO hay doncente :(")

            def __verdocen(self):
                #print("VERIFICANDO SI EL DOCENTE ESTA ASIGNADO...")
                if self.__imparticion == "Presencial":
                    return True
                else:
                    return False

            def __str__(self):
                text = "nombre: {0} / creditos: {1}"
                return text.format(self.nombre,self.creditos)

        curso1 = curso("matematicas", 5, "ingeniero civil")
        print(curso1)
        curso1.most()

    elif opcion == "32":
        print("*** Herencia ***")

        class Persona():

            def __init__(self, apePat, apeMat, nom):
                self.apellidoPaterno = apePat
                self.apellidoMaterno = apeMat
                self.nombres = nom

            def mosNomComplet(self):
                txt = "{0} {1}, {2}"
                return txt.format(self.apellidoPaterno, self.apellidoMaterno, self.nombres)

        class Estudiante(Persona):

            def __init__(self, apePat, apeMat, nom, pro):
                super().__init__(apePat, apeMat, nom)
                self.profesion = pro

        estu1 = Estudiante("vera", "medina", "antony", "Ingeniería en software")
        print(estu1.mosNomComplet())
        print(estu1.profesion)

    elif opcion == "33":
        print("*** Sobreescritura ***")

        class Persona():

            def __init__(self, apePat, apeMat, nom):
                self.apellidoPaterno = apePat
                self.apellidoMaterno = apeMat
                self.nombres = nom

            def mosNomComplet(self):
                txt = "{0} {1}, {2}"
                return txt.format(self.apellidoPaterno, self.apellidoMaterno, self.nombres)

            def datos(self):
                print(self.mosNomComplet())

        class Estudiante(Persona):

            def __init__(self, apePat, apeMat, nom, pro):
                super().__init__(apePat, apeMat, nom)
                self.profesion = pro

            def datos(self):
                super().datos()
                print("profesion: {0}".format(self.profesion))

        estu1 = Estudiante("vera", "medina", "antony", "Ingeniería en software")
        #print(estu1.mosNomComplet())
        #print(estu1.profesion)
        estu1.datos()

    elif opcion == "34":
        print("*** Sustitucion ***")

        class Persona():

            def __init__(self, apePat, apeMat, nom):
                self.apellidoPaterno = apePat
                self.apellidoMaterno = apeMat
                self.nombres = nom

            def mosNomComplet(self):
                txt = "{0} {1}, {2}"
                return txt.format(self.apellidoPaterno, self.apellidoMaterno, self.nombres)

            def datos(self):
                print(self.mosNomComplet())

        class Estudiante(Persona):

            def __init__(self, apePat, apeMat, nom, pro):
                super().__init__(apePat, apeMat, nom)
                self.profesion = pro

            def datos(self):
                super().datos()
                print("profesion: {0}".format(self.profesion))

        #estu1 = Estudiante("vera", "medina", "antony", "Ingeniería en software")
        estu1 = Persona("vera", "medina", "antony")
        #print(estu1.mosNomComplet())
        #print(estu1.profesion)
        #estu1.datos()

        print(isinstance(estu1,Persona))

    elif opcion == "35":
        print("*** Herencia multiple ***")

        class ClassA():

            def __init__(self, par1, par2):
                self.parametro1 = par1
                self.parametro2 = par2

        class ClassB():

            def __init__(self, par3, par4, par5):
                self.parametro3 = par3
                self.parametro4 = par4
                self.parametro5 = par5

        class ClaseXx(ClassA, ClassB):
            pass
        clasX1 = ClaseXx(12, 13)
        print("si ejecuto")

    elif opcion == "36":
        print("*** Polimorfismo ***")

        class Estudiante():

            def describir(self):
                print("Soy un buen estudiante.")

        class Maestro():

            def describir(self):
                print("Me dedico a enseñar.")

        class Empleado():

            def describir(self):
                print("Trabajo dentro de una gran empresa.")

        def describirPersona(persona):
            persona.describir()

        doc1 = Maestro()
        describirPersona(doc1)

    elif opcion == "37":
        print("*** Relaciones ***")

        class Pais():

            def __init__(self, nom, pre):
                self.nombre = nom
                self.presidente = pre

            def __str__(self):
                text = "País: {0} - Presidente: {1}"
                return text.format(self.nombre, self.presidente)

        class Ciudad():

            def __init__(self, nom, hab, pai):
                self.nombre = nom
                self.habitantes = hab
                self.pais = pai

            def __str__(self):
                text = "Ciudad: {0} - N° Habitantes: {1} ({2})"
                return text.format(self.nombre, self.habitantes, self.pais)

        class ciudadela():

            def __init__(self, nom, ciu):
                self.nombre = nom
                self.ciudad = ciu

            def __str__(self):
                text = "Urbanización: {0} ({1})"
                return text.format(self.nombre, self.ciudad)

        pais1 = Pais("Ecuador", "mi pana lasso")
        print(pais1)

        ciudad1 = Ciudad("babahoyo", "no se somos muchos", pais1)
        print(ciudad1)

        urba1 = ciudadela("Villa verona", ciudad1)
        print(urba1)

"""Estudiante Vera Medina
Software A1"""