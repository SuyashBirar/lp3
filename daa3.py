
def fractional_knapsack(capacity, items):
    # Calculate value-to-weight ratio
    items.sort(key=lambda x: x[1] / x[0], reverse=True)

    total_value = 0.0

    print("\nSelected Items:")

    for weight, value in items:
        if capacity == 0:
            break

        if weight <= capacity:
            # Take the complete item
            capacity -= weight
            total_value += value

            print("Weight:", weight, "Value:", value,
                  "Fraction: 1")

        else:
            # Take a fraction of the item
            fraction = capacity / weight
            total_value += value * fraction

            print("Weight:", weight, "Value:", value,
                  "Fraction:", round(fraction, 2))

            capacity = 0

    print("\nMaximum Total Value:", round(total_value, 2))


# Main program
n = int(input("Enter the number of items: "))

items = []

for i in range(n):
    weight = float(input("Enter weight of item: "))
    value = float(input("Enter value of item: "))

    items.append((weight, value))

capacity = float(input("Enter knapsack capacity: "))

fractional_knapsack(capacity, items)
