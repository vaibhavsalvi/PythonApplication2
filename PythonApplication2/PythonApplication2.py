from Employee import Employee;

x=10;
print x;
emp1 = Employee("Zara", 2000);
datafile = file('1.txt')
found = False
for line in datafile:
        if "Please" in line:
            print("Got the line");
            found = True
            break