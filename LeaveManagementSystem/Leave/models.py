from django.db import models

class Leave(models.Model):

    Employee_Name = models.ForeignKey('Employee_Detail',models.DO_NOTHING,related_name="empname")
    l = (
        ("Sick-Leave","Sick-Leave"),("Casual-Leave","Casual-Leave"),("Personal-Leave","Personal-Leave")
    )
    Leave_Type = models.CharField(max_length=20, choices= l, default="Sick-Leave")
    m = (
        ("January","January"),("February","February"),("March","March"),("April","April"),("May","May"),("June","June"),("July","July"),("August","August"),("September","September"),("October","October"),("November","November"),("December","december")
    )
    Month = models.CharField(max_length=10, choices= m)
    Year = models.CharField(max_length=4)
    Start_Date = models.DateField()
    End_Date = models.DateField(null=True, blank = True)
    Reason = models.CharField(max_length=200)
    s = (
       ("Accepted","Accepted"),("Pending","Pending"),("Canceled","Canceled")
    )
    Status = models.CharField(max_length=10, choices= s, default="Pending")


    def __str__(self):
        return str(self.Employee_Name)

class Employee_Detail(models.Model):
    Employee_Name = models.CharField(unique=True, max_length=30)
    password = models.CharField( max_length=30)
    Primary_Phone = models.CharField(max_length=12 )
    Email = models.EmailField(max_length=50, unique=True)


    def __str__(self):
        return str(self.Employee_Name)




