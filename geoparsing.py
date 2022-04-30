import csv
from geopy.geocoders import Nominatim



#clean locations from original csv input
def clean_loc(loc):
    if "RUSSIA" in loc or loc=="USSR" or "RUSIA" in loc or loc=="U.S.S.R." or "SOVIET" in loc:
        loc="RUSSIA"
    if "UNITED STATES" in loc or loc == "US" or loc == "U.S." or loc == "U.S" or loc == "USA" or loc=="AMERICA":
        loc="UNITED STATES"
    if "UNITED KINGDOM" in loc or loc == "UK"or loc=="U.K.":
        loc="UNITED KINGDOM"
    if "LVIV" in loc:
        loc="LVIV"
    if "ASIA" in loc:
        loc="ASIA"
    if "CALIF" in loc:
        loc="CALIFORNIA"
    if "AZOV" in loc:
        loc= "SEA OF AZOV"
    if "THE " in loc:
        loc=loc.replace("THE ", "")
        if "'S" in loc:
            loc=loc.replace("'S", "")
    if "CHECHEN" in loc:
        loc="CHECHEN REPUBLIC"
    if "STRYZHEN" in loc:
        loc= "STRYZHEN"
    if " OF MOLDOVA" in loc:
        loc= "REPUBLIC OF MOLDOVA"
    if "WIMBLEDON" in loc:
        loc= "WIMBLEDON"
    if "BUCHAREST" in loc:
        loc= "BUCHAREST"
    if loc=="AUS":
    	loc="AUSTRALIA"
    if loc=="LATIN AMERICA":
    	loc="SOUTH AMERICA"
    
    #replacements
    loc=loc.replace("'S", "")
    loc=loc.replace(" HOLOCAUST", "")
    loc=loc.replace(" NAVY", "")
    loc=loc.replace(" FLEET", "")
    loc=loc.replace("CITY OF ", "")
    loc=loc.replace(" 150 KILOMETRES", "")
    loc=loc.replace(" KVIV INDEPENDENT", "")
    loc=loc.replace(" IN KYIV", "")
    loc=loc.replace(" BIDEN", "")
    loc=loc.replace("PM ", "")
    loc=loc.replace("SIRT ", "")
    loc=loc.replace("ZELENSKYY", "")
    loc=loc.replace("POSTED", "")
    loc=loc.replace("POSI", "")
    
    

    return loc


