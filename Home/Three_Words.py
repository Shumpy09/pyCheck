def checkio(words):
    #petla przechodzaca przez podzielone wyrazy
    
    count = 0
    for w in words.split():
        
        if w.isalpha():
            count += 1
            if count >= 3:
                return True
        else:
            count = 0
    return False


print(checkio("Hello World hello")) #True
print(checkio("He is 123 man")) #False
print(checkio("1 2 3 4")) #False
print(checkio("bla bla bla bla")) #True
print(checkio("Hi")) #False
print(checkio("one two 3 four five six 7 eight 9 ten eleven 12"))