"""Finite-field checks of the maximal adjoint nilpotency-index formula.
Pure Python 3, no external dependencies. This checker tests finite instances only;
the uniform theorem requires the separate algebraic proof.
"""
from itertools import product
from math import comb
from random import Random


def field(q):
    if q in (2,3,5,7):
        p=q
        return p,list(range(q)),lambda a,b:(a+b)%q,lambda a,b:(a*b)%q
    if q==4:
        def mul(a,b):
            z=0
            for i in range(2):
                for j in range(2):
                    if (a>>i)&1 and (b>>j)&1: z^=1<<(i+j)
            for deg in (2,):
                if (z>>deg)&1:z^=0b111<<(deg-2)
            return z
        return 2,list(range(q)),lambda a,b:a^b,mul
    if q==9:
        def mul(a,b):
            a0,a1=a%3,a//3;b0,b1=b%3,b//3
            return (a0*b0+2*a1*b1)%3+3*((a0*b1+a1*b0)%3)
        return 3,list(range(q)),lambda a,b:(a%3+b%3)%3+3*((a//3+b//3)%3),mul
    raise ValueError(q)


def minus(a,p):
    if p==2:return a
    return ((-a%p) if a<p else (-a%p)+p*((-(a//p))%p))


def matmul(A,B,n,z,mul,add):
    C=[[z]*n for _ in range(n)]
    for i in range(n):
        for k in range(i+1,n):
            a=A[i][k]
            if not a:continue
            for j in range(k+1,n):
                b=B[k][j]
                if b:C[i][j]=add(C[i][j],mul(a,b))
    return C


def bracket(A,B,n,p,add,mul):
    AB=matmul(A,B,n,0,mul,add)
    BA=matmul(B,A,n,0,mul,add)
    return [[add(AB[i][j],minus(BA[i][j],p)) for j in range(n)] for i in range(n)]


def direct(X,n,p,add,mul):
    c=[]
    for i in range(n-1):
        Y=[[0]*n for _ in range(n)]
        Y[i][i+1]=1
        for _ in range(n-2):Y=bracket(X,Y,n,p,add,mul)
        # Every possible output should be central.
        assert all(Y[r][s]==0 for r in range(n) for s in range(n) if (r,s)!=(0,n-1))
        c.append(Y[0][n-1])
    return c


def predicted(a,n,p,add,mul):
    v=[]
    for i in range(n-1):
        z=comb(n-2,i)%p
        if (n-i-2)%2:z=minus(z,p)
        for j in range(n-1):
            if j!=i:z=mul(z,a[j])
        v.append(z)
    return v


def check(q,n,exhaustive=True):
    p,e,add,mul=field(q)
    rng=Random(41000+q*100+n)
    N=n*(n-1)//2
    M=sum(comb(n-2,k)%p!=0 for k in range(n-1))
    expected=(q**(N-(n-1)))*((q-1)**(n-1)+M*(q-1)**(n-2))
    vector_count=0;success=0
    iterable=product(e,repeat=n-1) if exhaustive else [tuple(rng.choice(e) for _ in range(n-1)) for _ in range(100)]
    for a in iterable:
        X=[[0]*n for _ in range(n)]
        for i,x in enumerate(a):X[i][i+1]=x
        got=direct(X,n,p,add,mul)
        want=predicted(a,n,p,add,mul)
        assert got==want,(q,n,a,got,want)
        success+=any(got)
        vector_count+=1
    if exhaustive:
        assert success*((q**(N-n+1)))==expected,(q,n,success,expected)
    # Add random higher-diagonal entries to check their irrelevance directly.
    for _ in range(40):
        X=[[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(i+1,n):X[i][j]=rng.choice(e)
        a=[X[i][i+1] for i in range(n-1)]
        assert direct(X,n,p,add,mul)==predicted(a,n,p,add,mul)
    print(f'q={q} n={n} first-superdiag cases={vector_count} max-index cases={success} random-higher=40 PASS')


if __name__=='__main__':
    for q,n in ((2,3),(2,4),(2,5),(2,6),(2,7),(2,8),(2,9),(3,3),(3,4),(3,5),(3,6),(3,7),(4,4),(4,5),(4,6),(5,4),(5,5),(9,4)):
        check(q,n)
    print('ALL CHECKS PASSED')
