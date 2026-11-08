#!/usr/bin/env python3
"""Finite-field-prime examples of affine point-hyperplane incidence domination."""
import itertools

def check(q,d):
    assert q>=2 and all(q%p for p in range(2,int(q**.5)+1))
    V=list(itertools.product(range(q),repeat=d))
    normal=[]
    for a in V[1:]:
        pivot=next(i for i,z in enumerate(a) if z)
        v=tuple(z*pow(a[pivot],-1,q)%q for z in a)
        if v not in normal:normal.append(v)
    H=[(a,b) for a in normal for b in range(q)]
    N={h:{v for v in V if sum(x*y for x,y in zip(h[0],v))%q==h[1]} for h in H}
    zero=(0,)*d
    def axis(i,t):return tuple(t if j==i else 0 for j in range(d))
    B={zero}|{axis(i,t) for i in range(d) for t in range(1,q)}
    C={(tuple(1 if j==0 else 0 for j in range(d)),t) for t in range(q)}
    C|={(tuple(1 if j==i else 0 for j in range(d)),t) for i in range(1,d) for t in range(1,q)}
    B_prime=B
    C_prime={(tuple(1 if j==0 else 0 for j in range(d)),t) for t in range(q)}
    matching={((tuple(1 if j==i else 0 for j in range(d)),t),axis(i,t)) for i in range(d) for t in range(1,q)}
    matching.add(((tuple(1 if j==0 else 0 for j in range(d)),0),zero))
    assert len(H)==q*(q**d-1)//(q-1)
    assert len(B)==d*(q-1)+1 and len(C)==len(B)
    assert len(C_prime)==q
    assert all(bool(N[h]&B) for h in H)
    assert all(any(v in N[h] for h in C) for v in V)
    assert all(any(v in N[h] for h in C_prime) for v in V)
    assert len(matching)==len(B)==len(C)
    assert {h for h,v in matching}==C and {v for h,v in matching}==B
    assert all(v in N[h] for h,v in matching)
    assert len(B|C)==len(B)+len(C)  # bipartite vertex classes
    gap=len(B)*2-(len(B)+len(C_prime))
    assert gap==(d-1)*(q-1)
    print(f'q={q} d={d} points={len(V)} hyperplanes={len(H)} total={len(B)+len(C_prime)} paired={2*len(B)} gap={gap} incidence_and_matching=PASS')

for q,d in [(2,2),(3,2),(5,2),(7,2),(2,3),(3,3),(2,4),(3,4)]:
    check(q,d)
print('CONSTRUCTION_CHECKS_PASS')
