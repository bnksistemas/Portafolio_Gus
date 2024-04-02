from django.db import models

# Create your models here.
# Modelo para formacion= lo llamamos course
class Course(models.Model):
    period = models.CharField(max_length=50, blank=True, null=True, verbose_name='Periodo')    
    school = models.CharField(max_length=150, verbose_name='establecimiento')
    title = models.CharField(max_length=150, verbose_name='Título')
    description = models.TextField(verbose_name='Descripción')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha Modificación')

    # Pasos para convertir en español la aplación en el admin y ordenación de los registros 
    # de acuerdo al campo 'created' de forma descendente
    class Meta:
        verbose_name = 'formacion'
        verbose_name_plural = 'formaciones'
        db_table = "educations"
        ordering = ['-created']


    # Con esta función logro mostrar en la lista de formacion del admin, todos los cursos(fomracion) con su titulo
    def __str__(self):
        return self.title
        return f"{self.period},{self.school}, {self.title}"
    
# Modelo para conocimientos= skill
class Skill(models.Model):
    title = models.CharField(max_length=80, verbose_name='Título')
    image = models.ImageField(upload_to='skills', verbose_name='Imagen')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha Modificación')
        
    class Meta:
        verbose_name = 'conocimiento'
        verbose_name_plural = 'conocimientos'
        db_table = "skills"
        ordering = ['-created']
    
    def __str__(self):
        return self.title
# Experiencia
class Experience(models.Model):
    period = models.CharField(max_length=50, verbose_name='Periodo')    
    job_title = models.CharField(max_length=150, verbose_name='Cargo ocupado')
    location =  models.CharField(max_length=150, verbose_name='Lugar Trabajo')
    description = models.TextField(verbose_name='Descripción')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha Modificación')

    # Pasos para convertir en español la aplación en el admin y ordenación de los registros 
    # de acuerdo al campo 'created' de forma descendente
    class Meta:
        verbose_name = 'Experiencia'
        verbose_name_plural = 'Experiecias'
        db_table = "experiences"
        ordering = ['-created']


    # Con esta función logro mostrar en la lista de formacion del admin, todos los cursos(fomracion) con su titulo
    def __str__(self):
        return f"{self.period},{self.job_title}"
    
