protais={}
import random
Number_of_protais = int(input("Enter the number of friends joining (including you):\n"))
if Number_of_protais <= 0:   
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    x = range(int(Number_of_protais))
    for n in x:
      name=str(input())
      protais[f"{name}"]=0
    total_bill=float(input('Enter the total bill value:\n'))
    choices= input("Do you want to use the 'Who is lucky?'feature? Write Yes/No:\n")
    divide_bill=round(total_bill/Number_of_protais ,2)
    if choices.lower()=="yes":
        lucky_one=random.choice(list(protais.keys()))
        print(f"{lucky_one} is the lucky one!")
        protais[f"{name}"]=0
        Friends_to_pay_bills=Number_of_protais - 1
        Second_divide_bill=round(total_bill/Friends_to_pay_bills,2)
        for d in protais:
            if d != lucky_one:
                protais[f"{d}"]= Second_divide_bill
    else:
        print("No one is going to be lucky")
        for d in protais:
            protais[f"{d}"]=divide_bill
    print(protais)
    
