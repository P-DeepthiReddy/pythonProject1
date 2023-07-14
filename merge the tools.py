def merge_the_tools(string, k):
    while string:  # while string is not None
        seen = ''
        s = string[0:k]
        for c in s:
            if c not in seen:
                seen += c
        print(seen)
        string = string[k:]


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
