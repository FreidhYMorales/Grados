class Grado:
    def __init__(self):
        pass
    def AgregarGrado(self, codigo, nombre):
        self.codigo = codigo
        self.__nombre = nombre
        self.__alumnos = list()
        
    @property
    def _alumnos(self):
        return self.__alumnos

    @_alumnos.setter
    def _alumnos(self, value):
        self.__alumnos = value

    @property
    def _nombre(self):
        return self.__nombre

    @_nombre.setter
    def _nombre(self, value):
        self.__nombre = value

    def AgregarAlumno(self, alumno):
        if len(self._alumnos) < 3:
            self._alumnos.append(alumno)
            print("Alumno agregado con exito!!")
        else:
            print("Clase llena!!")
            print("Seleccione otra clase!!")
    def VerAlumnos(self):
        for alum in self._alumnos:
            print(alum)
            
    def VerGrado(self):
        print(f"{self.codigo} \t{self._nombre}")
