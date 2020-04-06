def divide(lst):
    Sum = 0
    Str = ""
    for i in lst:
        i = int(i)
        Sum += i
    if Sum>9:
        Str = str(Sum)
        print(Str)
        Str = " ".join(Str)
        lst = Str.split()
        return divide(lst)

    return Sum



s = input("Enert your DoB without space : (E.g : 20010202)")
s = " ".join(s)
lst = s.split()

print(divide(lst))
