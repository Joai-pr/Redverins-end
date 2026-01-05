def iniciar():
    while True:
        clase = input("""Seleccione la clase de su aventurero: \n
            > Guerrero
            > Mago
            > Curandero \n
            """)
        clase_min = clase.strip().lower()
        if clase_min == "guerrero":
            print("La clase de su aventurero es 'Guerrero'")
            break
        
        elif clase_min == "mago":
            print("La clase de su aventurero es 'Mago'")
            break
        
        elif clase_min == "curandero":
            print("La clase de su aventurero es 'Curandero'")
            break
        
        else:
            print("Por favor, seleccione una clase válida \n")

iniciar()