from Bio.KEGG import Enzyme

# Parse the enzyme file
with open("ec_5.4.2.2.txt") as file:
    records = Enzyme.parse(file)
    record = list(records)[0]  # Get the first record

# Access enzyme details
print("Classname:", record.classname)
print("Entry:", record.entry)