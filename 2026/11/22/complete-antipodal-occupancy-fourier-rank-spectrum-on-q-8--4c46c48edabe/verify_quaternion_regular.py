"""Separate exact verification using only group multiplication and regular matrices.

Requires SymPy. All arithmetic is symbolic; no numerical rank thresholds.
"""
from itertools import permutations, product
from pathlib import Path
import json
import math
import sympy as S

CERT = json.loads(Path(__file__).with_name('quaternion_witnesses.json').read_text('utf-8'))
H = ((1, 1, 1, 1), (1, 1, -1, -1), (1, -1, 1, -1), (1, -1, -1, 1))
# Quaternion basis 1, i, j, k; group coordinates 2*u + sign, 0<=u<4.
UNITS = ((0, 1, 2, 3), (1, 0, 3, 2), (2, 3, 0, 1), (3, 2, 1, 0))
SIGNS = ((0, 0, 0, 0), (0, 1, 0, 1), (0, 1, 1, 0), (0, 0, 1, 1))

def multiply(g, h):
    u, v = g // 2, h // 2
    return 2 * UNITS[u][v] + ((g & 1) ^ (h & 1) ^ SIGNS[u][v])

def convolution_matrix(s, d):
    f = [(s[j]+d[j])/2 if z==0 else (s[j]-d[j])/2 for j in range(4) for z in (0,1)]
    matrix = S.zeros(8)
    for g in range(8):
        for h in range(8):
            matrix[multiply(g,h), h] += f[g]
    return matrix

def parse(v):
    return S.sympify(v, locals={'I': S.I, 'sqrt': S.sqrt})


# Check the group law rather than assuming that the multiplication table is valid.
assert all(multiply(multiply(g,h),k)==multiply(g,multiply(h,k)) for g in range(8) for h in range(8) for k in range(8))
assert all(multiply(0,g)==g and multiply(g,0)==g for g in range(8))
assert all(multiply(2*t,2*t)==1 for t in range(1,4))
assert multiply(multiply(2,4),6)==1

assert sum(math.factorial(4) // (math.factorial(t['singles']) * math.factorial(t['pairs']) * math.factorial(4-t['singles']-t['pairs'])) * 2**t['singles'] for t in CERT)==255
assert all(sum(1 for perm in permutations(range(4)) if all(tuple(row[j] for j in perm) in H or tuple(-row[j] for j in perm) in H for row in H))==24 for _ in [0])

seen=set(); checked=0
for occ in product((0, 1, 2, 3),repeat=4):
    # 0=empty; 1=only positive; 2=only negative; 3=both signs.
    if occ==(0,0,0,0):continue
    singles=[j for j,o in enumerate(occ) if o in (1,2)]
    pairs=[j for j,o in enumerate(occ) if o==3]
    a,b=len(singles),len(pairs)
    row=next(r for r in CERT if r['singles']==a and r['pairs']==b)
    for rank,w in row['witnesses'].items():
        original_s=list(map(parse,w['s']))
        original_d=list(map(parse,w['d']))
        s=[S.Integer(0)]*4; d=[S.Integer(0)]*4
        for old, new in enumerate(singles):
            s[new]=original_s[old]
            d[new]=original_d[old] * (1 if occ[new]==1 else -1)
        for k,new in enumerate(pairs):
            s[new]=original_s[a+k]
            d[new]=original_d[a+k]
        # Exact support (no additional or missing taps).
        assert all((S.simplify(s[j]+d[j])!=0)==(occ[j] in (1,3)) for j in range(4))
        assert all((S.simplify(s[j]-d[j])!=0)==(occ[j] in (2,3)) for j in range(4))
        actual=convolution_matrix(s,d).rank(simplify=True)
        assert actual==int(rank),(occ,rank,actual)
        checked+=1
    seen.add(occ)
assert len(seen)==255
print('PASS: 255 exact supports; %d explicit rank-realization regular matrices; 24 Walsh coordinate permutations' % checked)
