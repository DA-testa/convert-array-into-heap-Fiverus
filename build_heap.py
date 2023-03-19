# Vladislavs Fedins 221RDB416

def heap(data,a, i, swaps):
    
    len1 = i*2+1
    len2 = i*2+2
    res = i
    if len1 < a and data[len1] < data[res]:
        res = len1
    if len2 < a and data[len2] < data[res]:
        res = len2
    if res != i:
        swaps.append((i,res))
        data[i], data[res] = data[res], data[i]
        heap(data, a, res, swaps)

def build_heap(data):
    swaps = []
    a = len(data)
    for i in range(a//2-1,-1,-1):
        heap(data, a, i, swaps)
 
    return swaps    

def main():
    teksts = input()

    if "I" in teksts:    
        n = int(input())
        data = list(map(int, input().split()))
    else:
        fails = input()
        with open("tests/" + fails, 'r') as fails:
            n = int(fails.readline())
            data = list(map(int, fails.readline().split()))

    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()
