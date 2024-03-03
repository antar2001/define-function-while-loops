i=1
while i<=5:
    print(i)
    i=i+1
    
i=0
while i<10:
    i=i+1
    if i%2==0:
        continue
    else:
        print(i)    
        
def user():
    print("Hello")
user()
def user(name):
    print("Hello, "+name.title()+"!")
user("Antar")    
def animals(pet,age):
    print("My "+pet.upper()+" is "+age+" years old")
animals('cat','7')    
        