# MY  SIMPLE CALCULATOR

opt = 0
while( opt < 8):
  print("***************** CALCULATOR *****************")
  print("1. Add ","2. Subtract ","3. Multiply ","4. Divide ","5. Floor Division ","6. Exponentiation ","7. Modulo","8. Exit ",sep='\n')
  opt = int(input("Enter your choice: "))
  if(opt == 8):
      print("Thank You Visit Again !!")
      print("******************** :) ************************")
      break
  a = input("Enter a: ")
  b = input("Enter b: ")
  if opt > 0 and opt < 8:
    if(opt == 1):
      c = float(a) +float(b)
      print("Addition :",a,"+",b,"=",c)
      print("*************************************************")
    if(opt == 2):
      c = float(a)-float(b)
      print("Subtraction :",a,"-",b,"=",c)
      print("*************************************************")
    if(opt == 3):
      c = float(a)*float(b)
      print("Multiplication :",a,"x",b,"=",c)
      print("*************************************************")
    if(opt == 4):
      c = float(a)/float(b)
      print("Division :",a,"/",b,"=",c)
      print("*************************************************")
    if(opt == 5):
      c = float(a)//float(b)
      print("Floor Division :",a,"//",b,"=",c)
      print("*************************************************")
    if(opt == 6):
      c = float(a)**float(b)
      print("Expotentiation :",a,"^",b,"=",c)
      print("*************************************************")
    if(opt == 7):
      c = int(a)%int(b)
      print("Modulus :",a,"%",b,"=",c)
      print("*************************************************")
  else:
    print("Enter Correct option :")
    opt = int(input("Enter your choice: "))
    print("1. Add ","2. Subtract ","3. Multiply ","4. Divide ","5. Floor Division ","6. Exponentiation ","7. Modulo","8. Exit ",sep='\n')
  

