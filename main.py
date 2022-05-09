from model.CodeNotFound import CodeNotFound
from model.Dispenser import Dispenser

dispenser = Dispenser()

dispenser.add_drink("A", "Water", 0.20)
dispenser.add_drink("B", "Cola", 0.30)
dispenser.add_drink("C", "Beer", 1.00)

dispenser.add_card(12)
dispenser.add_card(21)
dispenser.add_card(99)

try:
    price = dispenser.get_price("A")
    print(price)
except CodeNotFound:
    print("Code Not Found")

try:
    name = dispenser.get_name("A")
    print(name)
except CodeNotFound:
    print("Code Not Found")

dispenser.charge_card(12, 5.5)
dispenser.charge_card(21, 10.0)
dispenser.charge_card(99, 0.75)

try:
    credit = dispenser.get_credit(12)
    print(credit)
except CodeNotFound:
    print("Code Not Found")

try:
    credit = dispenser.get_credit(21)
    print(credit)
except CodeNotFound:
    print("Code Not Found")

try:
    credit = dispenser.get_credit(99)
    print(credit)
except CodeNotFound:
    print("Code Not Found")

dispenser.update_column(1, "Water", 40)
dispenser.update_column(2, "Cola", 1)
dispenser.update_column(3, "Beer", 50)
dispenser.update_column(4, "Water", 50)

num_can = dispenser.get_num_can("Water")
print(num_can)

dispenser.deliver_drink("A", 12)

try:
    credit = dispenser.get_credit(12)
    print(credit)
except CodeNotFound:
    print("Code Not Found")

num_can = dispenser.get_num_can("Water")
print(num_can)
