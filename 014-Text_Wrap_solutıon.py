import textwrap


def wrap(string, max_width):
    l = list()
    for i in range(0, len(string), max_width):
        l.append(string[i:i + max_width])

    return "\n".join(l)


if __name__ == '__main__':