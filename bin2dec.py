def main(binary):
    length = list(range(0, len(binary)))
    length.reverse()
    result = 0
    for i in enumerate(length):
        if binary[i[0]] == 1:
            result += 2**i[1]
    return result


def convert(binary):
    if isinstance(binary, str):
        return main(binary.strip().split())
    elif isinstance(binary, list):
        return main(binary)
