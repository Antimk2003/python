num1 =int(input("Enter the number :="))
num2 =int(input("Enter the number :="))
operater =input("Enter the operater ,+,_,/,//,%,*:=" )
if operater == "+":
    print("add",num1+num2) 
elif operater == "-":
    print("sub",num1-num2)
elif operater == "*":
    print("multi",num1*num2)  
elif operater == "/":
    print("divi",num1/num2)          
elif operater == "%":
    print("modu",num1%num2)
else:
    print("Enter a right operater")    