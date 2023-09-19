a=int(input("enter jug A capacity:"))
b=int(input("enter jug B capacity:"))
ai=int(input("initially water in jug A:"))
bi=int(input("initially water in jug B:"))
af=int(input("final state of jug A:"))
bf=int(input("final state of jug B:"))
print("list of operations you can do:\n")
print("1.fill jug A completely \n")
print("2.fill jug B completely \n")
print("3.empty jug A completely \n")
print("4.empty jug B completely \n")
print("5.pour from jug A fill jug B filled completely or A becomes empty \n")
print("6.pour from jug B till jug A filled completely or B becomes empty \n")
print("7.pour all from jug B to jug A \n")
print("8. pour all from jug A to jug B \n")
while((ai!=af or bi!=bf)):
   op=int(input("enter the operation:"))
   if(op==1):
     ai=a
   elif(op==2):
     bi=b
   elif(op==3):
     ai=0
   elif(op==4):
     bi=0
   elif(op==5):
     if(b-bi>ai):
       bi=ai+bi
       ai=0
     else:
        ai=ai-(b-bi)
        bi=b
   elif(op==6):
     if(a-ai>bi):
       ai=ai+bi
       bi=0
     else:
       bi=bi-(a-ai)
       print("***",ai)
   elif(op==7):
     if(ai<a):
       ai=ai+bi
       bi=0
     else:
       print("jug A overflow")
       exit()
   elif(op==8):
     if(bi<b):
       bi=bi+ai
       ai=0
     else:
       print("jug B empty")
       exit()
   print(ai,bi)