import Dashboard

def show_my_courses(student, course_list):
    print('\nMy Courses:')
    print('#\tCOURSE NAME\tINSTRUCTOR NAME')
    attending_dao = DAO.AttendingDAO()
    my_courses = attending_dao.get_student_courses(course_list, student.get_email())
    i = 1
    for course in my_courses:
        print(f'{i}\t{course.get_name()}\t{course.get_instructor()}')
        i+=1

def show_all_courses(course_list):
    print('\nAll Courses:')
    print('ID\tCOURSE NAME\tINSTRUCTOR NAME')
    for course in course_list:
        print(f'{course.get_id()}\t{course.get_name()}\t{course.get_instructor()}')

def main():
    print('Welcome!')
    entry=None
    while entry!='2':
        entry = input('\n1. Current Student\n2. New Student\n3. Quit\nPlease, enter 1, 2 or 3: ')

        if entry=='1':
            student_dao = DAO.StudentDAO()
            email = input('\nEnter Your Email: ')
            pw = input('Enter Your Password: ')

            if student_dao.validate_user(email, pw):
                course_dao = DAO.CourseDAO()
                attending_dao = DAO.AttendingDAO()
                student = student_dao.get_student_by_email(email)
                course_list = course_dao.get_courses()
                print(type(student))
                show_my_courses(student, course_list)
                print('\nWhat Would You Like To Do?')

                while entry!='2':
                    entry = input('\n1. Register To Course\n2. Logout\nPlease, enter 1 or 2: ')

                    if entry=='1':
                        show_all_courses(course_list)
                        course_id = input('\nSelect Course By ID Number: ')
                        print("\nAttempting to Register...")
                        if attending_dao.register_student_to_course(email, course_id, course_list):
                            show_my_courses(student, course_list)
                    elif entry=='2':
                        print('\nYou Have Been Logged Out.')
                    else:
                        print('\nInvalid Option...')


            else:
                print('\nWrong Credentials!')
        elif entry=='2':
            print("Welcome to the school!")
            student_dao = DAO.StudentDAO()
            email = input('Please provide your email : ')
            if not student_dao.get_student_by_email(email):
                name     = input("What is your full name? : ")
                password = input("What would you like your password to be? : ")
                student_dao.add_new_student(email, name, password)
                entry = '-1'
                continue;
            else:
                print("That email is already taken")

        elif entry=='3':
            print("Programming is closing, ")
            break;
        else:
            print('Invalid Option...')
    print('\nClosing Program. Goodbye.')

if __name__=='__main__':
    main()
