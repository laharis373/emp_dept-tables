from django.db import models

# Create your models here.
class Dept(models.Model):
    dept_no=models.PositiveBigIntegerField(primary_key=True)
    deptname=models.CharField(max_length=100)
    loc=models.CharField(max_length=100)
class Emp(models.Model):
    empno=models.PositiveBigIntegerField(primary_key=True)
    ename=models.CharField(max_length=100)
    salary=models.PositiveBigIntegerField()
    mgr=models.PositiveBigIntegerField()
    comm=models.PositiveBigIntegerField()
    hiredate=models.DateField()
    deptno=models.ForeignKey(Dept,on_delete=models.CASCADE)
