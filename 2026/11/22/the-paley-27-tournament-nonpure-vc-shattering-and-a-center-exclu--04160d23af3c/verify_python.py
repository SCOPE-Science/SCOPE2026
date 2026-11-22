#!/usr/bin/env python3
"""Exhaustive GF(27) Paley-tournament shattering/relative-center test.

Coordinates a+bu+cu^2 are encoded as a+3b+9c, where u^3=u-1.
The complex is the ordinary VC-shattering complex of all 27 residue translates;
its faces include the empty set. Only mod-two homology is computed.
"""
import csv
import itertools
import math
import collections
from pathlib import Path

Q=27

def coord(a):
    return tuple((a//(3**i))%3 for i in range(3))

def num(a):
    return a[0]+3*a[1]+9*a[2]

def plus(a,b):
    return num(tuple((x+y)%3 for x,y in zip(coord(a),coord(b))))

def times(a,b):
    x=coord(a);y=coord(b);p=[0]*5
    for i in range(3):
        for j in range(3):
            p[i+j]=(p[i+j]+x[i]*y[j])%3
    for k in (4,3):
        c=p[k];p[k]=0
        p[k-2]=(p[k-2]+c)%3
        p[k-3]=(p[k-3]-c)%3
    return num(p)

def power(a,n):
    v=1
    while n:
        if n&1: v=times(v,a)
        a=times(a,a);n//=2
    return v

squares={times(x,x) for x in range(1,Q)}
assert len(squares)==13 and 0 not in squares and 2 not in squares
blocks=[{plus(y,r) for r in squares} for y in range(Q)]
assert len(set(map(frozenset,blocks)))==27

def trace_count(s,off_support=False):
    return len({sum(1<<i for i,x in enumerate(s) if x in blocks[y])
                for y in range(Q) if not off_support or y not in s})

faces={0:[()]};off=[1]
for k in range(1,5):
    faces[k]=[s for s in itertools.combinations(range(Q),k) if trace_count(s)==(1<<k)]
    off.append(sum(trace_count(s,True)==(1<<k) for s in itertools.combinations(range(Q),k)))
assert [len(faces[k]) for k in range(5)]==[1,27,351,2925,5967]
assert off==[1,27,351,2925,0]

maps=[tuple(plus(times(a,power(x,3**j)),b) for x in range(Q))
      for j in range(3) for a in sorted(squares) for b in range(Q)]
assert len(set(maps))==1053
rows=[]
remaining=set(itertools.combinations(range(Q),4))
while remaining:
    s=min(remaining)
    orbit={tuple(sorted(f[x] for x in s)) for f in maps}
    assert orbit <= remaining
    remaining.difference_update(orbit)
    rows.append((s,len(orbit),trace_count(s),trace_count(s,True)))
assert len(rows)==22
assert sum(x[1] for x in rows)==math.comb(Q,4)
assert [(sum(r[1]==v and r[2]==16 for r in rows)) for v in (351,1053)] == [2,5]

extension=collections.Counter(t for q in faces[4] for t in itertools.combinations(q,3))
unextended=set(faces[3])-set(extension)
assert len(unextended)==351
assert collections.Counter(extension.values())=={5:351,8:1053,9:117,12:1053}
assert len({tuple(sorted(f[x] for x in (0,1,10))) for f in maps})==351
assert unextended == {tuple(sorted(f[x] for x in (0,1,10))) for f in maps}
# Each pair belongs to precisely three exceptional triples (a 2-(27,3,3) design).
pair_mult=collections.Counter(p for tri in unextended for p in itertools.combinations(tri,2))
assert set(pair_mult.values())=={3} and len(pair_mult)==math.comb(Q,2)

# Binary column-reduction of the exact 3-boundary. A bit is a triangle.
ids={s:i for i,s in enumerate(faces[3])}
pivot={}
for quad in faces[4]:
    col=sum(1<<ids[t] for t in itertools.combinations(quad,3))
    while col:
        bit=col.bit_length()-1
        if bit in pivot: col^=pivot[bit]
        else:
            pivot[bit]=col
            break
rank3=len(pivot)
assert rank3==2249
rank2=math.comb(Q-1,2)
b2=len(faces[3])-rank2-rank3
b3=len(faces[4])-rank3
assert (b2,b3)==(351,3718)
assert len(faces[4])-len(faces[3])+len(faces[2])-len(faces[1])+1 == b3-b2

orbit_path=Path(__file__).with_name('orbit_table.csv')
with orbit_path.open('w',encoding='utf-8',newline='') as f:
    out=csv.writer(f,lineterminator='\n')
    out.writerow(['representative_integer_coordinates','orbit_size','ordinary_traces','off_support_traces'])
    for r in rows:
        out.writerow([' '.join(map(str,r[0])),r[1],r[2],r[3]])
print('FIELD F_3[u]/(u^3-u+1); nonzero squares=',len(squares))
print('SHATTERING_COEFFICIENTS',*[len(faces[k]) for k in range(5)])
print('OFF_SUPPORT_COEFFICIENTS',*off)
print('TOTAL_FOUR_ORBITS',len(rows),'SHATTERED_ORBIT_HISTOGRAM',{351:2,1053:5})
print('NONPURE_TRIPLE_FACETS',len(unextended),'PAIR_BALANCE',set(pair_mult.values()))
print('BOUNDARY_RANKS',26,rank2,rank3)
print('REDUCED_F2_BETTI_2_3',b2,b3)
print('PYTHON_EXHAUSTIVE_OK')
