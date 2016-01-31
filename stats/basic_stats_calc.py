def main():

    option = True
    values = input("Enter a list of comma separated numbers: ").split(',')

    values = list(map(int, values))

    while option != "0":
        print("Options")
        print("1 = Mean")
        print("2 = Mode")
        print("3 = Median")
        print("0 = Exit")
        option = input("Select an option: ")

        if option == "1":
            result = mean_calc(values)
        elif option == "2":
            result = mode_calc(values)
        elif option == "3":
            result = median_calc(values)
        elif option == "0":
            result = "Exiting"
        else:
            result = "Invalid option"

        print(result)


def mean_calc(values):
    total = 0
    for value in values:
        total += value

    total /= len(values)
    return total


def mode_calc(values):
    total = max(set(values), key=values.count)
    return total


def median_calc(values):
    result = len(values)/2
    is_integer = result.is_integer()

    if is_integer:
        lower_value = result - .5
        higher_value = result + .5

        total = values[int(lower_value)] + values[int(higher_value)]
        total /= 2
        return total
    else:
        return values[result]

main()
