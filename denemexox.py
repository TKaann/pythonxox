sayi = 0
dikey = int(input('dikey gir:'))
yatay = int(input("yatay gir:"))

butuntahta = []

for i in range(dikey):
    yatayliste = []
    # print()

    if (yatayliste != []):
        butuntahta.append(yatayliste)

    for j in range(yatay):
        # print(sayi , end="\t")
        yatayliste.append(sayi)
        sayi = sayi + 1
    butuntahta.append(yatayliste)

# print (butuntahta)


for i in range(len(butuntahta)):
    print()
    for j in range(len(butuntahta[i])):
        print(butuntahta[i][j], end="\t")

isGamePlaying = True
inputCount = 0
sira = "X"


def xox(oyuncu, oyuncu2, inputCount):
    global sira,butuntahta

    usermove = int(input("Nereye oynican"))
    if usermove < yatay * dikey:
        obek = int(usermove / yatay)
        eleman = usermove % yatay
        if butuntahta[obek][eleman] != "X" and butuntahta[obek][eleman] != "O":
            butuntahta[obek][eleman] = oyuncu
            inputCount += 1
            sira = oyuncu2


    else:
        print("Lutfen gecerli bir sayi giriniz")

    return 0


while isGamePlaying:
    for i in range(len(butuntahta)):
        print()
        for j in range(len(butuntahta[i])):
            print(butuntahta[i][j], end="\t")

    if sira == "X":
        xox(sira , "O" , inputCount)
        '''usermove = int (input("Nereye oynican"))
    if usermove < yatay * dikey:
      obek = int (usermove / yatay)
      eleman = usermove % yatay
      if(butuntahta[obek][eleman]!="X" or butuntahta[obek][eleman]!="O"):

        butuntahta[obek][eleman]="X"
        inputCount +=1
        sira = "O"
    else:
      print("Lutfen gecerli bir sayi giriniz")'''


    else:
      xox(sira , "X" , inputCount)
    """ usermove = int(input("Nereye oynican"))
    if usermove < yatay * dikey:
      obek = int(usermove / yatay)
      eleman = usermove % yatay
      if (butuntahta[obek][eleman] != "X" or butuntahta[obek][eleman] != "O"):
        butuntahta[obek][eleman] = "O"
        inputCount += 1
        sira = "X"
    else:
      print("Lutfen gecerli bir sayi giriniz")"""

    if (inputCount == dikey * yatay):
        print("Oyun Biti butun yerler doldu")
        isGamePlaying = False