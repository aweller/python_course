# define a function that greets the class

def greet_class(all_students):
    for student in all_students:
        print "Good morning %s!" % student
    return len(all_students)
    
# use the function

all_students = ["Carme", "Suska"]
student_count = greet_class(all_students)
print "I have %s students." % student_count