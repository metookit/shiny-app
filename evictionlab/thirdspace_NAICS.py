import csv
var = 'a'
import sys
sys.path.insert(0,"/home/skim7/evictionlab/thirdspace_NAICS_hc.py")
print(sys.path)
from thirdspace_NAICS_hc import NAICS_dict2


"""creating a dictionary (businesstype_dict) where value is the
NAICS number and the key is the frequency"""

"""the code below was just to a list of exclusive keys (the first two numeral values of it) """

def main():
    naicstype_dict = dict([
     ])

    with open('naics.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            naicstype = row[0][:4]
            third_space = row[1]
            naicstype_dict[naicstype] = third_space
            line_count += 1

    key_copy = tuple(NAICS_dict2.keys())
    key_copy2 = tuple(naicstype_dict.keys())

    unknownspaces = []
    for k in key_copy:
        if str(NAICS_dict2[k]) == 'Unknown':
            unknownspaces.append(k)

    print(unknownspaces)

    for j in key_copy2:
        if j[:2] in unknownspaces:
            print(j)


        #print(naicstype_dict)
        #print(f'Processed {line_count} lines.')


    #for row in NAICS_dict:
    #    NAICS_dict[third_space] = "Third Space"

    #print(NAICS_dict)



main()
