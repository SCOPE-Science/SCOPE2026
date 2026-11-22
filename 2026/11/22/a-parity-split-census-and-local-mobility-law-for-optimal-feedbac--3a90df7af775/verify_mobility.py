"""A separate bit-mask implementation of optimal local-slide degree census.
Run: python3 verify_mobility.py
Independent of verify_forest.py.
"""
from collections import Counter
from itertools import combinations

def forest(mask,n):
    parent=list(range(n*2))
    def find(a):
        while parent[a]!=a:
            a=parent[a]
        return a
    for r in range(2):
        for c in range(n):
            a=r*n+c;b=r*n+(c+1)%n
            if (mask>>a)&1 or (mask>>b)&1:continue
            fa,fb=find(a),find(b)
            if fa==fb:return False
            parent[fa]=fb
    for c in range(n):
        if mask>>c&1 or mask>>(n+c)&1:continue
        fa,fb=find(c),find(n+c)
        if fa==fb:return False
        parent[fa]=fb
    return True

def check(n):
    k=(n+1)//2
    states=set()
    for cc in combinations(range(2*n),k):
        mask=sum(1<<i for i in cc)
        if forest(mask,n):states.add(mask)
    adj=[]
    for r in range(2):
        for c in range(n):
            adj.append((r*n+c,r*n+(c+1)%n))
    for c in range(n):adj.append((c,c+n))
    degrees=Counter();edges=0
    for s in states:
        d=0
        for a,b in adj:
            if (s>>a&1)^(s>>b&1):
                t=s^(1<<a)^(1<<b)
                if t in states:d+=1
        degrees[d]+=1;edges+=d
    edges//=2
    m=(n-1)//2
    if m==1:
        assert degrees=={2:6},degrees
        assert edges==6
    elif m==2:
        assert degrees=={2:20},degrees
        assert edges==20
    else:
        expected=Counter({m-1:n*2**(m-2),m:n*2**(m-1),m+1:n*2**(m-2)})
        assert degrees==expected,(n,degrees,expected)
        assert edges==n*m*2**(m-1),(n,edges)
    return n,len(states),edges,dict(sorted(degrees.items()))

if __name__=='__main__':
    for n in (3,5,7,9,11):print('slide',check(n))
    print('OK odd-prism slide degree polynomials and edge counts')
