"""Standalone exact-arithmetic checks for a three-site periodic Sobolev frame potential.

Uses Python 3 standard library only. Finite checks corroborate, but do not replace,
the analytical global critical-point proof in RESULT.md.
"""
from fractions import Fraction as Q


def bernoulli2(t):
    return t*t-t+Q(1,6)


def green(t):
    t %= 1
    return bernoulli2(t)/2


def frame_potential(gaps):
    a,b,c=gaps
    assert a>0 and b>0 and c>0 and a+b+c==1
    return 3*green(Q(0))**2+2*(green(a)**2+green(b)**2+green(c)**2)


def det3(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
            -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
            +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))


def check():
    assertions=0
    optimum=Q(5,216)
    g0=(Q(1,6),Q(1,6),Q(2,3))
    assert frame_potential(g0)==optimum; assertions+=1
    assert frame_potential((Q(1,3),)*3)==Q(11,432); assertions+=1
    assert frame_potential(g0)*144==Q(10,3); assertions+=1
    assert frame_potential((Q(1,3),)*3)*144==Q(11,3); assertions+=1
    assert 2*(green(Q(1,6))**2)+green(Q(1,3))**2==Q(1,864); assertions+=1

    # Distinct rational triples; the theorem covers irrational triples as well.
    for n in range(3,145):
        n4=n**4
        for i in range(1,n-1):
            for j in range(1,n-i):
                k=n-i-j
                # B_2(i/n) = (6i^2-6in+n^2)/(6n^2).
                qs=[6*v*v-6*v*n+n*n for v in (i,j,k)]
                deficit=6*sum(u*u for u in qs)-n4
                assert deficit>=0
                if deficit==0:
                    assert n%6==0 and sorted((i,j,k))==[n//6,n//6,2*n//3]
                assertions+=1

    # The optimized Gram matrix has characteristic factorization
    # (9*lambda-1)*(2592*lambda^2-360*lambda+11)/23328.
    x=(Q(0),Q(1,6),Q(1,3))
    gram=[[green(x[i]-x[j]) for j in range(3)] for i in range(3)]
    assert sum(gram[i][i] for i in range(3))==Q(1,4); assertions+=1
    assert sum(gram[i][j]**2 for i in range(3) for j in range(3))==optimum; assertions+=1
    assert det3(gram)==Q(11,23328); assertions+=1
    assert [gram[0][0],gram[0][1],gram[0][2]]==[Q(1,12),Q(1,72),-Q(1,36)]; assertions+=1

    # Analytic stationarity equation on the two-equal-gap branch:
    # w'(t)-w'(1-2t)=(3t-1)^2(6t-1)/6.
    def wp(t):return (2*t-1)*(6*t*t-6*t+1)/12
    for i in range(1,100):
        t=Q(i,201)
        assert wp(t)-wp(1-2*t)==(3*t-1)**2*(6*t-1)/6
        assertions+=1
    print(f"PASS: {assertions} exact rational assertions; sharp value 5/216")


if __name__=='__main__':
    check()
