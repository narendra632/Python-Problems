class Library:
    def __init__(self, list, name):
        self.booklist = list
        self.name = name
        self.lenddict = {}

    def displaybooks(self):
        print(f"We have the following books in our Library:{self.name}")
        for book in self.booklist:
            print(book)
    def lendbook(self, user, book):
        if book not in self.lenddict.keys():
            self.lenddict.update({book:user})
            print("Book-list has been Updated. You can choose the book now")
        else:
            print(f"Books is already been taken by {self.lenddict[book]}")
    def addbook(self, book):
        self.booklist.append(book)
        print("Book has been added to the Library")
    def returnbook(self, book):
        self.lenddict.pop(book)

if __name__ == '__main__':
    narendra = Library(["Psychology of money","Ikigai","Rich dad Poor dad"],"Narendra's Library")

    while(True):
        print(f"Welcome to the {narendra.name} library. Enter your chioce to continue")
        print("1. Display Books")
        print("2. Lend a Books")
        print("3. Add a Books")
        print("4. Return Books")
        user_choice=(input())
        if user_choice not in ['1','2','3','4']:
            print("Please enter a valid option")
            continue
        else:
            user_choice= int(user_choice)

        if user_choice==1:
            narendra.displaybooks()
        elif user_choice==2:
            book = input("Enter the book you want to lend:")
            user = input("Enter your name:")
            if book not in ["Psychology of money","Ikigai","Rich dad Poor dad"]:
                print("sorry we don't have this book")
            else:
                narendra.lendbook(user,book)
        elif user_choice==3:
            book = input("Enter the book you want to add:")
            narendra.addbook(book)
        elif user_choice==4:
            book = input("Enter the book you want to return:")
            narendra.returnbook(book)
        else:
            print("Not a valid option")
       
        print("Press q to quit or c to continue")
        user_choice2 = ""
        while(user_choice2!="c" and user_choice2!="q"):
            user_choice2=input()
            if user_choice2=="q":
                exit()
            elif user_choice2=="c":
                continue

