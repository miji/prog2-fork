from estudiante import Estudiante

# Crear instancias de Estudiante
est1 = Estudiante("Juan Pérez", 20, ["Matemáticas", "Historia"])
est2 = Estudiante("María Gómez", 17, ["Biología"])

# Probar inscribir_curso
print("\n➡️ Inscribiendo cursos:")
est1.inscribir_curso("Física")  # Debería agregar el curso
est1.inscribir_curso("Matemáticas")  # Debería indicar que ya está inscrito

# Probar mostrar_informacion
print("\n➡️ Información de los estudiantes:")
est1.mostrar_informacion()
est2.mostrar_informacion()

# Probar __str__ y __repr__
print("\n➡️ Representación en string:")
print(str(est1))
print(repr(est1))

# Probar desde_tupla (classmethod)
print("\n➡️ Creando un estudiante desde una tupla:")
tupla_estudiante = ("Carlos López", 22, ["Programación", "Inglés"])
est3 = Estudiante.desde_tupla(tupla_estudiante)
est3.mostrar_informacion()

# Probar es_mayor_de_edad (staticmethod)
print("\n➡️ Verificando mayoría de edad:")
print(f"{est1.nombre} es mayor de edad? {Estudiante.es_mayor_de_edad(est1.edad)}")
print(f"{est2.nombre} es mayor de edad? {Estudiante.es_mayor_de_edad(est2.edad)}")

# Mostrar total de estudiantes creados
print("\n➡️ Total de estudiantes creados:", Estudiante.total_estudiantes)