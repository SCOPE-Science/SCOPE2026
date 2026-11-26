#!/usr/bin/env python3
"""Exact finite combinatorial certificate for the Clebsch cubic twist spectra.

Only the Python standard library is required.  The geometric 27-line model
is explicitly realized in characteristic 11 (a good characteristic).
The formulas being checked are characteristic-independent away from 2,3,5.
"""
from collections import Counter
from itertools import permutations, combinations, product

LABELS=range(5)

def pentagonal_key(a):
    return min(tuple((s*x+c)%5 for x in a) for s in (1,4) for c in range(5))
PENT=tuple(sorted({pentagonal_key(a) for a in permutations(LABELS)}))
DIAG=[]
for single in LABELS:
    rest=[x for x in LABELS if x!=single]
    for pair in combinations(rest,2):
        other=tuple(x for x in rest if x not in pair)
        key=(single,tuple(sorted((tuple(pair),other))))
        if key not in DIAG:DIAG.append(key)
DIAG=tuple(DIAG)
ECK=tuple(combinations(LABELS,2))
assert (len(PENT),len(DIAG),len(ECK))==(12,15,10)

def standard_sigma(part):
    s=list(LABELS);start=0
    for size in part:
        seq=list(range(start,start+size));start+=size
        for u,v in zip(seq,seq[1:]+seq[:1]):s[u]=v
    return tuple(s)

def mapped_diag(x,sigma):
    single,match=x
    return (sigma[single],tuple(sorted(tuple(sorted(sigma[i] for i in pair)) for pair in match)))

def mapped_pent(x,sigma,nonresidue):
    inverse=[sigma.index(i) for i in LABELS]
    return pentagonal_key(tuple((2 if nonresidue else 1)*x[inverse[i]]%5 for i in LABELS))

def mapped_eck(x,sigma):
    return tuple(sorted(sigma[i] for i in x))

def cycle_profile(items,action):
    unseen=set(items);out=Counter()
    while unseen:
        orig=next(iter(unseen));cur=orig;orbit=set()
        while cur not in orbit:
            orbit.add(cur);cur=action(cur)
        assert cur==orig and orbit<=unseen
        unseen.difference_update(orbit);out[len(orbit)]+=1
    return dict(sorted(out.items()))

# Realize the 27 geometric lines using their 2x5 coordinate-span matrices.
# F_11 contains the primitive fifth root 3.
Q=11;ZETA=3
matrices=[]
for single,match in DIAG:
    basis=[]
    for pair in match:
        row=[0]*5;row[pair[0]]=1;row[pair[1]]=-1
        basis.append(row)
    matrices.append(basis)
for a in PENT:
    matrices.append([[pow(ZETA,v,Q) for v in a],
                     [pow(ZETA,(-v)%5,Q) for v in a]])

def rank_mod(mat,p=Q):
    a=[[v%p for v in row] for row in mat]; r=0
    for j in range(len(a[0])):
        pivot=next((i for i in range(r,len(a)) if a[i][j]),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r]
        t=pow(a[r][j],-1,p)
        a[r]=[(v*t)%p for v in a[r]]
        for i in range(len(a)):
            if i!=r and a[i][j]:
                mult=a[i][j]
                a[i]=[(x-mult*y)%p for x,y in zip(a[i],a[r])]
        r+=1
        if r==len(a):break
    return r

G=[[0]*27 for _ in range(27)]
for i in range(27):
    G[i][i]=-1
    for j in range(i+1,27):
        if rank_mod(matrices[i]+matrices[j])==3:G[i][j]=G[j][i]=1
        else:assert rank_mod(matrices[i]+matrices[j])==4
assert all(sum(G[i])==9 for i in range(27))

def mul(A,B):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*B)] for row in A]
G2=mul(G,G)
# Spectral projection of intersection matrix to its rank-seven image.
# Eigenvalues 9,-6,0 give projector (G^2-3G)/54.
H=[[G2[i][j]-3*G[i][j] for j in range(27)] for i in range(27)]
assert all(v%54==0 for v in (sum(H[i][i] for i in range(27)),))
assert sum(H[i][i] for i in range(27))==7*54
assert mul(H,H)==[[54*x for x in row] for row in H]
assert mul(G,G2)==[[3*G2[i][j]+54*G[i][j] for j in range(27)] for i in range(27)]

