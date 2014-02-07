#read in names file
names_file = open( "./names.txt")

#loop over file and read into list -- is there a type of list that sorts as you add names?
names = []
for line in names_file:
    line_names = line.split(",")
    for name in line_names:
        name = name.lower()
        name_wo_quotes = name[1:len(name)-1]
        names.append( name_wo_quotes )

#sort names
names.sort()


#dictionary of letter to number
alpha_dict = { "a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10,
               "k":11, "l":12, "m":13, "n":14, "o":15, "p":16, "q":17, "r":18, "s":19,
               "t":20, "u":21, "v":22, "w":23, "x":24, "y":25, "z":26 }


#loop over list of names and make a new list that keeps the scores for each name
#score = (sum of alpha_score for all letters) * (index of name in list)
names_scores = []
index = 1
for name in names:
    name_sum = 0
    for letter in name:
        name_sum += alpha_dict[letter]
    names_scores.append( name_sum * index )
    index = index + 1


print sum(names_scores)
