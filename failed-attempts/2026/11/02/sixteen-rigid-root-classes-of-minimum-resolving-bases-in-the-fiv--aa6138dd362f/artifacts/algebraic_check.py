"""Independent sign-matrix and transversal certificate for five-cube metric bases.
Requires only the Python standard library. Run: python algebraic_check.py.
"""
from collections import Counter
from itertools import combinations, product

DIM=5
FULL=31

def signs(v):
    return tuple(1-2*((v>>j)&1) for j in range(DIM))

def dot(x,y):
    return sum(a*b for a,b in zip(x,y))

def primitive_signature(S):
    # 4x4 determinants via permutations; integer signed cofactors of 4x5 sign matrix.
    from itertools import permutations
    def det4(A):
        out=0
        for p in permutations(range(4)):
            term=1
            for i in range(4):term*=A[i][p[i]]
            inv=sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
            out+=(-1 if inv&1 else 1)*term
        return out
    from math import gcd
    M=[signs(s) for s in S]
    v=[((-1)**j)*det4([[M[i][k] for k in range(5) if k!=j] for i in range(4)]) for j in range(5)]
    g=gcd(*v)
    return tuple(x//g for x in v) if g else None

families={}
all_sets=set()
for root in range(16):
    pairs=[tuple(sorted((root^(1<<j),root^(1<<j)^FULL))) for j in range(5)]
    family=[]
    for hole in range(5):
        indices=[j for j in range(5) if j!=hole]
        for bits in product((0,1),repeat=4):
            S=frozenset(pairs[j][bits[t]] for t,j in enumerate(indices))
            assert len(S)==4
            kernel=primitive_signature(S)
            assert kernel is not None and sorted(map(abs,kernel))==[1,1,1,1,2]
            assert all(dot(signs(s),kernel)==0 for s in S)
            # Every nonzero ternary vector must fail to lie in the kernel.
            assert all(any(dot(signs(s),z)!=0 for s in S)
                       for z in product((-1,0,1),repeat=5) if any(z))
            family.append(S);all_sets.add(S)
    assert len(family)==80 and len(set(family))==80
    families[root]=family
assert len(all_sets)==1280

# Coarse combinatorial comparison of every one-for-one exchange in all 1280 sets.
idx={S:i for i,S in enumerate(all_sets)}
labels={S:r for r,fs in families.items() for S in fs}
assert len(labels)==len(all_sets)
edge_count=0
for S in all_sets:
    neighbors=[T for T in all_sets if len(S&T)==3]  # independent of distance/resolving predicate
    assert len(neighbors)==12
    assert all(labels[S]==labels[T] for T in neighbors)
    edge_count+=len(neighbors)
assert edge_count//2==7680

# Every 4x4 +/-1 matrix has determinant in {0,+/-8,+/-16}.
# Enumerating all 2^16 matrices makes this determinant bound a finite exact check.
from itertools import permutations
perm_data=[]
for p in permutations(range(4)):
    inv=sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
    perm_data.append((p,-1 if inv&1 else 1))
for mask in range(1<<16):
    M=[[1-2*((mask>>(4*i+j))&1) for j in range(4)] for i in range(4)]
    determinant=sum(sgn*M[0][p[0]]*M[1][p[1]]*M[2][p[2]]*M[3][p[3]] for p,sgn in perm_data)
    assert determinant in (0,-8,8,-16,16)

print('SIGN_MATRIX_80_KERNEL_CLASSES_AND_65536_DETERMINANTS_PASS')
print('BASES',len(all_sets),'ROOT_CLASSES',len(families),'EXCHANGES',edge_count//2)
