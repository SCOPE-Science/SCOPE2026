from itertools import permutations
from math import comb
from fractions import Fraction

def fence_rel(n):
    return [(i,i+1) if i%2==0 else (i+1,i) for i in range(n-1)]

def linext_brute(n):
    rel=fence_rel(n); c=0
    for p in permutations(range(n)):
        pos=[0]*n
        for j,x in enumerate(p): pos[x]=j
        if all(pos[a]<pos[b] for a,b in rel): c+=1
    return c

def ideals_brute(n):
    rel=fence_rel(n); c=0
    for mask in range(1<<n):
        if all(not((mask>>b)&1) or ((mask>>a)&1) for a,b in rel): c+=1
    return c

def euler_zigzag(N):
    E=[0]*(N+1); E[0]=1
    if N>=1: E[1]=1
    # A'=(A^2+1)/2; for n>=1 coefficient recurrence
    for n in range(1,N):
        E[n+1]=sum(comb(n,k)*E[k]*E[n-k] for k in range(n+1))//2
    return E

def fib(N):
    F=[0]*(N+1)
    if N>=1:F[1]=1
    if N>=2:F[2]=1
    for n in range(3,N+1):F[n]=F[n-1]+F[n-2]
    return F

def independent_sets(n):
    for mask in range(1<<n):
        if mask & (mask<<1): continue
        yield {i for i in range(n) if (mask>>i)&1}

def det_int(A):
    A=[list(map(Fraction,row)) for row in A]; n=len(A); d=Fraction(1)
    for i in range(n):
        p=next((r for r in range(i,n) if A[r][i]),None)
        if p is None:return 0
        if p!=i:A[i],A[p]=A[p],A[i]; d=-d
        q=A[i][i]; d*=q
        for j in range(i,n):A[i][j]/=q
        for r in range(i+1,n):
            q=A[r][i]
            if q:
                for j in range(i,n):A[r][j]-=q*A[i][j]
    assert d.denominator==1
    return d.numerator

def active_normals(n,S):
    rows=[]
    for j in range(n):
        if j not in S:
            r=[0]*n;r[j]=1;rows.append(r)
    for j in range(n-1):
        if (j in S) ^ (j+1 in S):
            r=[0]*n;r[j]=1;r[j+1]=1;rows.append(r)
    return rows

E=euler_zigzag(100); F=fib(102)
assert E[:9]==[1,1,1,2,5,16,61,272,1385]
for n in range(1,10):
    assert linext_brute(n)==E[n]
    assert ideals_brute(n)==F[n+2]

smooth_checks=0
for n in range(1,17):
    smooth=[]
    for S in independent_sets(n):
        if n==1:
            is_smooth=True  # the chain polytope is the segment 0 <= y_1 <= 1
        else:
            rows=active_normals(n,S)
            is_smooth=(len(rows)==n and abs(det_int(rows))==1)
        if is_smooth:smooth.append(S)
        smooth_checks+=1
    if n==1:
        assert len(smooth)==2
    elif n==2:
        assert len(smooth)==3
    else:
        target=[set(),{0},{n-1},{0,n-1}]
        assert all(t in smooth for t in target) and len(smooth)==4

for n in range(1,101):
    if n<=4: assert E[n]<F[n+2]
    else: assert E[n]>F[n+2]
for n in range(2,99):
    assert E[n+2] >= (n+1)*E[n]

print('VERIFY_OK brute_n=1..9 smooth_n=1..16 smooth_vertices_checked=',smooth_checks,'crossover_n=1..100')
