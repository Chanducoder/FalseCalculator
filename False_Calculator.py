# I have created a false calculator which will also show some wrong answers to prank people
# I have created a function to manage the calculations
def falseCal():
    print("Select Your operator from (*, /, +, -)\n")
    operator = input()

    if operator=="*":
        print("Choose First Number")
        a = int(input())
        print("Choose Second Number")
        b = int(input())
        if a==45 and b==3 or a==3 and b==45:
            print("555")
        else:
            print(a*b)
    elif operator=="+":
        print("Choose First Number")
        a = int(input())
        print("Choose Second Number")
        b = int(input())
        if a==56 and b==9 or a==9 and b==56:
            print("77")
        else:
            print(a+b)
    elif operator=="-":
        print("Choose First Number")
        a = int(input())
        print("Choose Second Number")
        b = int(input())
        print(a-b)
    elif operator=="/":
        print("Choose First Number")
        a = int(input())
        print("Choose Second Number")
        b = int(input())
        if a==56 and b==6:
            print("4")
        else:
            print(a/b) 
    else:
        print("Choose the operator properly")

# I have created a for else conditionals so that you don't have to restart programs again and again.
falseCal()
print("Do you want to use the calculator again. Type Y for Yes and N for no.")
z = input()
if z=="Y" or z=="y":
    falseCal()
elif z=="N" or z=="n":
    exit

# Thanks for checking my code. It took 30 minutes to code this.
