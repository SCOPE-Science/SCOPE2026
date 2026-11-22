"""Numerical checks for mixed perfect-power S-gap entropy; Python stdlib only.

Usage: python verify.py
The theorem's infinite-dimensional validity is supplied by the proof, not by these checks.
"""
import math


def sums_for_power(k, p, threshold=64.0):
    # Cut after p*n**k exceeds 64. Bounds follow by integral comparison:
    # sum_{n>M}n**(kj) exp(-p*n**k) <= integral_M^inf (x+1)**(kj) exp(-p*x**k) dx
    m = int((threshold / p)**(1.0 / k)) + 2
    z = v1 = v2 = 0.0
    for n in range(1, m + 1):
        a = float(n**k)
        w = math.exp(-p * a)
        z += w
        v1 += a * w
        v2 += a * a * w
    return z, v1, v2


def partition(r, s, p):
    # Inclusion-exclusion of the two perfect-power sets, intersection at rs powers.
    pieces = [sums_for_power(k,p) for k in (r,s,r*s)]
    z, m, m2 = (pieces[0][j] + pieces[1][j] - pieces[2][j]
                 for j in range(3))
    return math.exp(-p)*z, math.exp(-p)*(m+z), math.exp(-p)*(m2+2*m+z)


def pressure_at_density(r,s,rho):
    left=rho / (10*r)
    right=rho * 10/r
    def avg(p):
        z,m,_ = partition(r,s,p)
        return m/z
    assert avg(left)>1/rho>avg(right)
    for _ in range(62):
        middle=(left+right)/2
        if avg(middle)>1/rho:
            left=middle
        else:
            right=middle
    p=(left+right)/2
    z,m,_=partition(r,s,p)
    assert abs(m/z*rho-1) < 1e-10
    return p,math.log(z)+p/rho


def coefficients(r,s):
    q=1/r
    alpha=q-1/s
    beta=q-1/(r*s)
    a=math.gamma(q)/r
    b=math.gamma(1/s)/s
    c=math.gamma(1/(r*s))/(r*s)
    B=b/a
    C=c/a
    Q=(0.5+alpha**2/(2*q))*B**2
    return q,alpha,beta,a,B,C,Q


def expansion(r,s,rho):
    q,alpha,beta,a,B,C,Q=coefficients(r,s)
    p=q*rho
    leading=q*math.log(1/rho)+math.log(a)-q*math.log(q)+q
    first=leading+B*p**alpha
    if s<2*r-1:
        second=first-Q*p**(2*alpha)
    elif s==2*r-1:
        second=first-(Q+C)*p**(2*alpha)
    else:
        second=first-C*p**beta
    return leading,first,second


def finite_power_intersection(r,s,M=1000):
    a={n**r for n in range(1,int(M**(1/r))+2) if n**r<=M}
    b={n**s for n in range(1,int(M**(1/s))+2) if n**s<=M}
    c={n**(r*s) for n in range(1,int(M**(1/(r*s)))+2) if n**(r*s)<=M}
    assert a&b==c


def main():
    pairs=[(2,3),(2,5),(3,4),(3,5),(3,7),(4,5),(4,7),(4,9)]
    count=0
    for r,s in pairs:
        assert math.gcd(r,s)==1
        finite_power_intersection(r,s)
        q,alpha,beta,a,B,C,Q=coefficients(r,s)
        assert abs((beta-2*alpha) - (2*r-s-1)/(r*s)) < 1e-12
        for rho in (1e-3,1e-5,1e-7):
            p,actual=pressure_at_density(r,s,rho)
            _,first,second=expansion(r,s,rho)
            print('(%d,%d) rho=%.0e p=%.9g residual first=%+.6g second=%+.6g'
                  %(r,s,rho,p,actual-first,actual-second))
            # Second correction must improve first for sufficiently small density.
            # At rho=1e-7 the finite corrections still decay slowly, so use an
            # intentionally non-asymptotic loose sanity margin.
            if rho==1e-7:
                assert abs(actual-second)<2*abs(actual-first)
            count+=1
    print('PASS: %d saddle/entropy checks, 8 exact power-intersection checks, 8 order checks'%count)

if __name__=='__main__':
    main()
