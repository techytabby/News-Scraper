'''
Plot a distribution of top 20 mentioned PERSON, NORP, ORG, GPE and
LOC in the entire dataset. A simple bar plot illustrating the number of
mentions is the best way to do it.
'''

import json, pandas as pd, matplotlib.pyplot as plt
from operator import itemgetter

# Dictionaries to store the top mentioned entities of each type
# Key is name of person/norp/etc.
# Value is number of mentions
person = dict()
norp = dict()
org = dict()
gpe = dict()
loc = dict()

# Parse the Aljazeera data:
# For each key-value pair, either insert the data or update the existing value.
with open("alj.jsonl", "r") as file:
    input_list = list(file)
    # Parse the Aljazeera PERSON entities:
    alj_person = json.loads(input_list[0])
    for k,v in alj_person.items():
        try:
            person[k] += v
        except:
            person[k] = v
    # Parse the Aljazeera NORP entities:
    alj_norp = json.loads(input_list[1])
    for k,v in alj_norp.items():
        try:
            norp[k] += v
        except:
            norp[k] = v
    # Parse the Aljazeera ORG entities:
    alj_org = json.loads(input_list[2])
    for k,v in alj_org.items():
        try:
            org[k] += v
        except:
            org[k] = v
    # Parse the Aljazeera GPE entities:
    alj_gpe = json.loads(input_list[3])
    for k,v in alj_gpe.items():
        try:
            gpe[k] += v
        except:
            gpe[k] = v
    # Parse the Aljazeera LOC entities:
    alj_loc = json.loads(input_list[4])
    for k,v in alj_loc.items():
        try:
            loc[k] += v
        except:
            loc[k] = v

# Parse the CNN data:
# For each key-value pair, either insert the data or update the existing value.
with open("cnn.jsonl", "r") as file:
    input_list = list(file)
    # Parse the CNN PERSON entities:
    cnn_person = json.loads(input_list[0])
    for k,v in cnn_person.items():
        try:
            person[k] += v
        except:
            person[k] = v
    # Parse the CNN NORP entities:
    cnn_norp = json.loads(input_list[1])
    for k,v in cnn_norp.items():
        try:
            norp[k] += v
        except:
            norp[k] = v
    # Parse the CNN ORG entities:
    cnn_org = json.loads(input_list[2])
    for k,v in cnn_org.items():
        try:
            org[k] += v
        except:
            org[k] = v
    # Parse the CNN GPE entities:
    cnn_gpe = json.loads(input_list[3])
    for k,v in cnn_gpe.items():
        try:
            gpe[k] += v
        except:
            gpe[k] = v
    # Parse the CNN LOC entities:
    cnn_loc = json.loads(input_list[4])
    for k,v in cnn_loc.items():
        try:
            loc[k] += v
        except:
            loc[k] = v

# Parse the Fox data:
# For each key-value pair, either insert the data or update the existing value.
with open("fox.jsonl", "r") as file:
    input_list = list(file)
    # Parse the Fox PERSON entities:
    fox_person = json.loads(input_list[0])
    for k,v in fox_person.items():
        try:
            person[k] += v
        except:
            person[k] = v
    # Parse the Fox NORP entities:
    fox_norp = json.loads(input_list[1])
    for k,v in fox_norp.items():
        try:
            norp[k] += v
        except:
            norp[k] = v
    # Parse the Fox ORG entities:
    fox_org = json.loads(input_list[2])
    for k,v in fox_org.items():
        try:
            org[k] += v
        except:
            org[k] = v
    # Parse the Fox GPE entities:
    fox_gpe = json.loads(input_list[3])
    for k,v in fox_gpe.items():
        try:
            gpe[k] += v
        except:
            gpe[k] = v
    # Parse the Fox LOC entities:
    fox_loc = json.loads(input_list[4])
    for k,v in fox_loc.items():
        try:
            loc[k] += v
        except:
            loc[k] = v

# Top 20 key-value pairs in each dict are:
top_people = dict(sorted(person.items(), key = itemgetter(1), reverse = True)[:20])
top_norp = dict(sorted(norp.items(), key = itemgetter(1), reverse = True)[:20])
top_org = dict(sorted(org.items(), key = itemgetter(1), reverse = True)[:20])
top_gpe = dict(sorted(gpe.items(), key = itemgetter(1), reverse = True)[:20])
top_loc = dict(sorted(loc.items(), key = itemgetter(1), reverse = True)[:20])

# Merge the dicts:
data = {}
data.update(top_people)
data.update(top_norp)
data.update(top_org)
data.update(top_gpe)
data.update(top_loc)
# Find the top 20 mentioned entities in the overall dataset:
top_20 = dict(sorted(data.items(), key = itemgetter(1), reverse = True)[:20])

# Create 5 bar charts:

#person graph
person = pd.DataFrame({'Person': top_people.keys(), 'Total Occurrences': top_people.values()})
graph = person.plot.bar(x='Person', y='Total Occurrences', color="red", title="Top 20 Person Occurrences")
#show graph
plt.show()

#norp graph
norp = pd.DataFrame({'NORP': top_norp.keys(), 'Total Occurrences': top_norp.values()})
graph = norp.plot.bar(x='NORP', y='Total Occurrences', color="red", title="Top 20 NORP Occurrences")
#show graph
plt.show()

#org graph
org = pd.DataFrame({'ORG': top_org.keys(), 'Total Occurrences': top_org.values()})
graph = org.plot.bar(x='ORG', y='Total Occurrences', color="red", title="Top 20 ORG Occurrences")
#show graph
plt.show()

#gpe graph
gpe = pd.DataFrame({'GPE': top_gpe.keys(), 'Total Occurrences': top_gpe.values()})
graph = gpe.plot.bar(x='GPE', y='Total Occurrences', color="red", title="Top 20 GPE Occurrences")
#show graph
plt.show()

#loc graph
loc = pd.DataFrame({'LOC': top_loc.keys(), 'Total Occurrences': top_loc.values()})
graph = loc.plot.bar(x='LOC', y='Total Occurrences', color="red", title="Top 20 LOC Occurrences")
#show graph
plt.show()
