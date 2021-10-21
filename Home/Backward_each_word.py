def backward_string_by_word(text):
    '''list_word = []
    for i in text:
        list_word.append(i)
    
    list_word.reverse()
    return ''.join(list_word)
    '''
        

    #list_word.reverse()
    #text = text.split(" ")
    #return ' '.join([i[::-1] for i in text.split(' ')])
    text1=[]
    for i in text.split(' '):
        #text = text.replace(i,i[::-1])
        
        #text.join(i[::-1])
        text1.append(i[::-1])
    return ' '.join(text1)

print(backward_string_by_word(''))
print(backward_string_by_word('world'))
print(backward_string_by_word('olleH Hello'))
print(backward_string_by_word('hellO World'))
print(backward_string_by_word('hello    world'))
print(backward_string_by_word('welcome to a game'))