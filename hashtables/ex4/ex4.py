def has_negatives(a):
    """
    YOUR CODE HERE
    """
    hash_table = {}
    result = []

    for num in a:
        hash_table[num] = -num

    for num in hash_table:
        if num > 0 and hash_table[num] in hash_table:
            result.append(num)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
