# import database module
from database import Read, Table, Database
from random import randint

# define a funcion called initializing
my_DB = Database()
read = Read()


class Admin:
    def __init__(self, id):
        self.id = id


    def see_project_info(self):
        print(_project.table)

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
                _person.insert({'ID': user_id, 'first': first_name, 'last': last_name, 'type': type})
                _login.insert({'ID': user_id, 'username': username, 'password': password, 'role': type})
                print(f'{user_id} {username} has added to the database')
            elif user_choice == '2':
                remove_id = input('User_id you want to delete: ')
                for person in _person.table:
                    if person['ID'] == remove_id:
                        _person.table.remove(person)
                for person in _login.table:
                    if person['ID'] == remove_id:
                        _login.table.remove(person)
            elif user_choice == '3':
                edit_id = input('User_id you want to edit: ')
                for person in _login.table:
                    if person['ID'] == edit_id:
                        print(f"{person['ID']}\n"
                              f"{person['username']} {person['password']}\n"
                              f" {person['role']}")
                change_choice = input('Select what to change:\n'
                                      '1.Password\n2.Role')
                if change_choice == '1':
                    new_password = randint(1000, 9999)
                    for person in _login.table:
                        if person['ID'] == edit_id:
                            person['password'] = new_password
                    print('The new password is:', new_password)
                elif change_choice == '2':
                    new_role = input('Enter new role:')
                    for person in _login.table:
                        if person['ID'] == edit_id:
                            person['role'] = new_role
            elif user_choice == '4':
                break
            else:
                print('Choice invalid. Please try again!')


class Student:
    def __init__(self, id):
        self.id = id
        # for i in _login:
        #     if i['ID'] == id:
        #         self.username = i['username']
        #         self.role = i['role']

    def create_project(self):
        print('Creating project....')
        project_name = input('Enter your project name: ')
        project_id = randint(000000, 999999)
        project_info = {'ProjectID': project_id,'Projectname': project_name,'Lead': self.id, 'Member1': '-',
                        'Member2': '-', 'Advisor': '-','Status': 'Working'}
        _login.update('ID',self.id,'role','lead')
        project_table = my_DB.search('project_table')
        project_table.table.insert(project_info)

    def invitation_detail(self):
        invitation_count = 0
        for i in student_pending.table:
            if i['ReceiverID'] == self.id:
                print(f"ProjectID: {i['ProjectID']}, LeadID: {i['InviterID']}")
                invitation_count += 1
            else:
                continue
        if invitation_count == 0:
            print('There are no invitation yet')
            return
        #TODOถามก่อนใส่ชื่อโปรเจ็ก
        respond = input('Enter project: ')
        for i in student_pending.table:
            if i['ProjectID'] == respond and i['ReceiverID'] == self.id:
                choice = input(f"Do you want to accept this {i['ProjectID']} from {i['InviterID']} (y/n): ")
                if choice.lower() == 'y':
                    i['Respond'] = 'Accepted'
                    self.role = 'member'
                    print(f'You are now a member of {i["ProjectID"]}')
                    _login.update('ID',self.id,'role','member')
                    student_pending.update2('ProjectID',respond,'ReceiverID',self.id,'Respond','Accepted')
                    #TODO:check group member,update project.csv
                elif choice.lower() == 'n':
                    i['Respond'] = 'Deny'
                    print(f'You have denied the invitation')
                    student_pending.update2('ProjectID', respond, 'ReceiverID', self.id, 'Respond', 'Deny')
                else:
                    print('Invalid choice.')
                    #TODO:update back to csv file
class Member:
    def __init__(self,id,projectID):
        self.id = id
        self.projectID = projectID
    def show_group_info(self):
        print(_project.table.filter(lambda x: x['ProjectID'] == self.projectID))


class Lead:
    def __init__(self,id,projectID):
        self.id = id
        self.projectID = projectID

    def send_invitation_member(self):
        receiverID = input('Enter ID who you want to invite: ')
        member_info = {'ProjectID': self.projectID, 'InviterID': self.id, 'ReceiverID': receiverID, 'Respond': 'Pending'}
        student_pending.insert(member_info)

    def send_invitation_advisor(self):
        advisorID = input('Enter ID who you want to invite: ')
        advisor_info = {'ProjectID': self.projectID, 'InviterID': self.id, 'ReceiverID': advisorID, 'Respond': 'Pending'}
        advisor_pending.insert(advisor_info)

    def show_project_detail(self):
        print(_project.table.filter(lambda x: x['ProjectID'] == self.projectID))

    def submit_project(self):
        _project.update2('ProjectID', self.projectID, 'Status', 'sent')
        # save('project')
        print('Project sent.')


