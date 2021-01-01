def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        a = string[i:i + k]
        sonuc = ""
        for j in a:
            if j not in sonuc:
                sonuc += j
        print(sonuc)


if __name__ == '__main__':