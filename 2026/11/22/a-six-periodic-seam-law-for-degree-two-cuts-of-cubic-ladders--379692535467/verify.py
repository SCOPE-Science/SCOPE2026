#!/usr/bin/env python3
"""Exact certificate for degree-two cuts of prisms and twisted ladders."""
from itertools import product

COLS = tuple(product(range(2), repeat=2))
PAIRS = tuple(product(range(4), repeat=2))

def valid_middle(a,b,c):
    L, M, R = COLS[a], COLS[b], COLS[c]
    return (M[0] == M[1] or
            all(M[j] == L[j] or M[j] == R[j] for j in range(2)))

def transpose(x):
    return COLS.index(COLS[x][::-1])

def matmul(a,b):
    n=len(a);m=len(b[0]);l=len(b)
    return [[sum(a[i][k]*b[k][j] for k in range(l)) for j in range(m)] for i in range(n)]

def identity(n): return [[int(i==j) for j in range(n)] for i in range(n)]
def trace(a):return sum(a[i][i] for i in range(len(a)))

def characteristic(a):
    """Exact integer Faddeev-LeVerrier characteristic coefficients."""
    n=len(a);B=identity(n);coeff=[1]
    for k in range(1,n+1):
        C=matmul(a,B);q=-trace(C)
        assert q%k==0
        c=q//k;coeff.append(c)
        B=[[C[i][j]+c*int(i==j) for j in range(n)] for i in range(n)]
    assert all(v==0 for row in B for v in row)
    return coeff

def matrices():
    T=[[0]*16 for i in range(16)]
    for i,(a,b) in enumerate(PAIRS):
        for c in range(4):
            if valid_middle(a,b,c):
                j=PAIRS.index((b,c))
                T[i][j]=1
    sigma=[PAIRS.index((transpose(a),transpose(b))) for (a,b) in PAIRS]
    assert all(sigma[sigma[i]]==i for i in range(16))
    assert all(T[sigma[i]][sigma[j]]==T[i][j] for i in range(16) for j in range(16))
    reps=[];seen=set()
    for i in range(16):
        if i not in seen:
            j=sigma[i]
            reps.append((i,j));seen.update((i,j))
    fixed=[(i,j) for i,j in reps if i==j];other=[(i,j) for i,j in reps if i!=j]
    assert len(fixed)==4 and len(other)==6
    def block(sign):
        orbits=(fixed+other if sign==1 else other)
        basis=[]
        for i,j in orbits:
            v=[0]*16;v[i]=1
            if j!=i:v[j]=sign
            basis.append(v)
        r=len(basis)
        # Construct matrix representing T acting on basis vectors (columns)
        A=[[0]*r for _ in range(r)]
        for k,v in enumerate(basis):
            t=[sum(T[i][j]*v[j] for j in range(16)) for i in range(16)]
            for h,(i,j) in enumerate(orbits):
                A[h][k]=t[i]
            rec=[sum(A[h][k]*basis[h][i] for h in range(r)) for i in range(16)]
            assert rec==t
        return A
    return T,sigma,block(1),block(-1)

def local_graph_count(n,twisted):
    # Independent enumeration without transfer matrices, using direct edge lists.
    assert n>=3
    edges=set()
    def edge(u,v):
        assert u!=v
        edges.add(tuple(sorted((u,v))))
    for i in range(n):
        edge(2*i,2*i+1)
        if i<n-1:
            edge(2*i,2*(i+1))
            edge(2*i+1,2*(i+1)+1)
    if twisted:
        edge(2*(n-1),1)
        edge(2*(n-1)+1,0)
    else:
        edge(2*(n-1),0)
        edge(2*(n-1)+1,1)
    adj=[[] for _ in range(2*n)]
    for a,b in edges:adj[a].append(b);adj[b].append(a)
    assert all(len(v)==3 for v in adj)
    valid=0
    for mask in range(1<<(2*n)):
        if all(any(((mask>>v)^(mask>>w))&1==0 for w in adj[v]) for v in range(2*n)):
            valid+=1
    return valid

