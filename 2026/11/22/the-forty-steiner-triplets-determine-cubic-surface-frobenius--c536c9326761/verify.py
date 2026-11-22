#!/usr/bin/env python3
"""Exact Frobenius permutation certificate for the 40 Steiner triplets.

Run as: python3 verify.py certificate.csv
Only the Python standard library is used. No downloaded data or CAS needed.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations
import csv, io, sys

# Divisors d*H - sum(m_i E_i) on the six-point blowup of P^2.
E = [(0,)+tuple(-int(i==j) for i in range(6)) for j in range(6)]
L = [(1,)+tuple(int(k==i or k==j) for k in range(6))
     for i,j in combinations(range(6),2)]
Q = [(2,)+tuple(int(k!=i) for k in range(6)) for i in range(6)]
curves = E+L+Q
assert len(curves)==len(set(curves))==27

def dot(a,b):
    return a[0]*b[0]-sum(x*y for x,y in zip(a[1:],b[1:]))

def reflection(v,r):
    return tuple(x+dot(v,r)*y for x,y in zip(v,r))

roots = [(0,)+tuple(-1 if j==i else 1 if j==i+1 else 0
                     for j in range(6)) for i in range(5)]
roots.append((1,1,1,1,0,0,0))
assert all(dot(r,r)==-2 for r in roots)
assert all(dot(c,c)==-1 for c in curves)
gen = [tuple(curves.index(reflection(c,r)) for c in curves) for r in roots]
unit=tuple(range(27))
def mul(a,b): return tuple(a[b[i]] for i in range(27))
assert all(mul(g,g)==unit for g in gen)

# Complete 51,840-element Weyl group, from six simple reflections.
seen={unit}; queue=deque([unit]); elements=[]
while queue:
    g=queue.popleft(); elements.append(g)
    for h in gen:
        x=mul(g,h)
        if x not in seen: seen.add(x); queue.append(x)
assert len(elements)==len(seen)==51840

# Incidence-only tritangent construction; the plane section is -K.
antiK=(3,1,1,1,1,1,1)
planes={frozenset((i,j,k)) for i,j,k in combinations(range(27),3)
        if tuple(curves[i][t]+curves[j][t]+curves[k][t]
                 for t in range(7))==antiK}
assert len(planes)==45
assert all(all(dot(curves[i],curves[j])==1 for i,j in combinations(p,2))
           for p in planes)

# For three tritangent planes with disjoint line sets, take their
# nine-line union. Precisely 120 unions admit two such triples.
support=defaultdict(set)
for ps in combinations(planes,3):
    lines=frozenset().union(*ps)
    if len(lines)==9:
        support[lines].add(frozenset(ps))
steiner={lines: triples for lines,triples in support.items()
         if len(triples)==2}
assert len(steiner)==120
for lines,triples in steiner.items():
    assert len([p for p in planes if p <= lines])==6
    row,col=tuple(triples)
    assert all(len(a&b)==1 for a in row for b in col)
    assert frozenset().union(*row)==frozenset().union(*col)==lines
pairs=sorted(steiner, key=lambda p:tuple(sorted(p)))

# Every nine-line Steiner pair has exactly two complementary pairs;
# three disjoint nine-line supports cover all 27 lines.
triplet_set=set()
for a in pairs:
    others=[b for b in pairs if not (a & b)]
    assert len(others)==2
    b,c=others
    assert len(a|b|c)==27 and not(b&c)
    triplet_set.add(frozenset((a,b,c)))
assert len(triplet_set)==40
triplets=sorted(triplet_set,
    key=lambda t: tuple(sorted(tuple(sorted(p)) for p in t)))
triplet_index={t:i for i,t in enumerate(triplets)}

# Independent orbit method: the Weyl orbit of one triplet is the
# entire 40-element set, so its stabilizer has order 1,296.
base=triplets[0]
orbit={frozenset(frozenset(g[i] for i in p) for p in base)
       for g in elements}
assert orbit==triplet_set and len(orbit)==40

def permutation_of_triplets(g):
    return tuple(triplet_index[frozenset(
        frozenset(g[i] for i in p) for p in t)] for t in triplets)

def spectrum(perm):
    visited=set(); counts=Counter()
    for i in range(len(perm)):
        if i not in visited:
            j=i; length=0
            while j not in visited:
                visited.add(j); j=perm[j]; length+=1
            counts[length]+=1
    return tuple(sorted(counts.items()))

def fixed(sp,n): return sum(a*b for a,b in sp if n%a==0)
def encoded(sp): return ','.join(f'{a}^{b}' for a,b in sp)

# Conjugacy closure under generators exactly equals full conjugacy;
# classes are not guessed from cycle structures.
visited=set(); rows=[]
for g in elements:
    if g in visited: continue
    q=deque([g]); visited.add(g); size=0
    while q:
        h=q.popleft();size+=1
        for s in gen:
            x=mul(mul(s,h),s)
            if x not in visited: visited.add(x);q.append(x)
    lines=spectrum(g); tri=spectrum(permutation_of_triplets(g))
    order=1
    from math import lcm
    for n,_ in lines:order=lcm(order,n)
    row={'class':len(rows)+1,'class_size':size,'order':order,
         'line_cycles':encoded(lines),'triplet_cycles':encoded(tri),
         'rational_lines':fixed(lines,1),
         'rational_triplets':fixed(tri,1),
         'counts_1_to_9':','.join(str(fixed(tri,n)) for n in range(1,10))}
    rows.append((row,lines,tri))
assert len(rows)==25 and sum(r['class_size'] for r,_,_ in rows)==51840
assert len({line for _,line,_ in rows})==20
assert len({tri for _,_,tri in rows})==25
assert len({(line,fixed(tri,1)) for _,line,tri in rows})==25
prefix=[len({tuple(fixed(tri,k) for k in range(1,n+1))
             for _,_,tri in rows}) for n in range(1,10)]
assert prefix==[10,14,20,22,23,24,24,24,25]
assert all(sum(n*m for n,m in tri)==40 for _,_,tri in rows)

fields=list(rows[0][0])
buf=io.StringIO(newline='')
writer=csv.DictWriter(buf,fieldnames=fields,lineterminator='\n')
writer.writeheader()
for r,_,_ in rows:writer.writerow(r)
certificate=buf.getvalue().encode('utf-8')
if len(sys.argv)>1:
    with open(sys.argv[1],'rb') as f:
        assert f.read()==certificate, 'certificate mismatch'
else:
    with open('certificate.csv','wb') as f:f.write(certificate)
print('VERIFIED_W_E6_51840_CLASSES_25_STEINER_PAIRS_120_TRIPLETS_40_SPECTRA_25_PREFIX_10_14_20_22_23_24_24_24_25')
