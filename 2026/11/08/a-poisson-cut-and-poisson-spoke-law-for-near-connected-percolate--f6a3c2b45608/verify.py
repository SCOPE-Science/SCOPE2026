"""Standalone exact checks for wheel bond-percolation reliability.

Only Python standard-library modules are used. These finite checks corroborate;
the infinite limit and law are proved analytically in RESULT.md.
"""
from fractions import Fraction
from itertools import product
from math import exp, cosh, sqrt


def mm(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(2)), Fraction(0))
             for j in range(2)] for i in range(2)]


def exact(n,p,q):
    M=[[p*(1-q)+(1-p)*q,p*q],[1-p,p]]
    P=[[Fraction(1),Fraction(0)],[Fraction(0),Fraction(1)]]
    while n:
        if n&1: P=mm(P,M)
        M=mm(M,M);n//=2
    return P[0][0]+P[1][1]


def wheel_formula(n,p,q):
    return exact(n,p,q)-2*(p*(1-q))**n


def enumeration(n, np,dp,nq,dq):
    """Exact enumeration using integer weights, independent of the transfer matrix."""
    total=0
    count=0
    zero=0
    for s in range(1<<n):
        ws=(nq**s.bit_count())*((dq-nq)**(n-s.bit_count()))
        for e in range(1<<n):
            w=ws*(np**e.bit_count())*((dp-np)**(n-e.bit_count()))
            # Flood-fill from the central hub, represented by bit n.
            reached=1<<n
            frontier=[n]
            while frontier:
                v=frontier.pop()
                if v==n:
                    cand=[i for i in range(n) if (s>>i)&1]
                else:
                    cand=[]
                    if (s>>v)&1:cand.append(n)
                    if (e>>v)&1:cand.append((v+1)%n)
                    if (e>>((v-1)%n))&1:cand.append((v-1)%n)
                for u in cand:
                    if not (reached>>u)&1:
                        reached|=1<<u
                        frontier.append(u)
            if reached==(1<<(n+1))-1: total+=w
            if reached==(1<<n):zero+=w
            count+=w
    den=dp**n*dq**n
    assert count==den
    return Fraction(total,den),Fraction(zero,den)


def limit_F(lam,mu):
    return 2*exp(-lam-mu)*(exp(lam/2)*cosh(sqrt(lam*lam+4*lam*mu)/2)-1)


def finite_float(n,lam,mu):
    original_n=n
    q=lam/n;p=1-mu/n
    A=[[p*(1-q)+(1-p)*q,p*q],[1-p,p]]
    B=[[1.,0.],[0.,1.]]
    while n:
        if n&1:B=[[sum(B[i][k]*A[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
        A=[[sum(A[i][k]*A[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
        n//=2
    return B[0][0]+B[1][1]-2*(p*(1-q))**original_n

if __name__=='__main__':
    assertions=0
    params=[(1,2,1,3),(2,3,1,4),(3,5,2,3),(1,1,1,2),(0,1,3,4),(1,2,1,1)]
    for n in range(3,7):
        for np,dp,nq,dq in params:
            p,q=Fraction(np,dp),Fraction(nq,dq)
            v,z=enumeration(n,np,dp,nq,dq)
            assert v==wheel_formula(n,p,q),('spanning',n,np,dp,nq,dq,v,wheel_formula(n,p,q))
            assertions+=1
            assert z==(1-q)**n,('hub isolated',n,np,dp,nq,dq)
            assertions+=1
            assert Fraction(0)<=v<=Fraction(1)
            assertions+=1
    # Independent exact zero-spoke and no-rim-break boundary checks.
    for n in range(3,15):
        for j in range(1,10):
            q=Fraction(j,10)
            assert wheel_formula(n,Fraction(1),q)==1-(1-q)**n
            assert wheel_formula(n,Fraction(0),q)==q**n
            assertions+=2
    # Analytic matrix-exponential limits are checked numerically, never used as proof.
    for lam,mu in ((0.,0.),(1.,0.),(0.,1.),(1.,1.),(2.,3.),(4.,0.5),(0.1,8.)):
        N=4000
        approx=finite_float(N,lam,mu)
        lim=limit_F(lam,mu)
        assert abs(approx-lim)<0.003, (lam,mu,approx,lim)
        assertions+=1
    print(f'VERIFY_OK {assertions} exact/boundary/limit consistency assertions')
