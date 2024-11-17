people = [
    {"name": "Harry", "House": "Votualevu"},
    {"name": "Grey", "House":"ATS"},
    {"name": "Barry", "House": "Namaka"}
]

def f(person):
    return person["House"]

people.sort(key=f)
print(people)

people.sort(key=lambda people:people["name"])
print(people)