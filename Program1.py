EmpDict = {}
EmpName = ""
EmpSalary = 0

while True:
    EmpName = input("Enter Employee name: ")
    EmpSalary = input("Enter Employee salary: ")
    if EmpName != "" and int(EmpSalary) > 0:
        EmpDict[EmpName] = EmpSalary
    
    loop = input("continue? (yes/no)\n").lower()
    if loop == "no":
        print("Dictionary:\n", EmpDict)
        quit()
    elif loop == "yes":
        EmpName = ""
        EmpSalary = 0
    else:
        print("wrong input! Quitting")
        quit()