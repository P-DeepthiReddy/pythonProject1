if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    a=set(arr)
    b=list(a)
    b.sort(reverse=True)
    print(b[1])
