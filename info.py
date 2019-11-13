class Student:

    def __init__(self, name, hours, qpoints):
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)

    def getName(self):
        return self.name

    def getHours(self):
        return self.hours

    def getQPoints(self):
        return self.qpoints

    def gpa(self):
        return self.qpoints/self.hours
    
    def addGrade(self, gradePoint, credits):
        self.hours= self.hours+ credits
        self.qpoints= gradePoint * credits + self.qpoints


def main():

    s= Student("Bob", 0,0)
    
    info= input("What is the gradepoint and credit of the class?: ")
    
    gradePoint, credits= info.split()

    gradePoint=float(gradePoint)
    credits=float(credits)
    
    s.addGrade(gradePoint, credits)

    
    

    print("gpa is: ", s.gpa())
    

    

    
main()
    
    
