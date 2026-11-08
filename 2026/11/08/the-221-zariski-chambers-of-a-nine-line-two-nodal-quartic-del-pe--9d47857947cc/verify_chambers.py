"""Exact intersection-lattice and independent combinatorial verification.

Requires Python 3.9+ standard library only. Computes all 2048 possible supports.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations

# Classes in the H,E0,...,E4 lattice, with intersection diag(1,-1,...,-1).
# E_i appears as a coefficient +1 in the exceptional basis.
curves = []
for i in range(5):
    curves.append(('E'+str(i), (0,)+tuple(int(j==i) for j in range(5))))
curves.extend([
    ('A', (1,-1,-1,-1,0,0)),
    ('B', (1,-1,0,0,-1,-1)),
    ('K13',(1,0,-1,0,-1,0)),
    ('K14',(1,0,-1,0,0,-1)),
    ('K23',(1,0,0,-1,-1,0)),
    ('K24',(1,0,0,-1,0,-1)),
])
names = [name for name,_ in curves]
assert len(names)==11 and len(set(names))==11

def intersection(v,w):
    return v[0]*w[0]-sum(x*y for x,y in zip(v[1:],w[1:]))

matrix=[[intersection(c,d) for _,d in curves] for _,c in curves]
assert [matrix[i][i] for i in range(11)]==[-1]*5+[-2]*2+[-1]*4
assert matrix[5][6]==0
assert [matrix[5][i] for i in range(5)]==[1,1,1,0,0]
assert [matrix[6][i] for i in range(5)]==[1,0,0,1,1]
assert all(matrix[k][i]==0 for k in (5,6) for i in range(7,11))

def determinant(a):
    """Exact Gaussian elimination over rational numbers."""
    if not a: return 1
    b=[[Fraction(x) for x in row] for row in a]
    det=Fraction(1)
    for k in range(len(b)):
        pivot=next((i for i in range(k,len(b)) if b[i][k]!=0),None)
        if pivot is None: return 0
        if pivot != k:
            b[k],b[pivot]=b[pivot],b[k]
            det=-det
        p=b[k][k]
        det*=p
        for i in range(k+1,len(b)):
            factor=b[i][k]/p
            for j in range(k+1,len(b)):
                b[i][j]-=factor*b[k][j]
            b[i][k]=Fraction(0)
    assert det.denominator==1
    return int(det)

def negative_definite(indices):
    return all(((-1)**r)*determinant([[matrix[i][j] for j in indices[:r]] for i in indices[:r]])>0
               for r in range(1,len(indices)+1))

# Algorithm 1: exhaustive exact Sylvester principal-minor test.
by_roots_matrix=Counter()
for mask in range(1<<len(names)):
    ids=[i for i in range(len(names)) if mask & (1<<i)]
    if negative_definite(ids):
        by_roots_matrix[(len(ids),int(5 in ids)+int(6 in ids))]+=1

# Algorithm 2: independent combinatorial sum using four crossing lines.
# A choice of crossing lines is allowed iff its members share vertices.
# Disjoint-pair crossings intersect on the blown-up surface.
lines=((1,3),(1,4),(2,3),(2,4))
by_roots_graph=Counter()
for k in range(5):
    for Kset in combinations(lines,k):
        if ((1,3) in Kset and (2,4) in Kset) or ((1,4) in Kset and (2,3) in Kset):
            continue
        blocked=set(v for pair in Kset for v in pair)
        available=sorted(set(range(1,5))-blocked)
        for s in range(len(available)+1):
            for Eset in combinations(available,s):
                for e0 in (0,1):
                    a=e0+len(set(Eset)&{1,2})
                    b=e0+len(set(Eset)&{3,4})
                    size=k+s+e0
                    by_roots_graph[(size,0)]+=1
                    if a<=1: by_roots_graph[(size+1,1)]+=1 # add A
                    if b<=1: by_roots_graph[(size+1,1)]+=1 # add B
                    if e0==0 and a<=1 and b<=1:
                        by_roots_graph[(size+2,2)]+=1 # add both

expected={
    0:[1,9,26,30,13,1],
    1:[0,2,18,46,38,4],
    2:[0,0,1,8,16,8],
}
for roots,coeffs in expected.items():
    actual=[by_roots_matrix[(size,roots)] for size in range(6)]
    assert actual==coeffs, (roots,actual)
assert by_roots_matrix==by_roots_graph, (by_roots_matrix,by_roots_graph)
assert sum(by_roots_matrix.values())==221
assert sum(by_roots_matrix[(s,0)] for s in range(6))==80
assert sum(by_roots_matrix[(s,1)]+by_roots_matrix[(s,2)] for s in range(6))==141
assert [sum(by_roots_matrix[(s,r)] for r in range(3)) for s in range(6)]==[1,11,45,84,67,13]
print('NEGATIVE_CURVE_CLASSES=11 (9 (-1), 2 (-2))')
print('CANDIDATE_SUBSETS=2048')
for root_count in range(3):
    print('ROOT_COUNT_{}={}'.format(root_count,expected[root_count]))
print('TOTAL_BY_SUPPORT_SIZE=[1,11,45,84,67,13]')
print('TOTAL_CHAMBERS=221; ROOT_FREE=80; ROOT_CONTAINING=141')
print('TWO_INDEPENDENT_COUNTS_AGREE')
print('ALL_CHECKS_PASSED')
