print("BINARY CLUE INVESTIGATOR\n")

a = 7
b = 7
print("PART 1: XOR Identity and Equality")
print("a =", a, "| b =", b)
print("a ^ a =", a ^ a)
print("a ^ 0 =", a ^ 0)
print("Result:", "Both numbers are equal" if (a ^ b) == 0 else "Both numbers are different")
print()

clues = [3, 5, 3, 5, 9]
xor_result = 0
for clue in clues:
    xor_result ^= clue

print("PART 2: XOR Cancellation")
print("Clues:", clues)
print("Remaining clue:", xor_result)
print()

numbers = [4, 7, 4, 2, 7, 2, 9]
odd_number = 0
for number in numbers:
    odd_number ^= number

print("PART 3: One Odd-Occurring Number")
print("Numbers:", numbers)
print("Odd-occurring number:", odd_number)
print()

pair_numbers = [3, 9, 3, 5, 5, 7]
xor_of_two = 0
for number in pair_numbers:
    xor_of_two ^= number

print("PART 4: XOR of Two Odd-Occurring Numbers")
print("Numbers:", pair_numbers)
print("XOR of two odd-occurring numbers:", xor_of_two)
print()

rightmost_set_bit = xor_of_two & -xor_of_two
first_odd = 0
second_odd = 0

for number in pair_numbers:
    if number & rightmost_set_bit:
        first_odd ^= number
    else:
        second_odd ^= number

print("PART 5: Splitting by the Rightmost Set Bit")
print("Rightmost set bit:", rightmost_set_bit)
print("First odd-occurring number:", first_odd)
print("Second odd-occurring number:", second_odd)
print()

print("BINARY CLUE INVESTIGATION SUMMARY")
print("XOR Identity: a ^ a = 0 | a ^ 0 = a")
print("One odd-occurring number:", odd_number)
print("Two odd-occurring numbers:", first_odd, "and", second_odd)
