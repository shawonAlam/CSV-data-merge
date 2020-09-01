
# import csv

# "C:/Users/USER/PycharmProjects/csvSort/data.csv"
import csv
print("Demo start!")
with open("C:/Users/USER/PycharmProjects/csvSort/notNullData1.csv", 'w') as title:
    writer = csv.writer(title)
    with open("C:/Users/USER/PycharmProjects/csvSort/data1.csv", 'r') as mycsv:
        reader = csv.reader(mycsv)
        c = 1
        for row in reader:
            for item in row:
                if item == 'Python':
                    c += 1
                    writer.writerow(row)
        print(c)
with open('C:/Users/USER/PycharmProjects/csvSort/notNullData1.csv') as input, \
        open('C:/Users/USER/PycharmProjects/csvSort/nullData1.csv', 'w') as output:
    non_blank = (line for line in input if line.strip())
    output.writelines(non_blank)
print("demo done!")

with open('C:/Users/USER/PycharmProjects/csvSort/data1.csv', 'r') as f1, \
        open('C:/Users/USER/PycharmProjects/csvSort/writeData.csv', 'a+') as f2:
    # for row in f1:
    #     print(row)
    f2.write(f1.read())
    a = csv.reader(f1)
    b = csv.writer(f2)
    for row in a:
        print(row)
print("Done!")
# KIRC labels.csv
print("Start!")
with open("C:/Users/USER/PycharmProjects/csvSort/data - Copy/nullableLabels.csv", 'w') as title:
    writer = csv.writer(title)
    with open("C:/Users/USER/PycharmProjects/csvSort/data - Copy/labels1.csv", 'r') as mycsv:
        reader = csv.reader(mycsv)
        c = 1
        for row in reader:
            for item in row:
                if item == 'KIRC' or item == 'PRAD':
                    c += 1
                    writer.writerow(row)
        print(c)
with open('C:/Users/USER/PycharmProjects/csvSort/data - Copy/nullableLabels.csv') as input, \
        open('C:/Users/USER/PycharmProjects/csvSort/data - Copy/notNullableLabels.csv', 'w') as output:
    non_blank = (line for line in input if line.strip())
    output.writelines(non_blank)
print("done!")


# KIRC data.csv [way: 1]
# print("Start.")
# print("Matching...")
# with open("C:/Users/USER/PycharmProjects/csvSort/data - Copy/sortedData.csv", 'w') as sortedData, \
#         open('C:/Users/USER/PycharmProjects/csvSort/data - Copy/notNullableLabels.csv', 'r') as labels, \
#             open("C:/Users/USER/PycharmProjects/csvSort/data - Copy/data.csv", 'r') as data:
#                 SortedData = csv.writer(sortedData)
#                 Labels = list(csv.reader(labels))
#                 Data = list(csv.reader(data))
#                 c = 0
#                 for lItem in Labels:
#                     # print(lItem[1])
#                     for dItem in Data:
#                         pass
#                         if lItem[0] == dItem[0]:
#                             c += 1
#                             SortedData.writerow(lItem+dItem)
#                 print("Total matched found: ", c)
# with open('C:/Users/USER/PycharmProjects/csvSort/data - Copy/sortedData.csv') as input, \
#         open('C:/Users/USER/PycharmProjects/csvSort/data - Copy/mainData.csv', 'w') as output:
#     non_blank = (line for line in input if line.strip())
#     output.writelines(non_blank)
# print("Done!")
import csv
# KIRC data.csv [way: 2]
print('Start...')
c1 = csv.reader(open('C:/Users/USER/PycharmProjects/csvSort/data - Copy/data1.csv', 'r'))
c2 = csv.reader(open('C:/Users/USER/PycharmProjects/csvSort/data - Copy/notNullableLabels.csv', 'r'))
c3 = csv.writer(open('C:/Users/USER/PycharmProjects/csvSort/data - Copy/sortedData.csv', 'w'))

labellist = list(c2) #[['sample_6', 'KIRC'], ['sample_11', 'KIRC'], ['sample_17', 'KIRC'], ['sample_18', 'KIRC']
datalist = list(c1) #[['sample_6', 'KIRC'], ['sample_11', 'KIRC'], ['sample_17', 'KIRC'], ['sample_18', 'KIRC']

c = 0
for lItem in labellist: #labels
    for dItem in datalist: #data
        if lItem[0] == dItem[0]:
            # print(dItem)
            c += 1
            c3.writerow(dItem)
print("Total matched found: ", c)
with open('C:/Users/USER/PycharmProjects/csvSort/data - Copy/sortedData.csv') as input, \
        open('C:/Users/USER/PycharmProjects/csvSort/data - Copy/mainData.csv', 'w') as output:
    non_blank = (line for line in input if line.strip())
    output.writelines(non_blank)
print('Done!')