def all_locs():
#OPEN CSV FILES
	alj_csv=open('gpe_loc_alj_final.csv', encoding='utf-8-sig')
	cnn_csv=open('gpe_loc_cnn_final.csv', encoding='utf-8-sig')
	fox_csv=open('gpe_loc_fox_final.csv', encoding='utf-8-sig')
	errors_csv=open('ERRORS.csv', encoding='ISO-8859-1')

	read_al_csv= csv.reader(alj_csv)
	read_cnn_csv= csv.reader(cnn_csv)
	read_fox_csv= csv.reader(fox_csv)
	read_errors= csv.reader(errors_csv)

	#STORAGE
	alj_dates=[]
	cnn_dates=[]
	fox_dates=[]
	alj_dict={}
	cnn_dict={}
	fox_dict={}
	all_fox=[]
	all_alj=[]
	all_cnn=[]
	errors=[]

	#Read CSV
	for i in read_al_csv:
	    alj_dates.append(i)
	for i in read_cnn_csv:
	    cnn_dates.append(i)
	for i in read_fox_csv:
	    fox_dates.append(i)
	for i in read_errors:
	    errors.append(i[0])


	#ALJ 
	#Iterate through each day and save into lists, dictionaries to save unique locations for specific days
	date=1
	while date<=31:
	    alj_loc=[]
	    count=0
	    while count<len(alj_dates):
	        row=alj_dates[count]
	        if row[1]!= "Date":
	            day=row[1].split("_")
	            day=day[0]
	            if str(day) == str(date):
	                loc=row[2].upper()
	                #Further cleans the inputs
	                if ("#" not in loc) and ("@" not in loc) and ("-" not in loc) and loc!= "ARCTIC" and loc!= "OBAMA" and loc!="WEST" and "MIG" not in loc and "G7" not in loc:
	                    loc=clean_loc(loc)
	                    if "'S" in loc:
	                        loc=loc.replace("'S ", "")
	                    if "NORTH AND SOUTH KOREA" in loc:
	                        loc="NORTH KOREA"
	                        loc1="SOUTH KOREA"
	                        if (loc1 not in alj_loc):
	                            alj_loc.append(loc1)
	                        if loc1 not in all_alj:
	                            all_alj.append(loc1) 
	                    if "NORTH AND SOUTH AMERICA" in loc:
	                        loc="NORTH AMERICA"
	                        loc1="SOUTH AMERICA"
	                        if (loc1 not in alj_loc):
	                            alj_loc.append(loc1)
	                        if loc1 not in all_alj:
	                            all_alj.append(loc1)
	                    if "NORTH KOREA IRAN" in loc:
	                        loc="NORTH KOREA"
	                        loc1="IRAN"
	                        if (loc1 not in alj_loc):
	                            alj_loc.append(loc1)
	                        if loc1 not in all_alj:
	                            all_alj.append(loc1) 
	                    if "NORTH AMERICA & EUROPE" in loc:
	                        loc="NORTH AMERICA"
	                        loc1="EUROPE"
	                        if (loc1 not in alj_loc):
	                            alj_loc.append(loc1)
	                        if loc1 not in all_alj:
	                            all_alj.append(loc1)
	                    if "UKRAIN" in loc:
	                        item=loc.split(" ")
	                        if len(item)>1:
	                            for i in item:
	                                if (i not in alj_loc):
	                                    alj_loc.append(i)
	                                if i not in all_alj:
	                                    all_alj.append(i)
	                            loc=" "
	                        else:
	                            loc="UKRAINE"
	                    if loc in errors:
	                        items=loc.split(" ")
	                        for i in items:
	                            if (i not in alj_loc):
	                                alj_loc.append(i)
	                            if i not in all_alj:
	                                all_alj.append(i)
	                    else:
	                        if (loc not in alj_loc):
	                            alj_loc.append(loc)
	                        if loc not in all_alj:
	                            all_alj.append(loc)

	        count+=1   
	    alj_dict[date]= alj_loc
	    date+=1

	    

	#CNN
	#Iterate through each day and save into lists, dictionaries to save unique locations for specific days
	date=1
	while date<=31:
	    cnn_loc=[]
	    count=0
	    while count<len(cnn_dates):
	        row=cnn_dates[count]
	        if row[1]!= "Date":
	            day=row[1].split("_")
	            if day[0]=="":
	                day=day[1:]  
	            if len(day)==0 or len(day)==1:
	                day="empty"
	            elif day[0]=='12':
	                day='12'
	            else:
	                day=day[1]
	            if day == str(date):
	                loc=row[2].upper()
	                #Further cleans the inputs
	                if ("#" not in loc) and ("@" not in loc) and ("-" not in loc) and loc!="ARCTIC" and loc!= "OBAMA" and loc!="WEST" and "MIG" not in loc and "G7" not in loc:
	                    loc=clean_loc(loc)
	                    if "'S" in loc:
	                        loc=loc.replace("'S ", "")
	                    if "NORTH AND SOUTH KOREA" in loc:
	                        loc="NORTH KOREA"
	                        loc1="SOUTH KOREA"
	                        if (loc1 not in cnn_loc):
	                            cnn_loc.append(loc1)
	                        if loc1 not in all_cnn:
	                            all_cnn.append(loc1) 
	                    if "NORTH AND SOUTH AMERICA" in loc:
	                        loc="NORTH AMERICA"
	                        loc1="SOUTH AMERICA"
	                        if (loc1 not in cnn_loc):
	                            cnn_loc.append(loc1)
	                        if loc1 not in all_cnn:
	                            all_cnn.append(loc1)
	                    if "NORTH KOREA IRAN" in loc:
	                        loc="NORTH KOREA"
	                        loc1="IRAN"
	                        if (loc1 not in cnn_loc):
	                            cnn_loc.append(loc1)
	                        if loc1 not in all_cnn:
	                            all_cnn.append(loc1) 
	                    if "NORTH AMERICA & EUROPE" in loc:
	                        loc="NORTH AMERICA"
	                        loc1="EUROPE"
	                        if (loc1 not in cnn_loc):
	                            cnn_loc.append(loc1)
	                        if loc1 not in all_cnn:
	                            all_cnn.append(loc1)
	                    if "UKRAIN" in loc:
	                        item=loc.split(" ")
	                        #print(item)
	                        if len(item)>1:
	                            for i in item:
	                                if (i not in cnn_loc):
	                                    cnn_loc.append(i)
	                                if i not in all_cnn:
	                                    all_cnn.append(i)
	                            loc=" "
	                        else:
	                            loc="UKRAINE"
	                    if loc in errors:
	                        items=loc.split(" ")
	                        for i in items:
	                            if (i not in cnn_loc):
	                                cnn_loc.append(i)
	                            if i not in all_cnn:
	                                all_cnn.append(i)
	                    else:
	                        if (loc not in cnn_loc):
	                            cnn_loc.append(loc)
	                        if loc not in all_cnn:
	                            all_cnn.append(loc)
	        count+=1
	    cnn_dict[date]= cnn_loc
	    date+=1


	#FOX  
	#Iterate through each day and save into lists, dictionaries to save unique locations for specific days  
	date=1
	while date<=31:
	    fox_loc=[]
	    count=0
	    while count<len(fox_dates):
	        row=fox_dates[count]
	        if row[0]!= "Source":
	            day=row[1].split("_")
	            if len(day)==0 or len(day)==1:
	                day="empty"
	            else:
	                day=day[1]
	            if day == str(date):
	                loc=row[2].upper()

	                #Further cleans the inputs
	                if ("#" not in loc) and ("@" not in loc) and ("-" not in loc) and loc!= "ARCTIC" and loc!= "OBAMA" and loc!="WEST" and "MIG" not in loc and "G7" not in loc:
	                    loc=clean_loc(loc)
	                    if "'S" in loc:
	                        loc=loc.replace("'S ", "")
	                    if "NORTH AND SOUTH KOREA" in loc:
	                        loc="NORTH KOREA"
	                        loc1="SOUTH KOREA"
	                        if (loc1 not in fox_loc):
	                            fox_loc.append(loc1)
	                        if loc1 not in all_fox:
	                            all_fox.append(loc1) 
	                    if "NORTH AND SOUTH AMERICA" in loc:
	                        loc="NORTH AMERICA"
	                        loc1="SOUTH AMERICA"
	                        if (loc1 not in fox_loc):
	                            fox_loc.append(loc1)
	                        if loc1 not in all_fox:
	                            all_fox.append(loc1)
	                    if "NORTH KOREA IRAN" in loc:
	                        loc="NORTH KOREA"
	                        loc1="IRAN"
	                        if (loc1 not in fox_loc):
	                            fox_loc.append(loc1)
	                        if loc1 not in all_fox:
	                            all_fox.append(loc1) 
	                    if "NORTH AMERICA & EUROPE" in loc:
	                        loc="NORTH AMERICA"
	                        loc1="EUROPE"
	                        if (loc1 not in fox_loc):
	                            fox_loc.append(loc1)
	                        if loc1 not in all_fox:
	                            all_fox.append(loc1)
	                    if "UKRAIN" in loc:
	                        item=loc.split(" ")
	                        #print(item)
	                        if len(item)>1:
	                            for i in item:
	                                if (i not in fox_loc):
	                                    fox_loc.append(i)
	                                if i not in all_fox:
	                                    all_fox.append(i)
	                            loc=" "
	                        else:
	                            loc="UKRAINE"
	                    if loc in errors:
	                        items=loc.split(" ")
	                        for i in items:
	                            if (i not in fox_loc):
	                                fox_loc.append(i)
	                            if i not in all_fox:
	                                all_fox.append(i)
	                    else:
	                        if (loc not in fox_loc):
	                            fox_loc.append(loc)
	                        if loc not in all_fox:
	                            all_fox.append(loc)
	        count+=1
	    fox_dict[date]= fox_loc
	    date+=1
	return all_alj, all_cnn, all_fox, alj_dict, cnn_dict, fox_dict

