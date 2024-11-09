def sol(arr):
    tmp = []
    res = []
    
    for x in arr:
        if x == 'E':
            v = min(tmp)
            tmp.remove(v)
            res.append(v)
        else:
            tmp.append(int(x))
    
    return res

if __name__ == "__main__":
    arr = input().split(" ")
    res = sol(arr)
    print(res)