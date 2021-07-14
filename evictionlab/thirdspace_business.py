import csv

"""creating a dictionary (businesstype_dict) where value is the
NAICS number and the key is the frequency"""

"""Map business types “is a third space” or “not a third space” or “unknown”
Similar to the naics codes, you should create a dictionary for each business
type and decide whether it is “is a third space” or “not a third space” or “unknown”
You can get a list of all business types by reading in the all cities dataframe
and doing df[‘business_type’].value_counts(sort=True) in Pandas """

def main():
    businesstype_dict = dict([
     ])

    with open('business_type.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            businesstype = row[0]
            third_space = row[1]
            businesstype_dict[businesstype] = third_space
            line_count += 1

        key_copy = tuple(businesstype_dict.keys())    # Feel free to use any iterable collection

        for k in key_copy:
            if int(naicstype_dict[k]) <= 300:
                del naicstype_dict[k]
                line_count -=1

            #if line_count < 5:
            #    print(row)
            #    print (NAICS_dict, third_space)

        print(businesstype_dict)
        print(f'Processed {line_count} lines.')

    #for row in NAICS_dict:
    #    NAICS_dict[third_space] = "Third Space"

    #print(NAICS_dict)



main()
