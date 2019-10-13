
import pandas as pd
from apyori import apriori

store_data = pd.read_csv('info.csv')

records = []
for i in range(0, 99):
    records.append([str(store_data.values[i,j]) for j in range(0,10)])


association_rules = apriori(records, min_support=0.04, min_confidence=0.4, min_lift=1.2, min_length=2)
association_results = list(association_rules)

print(len(association_results))
#print(association_results)

filename='pair.csv'
file=open(filename,'w')

for item in association_results:
    l=[]
    l=item[0]
    g=len(l)
    i=0
    for x in l:
          i+=1
          print(x)
          if(x!="nan"):
            file.write(x)
            if(i!=g):
              file.write('|')
    print("\n")
    file.write('\n')
     # first index of the inner list
     # Contains base item and add item
  #   pair = item[0]
  #   items = [x for x in pair]
#     print("Rule: " + items[0] + " -> " + items[1])
#     # file.write(items[0])
#     # file.write('-')
#     # file.write(items[1])
#     # file.write('\n')



#     #second index of the inner list
#     print("Support: " + str(item[1]))

#     #third index of the list located at 0th
#     #of the third index of the inner list

#     print("Confidence: " + str(item[2][0][2]))
#     print("Lift: " + str(item[2][0][3]))
#     print("=====================================")

'''for i, item in store_data.iteritems():
    print(item.unique())
'''
