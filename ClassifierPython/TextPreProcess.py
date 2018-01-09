import os
import sys
import nltk
import re

rootdir="C:/Users/Anupama/Documents/3SummerSemester/KPT/ProjectData/ProjectDataSet/hotels/new-york-city5"


for folder, subs, files in os.walk(rootdir):
    with open(os.path.join(folder, 'python-outfile.txt'), 'w') as dest:
        for fname in files:
             with open(os.path.join(folder, fname), 'r') as src:
              file = src.read()
              newstr = re.sub(r'[^a-zA-Z\n]', r' ', file)
              newstr =  re.sub(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)', r'', newstr)
              print(newstr)
              dest.write(newstr)
