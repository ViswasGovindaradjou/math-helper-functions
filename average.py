# to find the average of given numbers
def average(*a):
    t=[]
    s = 0
    for i in a:
        s+=i
    return s/len(a)
