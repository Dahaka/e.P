import random
L1 = [];

#random lists  .. me akeraious apo to 1 mexri to 20
L1=[random.randrange(1,21,1) for _ in range (20)]
L2=[random.randrange(1,21,1) for _ in range (20)]

finalList1=[];


#emfanhsh listwn
print("list1 : \n " , L1);
print("list2 : \n " , L2);





finalList=[];


#kanei ton pollaplasiasmo kai ton vazei se lista
for x in range(0 , len(L1)):
    for y in range(0 , len(L2)):
        
        finalList.append(L1[x] * L2[y]);


#an iparxei idi stin lista enas ari8mos dn ton ksanavazei ( apofigi duplicates)        
for i in finalList:
    if i not in finalList1:
        finalList1.append(i);

        
print("Ginomena : .. ");        
print(finalList1);

print(" Ginomena me tin seira .. : \n ", set(finalList));
