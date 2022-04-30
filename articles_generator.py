import pandas as pd
import os

# function that reads csv output from tessaract line by line
def csv_lines(source):
    directory = os.fsencode('output/' + source + '_cropped')
    
    objects = []
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".csv"):
            # print(os.path.join(directory, filename))
            with open('output/' + source + '_cropped/' + filename, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.rstrip()
                    objects.append(line)
            continue
            
    lines = []
    for x in objects:
        x = str(x).split(',')
        lines.append(x)

    new_lines = []
    for x in lines:
        del x[0]
        line_string = ''.join(x)
        new_lines.append(line_string.strip('"'))
    
    return new_lines

# function that creates filepaths and filenames	
def create_filepath(source,articles):
    filepath = []
    for item in articles:
        item = item.replace(':','_')
        item = item.replace('-','')
        item = item.replace(' ','_')
        item = item.replace('.','')
        filepath.append('articles/' + source + '/' + source + '_' + item +'.txt')
    return filepath

# function that writes articles to .txt files	
def article_out(filepath,content):
    for x in range(len(filepath)):
        with open(filepath[x], "w") as f:
            for item in content[x]:
                with open(filepath[x], 'a') as f:
                    f.write(item + ' ')
					
def main(source):
    new_lines = csv_lines(source)
    
    articles = []
    content_string = []
    content = []
    not_ad = 1
    ad_marker = ''
    
    if source == 'aljazeera':
        ad_marker = 'ADVERTISEMENT'
        for x in range(len(new_lines)):
            # detects date tag to indicate beginning of new article
            if new_lines[x][-3:] == 'GMT' and new_lines[x][0].isnumeric():
                content.append(content_string)
                content_string = []
                articles.append(new_lines[x])
                not_ad = 1
                continue
            # detects ad_marker keyword and does not append lines to content[] until new date tag is detected
            if new_lines[x] == ad_marker:
                not_ad = 0
            if not_ad == 1:
                content_string.append(new_lines[x])
            if x == len(new_lines)-1:
                content.append(content_string)
    
    elif source == 'cnn':
        ad_marker = 'CONTENT BY THE ASCENT'
        for x in range(len(new_lines)):
            # detects date tag to indicate beginning of new article
            if new_lines[x][-4:] == '2022' and new_lines[x][0].isnumeric():
                content.append(content_string)
                content_string = []
                articles.append(new_lines[x])
                not_ad = 1
                continue
            # detects ad_marker keyword and does not append lines to content[] until new date tag is detected
            if new_lines[x] == ad_marker:
                not_ad = 0
            if not_ad == 1:
                content_string.append(new_lines[x])
            if x == len(new_lines)-1:
                content.append(content_string)
                
    elif source == 'fox':
        ad_marker = 'Live Coverage begins here'
        for x in range(len(new_lines)):
            # detects date tag to indicate beginning of new article
            if (new_lines[x][-2:] == 'th' or new_lines[x][-2:] == 'st' or new_lines[x][-2:] == 'nd' or new_lines[x][-2:] == 'rd') and new_lines[x][-3].isnumeric():
                content.append(content_string)
                content_string = []
                articles.append(new_lines[x] + '_' + str(x))
                not_ad = 1
                continue
            # detects ad_marker keyword and does not append lines to content[] until new date tag is detected
            if new_lines[x] == ad_marker:
                not_ad = 0
            if not_ad == 1:
                content_string.append(new_lines[x])
            if x == len(new_lines)-1:
                content.append(content_string)
            
    del content[0]    
            
    filepath = create_filepath(source,articles)
    article_out(filepath,content)

news_sources = ['aljazeera','cnn','fox']

for source in news_sources:
    main(source)