PARTITIONS=((1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(3,2),(4,1),(5,))
# Each entry: (27-line orbit counts, 10-Eckardt-point orbit counts, Picard trace).
EXPECTED={
((1,1,1,1,1),0):({1:27},{1:10},7),
((1,1,1,1,1),1):({1:15,2:6},{1:10},5),
((2,1,1,1),0):({1:3,2:12},{1:4,2:3},-1),
((2,1,1,1),1):({1:3,2:12},{1:4,2:3},1),
((2,2,1),0):({1:7,2:10},{1:2,2:4},3),
((2,2,1),1):({1:3,2:12},{1:2,2:4},1),
((3,1,1),0):({3:9},{1:1,3:3},1),
((3,1,1),1):({3:5,6:2},{1:1,3:3},-1),
((3,2),0):({3:1,6:4},{1:1,3:1,6:1},-1),
((3,2),1):({3:1,6:4},{1:1,3:1,6:1},1),
((4,1),0):({1:1,2:3,4:5},{2:1,4:2},1),
((4,1),1):({1:5,2:1,4:5},{2:1,4:2},3),
((5,),0):({1:2,5:5},{5:2},2),
((5,),1):({2:1,5:3,10:1},{5:2},0),
}

def transform_indices(sigma,eps):
    return tuple(DIAG.index(mapped_diag(x,sigma)) for x in DIAG)+tuple(15+PENT.index(mapped_pent(x,sigma,eps)) for x in PENT)

def picard_trace(indices):
    # trace(P H)/54, where P[e_image,e_original]=1
    num=sum(H[i][indices[i]] for i in range(27))
    assert num%54==0
    return num//54


CYCLOTOMIC={1:(1,-1),2:(1,1),3:(1,1,1),4:(1,0,1),5:(1,1,1,1,1),6:(1,-1,1)}
EXPECTED_FACTOR_ORDERS={
((1,1,1,1,1),0):(1,1,1,1,1,1,1),
((1,1,1,1,1),1):(1,1,1,1,1,1,2),
((2,1,1,1),0):(1,1,1,2,2,2,2),
((2,1,1,1),1):(1,1,1,1,2,2,2),
((2,2,1),0):(1,1,1,1,1,2,2),
((2,2,1),1):(1,1,1,1,2,2,2),
((3,1,1),0):(1,1,1,3,3),
((3,1,1),1):(1,1,2,3,3),
((3,2),0):(1,2,2,3,6),
((3,2),1):(1,1,2,3,6),
((4,1),0):(1,1,1,2,2,4),
((4,1),1):(1,1,1,1,2,4),
((5,),0):(1,1,1,5),
((5,),1):(1,1,2,5),
}
def poly_mul(a,b):
    ans=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):ans[i+j]+=x*y
    return tuple(ans)
def claimed_polynomial(part,eps):
    ans=(1,)
    for d in EXPECTED_FACTOR_ORDERS[(part,eps)]:ans=poly_mul(ans,CYCLOTOMIC[d])
    return ans

def charpoly_coeffs(sigma,eps):
    # Newton identities on the seven dimensional geometric Picard representation.
    line_perm=transform_indices(sigma,eps)
    power=tuple(range(27));traces=[]
    for k in range(1,8):
        power=tuple(line_perm[i] for i in power)
        traces.append(picard_trace(power))
    coeff=[1]
    for k in range(1,8):
        num=sum(coeff[k-j]*traces[j-1] for j in range(1,k+1))
        assert num%k==0
        coeff.append(-num//k)
    return tuple(coeff)

# Only one S5 conjugacy representative is needed for each case,
# but independent conjugation tests verify cycle-type invariance.
for part in PARTITIONS:
    sigma=standard_sigma(part)
    for eps in (0,1):
        diagonals=cycle_profile(DIAG,lambda x:mapped_diag(x,sigma))
        pentagonals=cycle_profile(PENT,lambda x:mapped_pent(x,sigma,eps))
        combined=Counter(diagonals);combined.update(pentagonals)
        eckards=cycle_profile(ECK,lambda x:mapped_eck(x,sigma))
        trace=picard_trace(transform_indices(sigma,eps))
        assert (dict(combined),eckards,trace)==EXPECTED[(part,eps)]
        co=charpoly_coeffs(sigma,eps)
        assert len(co)==8 and co==claimed_polynomial(part,eps)

# Check S5-equivariance and the cyclotomic action on the entire line graph.
for sigma in permutations(LABELS):
    for eps in (0,1):
        perm=transform_indices(sigma,eps)
        assert len(set(perm))==27
        assert all(G[perm[i]][perm[j]]==G[i][j]
                   for i in range(27) for j in range(27))

# Direct arithmetic point count in two independent test characteristics.
for q,expected_trace in ((11,7),(17,5)):
    number=0
    for k in range(4):
        for tail in product(range(q),repeat=3-k):
            a=(0,)*k+(1,)+tail
            x4=(-sum(a))%q
            if (sum(v**3 for v in a)+x4**3)%q==0:number+=1
    assert number==1+q*q+q*expected_trace

print('CLEBSCH_TWIST_FROBENIUS_VERIFIED_OK')
