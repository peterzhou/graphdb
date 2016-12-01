class Person:
    def __init__(self, name, birthdate, gender):
        self.name = name
        self.birthdate = birthdate
        self.gender = gender

#Subfield Academics
class Academics(Person):
    def __init__(self, name, birthdate, gender, almamater, field):
        Person.__init__(self, name, birthdate, gender)
        self.almamater = almamater
        self.field = field

class Professor(Academics):
    def __init__(self, name, birthdate, gender, almamater, field, university):
        Academics.__init__(self, name, birthdate, gender, almamater, field)
        self.university = university

class Teacher(Academics):
    def __init__(self, name, birthdate, gender, almamater, field, school):
        Academics.__init__(self, name, birthdate, gender, almamater, field)
        self.school = school

class Researcher(Academics):
    def __init__(self, name, birthdate, gender, almamater, field, university, mentor):
        Academics.__init__(self, name, birthdate, gender, almamater, field)
        self.university = university
        self.mentor = mentor
        
#Subfield Cultural
class Cultural(Person):
    def __init__(self, name, birthdate, gender, culture):
        Person.__init__(self, name, birthdate, gender)
        self.culture = culture

#Subfield Industry
class Industry(Person):
    def __init__(self, name, birthdate, gender, field):
        Person.__init__(self, name, birthdate, gender)
        self.field = field

class Engineer(Industry):
    def __init__(self, name, birthdate, gender, field):
        Industry.__init__(self, name, birthdate, gender, field)

class SoftwareEngineer(Engineer):
    def __init__(self, name, birthdate, gender, field, employer, programminglanguage):
        Engineer.__init__(self, name, birthdate, gender, field)
        self.employer = employer
        self.programminglanguage = programminglanguage

#Test

name = raw_input()
birthdate = raw_input()
gender = raw_input()
almamater = raw_input()
field = raw_input()
university = raw_input()

print "create (" + name + ":Professor {birthdate:'" + birthdate + "', gender:'" + gender + "', almamater:'" + almamater + "', field:'" + field + "', university:'" + university + "'})"
