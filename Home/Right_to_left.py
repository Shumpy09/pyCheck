def left_join(phrases):

    return ",".join(phrases).replace('right','left') 

print(left_join(("left","right","left","stop")))
print(left_join(("bright aright","ok")))
print(left_join(("brightness wright",)))
print(left_join(("enough","jokes")))