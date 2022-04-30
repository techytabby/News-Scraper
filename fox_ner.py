'''
set up for spacy:
> pip install spacy
> python -m spacy download en_core_web_sm
'''

import spacy, os, json, pandas as pd, matplotlib.pyplot as plt, csv
from spacy import displacy
from operator import itemgetter

# Dictionaries to store the top mentioned entities of each type
# Key is name of person/norp/etc.
# Value is number of mentions

fox_person = dict()
fox_norp = dict()
fox_org = dict()
fox_gpe = dict()
fox_loc = dict()
sdGPE = [];
sdLOC = [];

NER = spacy.load("en_core_web_sm")

# Read all Fox texts:
directory = 'fox' # this doesn't exist yet - still need fox texts in a directory called fox
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        input = open(f, "rb")
        raw_text = input.read().decode(errors='replace')
        input.close()
        text = NER(raw_text)
        # Parse the entities found in the text and add the data to the corresponding dict
        for word in text.ents:
            if word.label_ == 'PERSON':
            	try:
            		fox_person[word.text] += 1
            	except:
            		fox_person[word.text] = 1
            if word.label_ == 'NORP':
            	try:
            		fox_norp[word.text] += 1
            	except:
            		fox_norp[word.text] = 1
            if word.label_ == 'ORG':
            	try:
            		fox_org[word.text] += 1
            	except:
            		fox_org[word.text] = 1
            if word.label_ == 'GPE':
            	try:
            		fox_gpe[word.text] += 1
            	except:
            		fox_gpe[word.text] = 1

            	sdGPE.append(['FOX', filename[4:12], word.text]); # need this data for csv input for step 5

            if word.label_ == 'LOC':
            	try:
            		fox_loc[word.text] += 1
            	except:
            		fox_loc[word.text] = 1
            	sdLOC.append(['FOX', filename[4:12], word.text]); # need this data for csv input for step 5

# Top 20 key-value pairs in each dict are:
top_people = dict(sorted(fox_person.items(), key = itemgetter(1), reverse = True)[:20])
top_norp = dict(sorted(fox_norp.items(), key = itemgetter(1), reverse = True)[:20])
top_org = dict(sorted(fox_org.items(), key = itemgetter(1), reverse = True)[:20])
top_gpe = dict(sorted(fox_gpe.items(), key = itemgetter(1), reverse = True)[:20])
top_loc = dict(sorted(fox_loc.items(), key = itemgetter(1), reverse = True)[:20])


# Write all the dicts to a jsonl file:
with open("fox.jsonl", "w") as outfile:
    outfile.write(json.dumps(fox_person) + "\n")
    outfile.write(json.dumps(fox_norp) + "\n")
    outfile.write(json.dumps(fox_org) + "\n")
    outfile.write(json.dumps(fox_gpe) + "\n")
    outfile.write(json.dumps(fox_loc))



# Write the GPE and LOC data to a csv file:
headers = ['Source', 'Date', 'GPE/LOC']
with open("gpe_loc_fox.csv", "w") as outfile:
	write = csv.writer(outfile)
	write.writerow(headers)
	write.writerows(sdGPE)
	write.writerows(sdLOC)



# Create 5 bar charts:

#person graph
person = pd.DataFrame({'Person': top_people.keys(), 'Total Occurrences': top_people.values()})
graph = person.plot.bar(x='Person', y='Total Occurrences', color="green", title="Top 20 FOX Person Occurrences")
#show graph
plt.show()

#norp graph
norp = pd.DataFrame({'NORP': top_norp.keys(), 'Total Occurrences': top_norp.values()})
graph = norp.plot.bar(x='NORP', y='Total Occurrences', color="green", title="Top 20 FOX NORP Occurrences")
#show graph
plt.show()

#org graph
org = pd.DataFrame({'ORG': top_org.keys(), 'Total Occurrences': top_org.values()})
graph = org.plot.bar(x='ORG', y='Total Occurrences', color="green", title="Top 20 FOX ORG Occurrences")
#show graph
plt.show()

#gpe graph
gpe = pd.DataFrame({'GPE': top_gpe.keys(), 'Total Occurrences': top_gpe.values()})
graph = gpe.plot.bar(x='GPE', y='Total Occurrences', color="green", title="Top 20 FOX GPE Occurrences")
#show graph
plt.show()

#loc graph
loc = pd.DataFrame({'LOC': top_loc.keys(), 'Total Occurrences': top_loc.values()})
graph = loc.plot.bar(x='LOC', y='Total Occurrences', color="green", title="Top 20 FOX LOC Occurrences")
#show graph
plt.show()
