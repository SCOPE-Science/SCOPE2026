#!/usr/bin/env python3
"""Exact finite check of symmetry on Möbius--Kantor independence homology.
Python 3, networkx>=3, sympy>=1.12. No external data or network needed.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations
import networkx as nx
from sympy.polys.domains import QQ
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.sdm import SDM

N = 16
E = set()
for i in range(8):
    for a,b in ((i,(i+1)%8), (i,8+i), (8+i,8+(i+3)%8)):
        E.add(tuple(sorted((a,b))))
assert len(E) == 24
G=nx.Graph(); G.add_nodes_from(range(N)); G.add_edges_from(sorted(E))
all_aut={tuple(perm[v] for v in range(N)) for perm in
    nx.algorithms.isomorphism.GraphMatcher(G,G).isomorphisms_iter()}
assert len(all_aut)==96
identity=tuple(range(N))
def compose(g,h): return tuple(g[h[v]] for v in range(N))
def inverse(g): return tuple(g.index(v) for v in range(N))
def parity(seq):
    return -1 if (sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))%2) else 1
r=tuple((v+1)%8 if v<8 else 8+(v-7)%8 for v in range(N))
a=(0,8,11,3,4,12,15,7,1,13,14,2,5,9,10,6)
assert r in all_aut and a in all_aut
# Group law and linear character specified by the two generators.
byword={identity:''}; lam={identity:1}; queue=deque([identity])
while queue:
    g=queue.popleft()
    for letter,h,sgn in [('r',r,1),('R',inverse(r),1),('a',a,-1),('A',inverse(a),-1)]:
        k=compose(g,h); value=lam[g]*sgn
        if k not in byword: byword[k]=byword[g]+letter;lam[k]=value;queue.append(k)
        else: assert lam[k]==value
assert set(byword)==all_aut
for g in all_aut:
    for h in all_aut:
        assert lam[compose(g,h)]==lam[g]*lam[h]

faces=[()]
adj={v:set(G.neighbors(v)) for v in range(N)}
for v in range(N):
    faces += [s+(v,) for s in list(faces) if not adj[v].intersection(s)]
bydim={d:sorted(s for s in faces if len(s)==d+1) for d in range(8)}
assert tuple(map(len,(bydim[d] for d in range(8))))==(16,96,272,376,240,72,16,2)
assert len(faces)==1091
index={d:{s:i for i,s in enumerate(bydim[d])} for d in range(8)}

def boundary(d):
    col=[]
    for s in bydim[d]:
        col.append({index[d-1][s[:j]+s[j+1:]]:(-1)**j for j in range(d+1)})
    return col
bound={d:boundary(d) for d in range(1,8)}
# Verify integer chain condition for every basis face.
for d in range(2,8):
    for chain in bound[d]:
        res={}
        for row,coeff in chain.items():
            for i,v in bound[d-1][row].items():res[i]=res.get(i,0)+coeff*v
        assert all(v==0 for v in res.values())
# Exact rational boundary ranks (not modular approximations).
ranks={}
for d in range(1,8):
    data={}
    for j,col in enumerate(bound[d]):
        for i,c in col.items():data.setdefault(i,{})[j]=QQ(c)
    ranks[d]=DomainMatrix.from_rep(SDM(data,(len(bydim[d-1]),len(bydim[d])),QQ)).rank()
assert [ranks[d] for d in range(1,8)]==[15,81,191,181,58,14,2]
betti={d:len(bydim[d])-ranks.get(d,0)-ranks.get(d+1,0) for d in range(8)}
assert betti=={0:1,1:0,2:0,3:4,4:1,5:0,6:0,7:0}

# All 96 group elements are checked against chain differentials.
for g in all_aut:
    for d in range(1,8):
        for j,s in enumerate(bydim[d]):
            ns=[g[v] for v in s]
            im=index[d][tuple(sorted(ns))]
            coeff=parity(ns)
            left={i:c*coeff for i,c in bound[d][im].items()}
            right={}
            for i,c in bound[d][j].items():
                t=bydim[d-1][i]; nt=[g[v] for v in t]
                q=index[d-1][tuple(sorted(nt))]
                right[q]=c*parity(nt)
            assert left==right

def reduce_mod(source,basis,p):
    vec={k:v%p for k,v in source.items() if v%p}
    while vec and max(vec) in basis:
        row=max(vec); basiscol=basis[row]
        factor=vec[row]*pow(basiscol[row],-1,p)%p
        for k,c in basiscol.items():
            x=(vec.get(k,0)-factor*c)%p
            if x:vec[k]=x
            else:vec.pop(k,None)
    return vec

def image_basis(cols,p):
    basis={}
    for col in cols:
        x=reduce_mod(col,basis,p)
        if x:basis[max(x)]=x
    return basis

def mod_generator(p):
    image=image_basis(bound[5],p)
    assert len(image)==ranks[5]
    # Track dependencies among columns of boundary degree four.
    pivots={};generator=None
    for j,col in enumerate(bound[4]):
        z={i:v%p for i,v in col.items()}; coefficients={j:1}
        while z and max(z) in pivots:
            key=max(z); b,c=pivots[key]
            factor=z[key]*pow(b[key],-1,p)%p
            for i,v in b.items():
                x=(z.get(i,0)-factor*v)%p
                if x:z[i]=x
                else:z.pop(i,None)
            for i,v in c.items():
                x=(coefficients.get(i,0)-factor*v)%p
                if x:coefficients[i]=x
                else:coefficients.pop(i,None)
        if z:pivots[max(z)]=(z,coefficients)
        elif reduce_mod(coefficients,image,p):
            generator=coefficients;break
    assert generator is not None
    assert len(image_basis([x for x in image.values()]+[generator],p))==ranks[5]+1
    assert all(sum(v*generator.get(j,0) for j,c in enumerate(bound[4]) for i,v in c.items() if i==row)%p==0 for row in range(len(bydim[3])))
    return image,generator

def transport(g,d,cycle,p):
    vec={}
    for j,c in cycle.items():
        ns=[g[v] for v in bydim[d][j]]
        row=index[d][tuple(sorted(ns))]
        x=(vec.get(row,0)+parity(ns)*c)%p
        if x:vec[row]=x
        else:vec.pop(row,None)
    return vec

def signs_on_top(p):
    image,cycle=mod_generator(p)
    values={}
    for g in all_aut:
        transported=transport(g,4,cycle,p)
        matched=[]
        for sign in (-1,1):
            diff=transported.copy()
            for row,c in cycle.items():
                x=(diff.get(row,0)-sign*c)%p
                if x:diff[row]=x
                else:diff.pop(row,None)
            if not reduce_mod(diff,image,p): matched.append(sign)
        assert len(matched)==1
        values[g]=matched[0]
    return values
for prime in (101,103):
    for d in range(1,8):assert len(image_basis(bound[d],prime))==ranks[d]
mu=signs_on_top(101)
assert mu==signs_on_top(103)
bipartition=nx.algorithms.bipartite.color(G)
assert all(mu[g]==(-1 if bipartition[g[0]]!=bipartition[0] else 1) for g in all_aut)
assert all(mu[compose(g,h)]==mu[g]*mu[h] for g in all_aut for h in all_aut)
assert (mu[r],mu[a],lam[r],lam[a])==(-1,1,1,-1)

# Signed chain traces give Lefschetz numbers; exact rational ranks
# imply the other positive homology is H_3 of rank four.
L={};chi3={};psi={}
for g in all_aut:
    tr=0
    for d in range(8):
        trd=sum(parity([g[v] for v in s]) for s in bydim[d] if {g[v] for v in s}==set(s))
        tr+=((-1)**d)*trd
    L[g]=tr
    chi3[g]=1+mu[g]-tr
    psi[g]=chi3[g]-lam[g]
assert chi3[identity]==4 and psi[identity]==3
assert sum(chi3[g]*lam[g] for g in all_aut)==96
assert sum(chi3[g]**2 for g in all_aut)==192
assert sum(psi[g]**2 for g in all_aut)==96
assert sum(chi3.values())==0 and sum(mu.values())==0
assert sum(lam.values())==0 and sum(psi.values())==0
# Complete conjugacy-class enumeration.
conjugacy=[]; remaining=set(all_aut)
while remaining:
    g=min(remaining,key=lambda t:(len(byword[t]),byword[t]))
    cl={compose(compose(h,g),inverse(h)) for h in all_aut}
    assert cl<=remaining
    conjugacy.append((g,cl));remaining-=cl
conjugacy.sort(key=lambda pair:(len(pair[1]),len(byword[pair[0]]),byword[pair[0]]))
assert len(conjugacy)==13
# Compare with natural subgroups and ordinary quotient cohomology.
for label,character in [('full',{g:1 for g in all_aut}),('kernel_lambda',lam),('bipartition_preserving',mu)]:
    subgroup=[g for g in all_aut if character[g]==1]
    b3=sum(chi3[g] for g in subgroup)//len(subgroup)
    b4=sum(mu[g] for g in subgroup)//len(subgroup)
    assert (b3,b4)=={'full':(0,0),'kernel_lambda':(1,0),'bipartition_preserving':(0,1)}[label]
    print('QUOTIENT',label,len(subgroup),'rational_betti3_4',b3,b4)
print('EXACT_BOUNDARY_RANKS',*[ranks[d] for d in range(1,8)])
print('CHAIN_FACE_COUNTS',*[len(bydim[d]) for d in range(8)])
print('GROUP_GENERATORS',r,a)
print('CONJUGACY_TABLE size word chi3 chi4 lambda three_dimensional')
for g,cl in conjugacy:
    representative=min(cl,key=lambda t:(len(byword[t]),byword[t]))
    print(len(cl),byword[representative] or 'e',chi3[representative],mu[representative],lam[representative],psi[representative])
print('COMPLETE_MOBIUS_KANTOR_AUTOMORPHISM_CHARACTER_PASS')
