# Final project for 2023's 219114/115 Programming I
### A list of file in this project
  - database.py 
    - There are 4 classes in this files
      - the function is all about database(ex.convert,update,insert and etc.)
  - project_manage.py
    - initializing()
      - to read all .csv files and insert them in a table
    - login()
      - Ask user to enter username/password to proceed into program and return UserID and role
    - exit()
      - to convert the data and inset it back in to .csv files
    - Admin(class)
      - Can see a project info
      - Can manage the database
    - Student(class)
          - Can create a new project
          - Can see an invitation message and respond to it
      - Member(class)
        - Can see a project info of a group that you are in
      - Lead(class)
        - Can sent invitation to other member to form a group
        - Can sent invitation to faculty for ask them to be an advisor for us
    - Faculty(class)
          - Can see an invitation message and respond to it
          - Can see a project info 
          - Can evaluate the project like pass or fail
      - Advisor(class)
        - Can see a project info of all group and a group that you are an advisor
        - Can estimate and approve project 
      - Main code
        - that contain about variety of choice to choose when you logged in as any roles
  - All of this is a files to store data
    - login.csv
    - project.csv
    - advisor_pending_invitation.csv
    - student_pending_invitation.csv
   
### How to run the program
    - run the program(project_manage.py)
    - enter your username and password
    - choose the options you want to use
    - choose option 'Exit' once you finished

  The table detailing each role and its actions:

|  Role   | Action                                                         | Method                  |  Class  | Completion<br/>Percentage |
|:-------:|----------------------------------------------------------------|-------------------------|:-------:|--------------------------:|
|  Admin  | Insert information                                             | manage_info             |  Admin  |                      100% |
|  Admin  | Delete information                                             | manage_info             |  Admin  |                      100% |
|  Admin  | Edit information                                               | manage_info             |  Admin  |                       80% |
| Student | Create project                                                 | create_project          | Student |                       95% |
| Student | See an invitation request(to be group member)                  | invitation_detail       | Student |                       95% |
| Student | Respond to an invitation                                       | invitation_detail       | Student |                       95% |
| Member  | See project info(your own group)                               | show_group_info         | Member  |                      100% |
|  Lead   | Send an invitation to other student                            | send_invitation_member  |  Lead   |                       95% |
|  Lead   | Send an invitation to faculty                                  | send_invitation_advisor |  Lead   |                       95% |
|  Lead   | See project info(your own group)                               | show_project_detail     |  Lead   |                      100% |
|  Lead   | Submit project                                                 | submit_project          |  Lead   |                      100% |
| Faculty | See an invitation request(to be an advisor)                    | invitation_detail       | Faculty |                      100% |
| Faculty | Respond to an invitation                                       | invitation_detail       | Faculty |                      100% |
| Faculty | See all the project info                                       | show_project_detail     | Faculty |                      100% |
| Faculty | Evaluate project                                               | evaluate_project        | Faculty |                      100% |
| Advisor | See all project detail(also the group that you are an advisor) | show_project_detail     | Advisor |                      100% |
| Advisor | Evaluate project                                               | evaluate_project        | Advisor |                      100% | 
| Advisor | Approve project                                                | approve_project         | Advisor |                       90% |

### Missing features
    - i think that there a lot of features that i miss such as giving some feed back or something
    - Edit_information() in Admin class seems doesn't match the requirement that much
    - Since i didn't test a lots so maybe there will be a bug that i didn't find it :)
    
