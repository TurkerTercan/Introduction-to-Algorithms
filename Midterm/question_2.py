BIT_SIZE: int = 32


def convert_to_bits(binaries):
    bits = [False] * BIT_SIZE
    n = len(binaries)
    i = 0
    for j in range(BIT_SIZE - n, BIT_SIZE):
        if binaries[i]:
            bits[j] = True
        else:
            bits[j] = False
        i += 1
    return bits


def find_absent(arr, least_significant_bit):
    if least_significant_bit < 0:
        return 0
    odd_numbers = []
    even_numbers = []
    for i in arr:
        if i[least_significant_bit]:
            odd_numbers.append(i)
        else:
            even_numbers.append(i)
    if len(odd_numbers) >= len(even_numbers):
        ret_val = find_absent(even_numbers, least_significant_bit - 1)
        ret_val = ret_val << 1
        return ret_val
    else:
        ret_val = find_absent(odd_numbers, least_significant_bit - 1)
        ret_val = ret_val << 1
        ret_val += 1
        return ret_val


if __name__ == '__main__':
    array = [convert_to_bits([False, False, False, False]), convert_to_bits([False, False, False, True]),
             convert_to_bits([False, False, True, True]), convert_to_bits([False, True, False, False])]
    # array is 0, 1, 2, 3, 4 but 2 is absent
    missing = find_absent(array, BIT_SIZE - 1)
    print(missing)
