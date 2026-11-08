"""Reproduce exact Markov-chain comparisons for a switching-noise voter model.

No external packages.  Run: python verify.py
"""
from fractions import Fraction as F


def solve(a, b):
    n = len(b)
    A = [[F(a[i][j]) for j in range(n)] + [F(b[i])] for i in range(n)]
    for j in range(n):
        k = next(k for k in range(j, n) if A[k][j])
        A[j], A[k] = A[k], A[j]
        d = A[j][j]
        for z in range(j, n + 1):
            A[j][z] /= d
        for i in range(n):
            if i != j:
                d = A[i][j]
                if d:
                    for z in range(j, n + 1):
                        A[i][z] -= d * A[j][z]
    return [A[i][-1] for i in range(n)]


def direct(N, a0, a1, h, lam, r0, r1):
    rates = (a0, a1)
    n = 2*(N+1)
    Q = [[F(0) for _ in range(n)] for _ in range(n)]
    for s in range(2):
        for i in range(N+1):
            j = s*(N+1)+i
            plus=(N-i)*(rates[s]+h*F(i,N))
            minus=i*(rates[s]+h*F(N-i,N))
            sw=lam*(r0 if s==0 else r1)
            events=[]
            if i<N: events.append((j+1,plus))
            if i>0: events.append((j-1,minus))
            events.append(((1-s)*(N+1)+i,sw))
            for k,v in events:
                Q[j][k] += v
                Q[j][j] -= v
    A=[[Q[j][i] for j in range(n)] for i in range(n)]
    A[-1]=[F(1)]*n
    bb=[F(0)]*(n-1)+[F(1)]
    p=solve(A,bb)
    assert sum(p)==1 and all(x>0 for x in p)
    v=sum(p[s*(N+1)+i]*(F(i)-F(N,2))**2 for s in range(2) for i in range(N+1))
    return v


def formula(N,a0,a1,h,lam,r0,r1):
    c0=4*a0+2*h/N; c1=4*a1+2*h/N
    b0=N*(a0+h/2); b1=N*(a1+h/2)
    ss=r0+r1
    pi0=r1/ss; pi1=r0/ss
    C=pi0*c0+pi1*c1
    B=pi0*b0+pi1*b1
    return B/C+ 8*h*(N-1)*pi0*pi1*(a1-a0)**2/(C*(c0*c1+lam*ss*C))


def check():
    count=0
    for N in range(2,8):
        for (a0,a1,h,lam,r0,r1) in [
            (F(1,5),F(3,4),F(2,3),F(1,7),F(1),F(1)),
            (F(1,3),F(7,5),F(3,2),F(4,5),F(2),F(3)),
            (F(1,11),F(5,2),F(1,4),F(2),F(3,7),F(5,6)),
            (F(1,3),F(1,3),F(5,4),F(1),F(3),F(1)),
            (F(1,9),F(7,3),F(0),F(1,7),F(2),F(1)),
        ]:
            actual=direct(N,a0,a1,h,lam,r0,r1)
            predicted=formula(N,a0,a1,h,lam,r0,r1)
            assert actual==predicted,(N,actual,predicted)
            count+=1
    for N in range(2,20):
        a0,a1,h,r0,r1=F(1,4),F(5,3),F(2),F(3,4),F(7,5)
        ls=[F(1,1000),F(1,3),F(2),F(100)]
        vals=[formula(N,a0,a1,h,ll,r0,r1) for ll in ls]
        assert all(vals[i]>vals[i+1] for i in range(len(vals)-1))
        count+=3
    print('PASS:',count,'exact rational identities / monotonicity inequalities')

if __name__=='__main__': check()
