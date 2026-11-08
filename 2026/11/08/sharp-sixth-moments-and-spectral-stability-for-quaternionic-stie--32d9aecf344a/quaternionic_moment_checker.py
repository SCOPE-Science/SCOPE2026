"""Reproducible exact and numerical checks for sixth moments of quaternionic Stiefel linear forms."""
from fractions import Fraction
import random

def a(n):
    d=4*n
    return Fraction(15,d*(d+2)*(d+4))
def b(n):
    d=4*n
    return Fraction(3,4*(n-1)*(d+2)*(d+4))
def c(n):
    assert n>=3
    return (Fraction(15,64)-n*a(n)-15*n*(n-1)*b(n))/(15*n*(n-1)*(n-2))
def direct6(n,sq):
    sq=list(map(Fraction,sq))
    r=len(sq)
    val=a(n)*sum(x**3 for x in sq)
    val+=15*b(n)*sum(sq[i]**2*sq[j] for i in range(r) for j in range(r) if i!=j)
    if n>=3:
        val+=90*c(n)*sum(sq[i]*sq[j]*sq[k] for i in range(r) for j in range(i+1,r) for k in range(j+1,r))
    return val

def formula6(n,sq):
    sq=list(map(Fraction,sq))
    p=sum(sq)
    if n==2:
        return Fraction(20,1)-12*sum(x*x for x in sq)/p**2
    return Fraction(15*n*n,(n-2)*(n-1)*(n+1)*(2*n+1))* (2*n*n-3*n-1 - 3*(n-1)*sum(x*x for x in sq)/p**2 + 2*sum(x*x*x for x in sq)/p**3)

def qmul(a,b):
    a0,a1,a2,a3=a
    b0,b1,b2,b3=b
    return (a0*b0-a1*b1-a2*b2-a3*b3,
        a0*b1+a1*b0+a2*b3-a3*b2,
        a0*b2-a1*b3+a2*b0+a3*b1,
        a0*b3+a1*b2-a2*b1+a3*b0)

def qconj(x):return (x[0],-x[1],-x[2],-x[3])
def qnorm(x):return sum(y*y for y in x)

def stiefel_diag(n,r,rng):
    cols=[]
    for j in range(r):
        w=[tuple(rng.gauss(0,1) for _ in range(4)) for _ in range(n)]
        for v in cols:
            alpha=[0.0]*4
            for i in range(n):
                x=qmul(qconj(v[i]),w[i])
                for t in range(4): alpha[t]+=x[t]
            for i in range(n):
                x=qmul(v[i],alpha)
                w[i]=tuple(w[i][t]-x[t] for t in range(4))
        norm=sum(qnorm(w[i]) for i in range(n))**.5
        w=[tuple(x/norm for x in v) for v in w]
        cols.append(w)
    return [cols[j][j][0] for j in range(r)]

def pairings_and_trace_moments():
    def matchings(remaining):
        if not remaining:
            yield []
            return
        a=remaining[0]
        for b in remaining[1:]:
            for rest in matchings([x for x in remaining[1:] if x!=b]):
                yield [(a,b)]+rest
    def lds(perm):
        dp=[1]*len(perm)
        for i in range(len(perm)):
            dp[i]=1+max([dp[j] for j in range(i) if perm[j]>perm[i]],default=0)
        return max(dp)
    p=[]
    for pairs in matchings(list(range(6))):
        perm=[None]*6
        for i,j in pairs:perm[i]=j;perm[j]=i
        p.append(lds(perm))
    assert len(p)==15
    assert sum(x<=4 for x in p)==14
    assert sum(x<=6 for x in p)==15
    print('EXACT_FIXED_POINT_FREE_INVOLUTION_TRACE_COUNTS_OK 14 15')

def exact_checks():
    pairings_and_trace_moments()
    for n in range(2,30):
        for r in range(1,min(n,7)+1):
            for k in range(1,10):
                sq=[Fraction(((j+3*k)**2+5*j)%31+1,19) for j in range(r)]
                p=sum(sq)
                expected=formula6(n,sq)*(p/(4*n))**3
                if expected != direct6(n,sq):
                    raise AssertionError((n,r,k,expected,direct6(n,sq)))
            if n>=3:
                assert c(n) == Fraction(2*n*n-3*n-1,64*n*(n-2)*(n-1)*(n+1)*(2*n+1))
            z=[Fraction(1,r)]*r
            top=formula6(n,z)
            for j in range(1,r+1):
                sample=[Fraction(1,j)]*j
                assert top>=formula6(n,sample)
            assert top>=formula6(n,[1])
    assert formula6(2,[1])==8
    for n in range(2,30):
        for r in range(1,min(n,7)+1):
            for j in range(1,13):
                sq=[Fraction((i+2*j)**2 % (9+j)+1,1) for i in range(r)]
                total=sum(sq)
                t=[x/total for x in sq]
                bottom=formula6(n,[1])
                top=formula6(n,[1]*r)
                value=formula6(n,sq)
                if n==2:
                    lowdef=12*sum(x*(1-x) for x in t)
                    highdef=12*sum((x-Fraction(1,r))**2 for x in t)
                else:
                    factor=Fraction(15*n*n,(n-2)*(n-1)*(n+1)*(2*n+1))
                    lowdef=factor*sum(x*(1-x)*(3*(n-1)-2*(1+x)) for x in t)
                    highdef=factor*sum((x-Fraction(1,r))**2*(3*(n-1)-2*(x+Fraction(2,r))) for x in t)
                assert lowdef==value-bottom and highdef==top-value
                assert lowdef>=0 and highdef>=0
    print('EXACT_TWO_SPECTRAL_STABILITY_IDENTITIES_OK')
    assert formula6(2,[1,1])==14
    for n in range(3,30):
        assert formula6(n,[1]*n)==15
        assert formula6(n,[1]) == Fraction(30*n*n,(n+1)*(2*n+1))
    print('EXACT_SIXTH_MOMENT_EXPANSION_AND_BOUNDARY_CASES_OK')

if __name__=='__main__':
    exact_checks()
    rng=random.Random(12431)
    for n,r,sq in [(2,2,[1,1]),(3,3,[1,1,1]),(3,3,[2,1,3]),(4,2,[1,3])]:
        size=50000
        fs=[0.,0.,0.]
        for _ in range(size):
            diag=stiefel_diag(n,r,rng)
            f=sum(diag[i]*(sq[i]**.5) for i in range(r))
            fs[0]+=f*f
            fs[1]+=f**4
            fs[2]+=f**6
        obs=tuple(x/size for x in fs)
        pred=(sum(sq)/(4*n),None,float(direct6(n,sq)))
        diff=abs(obs[2]-pred[2])/pred[2]
        print('MONTE_CARLO_STIEFEL',n,r,'E2',obs[0],pred[0],'E6',obs[2],pred[2],'relerr',diff)
        assert diff<0.13
    print('INDEPENDENT_QUATERNIONIC_GRAM_SCHMIDT_CHECKS_OK')
