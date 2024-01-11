
> mkdir comp 370 / > cd comp 370 / > mkdir hw3 / > cd hw3   
> curl https://raw.githubusercontent.com/derpypony/My-Little-Pony-Data-Science-is-Magic-/master/clean_dialog.csv >  ~/comp370/hw3/pony.csv

Task 1: Exploring the dataset

1. How big is the dataset?
36860 lines, using the command:
> wc -l pony.csv

2. What’s the structure of the data?
> sudo apt install csvtool
> csvstat pony.csv  // get error because not in utf-8 format
// opened the csv file on vscode and saved the file with utf-8 format
fields are: "title", "writer", "dialog", and "pony"
types are: Text (for each field)

3. How many episodes does it cover?
> csvstat pony.csv
the # of titles = # of episodes so look at the unique values under title
197 episodes

4. During the exploration phase, find at least one aspect of the dataset that is unexpected
In the dialog field, you can see that it says true that there are null values, meaning that if someone were to look at the relationship between any of the 2 fields, the fact that there are null values corresponding to noon-null values in other fiellds might cause confusion.

Task 2: Analyze speaker frequency
> csvstat pony.csv
# from most common values in the field "pony", we can see who has the most lines
most common values: Twilight Sparkle, Rainbow Dash, Pinkie Pie, Applejack, Rarity
> csvgrep -c "pony" -m "Twilight Sparkle" pony.csv | wc -l 
// 4832
> csvgrep -c "pony" -m "Rainbow Dash" pony.csv | wc - 
// 3155
> csvgrep -c "pony" -m "Pinkie Pie" pony.csv | wc -l
 // 2923
> csvgrep -c "pony" -m "Applejack" pony.csv | wc -l 
// 2872
> csvgrep -c "pony" -m "Rarity" pony.csv | wc -l 
// 2723

> head -n 1 pony.csv    # checking whether header is included -- it is 

number of lines: 36860 - 1  = 36859
> bc -l // to calculate statistics            
(line_num / 36859) * 100