def main():
    T,sigma,P,M=matrices()
    print('PLUS_CHARACTERISTIC',characteristic(P))
    print('MINUS_CHARACTERISTIC',characteristic(M))
    assert characteristic(M)==[1,-1,1,0,0,0,0]
    # Multiply monic polynomial factors using coefficient lists highest-degree first
    def poly_mul(a,b):
        out=[0]*(len(a)+len(b)-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b):out[i+j]+=x*y
        return out
    assert characteristic(P)==poly_mul(poly_mul([1,0,2],[1,-3,-1,0,2]),[1,0,0,0,0])
    assert characteristic(M)==poly_mul([1,-1,1],[1,0,0,0,0])
    print('EXACT_TWO_BLOCK_CHARACTERISTIC_POLYNOMIALS_PASS')
    def matpower(A,n):
        R=identity(len(A))
        while n:
            if n&1:R=matmul(R,A)
            A=matmul(A,A);n//=2
        return R
    for n in range(3,9):
        tn=matpower(T,n)
        a=trace(tn)
        b=sum(tn[i][sigma[i]] for i in range(16))
        ea=local_graph_count(n,False);eb=local_graph_count(n,True)
        assert (a,b)==(ea,eb),(n,a,b,ea,eb)
        assert a%2==0 and b%2==0
        print('DIRECT_GRAPH_ENUMERATION_PASS',n,(a-2)//2,(b-2)//2)
    # The recurrence of the two-dimensional anti-symmetric spectrum has q0=2, q1=1, q[n]=q[n-1]-q[n-2].
    q0,q1=2,1
    for n in range(1,101):
        q=q1 if n==1 else q0 if n==0 else None
        if n>=2:
            q0,q1=q1,q1-q0
            q=q1
        t=matpower(T,n)
        diff=trace(t)-sum(t[i][sigma[i]] for i in range(16))
        if n>=3:assert diff==2*q,(n,diff,q)
    print('TWIST_DIFFERENCE_PERIOD_SIX_PASS 3..100')
    # Independently check every local-seam bijection on configurations with
    # at least one monochromatic rung, for small lengths.
    def is_valid(columns, twisted):
        n=len(columns)
        for i in range(n):
            a=columns[(i-1)%n]
            c=columns[(i+1)%n]
            if twisted and i==0:a=transpose(a)
            if twisted and i==n-1:c=transpose(c)
            if not valid_middle(a,columns[i],c):return False
        return True
    for n in range(3,9):
        allwords=product(range(4),repeat=n)
        for columns in allwords:
            mono=[i for i,x in enumerate(columns) if COLS[x][0]==COLS[x][1]]
            if not mono: continue
            j=mono[-1]
            phi=columns[:j+1]+tuple(transpose(x) for x in columns[j+1:])
            assert is_valid(columns,False)==is_valid(phi,True)
            assert (phi[:j+1]+tuple(transpose(x) for x in phi[j+1:]))==columns
    print('MONOCHROMATIC_RUNG_SEAM_BIJECTION_PASS 3..8')
    # Cross-check full individual counts with the two stated linear recurrences.
    B=[4,3,11,36]
    for k in range(4,101):B.append(3*B[k-1]+B[k-2]-2*B[k-4])
    A=[2,0];C=[2,1]
    for k in range(2,101):
        A.append(-2*A[k-2]);C.append(C[k-1]-C[k-2])
    for n in range(3,101):
        power=matpower(T,n)
        cp=(B[n]+A[n]+C[n]-2)//2
        cm=(B[n]+A[n]-C[n]-2)//2
        assert B[n]+A[n]+C[n]==trace(power)
        assert B[n]+A[n]-C[n]==sum(power[i][sigma[i]] for i in range(16))
        assert (cp-cm)==C[n] and max(cp,cm)>0
    print('EXACT_TOTAL_COUNT_RECURRENCES_PASS 3..100')
    print('VERIFY_OK')
if __name__=='__main__': main()
