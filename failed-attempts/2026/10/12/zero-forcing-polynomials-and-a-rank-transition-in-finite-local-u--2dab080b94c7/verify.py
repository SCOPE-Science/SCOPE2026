#!/usr/bin/env python3
from itertools import combinations
from fractions import Fraction
from math import comb, gcd


def zero_forces(S,N):
    blue=set(S)
    while True:
        if len(blue)==len(N):
            return True
        move=None
        for v in sorted(blue):
            W=N[v]-blue
            if len(W)==1:
                move=next(iter(W))
                break
        if move is None:
            return False
        blue.add(move)


def polynomial(N):
    out={}
    n=len(N)
    for k in range(n+1):
        c=sum(1 for S in combinations(range(n),k) if zero_forces(S,N))
        if c:
            out[k]=c
    return out


def local_model(q,s,even_char):
    # q residue classes, each of cardinality s.
    cls=[a for a in range(q) for _ in range(s)]
    N=[set() for _ in cls]
    if even_char:
        for i in range(len(cls)):
            for j in range(i+1,len(cls)):
                if cls[i]!=cls[j]:
                    N[i].add(j);N[j].add(i)
    else:
        # Pair residue classes 1<->2, 3<->4, ... abstractly; 0 is self-opposite.
        opp={0:0}
        for a in range(1,q,2):
            opp[a]=a+1; opp[a+1]=a
        for i in range(len(cls)):
            for j in range(i+1,len(cls)):
                a,b=cls[i],cls[j]
                edge = (a+b != 0)  # placeholder overwritten below
                if a==0 and b==0:
                    edge=False
                elif a==b:
                    edge=(a!=0)
                else:
                    edge=(b!=opp[a])
                if edge:
                    N[i].add(j);N[j].add(i)
    return cls,N


def direct_Zn(n):
    V=list(range(n))
    N=[set() for _ in V]
    for x in V:
        for y in range(x+1,n):
            if gcd(x+y,n)==1:
                N[x].add(y);N[y].add(x)
    return V,N


def direct_F4_dual():
    # F4 is represented additively as F2^2, so addition is xor.
    # In F4[e]/(e^2), (a,b) is a unit iff a != 0.
    V=[(a,b) for a in range(4) for b in range(4)]
    N=[set() for _ in V]
    for i,x in enumerate(V):
        for j in range(i+1,len(V)):
            y=V[j]
            if (x[0]^y[0]) != 0:
                N[i].add(j);N[j].add(i)
    return V,N


def predicted(q,s):
    N=q*s
    return {N-2:comb(q,2)*s*s, N-1:N, N:1}


def rank_fraction(M):
    A=[[Fraction(x) for x in row] for row in M]
    m=len(A); n=len(A[0]) if A else 0
    r=c=0
    while r<m and c<n:
        p=next((i for i in range(r,m) if A[i][c]),None)
        if p is None:
            c+=1; continue
        A[r],A[p]=A[p],A[r]
        z=A[r][c]
        A[r]=[x/z for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                z=A[i][c]
                A[i]=[A[i][j]-z*A[r][j] for j in range(n)]
        r+=1;c+=1
    return r


def odd_rank2_witness(q,s,N):
    h=(q-1)//2
    t={0:0}
    for j in range(h):
        a=1+2*j; b=a+1
        t[a]=j+1; t[b]=-(j+1)
    vec=[]
    for a in range(q):
        vec.extend([(1,t[a])]*s)
    H=((0,1),(1,0))
    M=[[sum(vec[i][u]*H[u][v]*vec[j][v] for u in range(2) for v in range(2))
        for j in range(len(vec))] for i in range(len(vec))]
    for i in range(len(vec)):
        for j in range(i+1,len(vec)):
            assert ((M[i][j]!=0)==(j in N[i]))
    assert rank_fraction(M)==2
    return 2


def q2_rank2_witness(s,N):
    vec=[(1,0)]*s+[(0,1)]*s
    H=((0,1),(1,0))
    M=[[sum(vec[i][u]*H[u][v]*vec[j][v] for u in range(2) for v in range(2))
        for j in range(len(vec))] for i in range(len(vec))]
    for i in range(len(vec)):
        for j in range(i+1,len(vec)):
            assert ((M[i][j]!=0)==(j in N[i]))
    assert rank_fraction(M)==2
    return 2


def even_rank3_witness(q,s,N):
    ts=list(range(q))
    vec=[]
    for t in ts:
        vec.extend([(1,t,t*t)]*s)
    H=((0,0,1),(0,-2,0),(1,0,0))
    M=[[sum(vec[i][u]*H[u][v]*vec[j][v] for u in range(3) for v in range(3))
        for j in range(len(vec))] for i in range(len(vec))]
    for i in range(len(vec)):
        for j in range(i+1,len(vec)):
            assert ((M[i][j]!=0)==(j in N[i]))
    assert rank_fraction(M)==3
    return 3


# Direct-ring exhaustive checks.
for n,q,s,even in [(4,2,2,True),(8,2,4,True),(9,3,3,False)]:
    V,Nd=direct_Zn(n)
    # Compare directly with the residue-field criterion x+y unit iff
    # the two residue classes do not add to zero.
    for i,x in enumerate(V):
        for j in range(i+1,len(V)):
            y=V[j]
            expected=((x%q)+(y%q))%q != 0
            assert ((j in Nd[i])==expected),(n,x,y)
    brute=polynomial(Nd)
    assert brute==predicted(q,s),(n,brute,predicted(q,s))
    print(f'Z/{n}Z: q={q}, s={s}, polynomial={brute}')

V,Nd=direct_F4_dual()
for i,x in enumerate(V):
    for j in range(i+1,len(V)):
        y=V[j]
        # In characteristic two, x+y is a unit iff the residue
        # coordinates in F_4 are distinct.
        expected=(x[0]^y[0]) != 0
        assert ((j in Nd[i])==expected),(x,y)
brute=polynomial(Nd)
assert brute==predicted(4,4),(brute,predicted(4,4))
print(f'F4[e]/(e^2): q=4, s=4, polynomial={brute}')

# Exact rank witnesses against the graph patterns.
for q,s,even in [(2,2,True),(2,4,True),(3,3,False),(5,5,False),(4,4,True)]:
    cls,N=local_model(q,s,even)
    if q==2:
        rk=q2_rank2_witness(s,N)
    elif even:
        rk=even_rank3_witness(q,s,N)
    else:
        rk=odd_rank2_witness(q,s,N)
    print(f'rank witness q={q}, s={s}: rank={rk}')

# Profile theorem and parameter recovery for many abstract local parameters.
for q,s,even in [(2,2,True),(2,8,True),(3,3,False),(5,5,False),(7,14,False),(4,4,True),(8,8,True)]:
    cls,N=local_model(q,s,even)
    # Every pair of distinct residue fibers gives a forcing complement.
    reps=[next(i for i,a in enumerate(cls) if a==c) for c in range(q)]
    for a,b in combinations(range(q),2):
        blue=set(range(len(cls)))-{reps[a],reps[b]}
        assert zero_forces(blue,N)
    # Three white fibers stall at the initial coloring.
    if q>=3:
        W=set(reps[:3]); blue=set(range(len(cls)))-W
        assert not zero_forces(blue,N)
    Norder=q*s
    c=comb(q,2)*s*s
    rq=Norder*Norder//(Norder*Norder-2*c)
    rs=Norder//rq
    assert (rq,rs)==(q,s)
print('PROFILE_AND_RECOVERY_OK')
print('VERIFY_OK')
