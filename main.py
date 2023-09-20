# Apple XML extractor by Glenn Woodward

import pandas as pd
import xml.etree.ElementTree as ET


# Enter the filename for the xml file here (the below is an example):
filename = 'iTunes Music Library.xml'



tree = ET.parse(filename)
root = tree.getroot()
main_dict=root.findall('dict')
for item in list(main_dict[0]):
    if item.tag=="dict":
        tracks_dict=item
        break
tracklist=list(tracks_dict.findall('dict'))

podcast=[]
purchased=[]

datalist = []

for i in range(len(tracklist)):
    target = tracklist[i]

    x = []

    for item in target:
        x.append(item.text)

    list_a = x[::2]
    list_b = x[1::2]

    dict = {}
    for key in list_a:
        for value in list_b:
            dict[key] = value
            list_b.remove(value)
            break
    datalist.append(dict)
    for item in list_a:
        b = dict.get(item)
    i += 1


df = pd.DataFrame(datalist)
print(df.tail().to_string())

df.to_csv('extract.csv', index=False)