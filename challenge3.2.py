class student:
  def __init__(self,name,roll_number,cgpa):
    self.name=name
    self.roll_number=roll_number
    self.cgpa=cgpa
  def sort_student(student_list):
    sorted_student=sorted(student_list,key=lambda student:student.cgpa,reverse=True)
    return sorted_student
student=[
  student("Hari","A123",7.8),
  student("Madhan","B123",7.9),
  student("Arul jaothi","c123",8.1),
  student("Sujith","SB513",5.13)
]
sorted_student=sort_student(student)
for student in sorted_student:
  print("Name:{},     RollNumber:{}.    cgpa:{},       ".format(student.name,student.roll_number,student.cgpa))