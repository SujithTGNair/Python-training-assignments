physics=int(input("Enter the value less than or equal to 200 for the subject physics: "))
if physics>200:
    print("Enter the value less than or equal to 200 for the subject physics: ")
    physics=(input())
else:
    print("Entered value less than 200 for the subject physics: ")
chemistry=int(input("Enter the value less than or equal to 200  for the subject chemistry: "))
if chemistry>200:
    print("Enter the value less than or equal to 200 for the subject chemistry: ")
    chemistry=(input())
else:
    print("Entered value less than 200 for the subject chemistry: ")
maths=int(input("Enter the value less than or equal to 200 for the subject maths: "))
if maths>200:
    print("Enter the value less than or equal to 200 for the subject maths: ")
    maths=(input())
else:
    print("Entered value less than 200 for the subject maths: ")


cutoff=int((physics/4+chemistry/4+maths/2))
print("Total average marks: ", cutoff)

if cutoff>195:
    print("Admission can be done in IISC")
elif cutoff<=195 and cutoff>190:
    print("Admission can be done in IIT Mumbai")
elif cutoff<=190 and cutoff>180:
    print("Admission can be done in IIT Bngalore")
elif cutoff<=180 and cutoff>150:
    print("Admission can be done in IIT Kharakpur")
elif cutoff<=150:
    print("Try next year")
