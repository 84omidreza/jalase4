print("calculation of lcm between two number")

first=int(input("pleas enter your first number"))
socond=int(input("pleas enter your second number:"))



def icm():
    higher = max(first,socond)
    alt = higher
    while True:
        if higher % firstn == 0 and higher % socond == 0:
            print("icm between", str(first),"and"< str(socond),"is",str(higher))
            break
        else:higher=alt+higher

icm()