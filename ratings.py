"""Restaurant rating lister."""

def ratings_dict(filename):

	restaurant_ratings = open(filename,"r")

	ratings_dict = {}

	for line in restaurant_ratings:
		name, rating = line.rstrip().split(":")
	
		ratings_dict[name] = rating
	
	sorted_keys = sorted(ratings_dict.keys())
	# for key in sorted_keys:
	#  	print("{} is rated at {}.".format(key, ratings_dict[key]))

	return ratings_dict

# put your code here

def user_ratings():
	user_dict = ratings_dict("scores.txt")
	name = input("What is the name of the restaurant?")
	score = input ("What is your rating for this restaurant?")
	user_dict[name] = score
	
	sorted_keys = sorted(user_dict.keys())
	for key in sorted_keys:
	 	print("{} is rated at {}.".format(key, user_dict[key]))


user_ratings()


#  Traceback (most recent call last):
#   File "ratings.py", line 14, in <module>
#     ratings_dict("scores.txt")
#   File "ratings.py", line 10, in ratings_dict
#     restaurant_name =restaurant_ratings.split(":")[0]
# AttributeError: '_io.TextIOWrapper' object has no attribute 'split'

