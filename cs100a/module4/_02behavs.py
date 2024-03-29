#1.

import random

#import function to generate students
#don't start filenames with numbers
#and remember not to label them .py in import statements
#from _01props import student_objects
#that's not working, since i think it uses the old student class, which doesn't have behavior ask_question

class Student:
    #default statement
    def __init__(self):
        """
        Create a default statement
        """
        self.name = ''
        self.id = -1
        self.birthdate = '1/1/2001'

    #study behavior
    def study(self):
        """
        Time to study
        """
        print(f'{self.name} is studying')

    #do homework behavior, taking course parameter
    def do_homework(self, course):
        """
        Time to do homework
            Parameters: course(str): the course to do the homework for
        """
        print(f'{self.name} is doing homework')

    #ask question behavior
    def ask_question(self):
        """
        Time to ask questions
        """
        print(f'What?')

class Teacher:
    def __init__(self):
        """
        Create a default statement
        """
        self.name = ''
        self.id = -1
        self.birthdate = '1/1/2001'

    def erase_board(self):
        """
        There is no more room on this board
        """
        print(f'{self.name} is erasing the board.')

    def grade_homework(self, student_name):
        """
        I need to grade this homework
        Parameters:
        student: course for whom to grade homework
        """
        print(f"{self.name} is grading {student_name}'s homework.")

    def give_lecture(self, course):
        """
        Today's lecture is on...
        Parameters: 
        course: course for which to give lecture
        """
        print(f'{self.name} is giving a lecture on {course}')

#2.

class Course:
    def __init__(self):
        """
        Create a default statement
        """
        self.name = ''
        self.id = -1
        self.teacher_id = -1

    def fill_up(self):
        """
        This class is full
        """
        print(f'{self.name} is accepting no more students at this time.')
    
    def advising_week(self):
        """
        It is advising week!
        """
        print(f'{self.name} is getting out early for advising week.')

    def required(self, req):
        """
        Is this class required for a major?
        """
        print(f'{self.name} is required for these majors: {req}')

#function to generate student objects
def student_objects(students):
    #list of names
    namepile = ['Maeve', 'Mahabala', 'Mary', 'Mathrudev', 'Meghan', 'Meru', 'Moira']
    #list of students
    

    #create student objects
    stud01 = Student()
    stud02 = Student()
    stud03 = Student()
    stud04 = Student()
    stud05 = Student()
    #'extend' students to student list
    #so this is REALLY the only place i use the double parentheses
    students.extend((stud01, stud02, stud03, stud04, stud05))
    for index, s in enumerate(students, start = 1):
        s.name = namepile[random.randrange(len(namepile))]
        #oh, THIS is a better way to prevent duplicates, you remove after using...
        namepile.remove(s.name)


stud = Student()
#Set the student's properties
stud.name = 'Mary'
stud.ID = 10101
stud.birthdate = '1/1/1999'

print(stud.name)

#doing student behaviors
stud.do_homework('CS100A')
stud.ask_question()
stud.study()

#2 & #3 test out other functions

teach = Teacher()
teach.name = 'Meredith'
teach.id = 5004
teach.birthdate = '3/2/1959'

print(teach.name)

teach.give_lecture("Physics")
teach.erase_board()
teach.grade_homework("Fanny Bogelson")

#wait, what? composition? i think i need something like that to pass student into grade_homework
#i don't know, MAYBE i should wait until i at least get to the constructors...
#i mean, really though, i'm noticing database stuff that i'm NOT doing in here

c1 = Course()
c1.name = "Archaeology"
c1.id = 666
c1.teacher_id = 74147

c1.fill_up()
c1.advising_week()
#oh, i'm also using double parentheses here.
#well, that makes sense, right? using a tuple as an argument?
c1.required(("math", "computer science"))

#3.

#initialize roster
students = []

student_objects(students)

for s in students:
    rando = random.randrange(0, 3)
    if rando == 0:
        s.ask_question()
    elif rando == 1:
        s.do_homework("Statistics")
    elif rando == 2:
        s.study()













