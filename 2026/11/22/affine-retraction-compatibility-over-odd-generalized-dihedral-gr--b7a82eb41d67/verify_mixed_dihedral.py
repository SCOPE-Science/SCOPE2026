"""Direct finite-group checks for commuting retractions of Dih(C9 + C3).
Only the Python standard library is needed.
"""
from itertools import product
from math import comb

A = [(x,y) for x in range(9) for y in range(3)]
zero=(0,0)
def plus(x,y): return ((x[0]+y[0])%9,(x[1]+y[1])%3)
def neg(x): return ((-x[0])%9,(-x[1])%3)
def mul(x,y):
    a,s=x; b,t=y
    return (plus(a, b if s==0 else neg(b)),(s+t)%2)

def linear(z,v):
    a,b,c,d=z; x,y=v
    return ((a*x+3*b*y)%9,(c*x+d*y)%3)

def compose(x,y):
    return tuple(linear(x,linear(y,v)) for v in [(1,0),(0,1)])

def map_group(f,g):
    z,u=f; a,s=g
    return (linear(z,a) if s==0 else plus(linear(z,a),u),s)

assert all(mul(mul(x,y),z)==mul(x,mul(y,z)) for x in product(A,range(2)) for y in product(A,range(2)) for z in [(zero,0),((1,0),0),(zero,1)])
endo=list(product(range(9),range(3),range(3),range(3)))
idem=[z for z in endo if compose(z,z)==(linear(z,(1,0)),linear(z,(0,1)))]
F=[(z,u) for z in idem for u in A if linear(z,u)==zero]
assert len(idem)==20 and len(F)==136, (len(idem),len(F))
for z,u in F:
    f=(z,u)
    assert all(map_group(f,mul(x,y))==mul(map_group(f,x),map_group(f,y)) for x in [((1,0),0),((0,1),0),(zero,1)] for y in product(A,range(2)))
    assert all(map_group(f,map_group(f,x))==map_group(f,x) for x in product(A,range(2)))

def affine_comp(x,y):
    z,u=x; w,v=y
    return (compose(z,w),plus(u,linear(z,v)))

def commute(x,y): return affine_comp(x,y)==affine_comp(y,x)
N=len(F)
adj=[0]*N
count=0
for i in range(N):
    for j in range(N):
        if commute(F[i],F[j]):
            count+=1
            if i!=j: adj[i]|=1<<j
assert count==1864, count
# Every group map commutes with the trivial group homomorphism.
assert count+2*N+1==2137
# Count ordered pairwise-commuting triples directly from the full relation,
# allowing repeated entries, rather than evaluating the closed formula.
rel=[adj[i] | (1<<i) for i in range(N)]
triples=sum((rel[i]&rel[j]).bit_count() for i in range(N) for j in range(N) if (rel[i]>>j)&1)
assert triples==11152,triples

# Exact maximal cliques of the nontrivial affine component, using pivoted bitset recursion.
cliques=[]
def bronk(R,P,X):
    if not P and not X:
        cliques.append(R)
        return
    U=P|X
    if U:
        pivot=max((u for u in range(N) if (U>>u)&1),key=lambda u:(P&adj[u]).bit_count())
        choices=P&~adj[pivot]
    else: choices=P
    while choices:
        bit=choices&-choices
        i=bit.bit_length()-1
        bronk(R|bit,P&adj[i],X&adj[i])
        P^=bit
        X|=bit
        choices^=bit
bronk(0,(1<<N)-1,0)
assert len(cliques)==243 and all(x.bit_count()==4 for x in cliques),(len(cliques),set(x.bit_count() for x in cliques))

# Closed mixed-exponent formula, with short factor p^a and long factor p^b.
def mixed_count(p,a,b,t):
    Q=2**t
    r,R=p**a,p**b
    return 1+(Q-1)*r*R+r*r*(Q-1)*((Q-2)*r*R+r+R)
assert [mixed_count(3,1,2,t) for t in range(4)]==[1,136,1864,11152]
assert mixed_count(3,1,3,1)==352
# Independent exponent-27 one-tuple census, not just formula evaluation.
A27=list(product(range(27),range(3)))
def lin27(z,v):
    a,b,c,d=z; x,y=v
    return ((a*x+9*b*y)%27,(c*x+d*y)%3)
idem27=[z for z in product(range(27),range(3),range(3),range(3))
        if all(lin27(z,lin27(z,v))==lin27(z,v) for v in ((1,0),(0,1)))]
assert len(idem27)==20
F27_count=sum(1 for z in idem27 for v in A27 if lin27(z,v)==(0,0))
assert F27_count==352, F27_count
print('MIXED_DIHEDRAL_CHECKS_PASSED')
print('group_order=54, additive_idempotents=20, nontrivial_retractions=136, all_retractions=137')
print('nontrivial_commuting_ordered_pairs=1864, nontrivial_commuting_ordered_triples=11152, all_commuting_ordered_pairs=2137')
print('maximal_cliques=243, each_size=5, nontrivial_subclique_size=4')
