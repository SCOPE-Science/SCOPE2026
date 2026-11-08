"""Finite exact checks for tree-Hardy composition norm examples."""
from fractions import Fraction
from itertools import product

def levels(q, n):
    if n == 0:
        return [()]
    return [(k,)+s for k in range(q+1) for s in product(range(q), repeat=n-1)]

def phi_spike(q, n, v):
    if n == 2:
        return levels(q,2)[0]
    return v

def phi_cycle(q,n,v):
    if n < 2:
        return v
    # Cycle siblings at every parent, for q=3.
    return v[:-1]+((v[-1]+1)%q,)

def matrix(q,n,typ):
    vs=levels(q,n)
    if typ=='spike':
        vs2=levels(q,2)
        return [[int(phi_spike(q,n,v)==w) for w in vs2] for v in vs] if n==2 else [[int(v==w) for w in vs] for v in vs]
    if typ=='cycle_diff':
        return [[int(v==w)-int(phi_cycle(q,n,v)==w) for w in vs] for v in vs]
    raise ValueError(typ)

def gram(a):
    return [[sum(row[i]*row[j] for row in a) for j in range(len(a[0]))] for i in range(len(a[0]))]

count=0
for q in (2,3,4):
    for n in range(4):
        a=matrix(q,n,'spike')
        # finite fibre multiplicities and row-sum identity
        for row in a:
            assert sum(row)==1;count+=1
        for j in range(len(a[0])):
            cnt=sum(row[j] for row in a)
            assert cnt == (len(a) if n==2 and j==0 else (0 if n==2 else 1))
            count+=1
for n in range(2,6):
    q=3
    a=matrix(q,n,'cycle_diff')
    assert all(sum(row)==0 for row in a);count+=1
    assert max(sum(abs(row[j]) for row in a) for j in range(len(a[0])))==2;count+=1
    g=gram(a)
    # Each sibling triple has Gram matrix 3I-J; zero between triples.
    for i in range(len(g)):
        for j in range(len(g)):
            expected=2 if i==j else (-1 if i//3==j//3 else 0)
            assert g[i][j]==expected,(n,i,j,g[i][j],expected)
            count+=1
    # gram^2 =3 gram shows nonzero singular values sqrt(3)
    for i in range(len(g)):
        for j in range(len(g)):
            assert sum(g[i][h]*g[h][j] for h in range(len(g)))==3*g[i][j]
            count+=1
# Exact 1/(c_n) level normalization of the spike for 1<=p=1,2:
for p in (1,2):
    for q in (2,3,4):
        c2=(q+1)*q
        a=matrix(q,2,'spike')
        # A single input c2^(1/p) produces a constant output: norm^p=c2.
        val_p=Fraction(sum(abs(row[0])**p for row in a),len(a))*c2
        assert val_p==c2
        count+=1
print('TREE_ESSENTIAL_EXACT_FINITE_OK',count)
