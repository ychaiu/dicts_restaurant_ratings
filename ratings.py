"""Restaurant rating lister."""

def ratings_dict(filename):

	restaurant_ratings = open(filename,"r")
	contents = restaurant_ratings.read()
	lined_contents = contents.splitlines()

	ratings_dict = {}

	for line in lined_contents:
		name_rating = line.split(":")
		name = name_rating[0]
		rating = name_rating[1]
	
		ratings_dict[name] = rating
	
	sorted_keys = sorted(ratings_dict.keys())
	for key in sorted_keys:
	 	print("{} is rated at {}.".format(key, ratings_dict[key]))

		
ratings_dict("scores.txt")

# put your code here
