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

alj_person = dict()
alj_norp = dict()
alj_org = dict()
alj_gpe = dict()
alj_loc = dict()
sdGPE = [];
sdLOC = [];
baddates = [];

NER = spacy.load("en_core_web_sm")

directory = 'aljazeera'
for filename in os.listdir(directory):
    if filename[0] != ".":
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            input = open(f, "rb")
            raw_text = input.read().decode(errors='replace')
            input.close()
            text = NER(raw_text)
            # Parse the entities found in the text and add the data to the corresponding dict
            for word in text.ents:
                if ("1_Mar" == filename[10:15]) or ("2_Mar" == filename[10:15]) or ("3_Mar" == filename[10:15]) or ("4_Mar" == filename[10:15]) or ("5_Mar" == filename[10:15]) or ("6_Mar" == filename[10:15]) or ("7_Mar" == filename[10:15]) or ("8_Mar" == filename[10:15]) or ("9_Mar" == filename[10:15]) or ("10_Ma" == filename[10:15]) or ("11_Ma" == filename[10:15]):
                    baddates.append(filename[10:15])
                else:
                    if word.label_ == 'PERSON':
                        try:
                            alj_person[word.text] += 1
                        except:
                            alj_person[word.text] = 1
                    if word.label_ == 'NORP':
                        try:
                            alj_norp[word.text] += 1
                        except:
                            alj_norp[word.text] = 1
                    if word.label_ == 'ORG':
                        try:
                            alj_org[word.text] += 1
                        except:
                            alj_org[word.text] = 1
                    if word.label_ == 'GPE':
                        try:
                            alj_gpe[word.text] += 1
                        except:
                            alj_gpe[word.text] = 1
                        
                        sdGPE.append(['Aljazeera', filename[10:15], word.text]);
                    if word.label_ == 'LOC':
                        try:
                            alj_loc[word.text] += 1
                        except:
                            alj_loc[word.text] = 1
                       
                        sdLOC.append(['Aljazeera', filename[10:15], word.text]);

# Top 20 key-value pairs in each dict are:
top_people = dict(sorted(alj_person.items(), key = itemgetter(1), reverse = True)[:20])
top_norp = dict(sorted(alj_norp.items(), key = itemgetter(1), reverse = True)[:20])
top_org = dict(sorted(alj_org.items(), key = itemgetter(1), reverse = True)[:20])
top_gpe = dict(sorted(alj_gpe.items(), key = itemgetter(1), reverse = True)[:20])
top_loc = dict(sorted(alj_loc.items(), key = itemgetter(1), reverse = True)[:20])


# Write all the dicts to a jsonl file:
with open("alj.jsonl", "w") as outfile:
    outfile.write(json.dumps(alj_person) + "\n")
    outfile.write(json.dumps(alj_norp) + "\n")
    outfile.write(json.dumps(alj_org) + "\n")
    outfile.write(json.dumps(alj_gpe) + "\n")
    outfile.write(json.dumps(alj_loc))


# Write the GPE and LOC data to a csv file:
headers = ['Source', 'Date', 'GPE/LOC']
with open("gpe_loc_al.csv", "w") as outfile:
    write = csv.writer(outfile)
    write.writerow(headers)
    write.writerows(sdGPE)
    write.writerows(sdLOC)


# Create 5 bar charts:

#person graph
person = pd.DataFrame({'Person': top_people.keys(), 'Total Occurrences': top_people.values()})
graph = person.plot.bar(x='Person', y='Total Occurrences', color="orange", title="Top 20 Aljazeera Person Occurrences")
#show graph
plt.show()

#norp graph
norp = pd.DataFrame({'NORP': top_norp.keys(), 'Total Occurrences': top_norp.values()})
graph = norp.plot.bar(x='NORP', y='Total Occurrences', color="orange", title="Top 20 Aljazeera NORP Occurrences")
#show graph
plt.show()

#org graph
org = pd.DataFrame({'ORG': top_org.keys(), 'Total Occurrences': top_org.values()})
graph = org.plot.bar(x='ORG', y='Total Occurrences', color="orange", title="Top 20 Aljazeera ORG Occurrences")
#show graph
plt.show()

#gpe graph
gpe = pd.DataFrame({'GPE': top_gpe.keys(), 'Total Occurrences': top_gpe.values()})
graph = gpe.plot.bar(x='GPE', y='Total Occurrences', color="orange", title="Top 20 Aljazeera GPE Occurrences")
#show graph
plt.show()

#loc graph
loc = pd.DataFrame({'LOC': top_loc.keys(), 'Total Occurrences': top_loc.values()})
graph = loc.plot.bar(x='LOC', y='Total Occurrences', color="orange", title="Top 20 Aljazeera LOC Occurrences")
#show graph
plt.show()