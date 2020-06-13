import Models

class StudentDashboard:
    def __init__(self):
        # You set in a try statement so that the user knows why it crashes if there is no file
        try:
            # This array will hold the list of students in it
            studentClassTable = []
            with open("students.csv", 'r') as f:
                # Read in the student table
                studentTable = f.read().split("\n")
                for k in studentTable[:-1]:
                    sList = k.split(",") # break into the three parts, email, name, and pass
                    firstName = (sList[1].split(" "))[0] #sets the first name
                    firstName = Models.Student(sList[0], sList[1], sList[2])
                    studentClassTable.append(firstName)
        except:
            print("No student file found")

        # Declaring the actual self table here (it didn't like me declaring it eariler)
        self.studentList = studentClassTable

    def get_students(self):
        result = [] # this is the list of students that we'll return
        for k in self.studentList:
            result.append(k.get_name())
        return(result)

    def validate_user(self, email, pw):
        for k in self.studentList:
            if k.get_email() == email: #cycles through the classes to find the right one
                if k.get_password() == pw:
                    return True
                else:
                    return False

    def get_student_by_email(self, email):
        for tick, k in enumerate(self.studentList):
            if k.get_email() == email:
                return self.studentList[tick]
        print("There is no student with this email")
        return False

    def add_new_student(self, email, name, password):
        newDude = Models.Student(email, name, password)
        self.studentList.append(newDude)
        self.save_student()
        print("You've been added!")

    def save_student(self):
        # This array will hold the list of students in it
        with open("students.csv", 'w') as f:
            # Read in the student table
            for k in self.studentList:
                f.write(k.get_email() + "," + k.get_name() + "," + k.get_password() + "\n")



class CourseDashboard:
    def __init__(self):
        try:
            # This array will hold the list of students in it
            courseClassTable = []
            with open("courses.csv", 'r') as f:
                # Read in the student table
                courseTable = f.read().split("\n")
                for k in courseTable[:-1]:
                    sList = k.split(",") # break into the three parts, email, name, and pass
                    course = Models.Course(sList[0], sList[1], sList[2])
                    courseClassTable.append(course)
        except:
            print("No course file found")

        # Declaring the actual self table here (it didn't like me declaring it eariler)
        self.courseList = courseClassTable


    def get_courses(self):
        return(self.courseList)

class AttendingDashboard:
    def __init__(self):
        # You set in a try statement so that the user knows why it crashes if there is no file
        try:
            # This array will hold the list of students in it
            attendingClassTable = []
            with open("attending.csv", 'r') as f:
                # Read in the student table
                attendingTable = f.read().split("\n")
                for k in attendingTable[:-1]:
                    sList = k.split(",") # break into the three parts, email, name, and pass
                    attending = Models.Attending(sList[0], sList[1])
                    attendingClassTable.append(attending)
        except:
            print("No attendance file found")

        # Declaring the actual self table here (it didn't like me declaring it eariler)
        self.attendingList = attendingClassTable

    def get_attending(self):
        return(self.attendingList)

    def get_student_courses(self, course_list, email):
        classesAttending = []
        attendingList = self.get_attending()
        # get list of course he is attending
        for k in attendingList:
            if k.student_email == email:
                classesAttending.append(k.course_id)

        results = []
        for k in course_list:
            for i in classesAttending:
                if k.get_id() == i:
                    results.append(k)

        return(results)

    def register_student_to_course(self, email, course_id, course_list):
        totalCourses = []
        for k in course_list:
            totalCourses.append(k.get_id())

        if course_id in totalCourses:
            flag = True
            attendingList = get_attending()
            for k in attendingList:
                if (k.get_course_id() == course_id) and (k.get_student_email() == email):
                    flag = False

            if flag == True:
                self.attendingList.append(Models.Attending(course_id, email))
                print("I've added you to the class")
                self.save_attending()
                return True
            else:
                print("You are already in this class!")
                return False
        else:
            print("This is not a class!")
            return False

    def save_attending(self):
        # This array will hold the list of students in it
        with open("attending.csv", 'w') as f:
            # Read in the student table
            for k in self.attendingList:
                f.write(k.get_course_id() + "," + k.get_student_email() + "\n")















#
