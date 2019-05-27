#Exercise 3
from pathlib import Path
import os
import utils
    
# 1. Contstruct the path to the text file in the data directory using the `pathlib` module [2P]

data_dir = "C:/Users/Admin/Documents/GitHub/exercise-3-SoBoeckler/data"
output_dir = data_dir + "solution/"


creat_cars_path=Path(data_dir, "cars.txt")

# 2. Read the text file [2P]

cars=open(str(creat_cars_path), "r").read()

# 3. Count the occurences of each item in the text file [2P]

carlist=list(cars.split("\n"))#bessere listengestaltung(Wörtertrennung)
count= word_count(carlist)

# 4. Using `pathlib` check if a directory with name `solution` exists and if not create it [2P]

os.path.isdir(data_dir+"/solution") #if true the dir exists
###Path('C:/Users/Admin/Documents/GitHub/exercise-3-SoBoeckler/data/solution').mkdir(parents=True, exist_ok=True) 

# 5. Write the counts to the file `counts.csv` in the `solution` directory in the format (first line is the header): [2P]

#    item, count
#    item_name_1, item_count_1
#    item_name_2, item_count_2
#    ...
with open(output_dir+"count.csv", 'w') as file:
    for key in count.keys():
        file.write("%s,%s\n"%(key,count[key]))


