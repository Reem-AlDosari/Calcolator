#multiple two numbers
def  multiply_Function(x,y):
  return x*y
#add two numbers
def  add_Function(x,y):
    return x+y
#substract two numbers 
def  substract_Function(x,y):
    return x-y
#divide two numbers
def  divide_Function(x,y):
    return x/y


print("Choose the operation you want")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")

while True:
        #read user input
        choice=input("Enter your choice (1,2,3,4):")
        #check if choice is one of the four option
        if choice in ('1','2','3','4'):
            try:
                num1=float(input("Enter your first number: "))
                num2=float(input("Enter your second number: "))
            except ValueError:
                print("invalid input, please enter numbers again")
                continue
            if choice=='1':
              print(num1, "+",num2,"= ",add_Function(num1,num2)) 
            elif choice=='2':
                print(num1,"-",num2,"= ",substract_Function(num1,num2)) 
            elif choice=='3':
              print(num1,"*",num2,"= ",multiply_Function(num1,num2))
            elif choice=='4':
             print(num1,"/",num2,"=", divide_Function(num1,num2))

            next_Calculation=input("Do you want to continue the operation? (yes/no): ")
            if(next_Calculation)=="no":
                break
        else:
            print("invalid input")