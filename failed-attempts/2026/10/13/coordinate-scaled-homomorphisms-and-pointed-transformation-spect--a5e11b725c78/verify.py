#!/usr/bin/env python3
"""Exact finite verification for coordinate forms in truncated-difference algebras."""
from itertools import product
from collections import Counter
from math import factorial, comb

checks=0

def test(cond,msg):
    global checks
    checks+=1
    if not cond: raise AssertionError(msg)

def dotsub(x,y):
    return tuple(max(0,b-a) for a,b in zip(x,y))

def lower_sets(maxima):
    universe=list(product(*(range(r+1) for r in maxima)))
    for mask in range(1,1<<len(universe)):
        if not (mask&1):continue
        members={universe[i] for i in range(len(universe)) if mask>>i&1}
        if all(all(b in members for b in product(*(range(a+1) for a in v))) for v in members):
            yield tuple(sorted(members))

def maps_classified(D,E):
    srcm=len(D[0]); tgtm=len(E[0]); srcmax=[max(v[i] for v in D) for i in range(srcm)]
    options=[]
    for j in range(tgtm):
        op=[None]
        for i,r in enumerate(srcmax):
            if r:
                for k in range(1, max(v[j] for v in E)//r+1): op.append((i,k))
        options.append(op)
    for choices in product(*options):
        vals=tuple(tuple(0 if ch is None else ch[1]*a[ch[0]] for ch in choices) for a in D)
        if set(vals)<=set(E):yield vals

def is_hom(D,E,vals):
    place={a:i for i,a in enumerate(D)}
    return all(vals[place[dotsub(a,b)]]==dotsub(vals[i],vals[j]) for i,a in enumerate(D) for j,b in enumerate(D))

D1=[]
for n in range(1,4):D1+=list(lower_sets((n,)))
D2=list(lower_sets((2,2)))
D3=list(lower_sets((1,1,1)))
Dsmall=[D for D in D1+D2+D3 if len(D)<=6]
# Exhaust all scalar maps, including arbitrary nonrectangular sources and targets.
scalar_maps=0
for D in Dsmall:
  for t in range(0,4):
    E=tuple((k,) for k in range(t+1))
    expected=set(maps_classified(D,E))
    actual=set()
    for tail in product(E,repeat=len(D)-1):
      vals=(E[0],)+tail
      if is_hom(D,E,vals):actual.add(vals)
      scalar_maps+=1
    test(actual==expected, f'scalar {D} -> {E}: actual {actual} expected {expected}')

# Arbitrary finite downset pairs, maps exhaustive for small sizes.
small=[D for D in D1+D2+D3 if len(D)<=4]
pair_maps=0
for D in small:
  for E in small:
    if len(D[0])>3 or len(E[0])>3:continue
    if len(E)**(len(D)-1)>6000:continue
    expected=set(maps_classified(D,E))
    actual=set()
    for tail in product(E,repeat=len(D)-1):
      vals=(E[0],)+tail
      if is_hom(D,E,vals):actual.add(vals)
      pair_maps+=1
    test(actual==expected, f'pair {D}->{E}: {len(actual)} != {len(expected)}')

# Verify all rectangular hom counts for source/target <= three axes and side lengths <=3.
boxes=[]
for m in (1,2,3):
  for radii in product((1,2,3),repeat=m):
    if len(tuple(product(*(range(r+1) for r in radii))))<=48:
      boxes.append((radii,tuple(product(*(range(r+1) for r in radii)))))
for rs,D in boxes:
  for ts,E in boxes:
    if len(rs)>3 or len(ts)>3: continue
    predicted=1
    for tj in ts:predicted*=1+sum(tj//ri for ri in rs)
    got=sum(1 for _ in maps_classified(D,E))
    test(got==predicted,f'box hom {rs}->{ts}: {got} != {predicted}')

# Endomorphism rank spectrum, idempotents, embedded retract sets for homogeneous boxes.
def stirling(n,k):
    if n==k:return 1
    if k==0:return 0
    return k*stirling(n-1,k)+stirling(n-1,k-1)

def bell(n):return sum(stirling(n,k) for k in range(1,n+1))
for m in range(1,5):
  for radius in (1,2,3):
    D=tuple(product(range(radius+1),repeat=m))
    if m==4 and radius==3: continue
    endos=list(maps_classified(D,D))
    expected=(m+1)**m
    test(len(endos)==expected, f'endomorphisms m={m} r={radius}')
    ranks=Counter(len(set(vals)) for vals in endos)
    for k in range(m+1):
      exp=comb(m,k)*factorial(k)*stirling(m+1,k+1)
      test(ranks[(radius+1)**k]==exp,f'rank m={m},r={radius},k={k}')
    idem=[]
    for vals in endos:
      lookup=dict(zip(D,vals))
      if all(lookup[lookup[x]]==lookup[x] for x in D): idem.append(vals)
    predicted=sum(comb(m,k)*(k+1)**(m-k) for k in range(m+1))
    test(len(idem)==predicted,f'idempotents m={m},r={radius}')
    idem_ranks=Counter(len(set(vals)) for vals in idem)
    for k in range(m+1):
      test(idem_ranks[(radius+1)**k]==comb(m,k)*(k+1)**(m-k),f'idempotent rank m={m},r={radius},k={k}')
    images={frozenset(vals) for vals in idem}
    test(len(images)==bell(m+1),f'retract images m={m},r={radius}')
    image_ranks=Counter(len(im) for im in images)
    for k in range(m+1):
      test(image_ranks[(radius+1)**k]==stirling(m+1,k+1),f'retract rank m={m},r={radius},k={k}')

print(f'VERIFY_OK {checks} independent exact comparisons; {scalar_maps} scalar maps; {pair_maps} small downset-pair maps; {len(boxes)**2} rectangular pairs; homogeneous endomorphism/retract spectra m<=4')
