"""Exact finite verification for preconditionals on pointed coatom extensions.
Only verifies finite instances; the general formulas require the written proof.
"""
from itertools import product,combinations
from math import comb,factorial

def check(m):
    n=m+3; c=m+1; top=m+2
    lower=[{0}]+[{0,i} for i in range(1,m+1)]+[set(range(m+2)),set(range(n))]
    def le(x,y):return x in lower[y]
    meet=[[max((z for z in range(n) if le(z,x) and le(z,y)),key=lambda z:len(lower[z])) for y in range(n)] for x in range(n)]
    T=F=0; profiles=set(); orbits=set(); cases=0
    for h in product(range(m+1),repeat=m):
        if any(h[i]==i+1 for i in range(m)):continue
        targets={a for a in h if a>0}
        for opts in product((False,True),repeat=m):
            S={i+1 for i,b in enumerate(opts) if b}
            if S&targets:continue
            rows=[(top,)*n]
            for i in range(1,m+1):
                rows.append(tuple(top if y in (i,c,top) else h[i-1] for y in range(n)))
            rows.append(tuple(0 if y==0 else (top if y in (c,top) or y in S else y) for y in range(n)))
            rows.append(tuple(range(n)))
            assert all(rows[x][x]==top and meet[x][rows[x][0]]==0 for x in range(n))
            for x in range(n):
                for y in range(n):
                    assert le(meet[x][y],rows[x][y]) # P2
                    assert le(rows[x][y],rows[x][meet[x][y]]) # P3
                    if x==top:assert le(rows[x][y],y) # P1
                    for z in range(n):
                        assert le(rows[x][meet[y][z]],rows[x][y]) # P4
                        assert le(rows[x][rows[meet[x][y]][z]],rows[meet[x][y]][z]) # P5
            cases+=1;T+=1
            neg=tuple(rows[x][0] for x in range(n))
            if all(le(x,neg[neg[x]]) for x in range(n)):
                F+=1
                pairs={tuple(sorted((i+1,h[i]))) for i in range(m) if h[i]>0}
                assert all(h[j-1]==i for i,j in pairs)
                orbits.add((len(pairs),len(S)))
    expectedT=sum(comb(m,s)*(m-s+1)**s*(m-s)**(m-s) for s in range(m+1))
    expectedF=sum(factorial(m)//(2**j*factorial(j)*factorial(m-2*j))*2**(m-2*j) for j in range(m//2+1))
    expected_orbits=sum(m-2*j+1 for j in range(m//2+1))
    assert (T,F,len(orbits))==(expectedT,expectedF,expected_orbits)
    print(f'm={m} T={T} F={F} F_iso={len(orbits)} checks={cases}',flush=True)

for m in range(1,5):check(m)
print('POINTED_COATOM_PRECONDITIONAL_CHECKS_OK')
