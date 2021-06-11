def count_digits(text):
    
    count = 0
    text = text.split()
    for i in text:
        for j in i:
            if j.isdigit():
                count += 1
    
    return count




print(count_digits('hi'))
print(count_digits('who is 1st here'))
print(count_digits('my number is 2'))
print(count_digits('Petersen between 1845 and 1910 year'))
print(count_digits('5 plus 6 is'))
print(count_digits(''))