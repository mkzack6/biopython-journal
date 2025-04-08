from Bio.KEGG import REST
from Bio.KEGG import Enzyme

# Fetch the enzyme data from KEGG
request = REST.kegg_get("ec:5.4.2.2")  # Get data for enzyme EC 5.4.2.2
with open("ec_5.4.2.2.txt", "w") as file:
    file.write(request.read())  # Save the data to a file

# Parse the enzyme data
with open("ec_5.4.2.2.txt") as file:
    records = Enzyme.parse(file)
    record = list(records)[0]  # Get the first record

# Access enzyme details
print("Classname:", record.classname)  # ['Isomerases;', 'Intramolecular transferases;', 'Phosphotransferases (phosphomutases)']
print("Entry:", record.entry)  # '5.4.2.2'