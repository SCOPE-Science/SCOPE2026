"""Independent finite enumeration for midpoint-quandle idempotents (finite prime fields).
Run with Python 3; no third-party dependencies.
"""
from itertools import product
from collections import Counter


def verify(p,r,full_closure=False):
    V=list(product(range(p), repeat=r))
    n=len(V)
    idx={v:i for i,v in enumerate(V)}
    half=pow(2,-1,p)
    target_pairs=[]
    for z in V:
        target_pairs.append([(ix,idx[tuple((2*z[j]-x[j])%p for j in range(r))]) for ix,x in enumerate(V)])
    results=[]
    for a in product(range(p),repeat=n):
        aug=sum(a)%p
        # check coefficient of e_z in u star u for all z
        if all(sum(a[x]*a[y] for x,y in P)%p == a[z] for z,P in enumerate(target_pairs)):
            results.append((a,aug))
    ell=1
    while pow(2,ell,p)!=1:ell+=1
    N=(p**r-1)//ell
    want=p**N+1
    assert len(results)==want,(p,r,len(results),want)
    assert Counter(aug for a,aug in results)=={0:1,1:want-1}
    # Verify elementwise closure (the nonzero idempotents form the expected quandle).
    if full_closure:
        nonzero={a for a,aug in results if aug==1}
        def star(a,b):
            return tuple(sum(a[x]*b[y] for x,y in P)%p for P in target_pairs)
        for a in nonzero:
            for b in nonzero:
                assert star(a,b) in nonzero
    print(f'p={p},r={r},dimension={n},ell={ell},N={N},idempotents={len(results)},nonzero={len(results)-1},OK',flush=True)

if __name__=='__main__':
    verify(3,1,True)
    verify(5,1,True)
    verify(3,2,True)
    verify(7,1,False)

# Additional independent extension-field enumeration; F_9 = F_3[t]/(t^2+1).
def verify_nine():
    def add(x,y):
        return (x%3+y%3)%3 + 3*((x//3+y//3)%3)
    def mul(x,y):
        a,b=x%3,x//3
        c,d=y%3,y//3
        return (a*c+2*b*d)%3+3*((a*d+b*c)%3)
    p=3
    pairs=[[(i,(2*z-i)%p) for i in range(p)] for z in range(p)]
    count=0
    for a in product(range(9),repeat=3):
        if all(__import__('functools').reduce(add,(mul(a[i],a[j]) for i,j in z_pairs),0)==a[z] for z,z_pairs in enumerate(pairs)):
            count+=1
    assert count == 10, count
    print('q=9,p=3,r=1,idempotents=10,OK',flush=True)

if __name__=='__main__':
    verify_nine()
    print('VERIFY_OK',flush=True)
