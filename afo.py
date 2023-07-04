l1 = []
while True:
    try:
        print("""Hola:
estamos aqui para guardar su opinion musical
escribe por favor:""")
        z = input("Su nombre: ")
        q = input("Su DNI:")
        w = input("Su poblacion:")
        e = input("Su pais:")
        h = input("Su opinion: ")


        class Amigos():
            def __init__(self):
                self.nombre = z
                self.dni = q.upper()
                self.poblacion = w
                self.pais = e
                self.sentido = h


        class Musica(Amigos):
            def __init__(self):
                super().__init__()

        AM = Musica()
        qw =[f'Sus Datos  guardados: Eso es, {AM.nombre}, con su DNI, {AM.dni}, de poblacion,{AM.poblacion}, de país {AM.pais},'
             f' Su opinion de musica , {AM.sentido}']
        pregunta = input("Quieras guardar nueva persona ?")
        if pregunta == "No":
            l1.append(qw)
            break
        if pregunta == "Si":
            l1.append(qw)
            print(l1)
        else:
            print('escribe solo los "Si" o "No"')
            pregunta1 = input("Quieras guardar nueva persona ?")
            if pregunta1 == "No":
                l1.append(qw)
                break
            if pregunta1 == "Si":
                l1.append(qw)
                print("Vale")
                print(l1)
    except ValueError:
        print("escribe solo los comandes")
print(l1)
