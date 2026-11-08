"""Exact four-dimensional zonotope minor certificate, standard-library only.

Usage: python3 verify.py [PAIR_CERTIFICATE.tsv]
No numerical extrapolation or floating point arithmetic is used.
"""
import csv
import itertools
import pathlib
import sys

D = 4
E = [tuple(int(i == j) for i in range(D)) for j in range(D)]
def sub(a,b):
    return tuple(x-y for x,y in zip(a,b))

def determinant4(cols):
    # Independent Laplace/permutation formula; every operation integer.
    ans = 0
    for p in itertools.permutations(range(4)):
        inversions = sum(p[i] > p[j] for i in range(4) for j in range(i+1,4))
        term = 1 if inversions % 2 == 0 else -1
        for j in range(4):
            term *= cols[j][p[j]]
        ans += term
    return ans

def volume(cols):
    return sum(abs(determinant4(c)) for c in itertools.combinations(cols,4))

base = (E[0], E[1], E[2], sub(E[1],E[3]), sub(E[2],E[3]))
h = (1,-1,-1,0)
labels = tuple('e%d'%(i+1) for i in range(4)) + tuple('d%d%d'%(i+1,j+1) for i in range(4) for j in range(i+1,4))
vectors = dict(zip(labels, E + [sub(E[i],E[j]) for i in range(4) for j in range(i+1,4)]))
assert len(labels)==10 and len(set(labels))==10

def components(t, u, v):
    B = base + ((h,) if t else ())
    a = volume(B)
    b = volume(B+(u,))-a
    c = volume(B+(v,))-a
    z = volume(B+(u,v))-a-b-c
    return a,b,c,z

def coeff(u, v):
    a0,b0,c0,z0 = components(0,u,v)
    a1,b1,c1,z1 = components(1,u,v)
    da,db,dc,dz = a1-a0,b1-b0,c1-c0,z1-z0
    return (b0*c0-a0*z0,
            b0*dc+c0*db-a0*dz-z0*da,
            db*dc-da*dz)

out = {}
for p,q in itertools.combinations(labels,2):
    out[(p,q)] = coeff(vectors[p],vectors[q])
assert len(out)==45
assert components(0,vectors['d14'],vectors['d23'])==(4,8,4,8)
assert components(1,vectors['d14'],vectors['d23'])==(14,16,12,14)
assert out[('d14','d23')]==(0,-8,4)

# A finite exhaustive positivity argument: the exceptional polynomial is
# 4t(t-2), every other row has nonnegative coefficients and gamma>0.
for pair,(a,b,c) in out.items():
    if pair != ('d14','d23'):
        assert a>=0 and b>=0 and c>0, (pair,a,b,c)

# Exactly eight pairs have equality at t=0, precisely one at t=2.
assert sum(a==0 for a,b,c in out.values())==8
assert sum(a+2*b+4*c==0 for a,b,c in out.values())==1

path = pathlib.Path(sys.argv[1]) if len(sys.argv)>1 else pathlib.Path(__file__).with_name('PAIR_CERTIFICATE.tsv')
with path.open(newline='', encoding='utf-8') as f:
    rows=list(csv.DictReader(f,delimiter='\t'))
assert len(rows)==45
seen=set()
for row in rows:
    pair=(row['first'], row['second'])
    assert pair in out and pair not in seen, pair
    seen.add(pair)
    listed=(int(row['constant']), int(row['linear']), int(row['quadratic']))
    assert listed==out[pair], (pair,listed,out[pair])
assert len(seen)==45
print('EXACT_PAIR_CLASSIFICATION_OK 45 pairs; 44 nonnegative; one violation for 0<t<2; eight t=0 equalities')
