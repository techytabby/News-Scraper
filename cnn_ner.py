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

cnn_person = dict()
cnn_norp = dict()
cnn_org = dict()
cnn_gpe = dict()
cnn_loc = dict()
sdGPE = [];
sdLOC = [];

baddates = [];

NER = spacy.load("en_core_web_sm")

# Read all CNN texts:
directory = 'cnn' # this doesn't exist yet - still need fox texts in a directory called fox
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        input = open(f, "rb")
        raw_text = input.read().decode(errors='replace')
        input.close()
        text = NER(raw_text)
        # Parse the entities found in the text and add the data to the corresponding dict
    for word in text.ents:
        if ("March_1_202" in filename[15:28]) or ("March_2_202" in filename[15:28]) or ("March_3_202" in filename[15:28]) or ("March_4_202" in filename[15:28]) or ("March_5_202" in filename[15:28]) or ("March_6_202" in filename[15:28]) or ("March_7_202" in filename[15:28]) or ("March_8_202" in filename[15:28]) or ("March_9_202" in filename[15:28]) or ("March_10_202" in filename[15:28]) or ("March_11_202" in filename[15:28]):
            baddates.append(filename[15:28])
        else:
            if word.label_ == 'PERSON':
                try:
                    cnn_person[word.text] += 1
                except:
                    cnn_person[word.text] = 1
                    
            if word.label_ == 'NORP':
                try:
                    cnn_norp[word.text] += 1
                except:
                        cnn_norp[word.text] = 1
            if word.label_ == 'ORG':
                try:
                    cnn_org[word.text] += 1
                except:
                    cnn_org[word.text] = 1
            if word.label_ == 'GPE':
                try:
                    cnn_gpe[word.text] += 1
                except:
                    cnn_gpe[word.text] = 1
                sdGPE.append(['CNN', filename[15:28], word.text]); # need this data for csv input for step 5
            if word.label_ == 'LOC':
                try:
                    cnn_loc[word.text] += 1
                except:
                    cnn_loc[word.text] = 1
                sdLOC.append(['CNN', filename[15:28], word.text]); # need this data for csv input for step 5

# Top 20 key-value pairs in each dict are:
top_people = dict(sorted(cnn_person.items(), key = itemgetter(1), reverse = True)[:20])
top_norp = dict(sorted(cnn_norp.items(), key = itemgetter(1), reverse = True)[:20])
top_org = dict(sorted(cnn_org.items(), key = itemgetter(1), reverse = True)[:20])
top_gpe = dict(sorted(cnn_gpe.items(), key = itemgetter(1), reverse = True)[:20])
top_loc = dict(sorted(cnn_loc.items(), key = itemgetter(1), reverse = True)[:20])


# Write all the dicts to a jsonl file:
with open("cnn.jsonl", "w") as outfile:
    outfile.write(json.dumps(cnn_person) + "\n")
    outfile.write(json.dumps(cnn_norp) + "\n")
    outfile.write(json.dumps(cnn_org) + "\n")
    outfile.write(json.dumps(cnn_gpe) + "\n")
    outfile.write(json.dumps(cnn_loc))

# Write the GPE and LOC data to a csv file:
headers = ['Source', 'Date', 'GPE/LOC']
with open("gpe_loc_cnn.csv", "w") as outfile:
	write = csv.writer(outfile)
	write.writerow(headers)
	write.writerows(sdGPE)
	write.writerows(sdLOC)



# Create 5 bar charts:

#person graph
person = pd.DataFrame({'Person': top_people.keys(), 'Total Occurrences': top_people.values()})
graph = person.plot.bar(x='Person', y='Total Occurrences', color="blue", title="Top 20 CNN Person Occurrences")
#show graph
plt.show()

#norp graph
norp = pd.DataFrame({'NORP': top_norp.keys(), 'Total Occurrences': top_norp.values()})
graph = norp.plot.bar(x='NORP', y='Total Occurrences', color="blue", title="Top 20 CNN NORP Occurrences")
#show graph
plt.show()

#org graph
org = pd.DataFrame({'ORG': top_org.keys(), 'Total Occurrences': top_org.values()})
graph = org.plot.bar(x='ORG', y='Total Occurrences', color="blue", title="Top 20 CNN ORG Occurrences")
#show graph
plt.show()

#gpe graph
gpe = pd.DataFrame({'GPE': top_gpe.keys(), 'Total Occurrences': top_gpe.values()})
graph = gpe.plot.bar(x='GPE', y='Total Occurrences', color="blue", title="Top 20 CNN GPE Occurrences")
#show graph
plt.show()

#loc graph
loc = pd.DataFrame({'LOC': top_loc.keys(), 'Total Occurrences': top_loc.values()})
graph = loc.plot.bar(x='LOC', y='Total Occurrences', color="blue", title="Top 20 CNN LOC Occurrences")
#show graph
plt.show()