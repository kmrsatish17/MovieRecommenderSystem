'''
Cloud Computing Project ALS implementation
Group 21
Team: Satish Kumar, Abhijit Nair, Kshitij Khurana
'''

##It takes ratings.csv as input and generate the initital value matrix 

import sys
import csv

users=[]
movies=[]
rating_by_user={}

with open(sys.argv[1], "r") as ins:
    arrVal=[]
    for eachline in ins:
       array_row=eachline.split(',')
       movie_id= array_row[1]
       user_id=  array_row[0]
       ratingVal=array_row[2]
       if not int(movie_id) in movies:
          movies.append(int(movie_id))
       if not int(user_id) in rating_by_user:
          users.append(int(user_id))
          rating_by_user[int(user_id)]={}
          rating_by_user[int(user_id)][int(movie_id)]=float(ratingVal)
       else:
          rating_by_user[int(user_id)][int(movie_id)]=float(ratingVal)


val_X = open(sys.argv[2], 'w')
val_Y = csv.writer(val_X)

print ('Number of Users: %d' %len(users))
print ('Number of Movies: %d' %len(movies))

for user_id in users:
    users=[0.0]*len(movies)
    for movie_id in range(0, len(movies)):
        if user_id in rating_by_user:
           if movies[movie_id] in rating_by_user[user_id]:
              try:
                  exist_movieid=movies[movie_id]
                  users[movie_id]=float(rating_by_user[user_id][exist_movieid])
              except: 
                  continue;
    val_Y.writerows([users])
val_X.close() 
