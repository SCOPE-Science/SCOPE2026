#!/usr/bin/env python3
"""Direct finite-state traversal of XOR wheel dynamics, independent of matrix ranks."""

def update(x,n):
    hub=x&1
    rim=[(x>>(j+1))&1 for j in range(n)]
    out=sum(rim)%2
    for j in range(n):
        out |= ((hub ^ rim[(j-1)%n] ^rim[(j+1)%n])<<(j+1))
    return out

def predict(n):
    if n%2:return [1<<(n+1)]
    v=n&-n
    if v==2:ranks=[n+1,n,n-1,n-2]
    elif v==4:ranks=[n+1,n-2,n-3,n-4]
    else:ranks=[n+1,n-2,n-4]+[n-min(2*t,v) for t in range(3,v//2+1)]
    p=n-v
    c=[1<<(p+n+1-r) for r in ranks]
    return [c[0]]+[c[i]-c[i-1] for i in range(1,len(c))]

for n in range(3,12):
    hist={}
    for x in range(1<<(n+1)):
        seen={};state=x;t=0
        while state not in seen:
            seen[state]=t
            state=update(state,n)
            t+=1
        entry=seen[state]
        hist[entry]=hist.get(entry,0)+1
    actual=[hist.get(t,0) for t in range(max(hist)+1)]
    expected=predict(n)
    assert actual==expected, (n,actual,expected)
    print(n,actual)
print('DIRECT ENUMERATION PASSED')
