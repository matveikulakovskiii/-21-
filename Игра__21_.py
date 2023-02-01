import random
koloda=[6,7,8,9,10,2,3,4,11]
random.shuffle(koloda)
arv=0
while True:
    choice=input("Kas võtad kaardi?  y=Yes/n=No: ")
    if choice == "y":
        number=koloda.pop()
        print("Sul on kaardi number %d" %number)
        arv+=number
    if arv>21:
        print("Vabandust, aga sa kaotsid")
        break
    elif arv==21:
        print("Palju õnne, tabasite numbrit 21!")
        break
    else:
        if choice == "n":
             print("Teil on %d punkti ja olete mänghu lõpetanud" %arv)
             break