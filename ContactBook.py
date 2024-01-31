Contact = []

def buffer(j):
    k=1
    for i in Contact:
        if(k==j): return i
        k+=1

def Add():
    name = input()
    phone = input()
    address = input()
    profile = {'name': name,'phone': phone, 'address':address}
    Contact.append(profile)
    print("Contact after adding!")
    Show()

def Show():
    for i in Contact: 
        print('Name :',i['name'])
        print('Phone :',i['phone'])
        print('Address :',i['address'])

def Remove():
    print("Enter contact sequence!")
    q= int(input())
    Contact.pop(q-1)
    print("Contact after removing the item!")
    Show()

def Update():
      print('Enter contact sequence to update!')
      q = int(input())
      loc = buffer(q)
      while(True):
          print("Want to update! Enter 1 for Yes, 2 for No")
          q2 = int(input())
          if(q2==2): break
          print("Enter 1 to update name, 2 to update phone and 3 to update address")
          q3 = int(input())
          if(q3==1): 
              print("Enter updated name!")
              n = input()
              loc['name'] = n
              print("Contact after updating!")
              Show()
          elif(q3==2): 
              print("Enter updated phone!")
              n = input()
              loc['phone'] = n
              print("Contact after updating!")
              Show()
          elif(q3==3): 
              print("Enter updated address!")
              n = input()
              loc['address'] = n
              print("Contact after updating!")
              Show()
          else: print("Wrong Input!")

while(True): 
    print("1 for Add Contact")
    print("2 for Show Contact")
    print("3 for Remove Contact")
    print("4 for Update Contact")
    print("5 for Exit")
    q1=int(input())
    if(q1==5): break
    elif(q1==1): Add()
    elif(q1==2): Show()
    elif(q1==3): Remove()
    elif(q1==4): Update()
    else: print("Wrong Input!")
    
