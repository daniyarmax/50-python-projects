adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
place = input("Enter a place: ")
name = input("Enter a name: ")

story = f"One day, {adjective} {name} found a {noun} {verb} inside the {place}" 

print("Your story: ")
print(story)

def worstDayEver(adj, noun, verb, place, name, animal):
    story = f"Today, {name} woke up feeling {adj}.\nThey decided to go to {place} to buy a {noun}.\nSuddenly, a {animal} started {verb} in front of everyone.\nIt was the most {adj} day ever!"
    return story

def veryStrangeTeacher(adj, noun, verb, place, name, animal, subject):
    story = f"Our new teacher, {name}, is actually a {adj} {animal}.\nEvery morning, they {verb} into the classroom.\nInstead of teaching {subject}, they talk about {noun}.\nNobody understands what is happening!"      