class Faculty:
    def __init__(self,id):
        self.id = id


    def invitation_detail(self):
        invitation_count = 0
        for i in advisor_pending.table:
            if i['AdvisorID'] == self.id:
                print(f"ProjectID: {i['ProjectID']}, LeadID: {i['InviterID']}")
                invitation_count += 1
            else:
                continue
        if invitation_count == 0:
            print('There are no invitation yet')
            return
        # TODOถามก่อนใส่ชื่อโปรเจ็ก
        respond = input('Enter project: ')
        for i in advisor_pending.table:
            if i['ProjectID'] == respond and i['AdvisorID'] == self.id:
                choice = input(f"Do you want to accept this {i['ProjectID']} from {i['InviterID']} (y/n): ")
                if choice.lower() == 'y':
                    i['Respond'] = 'Accepted'
                    print(f'You are now an advisor of {i["ProjectID"]}')
                    _login.update('ID', self.id, 'role', 'advisor')
                    advisor_pending.update2('ProjectID', respond, 'AdvisorID', self.id, 'Respond', 'Accepted')
                    # TODO:check group member,update project.csv
                elif choice.lower() == 'n':
                    i['Respond'] = 'Deny'
                    print(f'You have denied the invitation')
                    advisor_pending.update2('ProjectID', respond, 'AdvisorID', self.id, 'Respond', 'Deny')
                else:
                    print('Invalid choice.')
                    # TODO:update back to csv file

    def show_project_detail(self):
        print(_project.table)

    def evaluate_project(self):
        advisor_choice = input('Enter project id you want to evaluate: ')
        for i in _project.table:
            if i['ProjectID'] == advisor_choice and i['Status'] == 'sent':
                evaluate = input('Pass or Failed(p/f):')
                if evaluate.lower() == 'p':
                    _project.update('ProjectID',advisor_choice,'Status','Passed')
                elif evaluate.lower() == 'f':
                    _project.update('ProjectID',advisor_choice,'Status','Failed')
            else:
                print('Invalid project')
class Advisor()


def initializing():
    # here are things to do in this function:
    # create an object to read all csv files that will serve as a persistent state for this program
    read_person = read.read_data('persons.csv')
    read_login = read.read_data('login.csv')
    read_project = read.read_data('project.csv')
    read_student_pending = read.read_data('student_pending_invitation.csv')
    read_advisor_pending = read.read_data('advisor_pending_invitation.csv')

    # create all the corresponding tables for those csv files
    person_table = Table('persons', read_person)
    login_table = Table('login', read_login)
    project_table = Table('project', read_project)
    student_pending_table = Table('student_pending', read_student_pending)
    advisor_pending_talbe = Table('advisor_pending', read_advisor_pending)
    # see the guide how many tables are needed
    # add all these tables to the database
    my_DB.insert(person_table)
    my_DB.insert(login_table)
    my_DB.insert(project_table)
    my_DB.insert(student_pending_table)
    my_DB.insert(advisor_pending_talbe)
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
_person = my_DB.search('persons')
_login =  my_DB.search('login')
_project = my_DB.search('project')
student_pending = my_DB.search('student_pending')
advisor_pending = my_DB.search('advisor_pending')
# for i in _login:
#     if i['ID'] == id:
#         username = i['username']
#         role = i['role']

# based on the return value for login, activate the code that performs activities according to the role defined for that person_id

if val[1] == 'admin':
    admin = Admin(val[0])
    while True:
        user_choice = input('Select your choice:\n1.See project info\n2.Manage project\n3.Exit\n')
        if user_choice == '1':
            admin.see_project_info()
        elif user_choice == '2':
            admin.manage_info()
        elif user_choice == '3':
            pass

elif val[1] == 'student':
    student = Student(val[0])
    while True:
        user_choice = input('Select your choice:\n1.See an invitation message\n3.Create Project\n4.Exit')
        if user_choice == '1':
            student.invitation_detail()
        elif user_choice == '2':
            student.create_project()
        elif user_choice == '3':
            pass
elif val[1] == 'member':
    projectID = ''
    for i in _project.table:
        if i['Member1'] or i['Member2'] == val[0]:
            projectID = i['ProjectID']
    member = Member(val[0],projectID)
    while True:
        user_choice = input('Select your choice:\n1.See project info\n2.Exit')
        if user_choice == '1':
            member.show_group_info()
        elif user_choice == '2':
            pass
elif val[1] == 'lead':
    projectID = ''
    for i in _project.table:
        if i['Lead'] == val[0]:
            projectID = i['ProjectID']
    lead = Lead(val[0],projectID)
    while True:
        user_choice = input('Select your choice:\n1.Send invitation to a member\n'
                            '2.Send invitation to an advisor\n3.See and edit project\n'
                            '4.Submit project\n5.Exit ')
        if user_choice == '1':
            lead.send_invitation_member()
        elif user_choice == '2':
            lead.send_invitation_advisor()
        elif user_choice == '3':
            lead.show_project_detail()
        elif user_choice == '4':
            lead.submit_project()
        elif user_choice == '5':
            pass
elif val[1] == 'faculty':
    faculty = Faculty()
    while True:
        user_choice = input('1.See an invitation message\n2.See project detail\n3.Evaluate project\n4.Exit')
        if user_choice == '1':
            faculty.invitation_detail()
        elif user_choice == '2':
            faculty.show_project_detail()
        elif user_choice == '3':
            faculty.evaluate_project()
        elif user_choice == '4':
            pass
elif val[1] == 'advisor':
    advisor = Advisor()
    while True:
        user_choice = input('1.See project detail\n2.Evaluate project\n3.Approve project\n4.Exit')
else:
    print('Invalid role')
# once everyhthing is done, make a call to the exit function
exit()
