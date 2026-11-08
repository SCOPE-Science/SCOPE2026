"""Exact finite-field checks for the additive Fourier spectrum of Jordan-product graphs.

Usage: python3 check_jordan_graph.py
Standard-library only. Matrix coordinates use row-major order and trace pairing.
"""
from itertools import product
from collections import Counter
from math import isclose


def add(a,b,q):
    return a ^ b if q == 4 else (a+b)%q

def mul(a,b,q):
    if q != 4: return (a*b)%q
    x = 0
    for i in range(2):
        if b>>i&1: x ^= a<<i
    if x&8: x ^= 0b1100
    if x&4: x ^= 0b111
    return x

def inv(a,q):
    if not a: raise ZeroDivisionError
    for i in range(1,q):
        if mul(a,i,q)==1:return i
    raise AssertionError('bad inverse')

def rank_mod(M,q):
    M=[v[:] for v in M]
    if not M:return 0
    r=0;n=len(M);m=len(M[0]);
    for c in range(m):
        p=next((i for i in range(r,n) if M[i][c]),None)
        if p is None:continue
        M[p],M[r]=M[r],M[p]
        scalar=inv(M[r][c],q)
        M[r]=[mul(scalar,x,q) for x in M[r]]
        for i in range(n):
            if i==r or not M[i][c]:continue
            f=M[i][c]
            # subtraction and addition coincide in characteristic two
            M[i]=[add(x, mul(f,y,q),q) if q in (2,4) else (x-f*y)%q for x,y in zip(M[i],M[r])]
        r+=1
        if r==n:break
    return r

def plus(a,b,q):return add(a,b,q)
def mprod(X,Y,n,q):
    return [sum(mul(X[i*n+k],Y[k*n+j],q) for k in range(n))%q if q!=4 else
            _xor([mul(X[i*n+k],Y[k*n+j],q) for k in range(n)])
            for i in range(n) for j in range(n)]
def _xor(xs):
    r=0
    for x in xs:r^=x
    return r

def S(C,n,q):
    N=n*n; out=[]
    for k in range(N):
        X=[0]*N;X[k]=1
        l=mprod(C,X,n,q); r=mprod(X,C,n,q)
        out.append([plus(u,v,q) for u,v in zip(l,r)])
    return [[out[k][j] for k in range(N)] for j in range(N)]

def trprod(A,X,n,q):
    Z=mprod(A,X,n,q)
    r=0
    for i in range(n):r=add(r,Z[i*n+i],q)
    return r

def character_counts(A,B,C,n,q):
    N=n*n; ct=[0]*q
    for X in product(range(q),repeat=N):
        ax=trprod(A,X,n,q)
        for Y in product(range(q),repeat=N):
            v=trprod(B,Y,n,q)
            j=mprod(X,Y,n,q);k=mprod(Y,X,n,q)
            z=[add(x,y,q) for x,y in zip(j,k)]
            w=trprod(C,z,n,q)
            t=add(add(ax,v,q),w,q)
            ct[t]+=1
    return ct

def check():
    expected3={0:30,1:24,2:26,4:1}
    for q in (2,3,4):
        n=2;N=4
        hist=Counter()
        for C in product(range(q),repeat=N):
            M=S(C,n,q)
            j=N-rank_mod(M,q)
            hist[j]+=1
        if q==2:
            want={2:14,4:2}
        elif q==3:
            want=expected3
        else:
            want={2:q**4-q,4:q}
        assert dict(hist)==want,(q,hist,want)
        support=sum(ct*q**(2*(N-j)) for j,ct in hist.items())
        closed = (q+(q**4-q)*q**4) if q in (2,4) else ((q**4-2*q**3+q)*q**8+q*(q*q-1)*q**6+(q**3-1)*q**4+1)
        assert support==closed,(q,support,closed)
        print('n2',q,'kernel_distribution',dict(sorted(hist.items())),'convolution_rank',support)
    # independent direct Fourier sums at several frequencies, q=2 and q=3
    for q in (2,3):
        n=2;N=n*n;zero=(0,)*N
        Cs=[zero, (1,0,0,0),(0,1,0,0),(1,0,0,1)]
        As=[zero, (1,0,0,0), (0,1,0,0)]
        for C in Cs:
            M=S(C,n,q);j=N-rank_mod(M,q)
            # A in image(S) iff augmented rank unchanged.
            col=[[M[i][k] for k in range(N)] for i in range(N)]
            for A in As:
                for B in As:
                    expected=rank_mod([row+[A[i]] for i,row in enumerate(col)],q)==N-j and rank_mod([row+[B[i]] for i,row in enumerate(col)],q)==N-j
                    # coord A is not tr-pairing; use A as a matrix, appropriate equations S(X)=-B.
                    coeff=character_counts(A,B,C,n,q)
                    if q==2:
                        value=coeff[0]-coeff[1]
                        assert (value!=0)==expected,(q,A,B,C,value,expected)
                        if expected:assert abs(value)==q**(N+j)
                    else:
                        # integer vector represents sum coefficients times zeta^i; zero iff all equal.
                        iszero= len(set(coeff))==1
                        assert (not iszero)==expected,(q,A,B,C,coeff,expected)
                        if expected:
                            import cmath
                            val=sum(v*cmath.exp(2j*cmath.pi*i/q) for i,v in enumerate(coeff))
                            assert isclose(abs(val),q**(N+j),rel_tol=1e-10,abs_tol=1e-8)
        print('direct_fourier_q',q,'passed',len(Cs)*len(As)**2,'frequencies')
    # independently classify all 3x3 binary matrices
    n=3;q=2;N=n*n; hist=Counter()
    for C in product(range(q),repeat=N):
        hist[N-rank_mod(S(C,n,q),q)]+=1
    assert sum(hist.values())==2**9 and min(hist)==3
    print('n3_binary_kernel_distribution',dict(sorted(hist.items())))
    n=3;q=3;N=9;hist=Counter()
    for C in product(range(q),repeat=N):
        hist[N-rank_mod(S(C,n,q),q)]+=1
    assert dict(hist)=={0:7722,1:3510,2:5148,3:2730,4:468,5:104,9:1}
    print('n3_ternary_kernel_distribution',dict(sorted(hist.items())))
    print('ALL_JORDAN_GRAPH_TESTS_OK')

if __name__=='__main__':check()
