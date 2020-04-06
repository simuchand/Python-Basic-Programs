s = input()
s1 = input()
s = s.replace(" ", "")
s1 = s1.replace(" ", "")
s = " ".join(s)
s1 = " ".join(s1)
lst = s.split()
lst1 = s1.split()
lst = sorted(lst)
lst1 = sorted(lst1)
print(lst)
print(lst1)
if lst == lst1:
    print("True")
else:
    print("False")



