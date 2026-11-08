"""Standalone finite arithmetic and spectral replay for the matching-channel FMMC formula.
Requires only Python 3 standard library. Run: python verify.py
The infinite-family proof is analytic and is stated in RESULT.md.
"""
import math
from fractions import Fraction
from decimal import Decimal, localcontext

SQRT2 = math.sqrt(2.0)

def weights(m,k):
    h=(1+SQRT2)*m-2*k
    b=SQRT2/h
    c=1-(m-k)*b
    d=(1-k*b)/(m-k)
    rate=(m-4*k+2*SQRT2*k)/(m+2*k-2*SQRT2*k)
    return b,c,d,rate

def matrix(m,k):
    r=m-k
    b,c,d,s=weights(m,k)
    n=2*m
    P=[[0.0]*n for _ in range(n)]
    for side in (0,1):
        z=side*m
        for i in range(k):
            for j in range(k,m):
                P[z+i][z+j]=P[z+j][z+i]=b
        for i in range(k,m):
            for j in range(k,m):
                if i!=j: P[z+i][z+j]=d
        for i in range(k):
            P[z+i][(1-side)*m+i]=c
    for i in range(n):
        P[i][i]=1-sum(P[i][j] for j in range(n) if j!=i)
    return P

def jacobi_eigs(a):
    a=[x[:] for x in a]
    n=len(a)
    for _ in range(200*n*n):
        p,q=max(((i,j) for i in range(n) for j in range(i+1,n)),key=lambda ij:abs(a[ij[0]][ij[1]]))
        if abs(a[p][q])<1.e-13:break
        tau=(a[q][q]-a[p][p])/(2*a[p][q])
        t=math.copysign(1,tau)/(abs(tau)+math.sqrt(1+tau*tau)) if tau else 1
        c=1/math.sqrt(1+t*t);s=t*c
        app,aqq,apq=a[p][p],a[q][q],a[p][q]
        a[p][p]=app-t*apq;a[q][q]=aqq+t*apq;a[p][q]=a[q][p]=0
        for i in range(n):
            if i in (p,q):continue
            x,y=a[i][p],a[i][q]
            a[i][p]=a[p][i]=c*x-s*y
            a[i][q]=a[q][i]=s*x+c*y
    else:raise AssertionError('Jacobi iteration failed')
    return sorted(a[i][i] for i in range(n))

# Exact rational identities in the expansion D(b) = 4 - 4 m b + A b^2:
# A-m^2=4k(m-k)>0, hence strict convexity of sqrt(D), for all m>=2k>=4.
for k in range(2,21):
    for m in range(2*k,6*k+1):
        A=m*m+4*m*k-4*k*k
        assert A-m*m==4*k*(m-k)>0
        assert Fraction(m-2*k,m) >= 0
        b,c,d,s=weights(m,k)
        D=4-4*m*b+A*b*b
        assert abs(D-2)<1e-11
        assert 0<b and c>=0 and d>=0
        assert 0<=m*b<=1+1e-13
        assert (m-k)*b>=.5-1e-13
        assert abs((m-k)*b+c-1)<1e-12
        assert abs(s-((m-2*k)*b+SQRT2)/2)<1e-12
        assert .5<=s<1
print('PARAMETER_IDENTITIES_OK', sum(4*k-2*k+1 for k in range(2,21)))

cases=0
for k in range(2,7):
    for m in range(2*k, min(6*k,24)+1):
        P=matrix(m,k); n=2*m
        assert all(abs(sum(row)-1)<1e-11 for row in P)
        assert all(min(row)>=-1.e-12 for row in P)
        assert all(abs(P[i][j]-P[j][i])<1e-12 for i in range(n) for j in range(n))
        ev=jacobi_eigs(P)
        b,c,d,s=weights(m,k)
        assert abs(ev[-1]-1)<1e-9
        assert abs(max(abs(x) for x in ev[:-1])-s)<2e-8
        mu_plus=(m-2*k)*b/2+math.sqrt(2)/2
        mu_minus=(m-2*k)*b/2-math.sqrt(2)/2
        target=sorted([1,1-m*b,mu_plus,mu_minus]+[c]*(k-1)+[-c]*(k-1)+[0]*(2*(m-k-1)))
        assert len(target)==n
        assert max(abs(x-y) for x,y in zip(ev,target))<2e-8
        cases+=1
print('FINITE_SPECTRAL_REPLAY_OK',cases)

# At the proposed point, test the scalar 2x2 lower bound against a grid of other
# feasible gateway-to-peripheral and matching rates. This is illustrative, not
# a global optimization certificate (the written calculus proof provides that).
checks=0
for k,m in [(2,4),(2,5),(3,9),(4,11),(5,20)]:
    b,c,d,s=weights(m,k)
    r=m-k
    for ib in range(41):
        x=ib/(40*r)
        for ic in range(41):
            y=(1-r*x)*ic/40
            D=m*m*x*x+4*(m-2*k)*x*y+4*y*y
            lam=1-(m*x+2*y)/2+math.sqrt(max(0,D))/2
            assert lam>=s-1e-11,(k,m,ib,ic,lam,s)
            checks+=1
print('FINITE_LOWER_BOUND_GRID_OK',checks)
print('VERIFY_OK')
