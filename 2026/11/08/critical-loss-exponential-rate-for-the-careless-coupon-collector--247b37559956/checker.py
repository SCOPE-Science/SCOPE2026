"""Exact small-system checks and numerical asymptotic diagnostics for the post-loss coupon collector.
Standard-library only. All finite tests are diagnostics; analytic arguments prove the limit.
"""
from fractions import Fraction as F
from math import comb, exp, log, log1p, expm1

def binom(n,k):
    return F(comb(n,k))

def transition(n,p):
    q=1-p
    P=[]
    for k in range(n+1):
        row=[]
        for j in range(n+1):
            b=lambda r,s: binom(r,s)*q**s*p**(r-s) if 0<=s<=r else F(0)
            row.append(F(k,n)*b(k,j)+F(n-k,n)*b(k+1,j))
        assert sum(row)==1
        P.append(row)
    return P

def linear_solve(A,b):
    d=len(A)
    A=[row[:] for row in A];b=b[:] 
    for c in range(d):
        r=next(r for r in range(c,d) if A[r][c])
        A[c],A[r]=A[r],A[c];b[c],b[r]=b[r],b[c]
        fac=A[c][c]
        A[c]=[a/fac for a in A[c]];b[c]/=fac
        for r in range(d):
            if r==c:continue
            fac=A[r][c]
            if fac:
                A[r]=[a-fac*v for a,v in zip(A[r],A[c])]
                b[r]-=fac*b[c]
    return b

def stationary_exact(P):
    d=len(P)
    A=[[P[i][j]-(i==j) for i in range(d)] for j in range(d-1)]
    A.append([F(1)]*d)
    b=[F(0)]*(d-1)+[F(1)]
    return linear_solve(A,b)

def joint_moment(n,p,j):
    q=1-p
    f=F(1)
    for k in range(1,j+1):
        f*=F(k,n)*q**k/(1-F(n-k,n)*q**k)
    return f

def subset_transition(n,p):
    q=1-p
    N=1<<n
    P=[[F(0) for _ in range(N)] for _ in range(N)]
    for mask in range(N):
        for i in range(n):
            before=mask|(1<<i)
            for after in range(N):
                if after&~before:continue
                present=after.bit_count()
                lost=before.bit_count()-present
                P[mask][after]+=F(1,n)*q**present*p**lost
        assert sum(P[mask])==1
    return P

def exact_mean(P):
    n=len(P)-1
    A=[[F(i==j)-P[i][j] for j in range(n)] for i in range(n)]
    return linear_solve(A,[F(1)]*n)[0]

def exact_checks():
    checks=0
    for n in range(1,8):
        for p in [F(1,7),F(1,3),F(2,3),F(5,6)]:
            P=transition(n,p)
            stat=stationary_exact(P)
            for k in range(n+1):
                assert stat[k]>=0
                checks+=1
            for j in range(n+1):
                lhs=sum(F(comb(k,j))*stat[k] for k in range(j,n+1))/F(comb(n,j))
                rhs=joint_moment(n,p,j)
                assert lhs==rhs,(n,p,j,lhs,rhs)
                checks+=1
            assert stat[n]==joint_moment(n,p,n)
            checks+=1
            for j in range(n):
                flux_from_out=sum(stat[k]*P[k][n] for k in range(n))
                assert flux_from_out == stat[n]*(1-P[n][n])
                checks+=1
    # Independently solve the original set-valued chain in small dimensions.
    for n in range(1,5):
        for p in [F(1,4),F(2,5)]:
            P=subset_transition(n,p)
            stat=stationary_exact(P)
            for j in range(n+1):
                lhs=sum(stat[mask]*F(comb(mask.bit_count(),j)) for mask in range(1<<n)) / F(comb(n,j))
                assert lhs==joint_moment(n,p,j)
                checks+=1
            assert stat[-1]==joint_moment(n,p,n)
            checks+=1
    return checks

def exponent(c):
    # Simpson integration with stable value at zero.
    N=100000
    assert N%2==0
    def f(x):
        return log1p(c) if x==0 else log1p(expm1(c*x)/x)
    sm=f(0)+f(1)
    for i in range(1,N): sm+=(4 if i&1 else 2)*f(i/N)
    return sm/(3*N)

def log_full_mass(n,c):
    p=c/n
    q=1-p
    return sum(log(k/n)+k*log(q)-log1p(-(1-k/n)*q**k) for k in range(1,n+1))

def asymptotic_checks():
    checks=0
    for c in [0.25,0.5,1,2,4]:
        I=exponent(c)
        assert I>log1p(c)
        checks+=1
        errors=[]
        for n in [200,500,1000,2000,4000]:
            a=-log_full_mass(n,c)/n
            assert a>log1p(c)
            errors.append(abs(a-I));checks+=1
        assert errors[-1] < errors[0] and errors[-1]<0.02
        checks+=1
        print('c=',c,'rate=',round(I,12),'independence_heuristic=',round(log1p(c),12),
              'at_n=4000=',round(-log_full_mass(4000,c)/4000,12))
    return checks

if __name__=='__main__':
    count=exact_checks()+asymptotic_checks()
    print(f'{count} checks passed')
