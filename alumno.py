class Alumno:
    def __init__(self, nombre, apellidos):
        self.__nombre = nombre
        self.__apellido = apellidos

    @property
    def _nombre(self):
        return self.__nombre

    @_nombre.setter
    def _nombre(self, value):
        self.__nombre = value

    @property
    def _apellido(self):
        return self.__apellido

    @_apellido.setter
    def _apellido(self, value):
        self.__apellido = value
    def __str__(self):
        return f"{self._nombre} {self._apellido}"