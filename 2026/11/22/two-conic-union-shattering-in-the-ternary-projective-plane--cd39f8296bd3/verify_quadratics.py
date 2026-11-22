#!/usr/bin/env python3
"""Independent quadratic-form and complete 8192-support trace census."""
from itertools import combinations, product
from collections import Counter

def normal(v):
    pivot=next(t for t in v if t)
    return tuple((x*pow(pivot,-1,3))%3 for x in v)
V=sorted({normal(t) for t in product(range(3),repeat=3) if any(t)})
assert len(V)==13

def det3(M):
    a,b,c=M[0]; d,e,f=M[1]; g,h,i=M[2]
    return (a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g))%3

quadrics=set()
for co in product(range(3),repeat=6):
    if not any(co) or co!=normal(co):
        continue
    a,b,c,d,e,f=co
    hess=((2*a,d,e),(d,2*b,f),(e,f,2*c))
    if not det3(hess):
        continue
    mask=0
    for j,(x,y,z) in enumerate(V):
        val=a*x*x+b*y*y+c*z*z+d*x*y+e*x*z+f*y*z
        if val%3==0:mask |=1<<j
    assert mask.bit_count()==4
    quadrics.add(mask)
assert len(quadrics)==234
concepts={a|b for a,b in combinations(sorted(quadrics),2)}
assert len(concepts)==4641
assert Counter(c.bit_count() for c in concepts)=={5:468,6:1248,7:1638,8:1287}

lines={sum(1<<j for j,v in enumerate(V)
           if sum(a*b for a,b in zip(u,v))%3==0) for u in V}
obstructions={a|b for a,b in combinations(sorted(lines),2)}
assert len(obstructions)==78
counts=[0]*14
shattered=set()
for s in range(1<<13):
    k=s.bit_count()
    if len({c&s for c in concepts}) == (1<<k):
        counts[k]+=1
        shattered.add(s)
assert counts==[1,13,78,286,715,1287,1716,1638,0,0,0,0,0,0],counts
bad7={s for s in range(1<<13) if s.bit_count()==7 and s not in shattered}
assert bad7==obstructions
assert all(any(s|(1<<i) in shattered for i in range(13) if not ((s>>i)&1))
           for s in shattered if s.bit_count()==6)
assert all(s.bit_count()==7 for s in shattered
           if all((s|(1<<i)) not in shattered for i in range(13) if not ((s>>i)&1)))
print('QUADRATIC_CENSUS_PASS; 234 smooth conics; 4641 unions; '
      'faces='+str(counts[:9])+'; nonfaces_seven=78 double lines; facets_seven=1638')
