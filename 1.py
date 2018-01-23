def normalize(name):
    return name.capitalize()

L1=['adam','lisa','bart']
L2=list(map(normalize,L1))
print(L2)