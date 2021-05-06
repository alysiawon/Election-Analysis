# print("Hellow World")

# # Data Structures: Lists
# counties = ["Arapahoe", "Denver", "Jefferson"]
# counties.append("El Paso")
# counties.insert(2, "El Paso")
# counties.remove("El Paso")
# counties[2] = "El Paso"
# counties.pop(3)
# print(counties)
# print(counties[1])
# print(len(counties))
# print(counties[0:2])
# print(counties[1:])
# print(counties[1:3])

# # Data Strucutres: Lists: Practice Question
# counties = ["Arapahoe", "Denver", "Jefferson"]
# counties.insert(1, "El Paso")
# counties.remove("Arapahoe")
# counties[2] = "Denver"
# counties[1] = "Jefferson"
# counties.append("Arapahoe")
# print(counties)

# # Data Structures: Dictionaries
# counties_dict = {}
# counties_dict["Arapahoe"] = 422829
# counties_dict["Denver"] = 463353
# counties_dict["Jefferson"] = 432438
# print(counties_dict)
# print(counties_dict)
# print(len(counties_dict))
# print(counties_dict.items())
# print(counties_dict.keys())
# print(counties_dict.values())

# # Data Structures: Dictionaries
# voting_data={
# 	"county": ["Arapahoe", "Denver", "Jefferson"],
# 	"registered_voters": [422829, 463353, 432438],
# }
# print(voting_data)

# # Data Structures: Dictionaries: Practice Question
# voting_data={
#     "county": ["Arapahoe", "Denver", "Jefferson"],
#     "registered_voters": [422829, 463353, 432438],
# }
# voting_data["county"].insert(2,"El Paso")
# voting_data["county"].remove("Arapahoe")
# voting_data["county"].remove("Denver")
# voting_data["county"].insert(3,"Denver")
# voting_data["county"].append("Arapahoe")
# print(voting_data)5

# Decision Statements: If Statement
counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

# Decision Statements: Else-If Statement
temperature = int(input("What is the temperature outside? "))

if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")