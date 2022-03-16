"""Restaurant rating lister."""

# put your code here
def score_reader():
    scores_txt = open('scores.txt')
    scores = {}
    for line in scores_txt:
        line = line.rstrip()
        restaurant, score = line.split(':')
        scores[restaurant] = int(score)
    return scores

def add_restaurants(scores):
    print("Add a restaurant")
    restaurant = input('Restaurant name \n')
    rating = int(input("Rating \n"))

    scores[restaurant] = rating

def print_sorted_scores(scores):
    for restaurant, rating in sorted(scores.items()):
        print(f"{restaurant} is rated at {rating}.")

scores = score_reader()
add_restaurants(scores)
print_sorted_scores(scores)