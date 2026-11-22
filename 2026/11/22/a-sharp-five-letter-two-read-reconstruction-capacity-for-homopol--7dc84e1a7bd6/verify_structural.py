"""Independent alternating-interval constructor for two-read Kautz conflicts.
Only standard Python. Run: python verify_structural.py
"""
from itertools import product
from math import comb


def structural(q,n):
    V={tuple(v) for v in product(range(q),repeat=n)
       if all(v[i]!=v[i+1] for i in range(n-1))}
    E=set()
    for x in V:
        for lo in range(n-1):
            for hi in range(lo+2,n+1):
                block=x[lo:hi]
                a,b=block[:2]
                if any(t != (a if k%2==0 else b) for k,t in enumerate(block)):continue
                if lo>0 and x[lo-1] in (a,b):continue
                if hi<n and x[hi] in (a,b):continue
                y=x[:lo]+tuple(b if k%2==0 else a for k in range(hi-lo))+x[hi:]
                assert y in V
                E.add(tuple(sorted((x,y))))
    return V,E

def direct(q,n):
    V={tuple(v) for v in product(range(q),repeat=n)
       if all(v[i]!=v[i+1] for i in range(n-1))}
    D={x:{x[:i]+x[i+1:] for i in range(n)} for x in V}
    E=set()
    for x in V:
        for y in V:
            if x<y and len(D[x]&D[y])>=2:E.add((x,y))
    return V,E

for q in range(2,6):
    for n in range(2,6):
        X,A=structural(q,n)
        X2,B=direct(q,n)
        assert X==X2 and A==B,(q,n, len(A),len(B))
        assert len(A)==comb(q,2)*(q-1)**(n-3)*((n-1)*(q-2)+1)
# A reproducible complete check of every exact-support graph at length five.
for s,card,edges in [(2,2,1),(3,42,57),(4,144,252),(5,120,240)]:
    V,E=structural(s,5)
    S={x for x in V if len(set(x))==s}
    J={e for e in E if len(set(e[0]))==s}
    assert len(S)==card and len(J)==edges
print('VERIFY_STRUCTURAL_OK')
