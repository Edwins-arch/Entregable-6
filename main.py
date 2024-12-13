# Diccionario principal para almacenar personas (contactos)
personas = {}

# Diccionario de operaciones para la calculadora
operaciones = {
    "suma": lambda x, y: x + y,
    "resta": lambda x, y: x - y,
    "multiplicacion": lambda x, y: x * y,
    "division": lambda x, y: x / y if y != 0 else "Error: No se puede dividir entre cero.",
}

# Función para agregar una persona al diccionario de contactos
def agregar_persona():
    nombre = input("Ingresa el nombre de la persona: ").strip()
    
    # Verificar si la persona ya existe
    if nombre in personas:
        print(f"Ya existe una persona llamada {nombre}.")
        return
    
    # Solicitar la información de la persona
    edad = input(f"Ingresa la edad de {nombre}: ").strip()
    profesion = input(f"Ingresa la profesión de {nombre}: ").strip()
    ciudad = input(f"Ingresa la ciudad de {nombre}: ").strip()
    telefono = input(f"Ingresa el teléfono de {nombre}: ").strip()
    correo = input(f"Ingresa el correo electrónico de {nombre}: ").strip()

    # Guardar la persona en el diccionario
    personas[nombre] = {
        "edad": edad,
        "profesion": profesion,
        "ciudad": ciudad,
        "telefono": telefono,
        "correo": correo
    }

    print(f"Persona {nombre} agregada correctamente.")

# Función para mostrar la información de una persona
def mostrar_informacion(nombre):
    if nombre in personas:
        persona = personas[nombre]
        print(f"\nInformación de {nombre}:")
        print(f"Edad: {persona['edad']}")
        print(f"Profesión: {persona['profesion']}")
        print(f"Ciudad: {persona['ciudad']}")
        print(f"Teléfono: {persona['telefono']}")
        print(f"Correo: {persona['correo']}")
    else:
        print(f"No se encontró a {nombre} en el sistema.")

# Función para realizar operaciones matemáticas
def realizar_operacion(num1, num2, operacion):
    if operacion in operaciones:
        return operaciones[operacion](num1, num2)
    else:
        return "Error: Operación no válida."

# Función principal para interactuar con el usuario
def menu():
    continuar = True
    while continuar:
        print("\nOpciones disponibles:")
        print("1. Realizar operación matemática")
        print("2. Agregar persona")
        print("3. Mostrar información de una persona")
        print("4. Salir")
        
        opcion = input("Elige una opción (1/2/3/4): ").strip()
        
        if opcion == "1":
            # Realizar operación matemática
            try:
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))
            except ValueError:
                print("Por favor, ingresa un número válido.")
                continue

            operacion = input("Ingresa la operación (suma, resta, multiplicacion, division): ").lower()
            resultado = realizar_operacion(num1, num2, operacion)
            print(f"El resultado de la operación es: {resultado}")
        
        elif opcion == "2":
            # Agregar persona
            agregar_persona()
        
        elif opcion == "3":
            # Mostrar información de una persona
            nombre = input("Ingresa el nombre de la persona cuya información deseas ver: ").strip()
            mostrar_informacion(nombre)
        
        elif opcion == "4":
            continuar = False
            print("¡Gracias por usar el sistema!")
        
        else:
            print("Opción no válida, por favor elige una opción correcta.")

# Ejecutar el menú
menu()




