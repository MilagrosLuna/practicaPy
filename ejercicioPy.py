def calcular_promedio(nota1,nota2,nota3):
    promedio = (nota1 + nota2 + nota3)/3    
    return promedio

def calcular_promedio_clase(promedio_estudiantes):
    promedio = sum(promedio_estudiantes)/len(promedio_estudiantes)
    return promedio

#1. Ingresar el número de estudiantes de una clase
print("****************************************")
num_estudiantes = int(input("Ingrese el numero de estudiantes: "))
estudiantes = []
promedio_estudiantes = []
notas_totales = []
calificacion_mas_alta = 0
calificacion_mas_baja = 100
nombre_mas_alto = ""
nombre_mas_bajo = ""
print("****************************************")

for i in range(num_estudiantes):
    #2. Para cada estudiante, ingresar su nombre, apellido y tres calificaciones (nota1, nota2,nota3) en el rango de 0 a 100.
    nombre = input("Ingrese el nombre del estudiante: ")
    apellido = input("Ingrese el apellido del estudiante: ")
    nota1 = float(input("Ingrese la 1° nota: ")) 
    nota2 = float(input("Ingrese la 2° nota: "))
    nota3 = float(input("Ingrese la 3° nota: "))
    # 3. Calcular y mostrar el promedio de cada estudiante.

    promedio_estudiante =  calcular_promedio(nota1,nota2,nota3)
    print(f"El promedio de {nombre} es de {round(promedio_estudiante,2)}")    

    #4. Calcular y mostrar la calificación más alta y más baja en la clase.
    notas = [nota1,nota2,nota3]
    calificacion_maxima = max(notas)  
    calificacion_minima = min(notas)  

    if calificacion_mas_alta < calificacion_maxima:
        nombre_mas_alto = nombre
        calificacion_mas_alta = calificacion_maxima

    if calificacion_mas_baja > calificacion_minima:
        nombre_mas_bajo = nombre
        calificacion_mas_baja = calificacion_minima

    #5. Calcular y mostrar el promedio de calificaciones de toda la clase
    promedio_estudiantes.append(promedio_estudiante)

    estudiantes.append({"Nombre": nombre, "Apellido": apellido, "Promedio": promedio_estudiante})
    
    print("****************************************")

print(f"La calificacion mas alta es {calificacion_mas_alta} y fue de {nombre_mas_alto}")
print(f"La calificacion mas baja es {calificacion_mas_baja} y fue de {nombre_mas_bajo}")
promedio_total_clase = calcular_promedio_clase(promedio_estudiantes)

print("****************************************")
print(f"El promedio total de toda la clase es de {round(promedio_total_clase,2)}")
print("****************************************")

for estudiante in estudiantes:
    if estudiante['Promedio'] > promedio_total_clase:
        print(f"El promedio de {estudiante['Nombre']} es superior al promedio de la clase y fue de {round(estudiante['Promedio'],2)}")

print("****************************************")

