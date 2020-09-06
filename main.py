inpath = input ("Eingabe Dateipfade:")

def make_dictionary(fi):
        dict = {}
        dict1 = {}

        for line in a:
                i = line.replace("\n", "")
                i = i.split(";")
                dict1 = {(int)(((((int)(i[1])/100)/100))): float(i[5])}
                dict.update(dict1)
        return dict


with open (inpath,"r",encoding="utf-8") as fi:
    a=fi.readlines()
    del a[0]
    a=a
    tab=make_dictionary(fi)
    for key,value in tab.items():
            if  key == key:
                    value1=(value+value)/12
                    print (f"{key} : {value}")

fi.close()
