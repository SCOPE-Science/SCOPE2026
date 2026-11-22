#!/usr/bin/env python3
"""Independent counts for deterministic three-opinion plurality on triangle windmills."""
from itertools import combinations_with_replacement,product
from math import factorial
from collections import Counter
COLORS=(0,1,2)
TYPES=list(combinations_with_replacement(COLORS,2))

def update(h, petals):
    counts=[0,0,0]
    for x,y in petals:
        counts[x]+=1;counts[y]+=1
    largest=max(counts)
    winners=[i for i in COLORS if counts[i]==largest]
    new_h=winners[0] if len(winners)==1 else h
    new_p=tuple(sorted(((h,h) if x!=y and h in (x,y) else (x,y)) for x,y in petals))
    return new_h,new_p

def time_to_fix(z):
    for t in range(5):
        w=update(*z)
        if w==z:return t
        z=w
    raise AssertionError('unsettled at update 4')

def fixed_count_formula(m):
    # Hub=0; each fixed petal lies in {00,11,22,12,21}.
    total=0
    for k in range(m+1):
     for a in range(m-k+1):
      for b in range(m-k-a+1):
       t=m-k-a-b
       c0,c1,c2=2*k,2*a+t,2*b+t
       if (c1==c2 or (c0>=c1 and c0>=c2)):
        total+=factorial(m)//(factorial(k)*factorial(a)*factorial(b)*factorial(t))*2**t
    return 3*total

def first_entry_census(m):
    C=Counter()
    for p in combinations_with_replacement(TYPES,m):
       ns=Counter(p)
       den=1
       for u in ns.values(): den*=factorial(u)
       mult=factorial(m)//den * 2**sum(ns[pair] for pair in TYPES if pair[0]!=pair[1])
       for h in COLORS:
           C[time_to_fix((h,p))]+=mult
    assert sum(C.values())==3**(2*m+1)
    assert C[0]==fixed_count_formula(m),(m,C[0],fixed_count_formula(m))
    return C

if __name__=='__main__':
    for m in range(1,11):
        c=first_entry_census(m)
        print(m, *(c[t] for t in range(4)), 'total',sum(c.values()))
    # Three residue-class witnesses. Adding one monochromatic petal of each
    # color contributes the same two extra neighbours to every hub score.
    witnesses = [
      (0, [(0,0),(0,1),(1,2),(1,2),(1,2)]),
      (2, [(0,0),(0,0),(0,1),(1,1),(1,2),(1,2)]),
      (2, [(0,0),(0,0),(0,1),(0,1),(1,1),(1,2),(1,2)]),
    ]
    for h, petals in witnesses:
      for extra in range(4):
        p = tuple(sorted(petals + [(i,i) for i in COLORS]*extra))
        assert time_to_fix((h,p)) == 3, (h,len(p))
    print('sharp witnesses and equal-count extensions passed')
    for q in [2,3]:
      for m in [1,2,3,4,5]:
       if q**(2*m+1)>200000:continue
       totals=Counter()
       def independent(s):
        h=s[0]; ns=[0]*q
        for v in s[1:]:ns[v]+=1
        mx=max(ns);win=[i for i,a in enumerate(ns) if a==mx]
        z=[win[0] if len(win)==1 else h]
        for i in range(m):
         x,y=s[1+2*i],s[2+2*i]
         z.append(h if y==h else x)
         z.append(h if x==h else y)
        return tuple(z)
       for s in product(range(q),repeat=2*m+1):
        seen={};t=0;z=s
        while z not in seen:
            seen[z]=t
            z=independent(z)
            t+=1
        assert t-seen[z]==1
        totals[seen[z]]+=1
       if q==3: assert totals==first_entry_census(m),(m,totals,first_entry_census(m))
       print('labeled',q,m,sorted(totals.items()))
