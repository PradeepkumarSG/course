class Flight():
  def __init__(self, capacity):
    self.capacity = capacity
    self.passenger = []

  def add_passenger(self, name):
    if not self.open_seats():
      return False
    self.passenger.append(name)
    return True    
  
  def open_seats(self):
    return self.capacity - len(self.passenger)

f = Flight(3)
pepole = ["A","B","C","D"]

for person in pepole:
  sucess = f.add_passenger(person)
  if sucess:
    print(f"Passenger {person} added sucessfully")
  else:
    print("Flight is Full")



