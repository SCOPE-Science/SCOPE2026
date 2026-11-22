"""Standalone mathematical checks for grounded heat-trace leader placement.

Run with: python3 verify.py. Uses only the Python standard library.
"""
from fractions import Fraction as F
from math import exp, sqrt, log


def alt(x, n):
    """Maclaurin partial sum for exp(-x) with x>=0."""
    return sum(((-x) ** k) / __import__('math').factorial(k) for k in range(n + 1))


def pos(x, n):
    return sum(x ** k / __import__('math').factorial(k) for k in range(n + 1))


def mat(q, a):
    # Small part has 2 vertices; large part q. Pin a small and 2-a large.
    ns, nl = 2-a, q-2+a
    N = ns+nl
    z = [[0]*N for _ in range(N)]
    for i in range(ns):
        z[i][i]=q
        for j in range(ns,N):z[i][j]=z[j][i]=-1
    for j in range(ns,N):z[j][j]=2
    return z


def multiply(a,b):
    n=len(a)
    return [[sum(a[i][k]*b[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def expected_power(q,a,r):
    if a==2:return q*(2**r)
    if a==1:return (q-2)*(2**r)+1+(q+1)**r
    # two roots sum q+2 and product 4
    u,v=2,q+2
    for j in range(2,r+1):u,v=v,(q+2)*v-4*u
    return (q-3)*(2**r)+q**r+(2 if r==0 else v)


def numerical_traces(q,t):
    delta=(q+2-sqrt((q+2)**2-16))/2
    return [
      (q-3)*exp(-2*t)+exp(-q*t)+exp(-delta*t)+exp(-(q+2-delta)*t),
      (q-2)*exp(-2*t)+exp(-t)+exp(-(q+1)*t),
      q*exp(-2*t)
    ]


def rational_bounds():
    # Alternating sums for exp(-x): odd sums lower; even sums upper.
    x=F(1,5); y=F(2,5); z=F(9,5)
    assert alt(x,3)>F(81,100)
    assert alt(y,3)>F(66,100)
    # exp(9/5)>100/17 => exp(-9/5)<17/100
    assert pos(z,8)>F(100,17)
    assert 1-F(81,100)-F(66,100)+2*F(17,100)<0
    assert 1-3*F(66,100)+2*F(17,100)<0
    t=F(67,100)
    lower=alt(F(19,50)*t,5)
    upper1=alt(t,6)
    upper2=alt(2*t,10)
    assert lower-upper1-upper2>0, (lower,upper1,upper2)
    # Tail for positive exp x, bounding all terms after degree 7 geometrically.
    x=t
    upper=pos(x,7)+x**8/__import__('math').factorial(8)/(1-x/9)
    assert upper<F(49,25)
    assert pos(F(4),8)>25
    assert F(49,25)+F(1,25)==2
    # delta_q<19/50 via q=9 quadratic sign and monotonicity.
    v=F(19,50)
    assert v*v-11*v+4<0
    # t=1: e^{-delta}>1-delta>31/50, and 3e^-2<3/7
    assert pos(F(2),6)>7
    assert F(31,50)-F(3,7)>0
    assert pos(F(1),2)>2
    return float(lower-upper1-upper2)


def main():
    margin=rational_bounds()
    checks=0
    for q in range(9,41):
        for a in (0,1,2):
            m=mat(q,a)
            P=[row[:] for row in m]
            for r in range(1,6):
                actual=sum(P[i][i] for i in range(len(P)))
                want=expected_power(q,a,r)
                assert actual==want,(q,a,r,actual,want)
                checks+=1
                if r<5:P=multiply(P,m)
        for t,a in ((.2,0),(.67,1),(1.,2)):
            H=numerical_traces(q,t)
            assert H[a]+1e-7<min(H[i] for i in range(3) if i!=a),(q,t,H)
            checks+=1
    phi=(1+sqrt(5))/2
    for t,a in ((.1,0),(.4,0),(.55,1),(.65,1),(.8,2),(1.2,2)):
        H=numerical_traces(2000,t)
        assert H[a]<min(H[i] for i in range(3) if i!=a)
        checks+=1
    assert log(phi)<.5*log(3)<log(2)
    print('VERIFY_OK',checks,'exact_and_numerical_crosschecks','lower_gap',margin)

if __name__=='__main__':main()
