plik=open("set1_run_30_f.txt", "r+")
plik2=open("genpop.txt", "r+")
plik3=open("klaster1.txt", "w")
plik4=open("klaster2.txt", "w")
plik5=open("klaster3.txt", "w")
plik6=open("klaster4.txt", "w")
add=[]
genpop=[]
for i in plik2:
    if len(i)>30:
        genpop.append(i.strip())
    else:
        add.append(i.strip())
gotowy=[]
for i in plik:
    linia=i.strip()
    linia=linia.split(" ")
    for i in linia:
        while '' in linia:
            linia.remove('')
    #print (linia)
    linia[4]=float(linia[4])
    linia[5]=float(linia[5])
    linia[6]=float(linia[6])
    gotowy.append(linia)
for i in add:
    plik3.write(i+'\n')
    plik4.write(i+'\n')
    plik5.write(i+'\n')
    plik6.write(i+'\n')
for i in range(len(gotowy)):
    if gotowy[i][4]>=0.9 and gotowy[i][5]<0.9 and gotowy[i][6]<0.9:
        plik3.write(genpop[i]+'\n')
    elif gotowy[i][4]<0.9 and gotowy[i][5]>=0.9 and gotowy[i][6]<0.9:
        plik4.write(genpop[i]+'\n')
    elif gotowy[i][4]<0.9 and gotowy[i][5]<0.9 and gotowy[i][6]>=0.9:
        plik5.write(genpop[i]+'\n')
    elif gotowy[i][4]<0.9 and gotowy[i][5]<0.9 and gotowy[i][5]<0.9:
        plik6.write(genpop[i]+'\n')

plik.close()
plik2.close()
plik3.close()
plik4.close()
plik5.close()
plik6.close()

