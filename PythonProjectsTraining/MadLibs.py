# Taken from https://www.freecodecamp.org/news/python-projects-for-beginners/#mad-libs-python-project

#String concatenation (aka how to put strings together)
#Create a string that says "Mariupol é uma cidade da Ucrânia localizada no leste do país, no ____ "
#To comment several lines of code you can use Ctrl + K, Ctrl + C, or Alt + Shift + A

# region = "Óblast de Donetsk" # some string variable

# a few ways to do this
# print("Mariupol é uma cidade da Ucrânia localizada no leste do país, no " + region)
# print("Mariupol é uma cidade da Ucrânia localizada no leste do país, no {}".format(region))
# print(f"Mariupol é uma cidade da Ucrânia localizada no leste do país, no {region}")

adj = input("Adjective that discribes someone that is mentally deranged or insane: ")
verb1 = input("Verb that shows a feeling of expectation and desire for a particular thing to happen: ")
verb2 = input("Verb that discribes a move from one place to another : ")
famous_person = input("Name of a Dictator: ")

madlib = f"This war is so {adj}! Why does {famous_person} decided to invade Ucraine? how dares he? \
I really {verb1} that he changes his mind and {verb2} back to his country"

print(madlib)