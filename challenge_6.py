import pickle, re, ast, zipfile

name = '90052'
lista = []
lista2 = []
comments = []

#46145 Collects the comments
# countN = 0
fileZip = zipfile.ZipFile("channel.zip")

# file = pickle.load(open('banner.p', "rb"))
# for l in file:
#     stg = ''
#     for a,b in l:
#         lista2.append(a)
        
try:
    while True:
        # print(name)
        with open('channel/' + name + ".txt", "r") as f:
            comments.append(fileZip.getinfo(name + ".txt").comment.decode("utf-8"))
            # ZipInfo.comment: comment for the individual archive member.
            content = f.read()
            name = content.split(' ')[-1]
            lista.append(name)
except:
    pass
    #print(lista, len(lista))

print("".join(comments)) #awnser is HOCKEY /// oxygen

# lista.insert(0,'90052')
# lista = lista[:-1]
# lista.append('46145')


# comments = [x[1] for x in zip(lista2, lista) if x[0]=='#']
# print(comments)
# print(sum(map(int, comments)))


