class Persona:
    def __init__(self, cedula, nombre, apellido, email, telefono, direccion, numero_libros, activo, carrera):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono
        self.direccion = direccion
        self.numero_libros = numero_libros
        self.activo = activo
        self.carrera = carrera

    def get_cedula(self):
        return self.cedula

    def set_cedula(self, cedula):
        self.cedula = cedula

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_apellido(self):
        return self.apellido

    def set_apellido(self, apellido):
        self.apellido = apellido

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_telefono(self):
        return self.telefono

    def set_telefono(self, telefono):
        self.telefono = telefono

    def get_direccion(self):
        return self.direccion

    def set_direccion(self, direccion):
        self.direccion = direccion

    def get_numero_libros(self):
        return self.numero_libros

    def set_numero_libros(self, numero_libros):
        self.numero_libros = numero_libros

    def get_activo(self):
        return self.activo

    def set_activo(self, activo):
        self.activo = activo

    def get_carrera(self):
        return self.carrera

    def set_carrera(self, carrera):
        self.carrera = carrera

    def pedir_libro(self):
        return True

    def devolver_libro(self):
        return True

    def __str__(self):
        return f'Persona: [Nombre: {self.nombre} {self.apellido}, Cedula: {self.cedula}]'


class Estudiante(Persona):
    contador_estudiante = 0

    def __init__(self, cedula, nombre, apellido, email, telefono, direccion, numero_libros, activo, carrera, nivel):
        super().__init__(cedula, nombre, apellido, email, telefono, direccion, numero_libros, activo, carrera)
        self.id = Estudiante.contador_estudiante + 1
        self.nivel = nivel
        Estudiante.contador_estudiante += 1


class Docente(Persona):
    contador_docente = 0

    def __init__(self, cedula, nombre, apellido, email, telefono, direccion, numero_libros, activo, carrera,
                 titulo_3er_nivel, titulo_4to_nivel):
        super().__init__(cedula, nombre, apellido, email, telefono, direccion, numero_libros, activo, carrera)
        self.id = Docente.contador_docente + 1
        self.titulo_3er_nivel = titulo_3er_nivel
        self.titulo_4to_nivel = titulo_4to_nivel
        Docente.contador_docente += 1


# Ejemplo de uso
estudiante = Estudiante('1234567890', 'Juan', 'Perez', 'juan@example.com', '123456789', 'Calle 123', 3, True,
                        'Informática', 2)
print(estudiante)
print(estudiante.pedir_libro())
print(estudiante.devolver_libro())

docente = Docente('0987654321', 'Maria', 'Lopez', 'maria@example.com', '987654321', 'Avenida 456', 5, True,
                  'Matemáticas', 'Licenciatura', 'Maestría')
print(docente)
print(docente.pedir_libro())
print(docente.devolver_libro())

# Ejemplo de uso
estudiante = Estudiante('1234567890', 'Juan', 'Perez', 'juan@example.com', '123456789', 'Calle 123', 3, True,
                        'Informática', 2)
print(estudiante)
print(estudiante.pedir_libro())
print(estudiante.devolver_libro())

docente = Docente('0987654321', 'Maria', 'Lopez', 'maria@example.com', '987654321', 'Avenida 456', 5, True,
                  'Matemáticas', 'Licenciatura', 'Maestría')
print(docente)
print(docente.pedir_libro())
print(docente.devolver_libro())
