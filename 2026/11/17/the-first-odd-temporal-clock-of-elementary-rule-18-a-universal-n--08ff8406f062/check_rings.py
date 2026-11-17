"""Independent direct local-rule evolution, without temporal-column graphs.
Run: python3 check_rings.py
"""
from collections import Counter

def F(x,n):
    y=0
    for i in range(n):
        left=(x>>((i-1)%n))&1
        middle=(x>>i)&1
        right=(x>>((i+1)%n))&1
        if (left,middle,right) in ((0,0,1),(1,0,0)):
            y|=1<<i
    return y

def census(n):
    nxt=[F(x,n) for x in range(1<<n)]
    visited=set()
    count=Counter()
    odd_cycles=[]
    for s in range(1<<n):
        if s in visited:continue
        seen={};path=[];p=s
        while p not in seen and p not in visited:
            seen[p]=len(path);path.append(p);p=nxt[p]
        visited.update(path)
        if p in seen:
            cyc=path[seen[p]:]
            count[len(cyc)]+=1
            if len(cyc)>1 and len(cyc)%2:
                odd_cycles.append(cyc)
    return count,odd_cycles

for n in range(3,12):
    periods,odd=census(n)
    if n<11:
        assert not odd,(n,odd)
    else:
        assert periods[11]==2 and len(odd)==2, (n,periods,odd)
        assert {min(c) for c in odd}=={75,105}
        for c in odd:
            x=c[0]
            for i in range(1,12):
                x=F(x,n)
                assert (x==c[0])==(i==11)
    print('n='+str(n)+' periods='+','.join(str(k)+':'+str(v) for k,v in sorted(periods.items())))
print('WITNESS_11='+format(579,'011b'))
print('TWO_ODD_ORBITS_AT_N11')
