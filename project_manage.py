# import database module
from database import Read, Table, Database
from random import randint

# define a funcion called initializing
my_DB = Database()
read = Read()


class Admin:
    def __init__(self, person_table, login_table,project_table):
        self.person_table = person_table
        self.login_table = login_table
        self.project_table = project_table


    def see_project_info(self):
        print(self.project_table.table)
    def manage_info(self):
        while True:
            user_choice = input('Select an option:\n '
                            '1.Add an information\n '
                            '2.Delete an information\n '
                            '3.Edit an information \n'
                            '4.Go back\n')
            if user_choice == '1':
                user_id = input('User_id: ')
                first_name = input('First name: ')
                last_name = input('Last name: ')
                type = input('Type: ')
                username = f'{first_name}.{last_name[0]}'
                password = randint(1000, 9999)
                self.person_table.insert({'ID': user_id, 'first': first_name, 'last': last_name, 'type': type})
                self.login_table.insert({'ID': user_id, 'username': username, 'password': password, 'role': type})
                print(f'{user_id} {username} has added to the database')
            elif user_choice == '2':
                remove_id = input('User_id you want to delete: ')
                for person in self.person_table.table:
                    if person['ID'] == remove_id:
                        self.person_table.table.remove(person)
                for person in self.login_table.table:
                    if person['ID'] == remove_id:
                        self.login_table.table.remove(person)
            elif user_choice == '3':
                edit_id = input('User_id you want to edit: ')
                for person in self.login_table.table:
                    if person['ID'] == edit_id:
                        print(f"{person['ID']}\n"
                            f"{person['username']} {person['password']}\n"
                            f" {person['role']}")
                change_choice = input('Select what to change:\n'
                                    '1.Password\n2.Role')
                if change_choice == '1':
                    new_password = randint(1000, 9999)
                    for person in self.login.table.table:
                        if person['ID'] == edit_id:
                            person['password'] = new_password
                    print('The new password is:', new_password)
                elif change_choice == '2':
                    new_role = input('Enter new role:')
                    for person in self.login_table.table:
                        if person['ID'] == edit_id:
                            person['role'] = new_role
            elif user_choice == '4':
                break
            else:
                print('Choice invalid. Please try again!')


class Student:
    def __init__(self, id, login_table,student_pending_table):
        self.id = id
        self.login_table = login_table
        for i in login_table:
            if i['ID'] == id:
                self.username = i['username']
                self.role = i['role']
        self.student_pending_table = student_pending_table
    def create_project(self):
        print('Creating project....')
        project_name = input('Enter your project name: ')
        self.role = 'lead'
        project_id = randint(000000, 999999)
        project_info = {'Projectname': project_name, 'ProjectID': project_id, 'Lead': self.username, 'Member1': '-',
                        'Member2': '-', 'Advisor': '-','Status': 'Working'}
        self.login_table.update('ID', self.id, 'username', self.username, 'role', 'lead')
        project_table = my_DB.search('project_table')
        project_table.table.insert(project_info)

    def invitaion_detail(self):
        invitation_count = 0
        for i in self.student_pending_table.table:
            if i['ReceiverID'] == self.id:
                print(f"ProjectID: {i['ProjectID']}, LeadID: {i['InviterID']}")
                invitation_count += 1
            else:
                continue
        if invitation_count == 0:
            print('There are no invitation yet')
            return
        respond = input('Enter project: ')
        for i in self.student_pending_table.table:
            if i['ProjectID'] == respond and i['ReceiverID'] == self.id:
                choice = input(f"Do you want to accept this {i['ProjectID']} from {i['ReceiverID']} (y/n): ")
                if choice.lower() == 'y':
                    i['Respond'] = 'Accepted'
                elif choice.lower() == 'n':
                    i['Respond'] = 'Deny'
                else:
                    print('Invalid choice.')







def initializing():
    # here are things to do in this function:
    # create an object to read all csv files that will serve as a persistent state for this program
    read_person = read.read_data('persons.csv')
    read_login = read.read_data('login.csv')
    read_project = read.read_data('project.csv')
    read_student_pending = read.read_data('student_pending_invitaion.csv')

    # create all the corresponding tables for those csv files
    person_table = Table('persons', read_person)
    login_table = Table('login', read_login)
    project_table = Table('project', read_project)
    student_pending_table = Table('student_pending', read_student_pending)
    # see the guide how many tables are needed
    # add all these tables to the database
    my_DB.insert(person_table)
    my_DB.insert(login_table)
    my_DB.insert(project_table)
    my_DB.insert(student_pending_table)
    return my_DB


# define a funcion called login

def login():
    username = input('Enter username: ')
    password = input('Enter password: ')
    user_info = my_DB.search('login')
    for i in user_info.table:
        if username == i['username'] and password == i['password']:
            print('Success.')
            return i['ID'], i['role']
        else:
            continue
    print('Invalid username or password.')
    return None



# here are things to do in this function:
# add code that performs a login task
# ask a user for a username and password
# returns [ID, role] if valid, otherwise returning None

# define a function called exit
def exit():
    pass


# here are things to do in this function:
# write out all the tables that have been modified to the corresponding csv files
# By now, you know how to read in a csv file and transform it into a list of dictionaries. For this project, you also need to know how to do the reverse, i.e., writing out to a csv file given a list of dictionaries. See the link below for a tutorial on how to do this:

# https://www.pythonforbeginners.com/basics/list-of-dictionaries-to-csv-in-python


# make calls to the initializing and login functions defined above

initializing()
val = login()

# based on the return value for login, activate the code that performs activities according to the role defined for that person_id

if val[1] == 'admin':
    admin = Admin(my_DB.search('persons'),my_DB.search('login'),my_DB.search('project'))
    while True:
        user_choice = input('Select your choice:\n1.See project info\n2.Manage project\n3.Exit\n')
        if user_choice == '1':
            admin.see_project_info()
        elif user_choice == '2':
            admin.manage_info()
        elif user_choice == '3':
            pass

elif val[1] == 'student':
    student = Student(val[0], my_DB.search('login'),my_DB.search('student_pending'))
    while True:
        user_choice = input('Select your choice:\n1.See an invitation message\n3.Create Project\n4.Exit')
        if user_choice == '1':
            student.invitaion_detail()
        elif user_choice == '2':
            student.create_project()
        elif user_choice == '3':
            pass
# elif val[1] = 'member':
# see and do member related activities
# elif val[1] = 'lead':
# see and do lead related activities
# elif val[1] = 'faculty':
# see and do faculty related activities
# elif val[1] = 'advisor':
# see and do advisor related activities
else:
    print('Invalid role')
# once everyhthing is done, make a call to the exit function
exit()
