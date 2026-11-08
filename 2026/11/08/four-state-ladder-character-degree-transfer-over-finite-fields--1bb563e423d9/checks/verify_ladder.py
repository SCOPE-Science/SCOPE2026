#!/usr/bin/env python3
"""Independent enumeration for tridiagonal matrix rank distribution."""
from itertools import product
from collections import Counter

def mul(a,b,q):
    if q != 4: return a*b%q
    v=0
    if b&1: v^=a
    if b&2: v^=(a<<1)
    if v&8: v^=0b1100 # x^3 -> x^2+x so x^3+x^2+x =0? x^3=x(x+1)=x^2+x=x+1+x=1; polynomial reduction by x^2+x+1: x^3+x^2+x = 0? x^3=1 yes. this path should never v>=8 for degree<=2 output <=4
    if v&4: v^=7 # Reduce modulo X^2 + X + 1.
    return v

def add(a,b,q):return (a^b) if q==4 else (a+b)%q
def sub(a,b,q):return (a^b) if q==4 else (a-b)%q

def rank(a,q):
    a=[row[:] for row in a]; n=len(a); rr=0
    for col in range(n):
        pivot=next((i for i in range(rr,n) if a[i][col]),None)
        if pivot is None:continue
        a[rr],a[pivot]=a[pivot],a[rr]
        inv=next(x for x in range(1,q) if mul(a[rr][col],x,q)==1)
        a[rr]=[mul(x,inv,q) for x in a[rr]]
        for row in range(rr+1,n):
            f=a[row][col]
            if f:a[row]=[sub(a[row][k],mul(f,a[rr][k],q),q) for k in range(n)]
        rr+=1
    return rr

def formula(n,q):
    # Coefficients of z^nullity, indexed nullity.
    def polyplus(a,b):
        out=[0]*max(len(a),len(b))
        for i,v in enumerate(a):out[i]+=v
        for i,v in enumerate(b):out[i]+=v
        return out
    def polymul(a,b):
        out=[0]*(len(a)+len(b)-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b):out[i+j]+=x*y
        return out
    if n==1: return [q-1,1]
    # state Z,H,X,F
    I=[[0],[q-1],[q*(q-1)],[0,1]]
    M=[
        [[q*q*(q-1)],[0],[0,q*q],[0]],
        [[q*(q-1)],[0],[q*q*(q-1),q],[0]],
        [[0],[q*(q-1)],[q*q*(q-1)],[0,q]],
        [[0],[q-1],[q*(q-1)],[q*q*(q-1),1]]
    ]
    T=[[0,q*q],[q*q-q,q],[q*q-q,q],[q*q-1,1]]
    for _ in range(n-2):
        out=[[0] for _ in range(4)]
        for a in range(4):
            for b in range(4):
                out[b]=polyplus(out[b],polymul(I[a],M[a][b]))
        I=out
    h=[0]
    for a in range(4): h=polyplus(h,polymul(I[a],T[a]))
    return h

def check(n,q):
    ct=Counter()
    for vals in product(range(q), repeat=3*n-2):
        d=vals[:n]; u=vals[n:2*n-1]; l=vals[2*n-1:]
        mat=[[0]*n for _ in range(n)]
        for i in range(n):mat[i][i]=d[i]
        for i in range(n-1):mat[i][i+1]=u[i];mat[i+1][i]=l[i]
        ct[n-rank(mat,q)]+=1
    expected=formula(n,q)
    got=[ct[i] for i in range(n+1)]
    assert got==expected,(q,n,got,expected)
    print(f'PASS q={q} n={n} count={q**(3*n-2)} nullity_counts={got}')

def check_graph(n,q):
    # L_n has two rows and n columns; enumerate its genuine edge weights.
    vertices=2*n
    edges=[(i,n+i) for i in range(n)]
    edges += [(i,i+1) for i in range(n-1)]
    edges += [(n+i,n+i+1) for i in range(n-1)]
    ct=Counter()
    for vals in product(range(q), repeat=len(edges)):
        skew=[[0]*vertices for _ in range(vertices)]
        for (u,v),w in zip(edges,vals):
            skew[u][v]=w
            skew[v][u]=sub(0,w,q)
        rr=rank(skew,q)
        assert rr%2==0
        ct[n-rr//2]+=1
    expected=formula(n,q)
    got=[ct[i] for i in range(n+1)]
    assert got==expected,(n,q,got,expected)
    if q%2:
        degree_counts=[q**(2*n-2*r)*expected[n-r] for r in range(n+1)]
        assert sum(degree_counts[r]*q**(2*r) for r in range(n+1))==q**(5*n-2)
    print(f'GRAPH_PASS q={q} rungs={n} weights={q**len(edges)} nullity_counts={got}')

if __name__=='__main__':
    for n,q in [(1,2),(2,2),(3,2),(4,2),(5,2),(2,3),(3,3),(4,3),(2,4),(3,4),(2,5),(3,5)]:check(n,q)
    for n,q in [(2,2),(3,2),(4,2),(2,3),(3,3),(2,5)]:check_graph(n,q)
    # Compare the z^0 coefficient to the established full-rank recursion.
    for q in (2,3,4,5,7,8):
        previous=q-1
        current=q*(q-1)**2*(q+1)
        assert formula(1,q)[0]==previous and formula(2,q)[0]==current
        for n in range(3,16):
            nxt=q*q*(q-1)*current+q**3*(q-1)**2*previous
            assert formula(n,q)[0]==nxt
            previous,current=current,nxt
        print(f'NONSINGULAR_PRECEDENT_PASS q={q} through_n=15')
    print('LADDER_CHARACTER_RANK_TRANSFER_PASS')