#Takes unique locations and passes them through geopy
def geopy_unique(all_alj, all_cnn, all_fox):
	all_locations=[]
	for i in all_alj:
	    if i not in all_locations:
	        all_locations.append(i)
	for i in all_cnn:
	    if i not in all_locations:
	        all_locations.append(i)
	for i in all_fox:
	    if i not in all_locations:
	        all_locations.append(i)
	#print(len(all_locations))

	from geopy.geocoders import Nominatim
	geolocator = Nominatim(user_agent="melissa727p@gmail.com")

	errors=[]
	unique_gpe={}
	for row in all_locations:
	    if row not in unique_gpe.keys():
	        try:
	            location = geolocator.geocode(row)
	            #Lat. Long for mapping
	            lat=location.latitude
	            long=location.longitude
	            #Country to differentiate between the two maps
	            address=geolocator.reverse(str(lat)+','+str(long), language='en')
	            address=address.raw['address']
	            country=address['country']
	            unique_gpe[row]=[lat,long,country]
	        except:
	            errors.append(row)
	return unique_gpe

#Combines all 3 source dictionaries
#Uses unique_gpe to include corresponding coordinates
#Output is one dictionary without repeated locations on one day
def organize_coord(unique_gpe, alj_dict, cnn_dict, fox_dict):
	coord_data=[]
	count=0
	for i in alj_dict.keys():
	    for j in (alj_dict[i]):
	        if j in unique_gpe.keys():
	            lat, long, country = unique_gpe[j]
	            if [i,j,lat,long, country] not in coord_data:
	                coord_data.append([i, j, lat, long, country])
	    
	for i in cnn_dict.keys():
	    for j in (alj_dict[i]):
	        if j in unique_gpe.keys():
	            lat, long, country = unique_gpe[j]
	            if [i,j,lat,long, country] not in coord_data:
	                coord_data.append([i, j, lat, long, country])
	            
	for i in cnn_dict.keys():
	    for j in (alj_dict[i]):
	        if j in unique_gpe.keys():
	            lat, long, country = unique_gpe[j]
	            if [i,j,lat,long, country] not in coord_data:
	                coord_data.append([i, j, lat, long, country])
	return coord_data

