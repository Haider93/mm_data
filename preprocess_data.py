import pandas as pd
from matplotlib import pyplot
from scipy.stats import shapiro
from numpy.random import seed
from numpy.random import randn


import csv

min, max = 325, 338

f = open('C://Users//Abbas//Desktop//data//ivv//lob_ivv_cleaned.csv', 'w+')
f.write("Date"+","+"Time"+","+"AP1"+","+"AP2"+","+"AP3"+","+"AP4"+","+"AP5"+
        "," + "AV1"+","+"AV2"+","+"AV3"+","+"AV4"+","+"AV5"+","+"BP1"+","+"BP2"+"," + "BP3"+
        "," + "BP4"+","+"BP5"+","+"BV1"+","+"BV2"+","+"BV3"+","+"BV4"+","+"BV5"+"\n")

f_tas = open('C://Users//Abbas//Desktop//data//ivv//tas_ivv_cleaned.csv', 'w+')
f_tas.write("Date"+","+"Time"+","+"Price"+","+"Size"+"\n")

with open('C://Users//Abbas//Desktop//data//ivv//tas_ivv.csv', 'r') as fd:
    reader = csv.reader(fd, delimiter=',')
    rows = list(reader)

with open('C://Users//Abbas//Desktop//data//ivv//lob_ivv.csv', 'r') as file:
    my_reader = csv.reader(file, delimiter=',')
    header = True
    row_count = 0
    for row in my_reader:
        ask = False
        bid = False
        if(header):
            header = False
            row_count = row_count + 1
        else:
            row_count = row_count + 1
            if(min<=float(row[2])<=max and min<=float(row[3])<=max and min<=float(row[4])<=max and min<=float(row[5])<=max
             and min<=float(row[6])<=max):
                ask = True
            if(row[12]!='' and row[13]!='' and row[14]!='' and row[15]!='' and row[16]!=''):
                if(min<=float(row[12])<=max and min<=float(row[13])<=max and min<=float(row[14])<=max and min<=float(row[15])<=max
                 and min<=float(row[16])<=max and float(row[12])<float(row[2]) and float(row[12])>float(row[13]) and ask):
                    f.write(row[0]+","+row[1]+","+row[2]+","+row[3]+","+row[4]+","+row[5]+","+row[6]+","+row[7]+","
                            + row[8] + ","+row[9]+","+row[10]+","+row[11]+","+row[12]+","+row[13]+","+row[14]+","
                            + row[15] + ","+row[16]+","+row[17]+","+row[18]+","+row[19]+","+row[20]+","+row[21]+"\n")
                    #print(rows[row_count][3])
                    if(row_count < len(rows)):
                        f_tas.write(rows[row_count][0]+","+rows[row_count][1]+","+rows[row_count][2]+","+rows[row_count][3]+"\n")
                    else:
                        f_tas.write(rows[len(rows)-1][0] + "," + rows[len(rows)-1][1] + "," + rows[len(rows)-1][2] + "," +
                                    rows[len(rows)-1][3] + "\n")
                else:
                    i = 12
                    no_blank_ask = False
                    if(row[i]!='' and row[i+1]!='' and row[i+2]!='' and row[i+3]!='' and row[i+4]!='' and row[i+5]!='' and
                    row[i+6]!='' and row[i+7]!= '' and row[i+8]!='' and row[i+9]!=''):
                        no_blank_ask = True
                        while (not(min<float(row[i])<max)):
                            i = i+1
                            if(i==(len(row)-1)):
                                break
                        if(len(row)-i>=10):
                            bp1 = row[i]
                            bp2 = row[i+1]
                            bp3 = row[i+2]
                            bp4 = row[i+3]
                            bp5 = row[i+4]
                            bv1 = row[i+5]
                            bv2 = row[i+6]
                            bv3 = row[i+7]
                            bv4 = row[i+8]
                            bv5 = row[i+9]
                            if(min<=float(bp1)<=max and min<=float(bp2)<=max and min<=float(bp3)<=max and min<=float(bp4)<=max
                                    and min<=float(bp5)<=max and float(bp1)<float(row[2]) and bp1>bp2):
                                bid = True

                if (ask and bid and no_blank_ask):
                    f.write(row[0] + "," + row[1] + "," + row[2] + "," + row[3] + "," + row[4] + "," + row[5] + "," + row[
                        6] + "," + row[7] + ","
                            + row[8] + "," + row[9] + "," + row[10] + "," + row[11] + "," + bp1 + "," + bp2 + "," +
                            bp3 + ","
                            + bp4 + "," + bp5 + "," + bv1 + "," + bv2 + "," + bv3 + "," + bv4 + "," + bv5 + "\n")
                    if (row_count < len(rows)):
                        f_tas.write(rows[row_count][0] + "," + rows[row_count][1] + "," + rows[row_count][2] + "," +
                                    rows[row_count][3] + "\n")
                    else:
                        f_tas.write(rows[len(rows)-1][0] + "," + rows[len(rows)-1][1] + "," + rows[len(rows)-1][2] + "," +
                                    rows[len(rows)-1][3] + "\n")


    f.close()
    f_tas.close()



# seed(1)
# data = 5 * randn(100) + 50
#
# # normality test
# stat, p = shapiro(data)
# print('Statistics=%.3f, p=%.3f' % (stat, p))
# # interpret
# alpha = 0.05
# if p > alpha:
# 	print('Sample looks Gaussian (fail to reject H0)')
# else:
# 	print('Sample does not look Gaussian (reject H0)')

# pyplot.hist(df['target_price'])
# pyplot.show()
