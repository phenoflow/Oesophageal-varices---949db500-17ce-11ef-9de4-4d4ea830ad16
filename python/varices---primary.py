# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"G852.00","system":"readv2"},{"code":"G85..11","system":"readv2"},{"code":"44424.0","system":"readv2"},{"code":"1641.0","system":"readv2"},{"code":"26319.0","system":"readv2"},{"code":"96756.0","system":"readv2"},{"code":"73139.0","system":"readv2"},{"code":"62582.0","system":"readv2"},{"code":"105611.0","system":"readv2"},{"code":"10797.0","system":"readv2"},{"code":"8363.0","system":"readv2"},{"code":"30655.0","system":"readv2"},{"code":"24989.0","system":"readv2"},{"code":"I85","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('oesophageal-varices-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["varices---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["varices---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["varices---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
