def find_gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def find_lcm(x, y):
    return (x // find_gcd(x, y)) * y


def get_next_departures(x, y, count):
    interval = find_lcm(x, y)
    return [interval * i for i in range(1, count + 1)]


sample_pairs = [(12, 18), (10, 15), (7, 5), (20, 80)]
for bus1, bus2 in sample_pairs:
    print(f"Buses at {bus1} and {bus2} min intervals meet every {find_lcm(bus1, bus2)} mins; "
          f"first 4 overlaps: {get_next_departures(bus1, bus2, 4)}")

print()
try:
    user_input = input("Enter two bus intervals in minutes (e.g. 12 18) or press Enter to skip: ")
except EOFError:
    user_input = ""

values = user_input.split()
if not values:
    print("No input provided: running sample tests only.")
elif len(values) != 2 or not all(v.isdecimal() and 0 < int(v) <= 999999 for v in values):
    print("Invalid input: please enter two positive whole numbers up to 999999.")
else:
    bus1, bus2 = int(values[0]), int(values[1])
    print(f"Buses at {bus1} and {bus2} min intervals will meet again in {find_lcm(bus1, bus2)} minutes.")

print("Time complexity: O(log min(a, b)) | Space complexity: O(1)")
