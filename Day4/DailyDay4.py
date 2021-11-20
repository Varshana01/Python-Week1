matrix=  [
    ['7','i','3'],
    ['T','s','i'],
    ['h','%','x'],
    ['i',' ','#'],
    ['s','M',' '],
    ['$','a',' '],
    ['#','t','%'],
    ['^','r','!']]
def matrix_decode(matrix):
    data=[]
    data2=[]
    data3=[]
    for i in matrix:
        if i[0].isalpha():
            data.append(i[0][0])
        if i[1].isalpha():
            data2.append(i[1][0])
        if ' ' in i[1]:
            data2.append(' ')
        if i[2].isalpha():
            data3.append(i[2][0])
    str1=' '.join(data)
    str2=' '.join(data2)
    str3 = ' '.join(data3)

    print(str1,'',str2,str3)
matrix_decode(matrix)


