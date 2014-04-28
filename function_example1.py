# define a function that greets the class

def greet_class(all_students):
    for student in all_students:
        print "Good morning %s!" % student

# use the function

all_students = ["Carme", "Suska"]
greet_class(all_students)
