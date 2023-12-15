print("*** LIBRARAY MANAGEMENT SYSTEM ***")

print()
print("**WELCOME***")
print("BELOW IS SOME INFORMATION ABOUT THE SYSTEM")
print("***READ ** IT ** CAREFULLY **")
print()
print("IF YOU WANT TO ISSUE THE BOOK YOU CAN DO IT!!")
print()
print("The Book numbers are Sequenced from 1 to 4")
print()
print("So when you want the book please give the input in Numbers from 1 to 4")
print()
print("PLEASE SELECT 1 FOR ISSUING THE BOOK")
print()
print("** 1=Motivational **")
print()
print("** 2=General Knowledge **")
print()
print("** 3=Educational **")
print()
print("** 4=Spiritual **")
print()
print()
a=int(input("ENTER THE BOOKS WHICH YOU WANT TO READ"))
print()

if(a==1):
    print("***WELCOME TO MOTIVATIONAL SECTION***")
    def motiv():
        print()
        j=int(input("ENTER THE BOOK N0:"))
        if(j==1):
            print("*Suddha Murthy*")
            print()
            print("Founder of Infosys")
            p= int(input("Are you interested for taking the book to Home:"))
            print()
            if (p == 1):
                print("***YES**")
                print("***This book is available for the issue ")
            else:
                print("***NO***")
                print()
                print("May be next week this book will be available")
        elif(j==2):
            print("*You Win Success*")
            print("This book tells us about the success path")
            q = int(input("Are you interested for taking the book to Home:"))
            print()
            if (q == 1):
                print("***YES**")
                print("***This book is available for the issue ")
            else:
                print("***NO***")
                print()
                print("May be next week this book will be available")
        elif(j==3):
            print("*Ikigai*")
            print("This book tells us about Lifestyle of Japaneese People")
            t= int(input("Are you interested for taking the book to Home:"))
            print()
            if (t == 1):
                print("***YES**")
                print("***This book is available for the issue ")
            else:
                print()
                print("***NO***")
                print()
                print("May be next week this book will be available")
        else:
            print("*** Please visit another section ***")
            print()
    motiv()
elif(a==2):
    def gk():
        print("***WELCOME TO GENERAL KNOWLEDGE SECTION***")
        print()
        k=int(input("ENTER THE BOOK NO:"))
        if(k==1):
            print("*Information about Plants*")
            print("This book tells about diiferent Speices of plants ")
            f=int(input("Enter"))
            if (f == 1):
                print("***YES**")
                print("***This book is available for the issue ")
            else:
                print()
                print("***NO***")
                print()
                print("May be next week this book will be available")
        elif(k==2):
            print("*Tourist Places*")
            print("Different places in the world ")
            h=int(input("ENTER"))
            if (h == 1):
                print("***YES**")
                print("***This book is available for the issue ")
            else:
                print()
                print("***NO***")
                print()
                print("May be next week this book will be available")
        elif(k==3):
            print("*World War*")
            print("Information about Wars between the Countries")
            i=int(input("ENTER"))
            if (i == 1):
                print("***YES**")
                print("***This book is available for the issue ")
            else:
                print()
                print("***NO***")
                print()
                print("May be next week this book will be available")
        else:
            print("*** Please visit another section ***")
            print()
    gk()
elif(a==3):
    print("*** WELCOME TO EDUCATIONAL BOOK SECTION***")
    print()
    def edu():
        l=int(input("** ENTER THE BOOK NO: **"))
        if(l==1):
            print("*DATA SCIENCE*")
            w=int(input("ENTER"))
            if (w== 1):
                print("***YES**")
                print("***This book is available for the issue ")
            else:
                print()
                print("***NO***")
                print()
                print("May be next week this book will be available")
        elif(l==2):
            print("*ARTIFICAL INTELLIGENCE")
            print()
            d=int(input("ENTER"))
            if (d == 1):
                print("***YES**")
                print("***This book is available for the issue ")
            else:
                print()
                print("***NO***")
                print()
                print("May be next week this book will be available")
        elif(l==3):
            print("*MACHINE LEARNING")
            print()
            y=int(input("ENTER"))
            if (y== 1):
                print("***YES**")
                print("***This book is available for the issue ")
            else:
                print()
                print("***NO***")
                print()
                print("May be next week this book will be available")
        elif(l==4):
            print("*PYTHON*")
            print()
            v=int(input("ENTER"))
            if (v== 1):
                print("***YES**")
                print("***This book is available for the issue ")
            else:
                print()
                print("***NO***")
                print()
                print("May be next week this book will be available")
        else:
            print("*** Please visit another section ***")
    edu()
elif(a==4):
    print("*** WELCOME TO SPIRITUAL BOOKS")
    print()
    def spir():
        s=int(input("ENTER THE BOOK NO:"))
        print()
        if(s==1):
            print("*RAMAYAN*")
            print("This is the book which tells us about life of Ram ")
            n=int(input("ENTER"))
            if (n == 1):
                print("***YES**")
                print("***This book is available for the issue ")
            else:
                print()
                print("***NO***")
                print()
                print("May be next week this book will be available")
        elif(s==2):
            print("*BHAGVAT GITA*")
            print("This is also one of the Hindu religion book")
            print()
            c=int(input("ENTER"))
            if (c == 1):
                print("***YES**")
                print("***This book is available for the issue ")
            else:
                print()
                print("***NO***")
                print()
                print("May be next week this book will be available")
        elif(s==3):
            print("*BIBLE*")
            print("This is the book which provide information about Jesus Christ")
            print()
            u=int(input("ENTER"))
            if (u == 1):
                print("***YES**")
                print("***This book is available for the issue ")
            else:
                print()
                print("***NO***")
                print()
                print("May be next week this book will be available")
        else:
            print("*** Please visit another section ***")
    spir()

else:
    print("*** INVALID ***")
