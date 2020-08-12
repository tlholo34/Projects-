import datetime
from datetime import date

#we open our users.txt 
file1 = open('user.txt','r')

users = {}
#for all the lines in users.txt
for lines in file1:
    #we strip the new line
    lines = lines.strip('\n')
    #make a list of all the items in the file
    userls = lines.split(', ')
    #add items into the dictionary
    users[userls[0]] = userls[1] 

#ask the user to enter a name
user_name1 = input("enter your User name here: ")
#while the answer is not in the users dictionary
while not user_name1 in users:
    #we print this statment
    print("This is an invalid user name")
    #and ask for the users user name
    user_name1 = input("enter your User name here: ")
#here we get the value of the user name they used
x = users.get(user_name1)
#we ask the user to give us the password
password = input("enter your password here: ")
#while the password is not equal to the value of the user name
while password != x:
    #we print this
    print("this is an invalid password.")
    #and ask the user to enter a password
    password = input("enter your password here: ")
file1.close()

def task_overview():
    file1 = open('tasks.txt','r')
    number_of_tasks = 0
    completed_tasks = 0
    uncomplete_task = 0
    over_dueTask = 0
    current_date = date.today()
    #for item in file1 
    for i in file1:
        #we increment the number of tasks
        number_of_tasks += 1
        i = i.strip('\n')
        #make a list of all the lines in the file 
        taskls = i.split(', ')
        #convert the date in the list bake to a date format
        date_object = datetime.datetime.strptime(taskls[3], '%d %b %Y').date()
        #if the task is completed
        if taskls[-1].upper() == "YES":
            # we increment the number of tasks
            completed_tasks += 1
        else:
            #otherwise we increament the number of uncomplete tasks
            uncomplete_task += 1
        # if the task is uncomplete
        if taskls[-1].upper() =="NO":
            #if the the task is over due
            if  date_object <  current_date:
                #we increment the over_due tasks 
                over_dueTask += 1
        #we calculate the percantage here 
        total_per = uncomplete_task/number_of_tasks*100
        total_over = over_dueTask/number_of_tasks*100       
    #we write the output here
    file3 = open('task_overview.txt','w')
    file3.write("the number of tasks: "+str(number_of_tasks)+'\n'+
    "Number of completed tasks: "+str(completed_tasks)+'\n'+
    'Number of incomplete tasks: '+str(uncomplete_task)+'\n'+
    "Number of over due tasks: "+str(over_dueTask)+
    "\n"+str(round(total_per,2))+"%"+" of the work are uncomplete"
    +"\n"+str(round(total_over,2))+"%"+" of the work are over due")

    file1.close()


def user_overview(user_name):
    file1 = open('tasks.txt','r')
    file2 = open('user.txt','r')
    total_users = 0
    #for all the users in file2(user.txt)
    for i in file2:
        #we increment the total users
        total_users += 1
    number_of_tasks = 0
    total_tasks = 0
    uncomplete_tasks = 0
    current_date = date.today()
    over_dueTask = 0
    completed_tasks = 0
    #for items in file1 (tasks.txt)
    for i in file1:
        i = i.strip('\n')
        #make a list of all the items
        taskls = i.split(', ')
        #we increment the number of total_tasks
        total_tasks += 1
        #we convert the string date back to the date format
        date_object = datetime.datetime.strptime(taskls[3], '%d %b %Y').date()
        #if the user name is the same as the one in file
        if user_name.upper() == taskls[0].upper():
            #we increment the number of tasks for the user
            number_of_tasks += 1
            # if the users task is not complete
            if taskls[-1].upper() == "NO":
                #we increment the the uncomplete tasks 
                uncomplete_tasks += 1
                #if the task is over due 
                if date_object <  current_date:
                    #we increment the overs due tasks
                    over_dueTask += 1
            else:
                #otherwise we increment the completed tasks
                completed_tasks += 1

    #we calculating the percentage here
    user_task=number_of_tasks/total_tasks*100
    uncom_per = 0.0
    over_per = 0.0
    over_per = 0.0
    #this only runs when the number of tasks are 0
    if number_of_tasks > 0:
        com_per = completed_tasks/number_of_tasks*100
        uncom_per = uncomplete_tasks/number_of_tasks*100
    #this only runs when the number of uncompleted tasks are 0 
    if uncomplete_tasks > 0:
        over_per = over_dueTask/uncomplete_tasks*100
    
    file1.close()
    file2.close()

    #we return the output here 
    return ("\n==============="+"\nDetails for username: "+ user_name +
    "\nYour total number of tasks: "+str(number_of_tasks)+
    "\n"+str(round(user_task,2))+"%"+" of the tasks are assigned to you"+
    "\n"+str(round(com_per,2))+"%"+" of your work has been completed."+
    "\n"+str(round(uncom_per,2))+"%"+" of your work still needs to be completed."+
    "\n"+str(round(over_per,2))+"%"+" of your work is overdue and uncomplete.\n")


def gerate_reports():
    file1 = open('tasks.txt','r')
    file2 = open('user.txt','r')
    total_users = 0
    #for all the users in file2(user.txt)
    for i in file2:
        i = i.split()
        #we increment the total users
        total_users += 1
    total_tasks = 0
    for i in file1:
        #we increment the number of total tasks
        total_tasks += 1

    file1.close()
    file2.close()

    file3 = open('user_overview.txt','w')
    usoverview = ""

    for key in users.keys():
        #we add to the empty string
        usoverview += user_overview(key)
    
    #we write the output into the file here
    file3.write("total number of users: "+str(total_users)+
    "\ntotal number of tasks: "+str(total_tasks)+ usoverview)
    task_overview()


