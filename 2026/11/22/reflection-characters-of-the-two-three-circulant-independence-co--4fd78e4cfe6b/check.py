"""Standalone check of the finite transfer identities and finite graph comparisons.
Scientific construction only; Python standard library.
"""
from functools import lru_cache

def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]

def power(M,e):
    n=len(M); R=[[int(i==j) for j in range(n)] for i in range(n)]
    while e:
        if e&1:R=matmul(R,M)
        M=matmul(M,M);e//=2
    return R

def mv(A,v):return [sum(a*b for a,b in zip(row,v)) for row in A]
def rowmul(v,A):return [sum(v[i]*A[i][j] for i in range(len(v))) for j in range(len(A[0]))]
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def add(A,B):return [[x+y for x,y in zip(a,b)] for a,b in zip(A,B)]

T=[[0]*8 for _ in range(8)];F=[[0]*8 for _ in range(8)]
for s in range(8):
    t=(s<<1)&7
    T[s][t]+=1;F[s][t]+=1
    if not(s&6):T[s][t|1]-=1
I=power(T,0)
v=[1,-1,0,0,-1,0,0,0]
w=mv(matmul(F,T),[1]*8)
B=add(power(T,4),I)
assert rowmul(rowmul(v,power(T,3)),B)==[0]*8
for j in range(3):
    assert dot(rowmul(rowmul(v,power(T,j)),B),w)==0

def transfer(L):
    assert L>=5
    return dot(rowmul(v,power(T,L-5)),w)

def period_formula(L):
    assert L>=3
    return -1 if ((L-3)//4)%2==0 else 1

for L in range(5,129):
    assert transfer(L)==period_formula(L)

def eval_independent(adj):
    @lru_cache(None)
    def rec(mask):
        if not mask:return 1
        v=max((j for j in range(len(adj)) if mask>>j&1),key=lambda j:(adj[j]&mask).bit_count())
        rest=mask & ~(1<<v)
        return rec(rest)-rec(rest & ~adj[v])
    return rec((1<<len(adj))-1)

def folded(n,k):
    orb=[];seen=set()
    for x in range(n):
        if x not in seen:
            o=tuple(sorted({x,(k-x)%n}));seen.update(o);orb.append(o)
    v2orb={x:j for j,o in enumerate(orb) for x in o}
    forbidden=set()
    for x in range(n):
        for delta in (2,3):
            y=(x+delta)%n
            if v2orb[x]==v2orb[y]:forbidden.add(v2orb[x])
    kept=[j for j in range(len(orb)) if j not in forbidden]
    adj=[0]*len(kept)
    to_new={old:j for j,old in enumerate(kept)}
    for x in range(n):
        for delta in (2,3):
            y=(x+delta)%n
            a,b=v2orb[x],v2orb[y]
            if a in to_new and b in to_new and a!=b:
                i,j=to_new[a],to_new[b]
                adj[i]|=1<<j;adj[j]|=1<<i
    return adj,kept,forbidden,len(orb)

# The folded graph after eliminating internally adjacent orbits is precisely
# the induced distance-{2,3} path graph with vertices 1 and L-2 removed.
cases=0
for n in range(6,97):
    for k in ((0,1) if n%2==0 else (0,)):
        adj,kept,ban,L=folded(n,k)
        assert ban=={1,L-2}
        assert kept==[j for j in range(L) if j not in {1,L-2}]
        canonical=[sum(1<<j for j,b in enumerate(kept) if abs(a-b) in (2,3)) for a in kept]
        assert adj==canonical
        assert eval_independent(adj)==period_formula(L)
        cases+=1
print('transfer identities: exact integer 8x8, PASS')
print('P(L+4)=-P(L) for L>=5, initial P(3..6)=-1, PASS')
print(f'folded graph and signed fixed-face identity: {cases} reflection cases (6<=n<=96), PASS')
print('sample reflection P(L), L=3..18:',*[period_formula(L) for L in range(3,19)])

def direct_lefschetz(n,k):
    # Inclusion-exclusion over all independent subsets, each invariant under reflection.
    # orientation on an invariant set is (-1)^{number of flipped pairs}.
    adj=[0]*n
    for j in range(n):
        for delta in (2,3,-2,-3):adj[j]|=1<<((j+delta)%n)
    tot=0
    for mask in range(1<<n):
        if any(((mask>>i)&1) and (adj[i]&mask) for i in range(n)):
            continue
        reflected=0
        for i in range(n):
            if mask>>i&1:reflected|=1<<((k-i)%n)
        if reflected!=mask:continue
        transpositions=sum(1 for i in range(n) if mask>>i&1 and i < (k-i)%n)
        tot+=(-1)**(mask.bit_count()+transpositions)
    return -tot
for n in range(6,19):
    for k in ((0,1) if n%2==0 else (0,)):
        L=(n//2+1 if k==0 else n//2)
        assert direct_lefschetz(n,k)==-period_formula(L)
print('direct oriented simplicial fixed-face traces: 20 cases (6<=n<=18), PASS')
