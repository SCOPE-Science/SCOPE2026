"""Independent 2000-class enumeration by Hermite normal form.

Requires Python 3 and sympy. Uses integer lattices rather than mod-prime ranks.
"""
import itertools
from sympy import Matrix
from sympy.matrices.normalforms import hermite_normal_form

V=list(itertools.combinations(range(5),2))
L=Matrix(10,10,lambda i,j:3 if i==j else -int(set(V[i]).isdisjoint(V[j])))
R=L[:9,:9]
H=hermite_normal_form(R)
d=[int(H[i,i]) for i in range(9)]
assert all(H[i,j]==0 for i in range(9) for j in range(i))
assert __import__('math').prod(d)==2000


def residue(z):
    w=list(map(int,z))
    for i in range(8,-1,-1):
        q,r=divmod(w[i],d[i])
        for j in range(i+1):
            w[j]-=q*int(H[j,i])
        assert w[i]==r
    return tuple(w)

representatives=list(itertools.product(*(range(k) for k in d)))
assert len(representatives)==len(set(representatives))==2000

def perm(part):
    p=[]; s=0
    for m in part:
        p+=list(range(s+1,s+m))+[s]; s+=m
    return [V.index(tuple(sorted((p[a],p[b])))) for a,b in V]

TYPES=[(1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(3,2),(4,1),(5,)]
EXPECTED=[(2000,16,125),(100,4,25),(20,4,5),(5,1,5),
          (1,1,1),(2,2,1),(5,1,5)]
for part,expect in zip(TYPES,EXPECTED):
    g=perm(part)
    def action(z):
        v=[0]*10
        for i in range(9):
            v[g[i]]+=z[i]
            v[g[9]]-=z[i]
        return residue(v[:9])
    fixed=[z for z in representatives if action(z)==z]
    zero=(0,)*9
    annihilator_counts=(
        len(fixed),
        sum(residue([2*x for x in z])==zero for z in fixed),
        sum(residue([5*x for x in z])==zero for z in fixed)
    )
    assert annihilator_counts==expect,(part,annihilator_counts,expect)
    assert all(residue([10*x for x in z])==zero for z in fixed)
    print(part,annihilator_counts)
print('PETERSEN_FROBENIUS_HERMITE_ENUMERATION_OK')
