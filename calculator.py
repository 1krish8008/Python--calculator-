while True :
   num1=float(input("enter first number:"))
   num2=float(input("enter sec number:"))
   operation= input("choose operation(+,-,*,/,**:,)")
   if operation== "+":
       print("Result=",num1+num2)
   elif operation=="-" :
       print("Result=",num1-num2)
   elif operation=="*":
       print("Result=",num1*num2)
   elif operation=="/":
       print("Result=",num1/num2)
   elif operation=="**":
       print("Result=",num1**num2)
   else:
       print("Invalid operation")
   again=input("do you want calculate again? (yes/no,)")
   if  again=="no":
         break