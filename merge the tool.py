def merge_the_tools(string, k):
    n = len(string)
    m = int(n/k)
    result = []
    for i in range(0,n,k):
        result.append("".join(dict.fromkeys(string[i:i+k])))
    print("\n".join(result))
