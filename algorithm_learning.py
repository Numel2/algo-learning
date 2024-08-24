list = [6, 5, 4, 3, 2, 1]
query = 5

def bruteforce():
    position = 0
    while position < len(list):
        if list[position] == query:
            return print(position)
        position += 1
    return print(-1)


def bruh():
    low = 0
    high = len(list) - 1

    while low <= high:
        middle = (low+high) // 2
        mid_num = list[middle]

        print("lo:", low, ", hi:", high, ", mid:", middle, ", mid_number:", mid_num)

        if mid_num == query:
            return print(middle)
        elif mid_num < query:
            high = middle - 1
        elif mid_num > query:
            low = middle + 1
    return print(-1)

bruh()