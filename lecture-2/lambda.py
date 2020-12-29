people = [{"Name":"Vasu", "country":"Singapore"},
  {"Name":"Anba", "country":"india"},
  {"Name":"Ram", "country":"Singapore"},
  {"Name":"Bharathi", "country":"india"}
]

#lambda is an one line function 
# syntax-(key:lambda input : output)
people.sort(key=lambda person: person["Name"])

print(people)

