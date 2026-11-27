def binary_to_decimal(bits):
    bits = bits.strip()
    if bits == "":
        return None, 0
    value = 0
    steps = 0
    for digit in bits:
        if digit not in "01":
            return None, 0
        value = value * 2 + int(digit)
        steps = steps + 1
    return value, steps

for bits in ["1101", "010", "1000", "11111111", "1012", ""]:
    value, steps = binary_to_decimal(bits)
    if value is None:
        print(f" '{bits}' is not a binary number (use only 0 and 1)")
    else:
        print(f"{bits:>12} -> {value:<4} steps = {steps}")

print()
print("Time: O(L) for L binary digits (one step per digit). Extra space: O(1).")
