# use the function blackbox(lst) that is already defined
lst = [1, 2, 3]
newlist = blackbox(lst)
if id(lst) == id(newlist):
    print("modifies")
else:
    print("new")
