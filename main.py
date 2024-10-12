import random


def main():
    total = 0
    numbers = []
    
    while total < 100:
        x = random.randint(0, 100)
        total += x
        numbers.append(x)
        if total > 100:
            total -= x
            break

    print(f'The random values are {numbers}')
    print(f'The total is {total}')

    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, total


if __name__ == '__main__':
    main()
