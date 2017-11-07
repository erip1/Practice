from emp import *

# from filename import * or from filename import method_name 

"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)

print "####################################################"

emp1.displayEmployee()
print "####################################################"
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount
