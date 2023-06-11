def errorhandle(n1,n2,oper):
  if not n1.isnumeric() and n2.isnumeric():
    print('Error: Numbers must only contain digits.')
  if not oper == '+' or oper == '-':
    print("Error: Operator must be '+' or '-'.")
  if int(n1) > 9999 or int(n2) > 9999:
    print('only four digit numbers')
  
def arithmetic_arranger(problems,mode=False):
  if len(problems) > 5:
    print('Error: Too many problems.')
  l1=''
  l2=''
  l3=''
  l4=''
  
  for prob in problems:
    ques = prob.split()
    num1 = ques[0]
    num2 = ques[2]
    oper = ques[1]
    maxlen=max(len(num1),len(num2))
    errorhandle(num1,num2,oper)
    l1+=(num1.rjust(maxlen+2)+'    ')
    l2+=(oper+num2.rjust(maxlen+1)+'    ')
    l3+=('-'*(maxlen+2)+'    ')
    
    if mode==True:
      if oper=='+':
        l4+=(str(int(num1)+int(num2)).rjust(maxlen+2)+'    ')
      else:
        l4+=(str(int(num1)-int(num2)).rjust(maxlen+2)+'    ')
        
  if mode==True:
    return l1+'\n'+l2+'\n'+l3+'\n'+l4
  else:
    return l1+'\n'+l2+'\n'+l3
  
      
