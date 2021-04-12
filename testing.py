tyod = [
    'red white blue'.split()
]

def mjoin(ty):
    ty[0] = (' ').join(ty[0])
    print(ty)
print(tyod)
mjoin(tyod)
print('outside fun')
print(tyod)