from django.db import models
from django.utils import timezone
# Create your models here.

RELLIGION = (
        ('0', 'Ninguno'),
        ('1', 'Otra'),
        ('2', 'Catolico'),
        ('3', 'Evangelico'),
        ('4', 'Adventista'),
    )

LATERALIDAD = (
        ('0', 'Diestro'),
        ('1', 'Zurdo'),
        ('2', 'Ambidiestro'),
    )

CARRERA = (
	('00','Biología'),
	('01','Física'),
	('02','Licenciatura en Matemáticas Matemáticas'),
	('03','Química'),
	('04','Derecho'),
	('05','Economía'),
	('06','Filosofía'),
	('07','Historia y Archivística'),
	('08','Licenciatura en Educación Básica con Énfasis en Ciencias Naturales y Educación Ambiental'),
	('09','Licenciatura en Educación Básica con Énfasis en Lengua Castellana'),
	('10','Licenciatura en Español y Literatura'),
	('11','Licenciatura en Inglés'),
	('12','Licenciatura en Lenguas Extranjeras con énfasis en Inglés'),
	('13','Licenciatura en Literatura y Lengua Castellana'),
	('14','Licenciatura en Música'),
	('15','Trabajo Social'),
	('16','Diseño Industrial'),
	('17','Ingeniería Civil'),
	('18','Ingeniería de Eléctrica'),
	('19','Ingeniería de Electrónica'),
	('20','Ingeniería Industrial'),
	('21','Ingeniería Mecánica'),
	('22','Ingeniería de Sistemas'),
	('23','Geología'),
	('24','Ingeniería Metalúrgica'),
	('25','Ingeniería de Petróleos'),
	('26','Ingeniería Química'),
	('27','Microbiología y Bioanálisis'),
	('28','Enfermería'),
	('29','Fisioterapia'),
	('30','Medicina'),
	('31','Nutrición y Dietética'),
	('32','Ingeniería Forestal'),
	('33','Zootecnia'),
	('34','Turismo'),
	)

class Paciente(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    cedula = models.CharField(max_length=200)
    carrera = models.CharField(max_length=2,
					        choices=CARRERA,
					        default=30)
    telefono = models.CharField('Teléfono', max_length=200)
    correo = models.EmailField('Correo Electrónico', max_length=250)
    edad = models.CharField(max_length=200)
    cree_dios = models.BooleanField('Cree en Díos', default=True)
    religion = models.CharField('Religión',max_length=2,
					        choices=RELLIGION,
					        default=0)
    trabaja = models.BooleanField(default=False)
    lateralidad = models.CharField(max_length=1,
					        choices=LATERALIDAD,
					        default=0)
    def __str__(self):
        return self.cedula + " - " + self.nombre +" " + self.apellido 


class HistoriaMedica(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    enfermedad = models.TextField(max_length=200)
    antecedentes = models.TextField(max_length=200)
    examen_mental = models.TextField(max_length=200)
    analisis = models.TextField('Análisis', max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.paciente.cedula + "_" + str(self.created_date)


class Terapia(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    ruta = models.CharField(max_length=200, default="biofeedback/")
    created_date = models.DateTimeField("Fecha de creación", default=timezone.now)

    def __str__(self):
        return self.paciente.cedula + "_" + str(self.created_date)

    
