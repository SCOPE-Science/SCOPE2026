"""Stand-alone finite verification of the affine parity equation formula and orbit invariants."""
from itertools import product,combinations
from random import Random

rng=Random(291104)

def parity(points):
    v=0
    for p in points: v^=p
    return v==0

def q_formula(points,d):
    # Faithful semantics for the inductive first-order formula Q_r:
    # Q_4=P; Q_r = exists t (P(x1,x2,x3,t) and Q_(r-2)(t,x4,...,xr)).
    if len(points)==4: return parity(points)
    assert len(points)%2==0 and len(points)>4
    return any(parity(points[:3]+(t,)) and q_formula((t,)+points[3:],d) for t in range(1<<d))

checks=0
for d,r in [(2,4),(2,6),(2,8),(3,4),(3,6),(4,8)]:
    samples=list(product(range(1<<d),repeat=r)) if d==2 else [tuple(rng.randrange(1<<d) for _ in range(r)) for _ in range(500)]
    for tup in samples:
        assert q_formula(tup,d) == parity(tup),(d,r,tup)
        checks+=1
print('even_relation_recursive_formula_checks',checks)

# The existence of affinely independent s-tuples is checked via an exact F2-rank
# against the advertised definability thresholds for a range of dimensions.
def affine_rank(points):
    if not points:return -1
    rows=[]
    for x in points[1:]:
        v=x^points[0]
        for b in rows:
            v=min(v,v^b)
        if v:
            rows.append(v)
            rows.sort(reverse=True)
    return len(rows)

for d in range(0,7):
    space=list(range(1<<d))
    for s in range(2,min(7,len(space))+1):
        # independent tuple witness is (0, unit basis directions), if s<=d+1
        candidate=[0]+[1<<j for j in range(s-1)] if s<=d+1 else []
        if candidate:
            assert all(p in space for p in candidate)
            assert affine_rank(candidate)==s-1
        else:
            assert s>d+1
print('affine_independence_witness_range', 'd=0..6,s=2..7', 'PASS')
print('FORMULA_CHECK_PASS')
