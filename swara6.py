def add_project():
  sProject_Id=input("Enter the Project_Id:->=")
  Project_Id.append(sProject_Id)
  sName=input("Enter the Name:->")
  Name.append(sName)
  sDescription=input("Enter the Description:->")
  Description.append(sDescription)
  sStarting_Date=input("enter the Starting_Date:->")
  Starting_Date.append(sStarting_Date)
  sEnd_Date=input("Eter the End_Date:->")
  End_Date.append(sEnd_Date)
  sTask_Ids=input("Enter the Task_Ids:->")
  Task_Ids.append(sTask_Ids)

def view_project():
    print("project_Id \t Name \t Description \t Starting_Date \t End_Date \t Task_Ids ")
    for i in range(len(Project_Id)):
      print(Project_Id[i],"\t",Name[i],"\t",Description[i],"\t",Starting_Date[i],"\t",End_Date[i],"\t",Task_Ids[i])

def update_project():
  fProject_Id=input("Enter find Project_Id:->")  
  for i in range(len(Project_Id)):
    uProject_Id=input("Enter the Project_Id:->")
    uName=input("Enter the Name:->")
    uDescription=input("Enter the Description:->")
    uStarting_Date=input("Enter the Starting_Date:->")
    uEnd_Date=input("Enter the End_Date:->")
    uTask_Ids=input("Enter the Task_Ids:->")
    Project_Id[i]=uProject_Id
    Name[i]=uName
    Description[i]=uDescription
    Starting_Date[i]=uStarting_Date
    End_Date[i]=uEnd_Date
    Task_Ids[i]=uTask_Ids

def delete_project():
  dName=input("Enter the delete Name:->")
  for i in range(len(Name)):
    if(Name[i]==dName):
      Project_Id.remove(Project_Id[i])
      Name.remove(Name[i])
      Description.remove(Description[i])
      Starting_Date.remove(Starting_Date[i])
      End_Date.remove(End_Date[i])
      Task_Ids.remove(Task_Ids[i])
      break

def ongoing_project():
     countt=0
     for i in range(len(Project_Id)):
               countt+=1
     print("Total number of Student with:-> ",countt)

def task_report():
     rProject_Id=input("\nEnter the Project_Id:-> ") 
     print("\nProject_Id \t Name \t Description \t Starting_Date \t End_Date \t Task_Ids")
     for i in range(len(Project_Id)):
          if(Project_Id[i]==rProject_Id):
             print(Project_Id[i],"\t",Name[i],"\t",Description[i],"\t",Starting_Date[i],"\t",End_Date[i],"\t",Task_Ids[i])

Project_Id=[]
Name=[]
Description=[]
Starting_Date=[]
End_Date=[]
Task_Ids=[]

count=3
while(count!=0):
  username=input("Enter the username:->")
  password=input("Enter the password:->")
  if(username=="swara" and password=="swara12"):
    print("login successfully....!!")
    count=0
    cnt=1

    while(cnt!=0):
      print("*** Project Management ***\n")
      print("\n[1]. Add Employees   ")
      print("[2]. View list   ")
      print("[3]. Update   ")
      print("[4]. Delete   ")
      print("[5]. ongoing_project ")
      print("[6]. task_report ")
      print("[7]. Exit   \n")

      ch=int(input("Enter the choice:->"))

      if(ch==1):
        print("\nAdd project")
        add_project()
      if(ch==2):
        print("View list")
        view_project()
      if(ch==3):
        print("Update")
        update_project()
      if(ch==4):
        print("Delete")
        delete_project()
      if(ch==5):
        print("ongoing_projec")
        ongoing_project()
      if(ch==6):
         print("task_report()")
         task_report()
      if(ch==7):
        print("Exit\n")
    
        cnt=0
        count=1

  elif(username!="swara" and password!="swara12"):
    print("uname & password incorrect")
  elif(username!="swara"):
    print("uname incorrect")
  elif(password!="swara12"):
    print("password is incorrect")

  count-=1
  print("remaining attempt=",count)