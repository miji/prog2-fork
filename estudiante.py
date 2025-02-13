class Estudiante:
    total_estudiantes = 0  # Contador de instancias

    def __init__(self, nombre, edad, cursos_inscritos):
        self.nombre = nombre
        self.edad = edad
        self.cursos_inscritos = cursos_inscritos
        Estudiante.total_estudiantes += 1  # Aumenta el contador cada vez que se crea un estudiante

    def inscribir_curso(self, curso):
        """Inscribe al estudiante en un nuevo curso."""
        if curso not in self.cursos_inscritos:
            self.cursos_inscritos.append(curso)
        else:
            print(f"{self.nombre} ya está inscrito en {curso}.")

    def mostrar_informacion(self):
        """Muestra la información del estudiante."""
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Cursos inscritos: {', '.join(self.cursos_inscritos) if self.cursos_inscritos else 'Ninguno'}")

    def __str__(self):
        """Devuelve una representación en cadena amigable del estudiante."""
        return f"Estudiante {self.nombre}, {self.edad} años, Cursos: {', '.join(self.cursos_inscritos)}"

    def __repr__(self):
        """Devuelve una representación formal del estudiante."""
        return f"Estudiante(nombre={self.nombre}, edad={self.edad}, cursos_inscritos={self.cursos_inscritos})"

    @classmethod
    def desde_tupla(cls, tupla):
        """Crea una instancia de Estudiante desde una tupla (nombre, edad, lista_cursos)."""
        return cls(*tupla)

    @staticmethod
    def es_mayor_de_edad(edad):
        """Determina si un estudiante es mayor de edad (18+ años)."""
        return edad >= 18