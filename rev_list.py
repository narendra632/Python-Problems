
print("Enter the numbers of the list one by one\n")
size=int(input("Enter size of list\n"))

mylist=[]
for i in range(size):
    mylist.append(int(input("Enter list Element\n")))

print(f'Your list is {mylist}')

mylist.reverse()
print(mylist)










