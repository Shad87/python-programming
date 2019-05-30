'''
#declare an empty list
classmates = []

#add items to lsit 
classmates.append("Sue")
classmates.append("Shad")
classmates.append("Aaron")
classmates.append("Chinonso")
classmates.append("Eva")
classmates.append("Jeremy")
classmates.append("Dan")
classmates.append("Mayank")
classmates.append("Eva")
classmates.append("Julain")
classmates.append("Gus")
print(classmates)

#access an itme at a  specific pposition

print(classmates[0])
print(classmates[5])

#get the size of the list
print(len(classmates))

#remove an item from the end of teh lsit
classmates.pop()
print(classmates)

#insert at a specific position (0,-infinity)
classmates.insert(0, "Gus")

print(classmates)

#removing an item from a list
classmates.remove("Shad")
print(classmates)


#edit an item in the list
classmates[1] = "Sue Work"
print(classmates)

#iterate over a list
for classmate in classmates:
    if(classmates == "Gus"):
        print("Great guys")


#edit elements while iterating
for index, classmate in enumerate(classmates):
   classmates[index] += " - Python Student"

print(classmates)

for index, classmate in enumerate(classmates):
   classmates[index] = ''

   print(classmates)

#changing the entire index to Upper Case
for index, classmate in enumerate(classmates):
   classmates[index] = classmates[index].upper()
   classmates[index] = classmate.upper()

   print(classmates)
'''

#create a list of all the marvel movies fromiron man to end game

marvel_movies = ['Captain America: The First Avenger','Captain Marvel','Iron Man','Iron Man 2','The Incredible Hulk','Thor','Avengers','Iron Man 3','Thor: The Dark World','Captain America: The Winter Soldier','Guardians of the Galaxy','Guardians of the Galaxy Vol. 2','Avengers: Age of Ultron','Ant-Man','Captain America: Civil War','Spider-Man: Homecoming','Doctor Strange','Black Panther','Thor: Ragnarok','Ant-Man and The Wasp','Avengers Infinity War','Avengers: Endgame']
movies_with_the = []

for movie in marvel_movies:
    if 'the ' in movie.lower():
        #print(movie)

        movies_with_the.append(movie)

# print(marvel_movies)

print(movies_with_the)



