"""Exact independent Walsh verification of domino tiling multipliers."""
from functools import lru_cache

def tiling_masks(n):
    @lru_cache(None)
    def rec(j):
        if j == n:
            return (0,)
        ans = [((1 << j) | rest) for rest in rec(j + 1)]
        if j + 1 < n:
            pair = ((1 << (n + 2*j)) | (1 << (n + 2*j+1)))
            ans += [pair | rest for rest in rec(j + 2)]
        return tuple(ans)
    return rec(0)

def walsh(a):
    step = 1
    while step < len(a):
        for start in range(0, len(a), 2*step):
            for j in range(start, start+step):
                x,y = a[j],a[j+step]
                a[j],a[j+step] = x+y,x-y
        step *= 2

def transfer(freq,n):
    f0, f1 = 1, (1 if not ((freq >> 0) & 1) else -1)
    if n == 1:return f1
    for j in range(1,n):
        a = -1 if freq & (1 << j) else 1
        b = -1 if bool(freq & (1 << (n+2*(j-1)))) != bool(freq & (1 << (n+2*(j-1)+1))) else 1
        f0,f1 = f1,a*f1+b*f0
    return f1

fib=[0,1]
for i in range(2,15):fib.append(fib[-1]+fib[-2])
for n in range(1,7):
    E = 3*n - 2
    arr = [0]*(1<<E)
    tilings=tiling_masks(n)
    for mask in tilings:arr[mask]=1
    walsh(arr)
    assert len(tilings)==fib[n+1]
    for freq,w in enumerate(arr):
        assert w==transfer(freq,n), (n,freq,w,transfer(freq,n))
    nonzero=[abs(x) for x in arr if x]
    gap=2 if n%3==2 else 1
    assert min(nonzero)==gap and max(nonzero)==fib[n+1]
    assert (0 in arr)==(n%3==2)
    print('direct n=',n,'edges=',E,'tilings=',len(tilings), 'zeros=',arr.count(0),'smallest positive=',min(nonzero))
print('DIRECT_OK')