def reg_user():
    file1 = open('user.txt','r+')
    #we ask the admin to enter a new user name
    user_name1 = input("enter your new user name here: ")
    #while user name is not in dictionary user
    while user_name1 in users:
        #we print this
        print("this user already exists!")
        #we ask the user to enter a new user name
        user_name1 = input("enter a new user name here: ")

    #we ask the admin to enter a password
    password = input ("enter your new password here: ")
    #we ask admin to enter the password again
    re_enter = input("re-enter your password here: ")

    #while the password is not the same as the first password
    while re_enter != password:
        #we print this
        print("your passwords dont match.") 
        #and ask the admin to re-enter the password
        re_enter = input("re-enter password here.")
    file1.read()
    #we write the new user name and password into the user.txt
    file1.write('\n'+user_name1+", "+password)
    file1.close()
    print("done!")



def add_task():
    #we ask for the user name that the task is assigned to
    user_name1 = input("Enter your user name the task is assigned to: ")
    #we ask for the title of the task
    title_task = input("Enter the title of the task: ")
    #we ask for the description of the task
    description = input("Enter the description of the task here: ")
    #we ask for the due date
    due_date = input("Enter the due date of the task here eg.30 Jul 2020: ")
    #we assign todays date to d
    d =datetime.datetime.today().__format__("%d %b %Y")
    #we assign end_date to no 
    end_date =  'No'
    file1 = open('tasks.txt','r+')
    file1.read()
    #we write all the information into the tasks.txt file
    file1.write('\n'+user_name1+', '+title_task+', '+description+', '+due_date+', '+str(d)+', '+end_date)
    file1.close()
    print('done!')

    

def view_all():
    file1 = open('tasks.txt','r')
    #for items in taske.txt
    for i in file1:
        #we split all the items
        taskls = i.split(', ')
        #we print all the information in this format
        print("User name: "+taskls[0]+"\n"
        +"Title of the task: "+taskls[1]+"\n"
        +"Due date: "+taskls[3]+"\n"
        +"Date assigned: "+taskls[4]+"\n"
        +"Task complete?: "+taskls[5]
        +"Description of the task: "+taskls[2]+"\n")
    file1.close()



def veiw_mine():
    file1 = open('tasks.txt','r')
    count = 0
    all_tasks = []
    #for all the items in task.txt
    for i in file1:
        #we split the information
        taskls = i.split(', ')
        #we add it to a file which will hold all the taks
        all_tasks.append(taskls)        
        #if the user name is equel to the user name of the list
        if user_name1 == taskls[0]:            
            #we print the information form the list in this format
            print("\n"+str(count)+" - Title of the task: "+taskls[1])
        count = count + 1
    while True:
        print("enter -1 to exit.")
        #we ask the user which task they would like to edit
        option2 = int(input("which task would you like to edit: "))
        if option2 <= count and option2 >= 0:
            #we ask the user what they would like to do 
            option3 = input("s - mark as complete\n"+
            "c - change the user name the task is assigned to\n"+
            "d - change the due date of the task\n"+
            "here -->")

            #we assign the users option to usersOP
            userOp = all_tasks[option2]
            
            #if the user enters s
            if option3 == 's':
                #if the task is complete
                if userOp[-1].upper() == "YES\n":
                    #we print this
                    print("this task has alredy been completed")
                else:
                    #else we replace the no to yes
                    userOp[-1] = "Yes\n"
                    print("Done!")
            #if the user enters c
            if option3 == 'c':
                #we ask the user to enter the user name
                new_user = input("enter user name here: ")
                #while the user is not in the task
                while not new_user in users:
                    #we print this
                    print("this user does not exist!")
                    #we ask the user to enter a user name
                    new_user = input("enter user name here: ")
                #we replace the the user in the list with the new user the admin has added 
                userOp[0] = new_user
                print("Done!")
            #if the user enters d
            if option3 == 'd':
                #we ask the user to enter a new date in this format
                new_date = input("Enter the new due date e.g 23 Apr 2020: ")
                userOp[3] = new_date
                # we print this 
                print("Done! your new date is now: "+str(new_date))
            all_tasks[option2] = userOp
        #if the option is -1 we exit the loop
        elif option2 == -1:
            break
        #else we print this 
        else:
            print ("This is an invalid option.")
        file2= open('tasks.txt','w')
        file2.flush()
        #we write into the file
        for i in all_tasks:
            file2.write(", ".join(i))
        file2.close()
    file1.close()

def displayStats():
    gerate_reports()
    file1 = open('task_overview.txt','r')
    file2 = open('user_overview.txt','r')
    #we print each line
    for i in file1:
        print(i)
    for i in file2:
        print(i)

    file1.close()
    file2.close()


while True:
    #if the user name is admin
    if user_name1 == 'admin':
        #we show them this menu
        options = str(input("Please enter one of the following options:\n"+
        "a - add task\n"+
        "r - register user\n"+
        "va- veiw all tasks\n"+
        "vm- veiw my tasks\n"+
        "gr- generate reports\n"+
        "ds- display stastistics\n"+
        "e - exit\n"+
        "here--> "))

    else:
        #else we show them this menu 
        options = str(input("please enter one of the following options: \n"+
        "a - add task\n"+
        "va- veiw all tasks\n"+
        "vm- veiw my tasks\n"+
        "e - exit\n"
        "here--> "))


    #if user/admin enters vm
    if options == 'vm':
        veiw_mine()

    #if user/admin enters va
    if options == 'va':
        view_all()

    #if user/admin enters a
    if options == 'a':
        add_task()

    #if the admin enters r from the menu 
    if options == 'r':
        reg_user()

    #if the admin enters ds
    if options == 'ds':
        displayStats()
        

    #if the admin enters gr
    if options == 'gr':
        gerate_reports()
        
    #if the admin/user enters e
    if options == 'e':
        break
