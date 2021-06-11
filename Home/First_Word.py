def first_word(text):
    '''
    text = text.replace("."," ").replace(","," ").strip()
    text = text.split()
    return text[0]
'''
    return text.replace("."," ").replace(","," ").strip().split()[0]



print(first_word("Hello world")) #"Hello"
print(first_word(" a word ")) #"a"
print(first_word("don't touch it")) #"don't"
print(first_word("greetings, friends")) #"greetings"
print(first_word("... and so on ...")) #"and"
print(first_word("hi")) #"hi"
print(first_word("Hello.World")) #"Hello"