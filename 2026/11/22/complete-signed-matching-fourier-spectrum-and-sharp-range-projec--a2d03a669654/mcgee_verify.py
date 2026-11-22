"""Reproducible exact verification of signed matching Fourier recovery on the McGee graph.
Run: python3 mcgee_verify.py (no third-party libraries required)."""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from math import gcd

V=24
LCF=(-12,7,-7)*8
E=tuple(sorted({tuple(sorted((i,(i+1)%V))) for i in range(V)} | {tuple(sorted((i,(i+LCF[i])%V))) for i in range(V)}))
assert len(E)==36 and all(sum(u==v or w==v for u,w in E)==3 for v in range(V))
adj=[[] for i in range(V)]
for i,(u,v) in enumerate(E):adj[u].append((v,i));adj[v].append((u,i))
assert all(len(x)==3 for x in adj)

def dist(src):
    d=[-1]*V;d[src]=0;Q=[src]
    for u in Q:
        for v,_ in adj[u]:
            if d[v]<0:d[v]=d[u]+1;Q.append(v)
    return d
assert all(-1 not in dist(s) for s in range(V))
girth=min(dist_without_edge(u,v,i)+1 for i,(u,v) in enumerate(E)) if False else None

def girth_bfs():
    g=V+1
    for src in range(V):
        d=[-1]*V;parent=[-1]*V;d[src]=0;Q=[src]
        for u in Q:
            for v,_ in adj[u]:
                if d[v]<0:d[v]=d[u]+1;parent[v]=u;Q.append(v)
                elif parent[u]!=v:g=min(g,d[u]+d[v]+1)
    return g
assert girth_bfs()==7

@lru_cache(None)
def enumerate_matchings(mask):
    if not mask:return (0,)
    u=(mask&-mask).bit_length()-1
    out=[]
    for v,i in adj[u]:
        if mask>>v&1:
            for tail in enumerate_matchings(mask^(1<<u)^(1<<v)):
                out.append(tail|(1<<i))
    return tuple(out)
M=enumerate_matchings((1<<V)-1)
assert len(M)==60 and len(set(M))==60 and all(m.bit_count()==12 for m in M)

parent=list(range(V))
def root(a):
    while parent[a]!=a:a=parent[a]
    return a
T=[];C=[]
for i,(u,v) in enumerate(E):
    ru,rv=root(u),root(v)
    if ru!=rv:parent[ru]=rv;T.append(i)
    else:C.append(i)
assert len(T)==V-1 and len(C)==len(E)-V+1==13

N=1<<len(C)
B=[0]*N
for m in M:
    x=sum(((m>>e)&1)<<j for j,e in enumerate(C))
    B[x]+=1
assert sum(B)==60

def hadamard(x):
    a=list(x);h=1
    while h<len(a):
        for p in range(0,len(a),2*h):
            for q in range(p,p+h):
                r,s=a[q],a[q+h]
                a[q],a[q+h]=r+s,r-s
        h*=2
    return a

W=hadamard(B)
assert W[0]==60

# A second signed perfect-matching recursion, independent of the matching-list transform.
# It enumerates via vertex subsets, with the negative edge signs assigned to cotree chords.
chord_index={e:i for i,e in enumerate(C)}
@lru_cache(None)
def signed_dp(mask,negative):
    if not mask:return 1
    u=(mask&-mask).bit_length()-1
    ans=0
    for v,e in adj[u]:
        if mask>>v&1:
            j=chord_index.get(e)
            sign=-1 if j is not None and negative>>j&1 else 1
            ans+=sign*signed_dp(mask^(1<<u)^(1<<v),negative)
    return ans
for s,w in enumerate(W):
    assert signed_dp((1<<V)-1,s)==w,('direct_signed_mismatch',s,w)
    signed_dp.cache_clear()

counts=Counter(abs(w) for w in W)
assert counts=={0:2112,4:2954,8:1728,12:896,16:192,20:208,24:64,28:36,60:2}
assert sum(counts.values())==N
assert all(w%4==0 for w in W)
assert min(abs(w) for w in W if w)==4
zero=sum(w==0 for w in W)
full_zero=zero*(1<<(V-1))
full_rank=(N-zero)*(1<<(V-1))
assert full_zero+full_rank==(1<<len(E))

indicator=[int(w!=0) for w in W]
P=hadamard(indicator)
assert sum(abs(a) for a in P)==120192
norm=Fraction(sum(abs(a) for a in P),N)
assert norm==Fraction(939,64)
assert sum(v!=0 for v in P)==2412

# Direct Fourier characters at small edge support are independent of gauge selection.
edge_multiplicity=[sum((m>>i)&1 for m in M) for i in range(len(E))]
assert set(edge_multiplicity)=={20}
zeros2=[]
for i in range(len(E)):
    assert len(M)-2*edge_multiplicity[i]==20
    for j in range(i+1,len(E)):
        both=sum((m>>i)&(m>>j)&1 for m in M)
        signed=len(M)-2*(edge_multiplicity[i]+edge_multiplicity[j])+4*both
        if signed==0:zeros2.append((i,j))
assert len(zeros2)==128
assert all(not(set(E[i])&set(E[j])) for i,j in zeros2)
print('PASS')
print('vertices',V,'edges',len(E),'girth',girth_bfs(),'matchings',len(M))
print('reduced_levels',sorted(counts.items()))
print('gauge_reduced_sign_classes',N,'gauge_multiplicity',1<<(V-1))
print('full_rank',full_rank,'full_nullity',full_zero)
print('min_nonzero_multiplier',min(abs(w) for w in W if w))
print('minimum_endpoint_projection_norm',str(norm))
print('kernel_support_on_cycle_space',sum(v!=0 for v in P))
print('first_cancel_weight',2,'two_edge_zero_characters',len(zeros2))
