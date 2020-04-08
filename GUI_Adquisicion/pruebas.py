import csv

cn=0 # para contar reptediso
farchi="aa.csv"  # archivo con todos los registros
cm=[]  # Para poder conocer los repetidos.

f=open("bb.csv","w")  # Archivo destino con los registros sin repetir.
swriter = csv.writer(f, delimiter=',')
with open(farchi, 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
                if len(row)>5:
                        s = row[2]+" "+row[5]
                        s = s.lower()
                        if s in cm:
                                cn += 1
                        else:
                                cm.append(s)
                                swriter.writerow(row)
f.close()
print ("Registros duplicados ",cn)