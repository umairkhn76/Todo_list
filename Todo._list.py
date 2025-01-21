def myfun():
    for i in range(1,task+1):
        mytask=input("Enter the task ")
        l1.append(mytask)
    return l1

def add():
    yourtask=input("Enter your new task")
    l1.append(yourtask)
    return l1

def delete():
    yourdel=input("Enter the task")
    if yourdel in l1:
        l1.remove(yourdel)
    return l1

def update():
    utask=input("Enter the task")
    if utask in l1:
        new=input("Enter the new")
        ind=l1.index(utask)
        l1[ind]=new
    return l1

def myseen():
    return l1

task=int(input("Enter the no of task"))
l1=[]
print(myfun())
print("Enter 1 for add a new task")
print("Enter 2 for delete a new task")
print("Enter 3 for update a new task")
print("Enter 4 for seen")
choice=int(input("Enter the choice"))
if choice==1:
    print(add())
elif choice==2:
    print(delete())
elif choice==3:
    print(update())
elif choice==4:
    print(myseen())
