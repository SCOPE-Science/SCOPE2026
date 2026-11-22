"""Independent exact enumeration of arithmetic progression supports in small abelian groups."""
from itertools import product
from collections import Counter
from math import gcd


def check(moduli):
    H=list(product(*(range(n) for n in moduli)))
    def mul(k,x): return tuple((k*u)%n for u,n in zip(x,moduli))
    def plus(x,y): return tuple((a+b)%n for a,b,n in zip(x,y,moduli))
    def minus(x,y): return tuple((a-b)%n for a,b,n in zip(x,y,moduli))
    def order(x):
        k=1
        while mul(k,x)!=tuple(0 for n in moduli):k+=1
        return k
    N=len(H)
    count_elements=Counter(order(h) for h in H)
    masks={m:set() for m in count_elements if m>=3}
    for h in H:
        m=order(h)
        if m<3:continue
        for x in H:
            triple=frozenset([minus(x,h),x,plus(x,h)])
            assert len(triple)==3
            for y in H:
                support=frozenset([(rot,0) for rot in triple]+[(y,1)])
                masks[m].add(support)
    seen=set()
    for m,S in sorted(masks.items()):
        expected=(N*N*count_elements[m])//(6 if m==3 else 2)
        assert len(S)==expected,(moduli,m,len(S),expected)
        assert not (seen & S),(moduli,m,'support overlap')
        seen.update(S)
        print('PASS',moduli,'step order',m,'supports',len(S))

for moduli in [(3,),(4,),(5,),(6,),(8,),(9,),(12,), (3,3),(4,2),(5,3),(6,2)]:
    check(moduli)
print('PASS all support-incidence checks')
