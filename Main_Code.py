'''
Main File
=========

'''
def validate_mob(x):
    if x.isdigit() and len(x)==10:
        return 1
    else:
        return 0

def create_contact():
    fp=open('data.txt','a')
    n=input("Enter Name: ")
    mn=input("Enter Mobile Number:")
    res=validate_mob(mn)

    if res==1:
        a,b=search_mob(mn)

        if b==1:
            print("Number Already Exist")
        else:
            d=n+":"+mn+"\n"
            fp.write(d)
            fp.close()
            print("Contact Created Successfully!!")

    else:
        print("Enter a valid mobile number")

def display():
    fp=open('data.txt','r')
    d=fp.read()
    print("__________Contact Directory___________")
    print()
    print(d)
    
print("Welcome Contact Directory console App")
print()


def search_mob(n):
    
    fp=open('data.txt','r')
    data=fp.readlines()
    for x in data:
        l=x.split(":")
        if int(n) == int(l[1]):
            #print("Contact Found")
            #print(x)

            return x,1

    else:
        return '',0


def search_name():
    print("search contact number by name")
    ns=input("Enter name: ")
    fp=open('data.txt','r')
    data=fp.readlines()
    #print(data)

    flag=0

    for x in data:
        #print(x)
        l=x.split(":")
        #print(l)
        #print(l[0])

        if ns.upper()==l[0].upper():
            print(x)
            flag=1

    if flag==0:
        print("CONTACT NOT FOUND")

    fp.close()

while True:

    print("1. Create Contact")
    print("2. View Contact")
    print("3. Search by Name")
    print("4. Search by Contact Number")
    print("5. exit")

    ch=int(input("Enter your choice: "))
       
    if ch==1:
        create_contact()
        
    elif ch==2:
        display()

    elif ch==3:
        search_name()
        
    elif ch==4:
        ms=int(input("Enter Mobile Number: "))
        a,b=search_mob(ms)

        if b==1:
            print("Mobile Number Found")
            print(a)

        else:
            print("Contact Not Found")

    elif ch==5:
        break

    else:
        ("Enter a valid Number")


print("Thanks for using the App")
