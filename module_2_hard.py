def pass_(vole):
    meaning = ''
    for i in range(1, vole):
        for j in range(i + 1, vole):
            if vole % (i + j) == 0:
                meaning += str(i) + str(j)
    return meaning
vole_ = int(input('enter a number: '))
print(pass_(vole_))

