def isPalindrome(a):
    apple = list(a)
    print(apple)
    reverseme = [each for each in reversed(apple)]
    print(reverseme)
    return apple == reverseme

print(isPalindrome('abbaL'))
print(isPalindrome('abomination'))
print(isPalindrome('racecar'))
print(isPalindrome('r aceca r'))
print(isPalindrome('race car'))
print(isPalindrome('🙃🙂🙃'))

def counter(a):
    a = list(a)
    output = dict()
    for each in a:
        if each not in output:
            output[each] =  a.count(each)
    return output

def  ourSharedValues(a, b):
    a = counter(a)
    b = counter(b)
    output = dict()
    
    for each in a:
        if each in b:
            if a[each]> b[each]:
                output[each] = b[each]
            else:
                output[each] = a[each]
    return output

print(ourSharedValues('abcdef', 'abba'))