pasajeros = []
rut = []
acomun=60000
piernas=80000
norec=50000
c_acomun=0
c_piernas=0
c_norec=0

while True: 
    print("Bienvenido ")
    print("(1)Comprar pasajes ")
    print("(2)Mostrar ubicaciones disponibles ")
    print("(3)Listar pasajeros ")
    print("(4)Buscar pasajero ")
    print("(5)Reasignar asiento ")
    print("(6)Mostrar ganancias totales ")

    op=int(input("Escoga una opción ")) 
    if op==1:   
        while True:
            print("¿Qué tipo de asiento desea comprar? ") 
            print("(1)Común= $60.000 ")
            print("(2)Extra espacio piernas= $80.000 ")
            print("(3)No reclinable= $50.000 ") 
            print("(4)Volver al menú anterior")
            opa=int(input("Escoga una opción"))
            if opa==1:  
                    c_acomun+=1
            elif opa==2:    
                    c_piernas+=1
            elif opa==3:    
                    c_norec+=1
            elif opa==4:
                    break

    elif op==2: 
        mostrar_ubic()
    elif op==3: 
        lista_pasajeros()
    elif op==4: 
        busc_pasajero()
    elif op==5:
        reas_asiento()
    elif op==6:
        total=((c_acomun*acomun)+(c_norec*norec)+(c_piernas*piernas))
        print(total)
    elif op==7: 
        break
