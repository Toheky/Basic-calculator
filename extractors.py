from math import factorial, sqrt, radians, degrees
from operations import lcm, summ

def extract_fact(s):
    '''Isolate the number in the factorial operation.'''
    while "!" in s:
        num = ""
        for j in range(s.find("!")-1,-1,-1):
            if s[j] in "0123456789":
                num += s[j]
            s = s.replace(num+"!", str(factorial(int(num))), 1)
            break
    return s

def extract_sqrt(s):
    '''Isolate the number in the sqrt operation.'''
    s = s+" "
    while "√" in s:
        num = ""
        i = s.find("√")+1
        while s[i] in "0123456789" and i < len(s)-1:
            num += s[i]
            i += 1
        s = s.replace("√"+num, str(sqrt(int(num))), 1)
    return s

def extract_lcm(s):
    '''Isolate the number in the lcm operation.'''
    string = s
    lst = []
    while "lcm" in s:
        s = s[s.find("lcm(")+4:]
        lst.append(s[:s.find(")")])
    for i in lst:
        n = str(lcm([int(i) for i in i.split(",")]))
        string = string.replace("lcm("+i+")", n)
    return string

def extract_summa(s):
    '''Isolate the number in the summation operation.'''
    string = s
    pog = []
    while "Σ" in s:
        s = s[s.find("Σ(")+2:]
        pog.append(s[:s.find(")")])
    for expre in pog:
        string = string.replace("Σ("+expre+")",str(summ(expre.split(","))))
    return string

def extract(s, active):
    '''Isolate the number in the trig functions.'''
    string = s
    lst = []
    while "cos" in s or "sin" in s or "tan" in s:
        for expre in ["cos(", "sin(", "tan("]:
            if expre in s:
                s = s[s.find(expre)+4:]
                lst.append(s[:s.find(")")])
    if active < 0:
        for val in set(lst):
            #convert the value to gradians or radians
            string = string.replace(val, "radians({0})".format(val))
    else:
        for val in set(lst):
            string = string.replace(val, "degrees({0})".format(val))

    return string