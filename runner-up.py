if _name_ == '_main_':
    n = int(input())
    arr = set(map(int, input().split()))
    arr = list(arr)
    arr.sort()
    print(arr[-2])
