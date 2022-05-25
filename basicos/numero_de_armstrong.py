def numeros_armstrong(max_digits):
    i = 0

    while True:
        if (len(list(str(i))) > max_digits):
            # print(str(i))
            break
        
        numbers = list(str(i))
        # print(numbers)
        # if (i > 20):
        #     break
        total = 0

        for number in numbers:
            # print(f"total before: {total}")
            total += int(int(number)**len(numbers))
            # print(f"sums {number}^{len(numbers)} {int(number)**int(len(numbers))}")
            # print(f"total after: {total}")
            # return

        if (total == i):
            print(f"Armstrong Number: {i}")
        # print(f"\ntotal: {total}\ni: {i}\n")
        i += 1

numeros_armstrong(6)