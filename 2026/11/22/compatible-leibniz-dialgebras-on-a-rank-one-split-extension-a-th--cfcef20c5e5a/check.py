"""Finite-field checks for a split Leibniz dialgebra extension theorem.

Uses only Python's standard library. Invoke: python check.py
"""
from itertools import product
from math import prod


def mm(A,B,d,q):
    return tuple(sum(A[i*d+k]*B[k*d+j] for k in range(d))%q
                 for i in range(d) for j in range(d))

def rank(A,d,q):
    M=[list(A[i*d:(i+1)*d]) for i in range(d)]
    r=0
    for c in range(d):
        k=next((i for i in range(r,d) if M[i][c]%q),None)
        if k is None:continue
        M[r],M[k]=M[k],M[r]
        z=pow(M[r][c],-1,q)
        M[r]=[v*z%q for v in M[r]]
        for i in range(d):
            if i!=r:
                z=M[i][c]
                M[i]=[(x-z*y)%q for x,y in zip(M[i],M[r])]
        r+=1
    return r

def GL(n,q):
    return prod(q**n-q**i for i in range(n))

def expected(d,q):
    g=GL(d,q)
    return {(a,b,d-a-b):g//(GL(a,q)*GL(b,q)*GL(d-a-b,q))
            for a in range(d+1) for b in range(d-a+1)}

def independent_count(d,q):
    matrices=[tuple(t) for t in product(range(q), repeat=d*d)]
    zero=(0,)*(d*d)
    idem=[M for M in matrices if mm(M,M,d,q)==M]
    result={}
    for A in idem:
        rA=rank(A,d,q)
        for E in idem:
            if mm(A,E,d,q)!=zero or mm(E,A,d,q)!=zero:continue
            rE=rank(E,d,q)
            k=(rA,rE,d-rA-rE)
            result[k]=result.get(k,0)+1
    return result

def direct_small(d,q):
    # Independent enumeration of all bilinear second products when d=1.
    assert d==1
    n=2
    # basis: v=e_0, t=e_1. Right Leibniz product mu(v,t)=v.
    def mu(x,y):
        return (x[0]*y[1]%q,0)
    basis=[(1,0),(0,1)]
    def lin(x,y,operation):
        return tuple(sum(x[i]*y[j]*operation[(i,j)][k]
                         for i in range(n) for j in range(n))%q for k in range(n))
    count=0
    forms=[]
    for C in product(range(q),repeat=n*n*n):
        op={(i,j):tuple(C[(i*n+j)*n+k] for k in range(n))
            for i in range(n) for j in range(n)}
        def nu(x,y):return lin(x,y,op)
        def add(x,y):return tuple((a+b)%q for a,b in zip(x,y))
        if all(
            mu(mu(x,y),z)==add(mu(mu(x,z),y),mu(x,mu(y,z)))
            and mu(nu(x,y),z)==add(nu(mu(x,z),y),nu(x,mu(y,z)))
            and nu(nu(x,y),z)==add(mu(nu(x,z),y),nu(x,nu(y,z)))
            and mu(x,mu(y,z))==mu(x,nu(y,z))
            and nu(mu(x,y),z)==nu(nu(x,y),z)
            for x in basis for y in basis for z in basis):
            count+=1
            forms.append(op)
    assert count==3, (q,count)
    assert all(op[(0,0)]==(0,0) and op[(1,1)]==(0,0)
               and op[(0,1)][1]==0 and op[(1,0)][1]==0
               for op in forms)
    return count


def direct_all_basis_identities(d,q):
    """Independent axiomatic check of every classified product on each basis triple."""
    zero=(0,)*(d*d)
    matrices=[tuple(t) for t in product(range(q),repeat=d*d)]
    idem=[P for P in matrices if mm(P,P,d,q)==P]
    def act(M,v):
        return tuple(sum(M[i*d+j]*v[j] for j in range(d))%q for i in range(d))
    basis=[tuple(int(i==j) for i in range(d+1)) for j in range(d+1)]
    def add(x,y):return tuple((a+b)%q for a,b in zip(x,y))
    def mu(x,y):return tuple((x[i]*y[d])%q for i in range(d))+(0,)
    num=0
    for P in idem:
      for E in idem:
        if mm(P,E,d,q)!=zero or mm(E,P,d,q)!=zero:continue
        def nu(x,y):
            u=tuple((x[d]*-w)%q for w in act(E,y[:d]))
            v=tuple((y[d]*w)%q for w in act(P,x[:d]))
            return add(u+(0,),v+(0,))
        for x,y,z in product(basis,repeat=3):
            assert mu(mu(x,y),z)==add(mu(mu(x,z),y),mu(x,mu(y,z)))
            assert mu(nu(x,y),z)==add(nu(mu(x,z),y),nu(x,mu(y,z)))
            assert nu(nu(x,y),z)==add(mu(nu(x,z),y),nu(x,nu(y,z)))
            assert mu(x,mu(y,z))==mu(x,nu(y,z))
            assert nu(mu(x,y),z)==nu(nu(x,y),z)
        num+=1
    return num

if __name__=='__main__':
    for d,q in ((1,2),(1,3),(2,2),(2,3),(3,2)):
        a=independent_count(d,q)
        b=expected(d,q)
        assert a==b,(d,q,a,b)
        print(f'd={d} q={q}: {sum(a.values())} structures; ranks {sorted(a.items())}')
    for d,q in ((2,2),(2,3),(3,2)):
        print(f'all five identities verified for (d,q)=({d},{q}): {direct_all_basis_identities(d,q)} products')
    for q in (2,3):
        print(f'full bilinear-product enumeration for (d,q)=(1,{q}): {direct_small(1,q)} structures')
    print('VERIFY_OK')