#Creates the new output CSV file for the final step

def write_GPE_csv(coord_data):
    GPE_csv2=open('GPE_LOC_new.csv', "w")
    writer = csv.writer(GPE_csv2)
    count=0
    for i in coord_data:
        if count==0:
            writer.writerow(["Date", "GPE", "Latitude", "Longitude", "Country"])
            print(i)
            writer.writerow(i)
        else:
            writer.writerow(i)
        count+=1
####For unique countries:

#Reads the GPE_LOC csv and makes a dictionary of unique countries each day
def unique_country():
    gpe_csv=open('GPE_LOC_new.csv', encoding='utf-8-sig')
    read_gpe= csv.reader(gpe_csv)
    gpe_file=[]
    for i in read_gpe:
        gpe_file.append(i)
    #print(gpe_file)
    country_dict={}
    all_counts=[]
    date=1
    while date<=31:
        count=0
        day_country=[]
        while count<len(gpe_file):
            row=gpe_file[count]
            if row[0]!= "Date":
                day=row[0]
                if day==str(date):
                    country=row[4]
                    if country not in day_country:
                        day_country.append(country)
                    if country not in all_counts:
                        all_counts.append(country)

            count+=1
        country_dict[date]=day_country
        date+=1

    #gets the latitude/longitude for each country    
    geolocator = Nominatim(user_agent="melissa727p@gmail.com")    
    unique_count={}
    for i in all_counts:
        try:
            location = geolocator.geocode(i) #assuming the csv is source, data, location
            lat=location.latitude
            long=location.longitude
            unique_count[i]=[lat,long]
        except:
            print(i)

    return country_dict, unique_count


#Organizes the data to be easily inputted into the csv file
def country_coord(country_dict, unique_count):
    coord_data=[]
    count=0
    for i in country_dict.keys():
        print(i)
        for j in (country_dict[i]):
            if j in unique_count.keys():
                lat, long = unique_count[j]
                if [i,j,lat,long] not in coord_data:
                    coord_data.append([i,j, lat, long])
    #print(coord_data)             
    return coord_data

#Writes csv with first mention of each country for each day.
#input for world map
def write_country_csv(country_coords):
    Count_csv=open('Country_new.csv', "w")
    writer = csv.writer(Count_csv)
    count=0
    for i in country_coords:
        if count==0:
            writer.writerow(["Date", "Country" "Latitude", "Longitude"])
            print(i)
            writer.writerow(i)
        else:
            writer.writerow(i)
        count+=1

#RUN ALL for command line

#Runs commands for all locations
all_alj, all_cnn, all_fox, alj_dict, cnn_dict, fox_dict = all_locs()
print("all_locs complete")
unique_gpe = geopy_unique(all_alj, all_cnn, all_fox)
print("geopy_unique complete")
coord_data = organize_coord(unique_gpe, alj_dict, cnn_dict, fox_dict)
print("organize_coords complete")
write_GPE_csv(coord_data)
print("GPE_LOC csv is complete")


#Runs commands for only countries
country_dict, unique_count=unique_country()
print("unique_country is complete")
country_coords=country_coord(country_dict, unique_count)
print("country_coord is complete")
write_country_csv(country_coords)
print("Country coordinates csv is complete")















