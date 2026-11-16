"""Exact finite-field certificate for order-four Latin-square marginal recovery.
Requires Python 3 and NumPy. No numerical floating-point arithmetic is used.
Run: python verify_primary.py [path-to-pivot-manifest.json]
"""
import itertools
import json
import sys
from collections import Counter
from functools import reduce
import numpy as np

PERMS=list(itertools.permutations(range(4)))
SQUARES=[]
def append_rows(rows):
    if len(rows)==4:
        SQUARES.append(tuple(x for r in rows for x in r))
        return
    for row in PERMS:
        if all(row[c] not in (r[c] for r in rows) for c in range(4)):
            append_rows(rows+[row])
append_rows([])
assert len(SQUARES)==576 and len(set(SQUARES))==576
index={s:i for i,s in enumerate(SQUARES)}

PAIRPARTS=[]
for ab in itertools.combinations(range(4),2):
    cd=tuple(k for k in range(4) if k not in ab)
    if ab<cd:
        PAIRPARTS.append((ab,cd))
assert len(PAIRPARTS)==3

CUBES={}
for s in SQUARES:
    for rp in PAIRPARTS:
        for cp in PAIRPARTS:
            blocks=[]
            for rr in rp:
                for cc in cp:
                    q=(4*rr[0]+cc[0],4*rr[0]+cc[1],4*rr[1]+cc[0],4*rr[1]+cc[1])
                    a,b,c,d=(s[k] for k in q)
                    if a!=d or b!=c or a==b:break
                    blocks.append(q)
                if len(blocks)!=2*(rp.index(rr)+1):break
            if len(blocks)!=4:continue
            cube=[]
            for bs in itertools.product((0,1),repeat=4):
                t=list(s)
                for j,on in enumerate(bs):
                    if on:
                        u,v=s[blocks[j][0]],s[blocks[j][1]]
                        for k in blocks[j]:t[k]=v if s[k]==u else u
                cube.append((index[tuple(t)],(-1)**sum(bs)))
            ids=tuple(sorted(i for i,_ in cube))
            if ids not in CUBES:CUBES[ids]=dict(cube)
assert len(CUBES)==54
membership=Counter(i for c in CUBES for i in c)
assert Counter(membership.values())=={1:432,3:144}
assert all(sum(membership[i]==1 for i in c)==8 for c in CUBES)

# Each three-cell event depends on at most three blocks of a four-block cube.
# Alternating signs in the remaining block cancel all such events.
for c in CUBES.values():
    assert sum(c.values())==0
    for cell in range(16):
        for value in range(4):
            assert sum(w for i,w in c.items() if SQUARES[i][cell]==value)==0
    for cells in itertools.combinations(range(16),3):
        pattern_counts={}
        for i,w in c.items():
            t=tuple(SQUARES[i][cell] for cell in cells)
            pattern_counts[t]=pattern_counts.get(t,0)+w
        assert all(v==0 for v in pattern_counts.values())

# Sorted one-hot coordinates. Restrict to compatible distinct cells only.
MASKS=[]
for cell in range(16):
    for value in range(4):
        MASKS.append(sum(1<<i for i,s in enumerate(SQUARES) if s[cell]==value))

basis={}
pivots=[]
rank_by_degree=[]
prime=5
whole=(1<<576)-1

def add_column(mask,label):
    if mask==0:return
    v=np.unpackbits(np.frombuffer(mask.to_bytes(72,'little'),dtype=np.uint8),bitorder='little').astype(np.int16)
    for lead,b in basis.items():
        if v[lead]:v=(v-v[lead]*b)%prime
    nz=np.flatnonzero(v)
    if len(nz):
        lead=int(nz[0])
        basis[lead]=(v*pow(int(v[lead]),-1,prime))%prime
        pivots.append(label)

add_column(whole,[])
rank_by_degree.append(len(pivots))
for d in range(1,5):
    for items in itertools.combinations(range(64),d):
        if len({i//4 for i in items})<d:continue
        v=whole
        for i in items:v&=MASKS[i]
        add_column(v,list(items))
        if len(pivots)==576:break
    rank_by_degree.append(len(pivots))
    if len(pivots)==576:break
assert rank_by_degree==[1,28,246,522,576], rank_by_degree
# Independent integer cube measures imply real rank <=522 at degree 3;
# rank 522 mod 5 implies real rank >=522. Full rank mod 5 proves real
# interpolation by degree 4.

result={"schema_version":1,"modulus":5,"ordered_squares_sha256":None,
 "rank_lower_by_degree":rank_by_degree,"columns":pivots,
 "certificate_columns_by_degree":Counter(map(len,pivots))}
import hashlib
result['ordered_squares_sha256']=hashlib.sha256(bytes(x for s in SQUARES for x in s)).hexdigest()
out=sys.argv[1] if len(sys.argv)>1 else 'pivot_manifest.json'
with open(out,'w',encoding='utf8') as f:
    json.dump(result,f,sort_keys=True,separators=(',',':'))
    f.write('\n')
print('PASS: 576 squares, 54 independent 4-block cubes; mod-5 ranks',rank_by_degree)
print('PASS: 432 private cube states, 144 states in three cubes; all cubic moments cancel')
print('PASS: 576 independent event columns, exact prime-field arithmetic')
