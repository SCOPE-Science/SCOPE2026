"""Exact finite checks for a sharp subnormal-weighted-shift envelope.

Uses only the Python standard library. Infinite-dimensional assertions are
proved analytically in RESULT.md, not by these computations.
"""
from fractions import Fraction as F
from random import Random


def moments(atoms, probabilities, k):
    return sum((p * x**k for x, p in zip(atoms, probabilities)), F(0))


def extremals(m, s, R):
    if not (F(0) < m < R and m <= s <= R):
        raise ValueError('Parameters must satisfy 0 < m < R, m <= s <= R')
    a = m * (R - s) / (R - m)
    pi = (m - a) / (R - a)
    return a, pi


def upper(m, s, R, n):
    a, pi = extremals(m, s, R)
    return ((1-pi)*a**(n+1)+pi*R**(n+1))/((1-pi)*a**n+pi*R**n)


def h(degree, variables):
    # Complete homogeneous symmetric polynomial, calculated from its
    # generating series: product_j (1 - variables[j] * t)^(-1).
    if degree < 0:
        return F(0)
    coeff = [F(1)] + [F(0)]*degree
    for v in variables:
        for k in range(1, degree+1):
            coeff[k] += v*coeff[k-1]
    return coeff[degree]


def evaluate_f(x, n, c):
    return x**(n+1) - c*x**n


def certificate_q(t, a, R, n, c):
    # Quadratic Hermite interpolant through (a, f(a)), (a, f'(a)),
    # and (R, f(R)).
    fa = evaluate_f(a,n,c)
    da = (n+1)*a**n - c*n*a**(n-1)
    d = R-a
    K = (evaluate_f(R,n,c)-fa-da*d)/d**2
    return fa+da*(t-a)+K*(t-a)**2


def run():
    count = 0
    rng = Random(20261028)
    for _ in range(600):
        R=F(rng.randint(2,15),rng.randint(1,9))
        atoms=[R*F(rng.randint(0,100),100) for _ in range(rng.randint(2,7))]
        weights=[rng.randint(1,40) for x in atoms]
        denom=sum(weights)
        p=[F(w,denom) for w in weights]
        m=moments(atoms,p,1)
        if m==0 or m==R: continue
        s=moments(atoms,p,2)/m
        a,pi=extremals(m,s,R)
        count+=1; assert F(0)<=a<=m and F(0)<=pi<=1
        count+=1; assert (1-pi)*a+pi*R==m
        count+=1; assert (1-pi)*a*a+pi*R*R==m*s
        for n in range(1,13):
            z=moments(atoms,p,n+1)/moments(atoms,p,n)
            lo=s; hi=upper(m,s,R,n)
            count+=2; assert lo<=z and z<=hi,(m,s,R,n,z,hi)
            count+=1; assert hi==((1-pi)*a**(n+1)+pi*R**(n+1))/((1-pi)*a**n+pi*R**n)
            if n>=2:
                c=hi
                count+=1; assert (1-pi)*evaluate_f(a,n,c)+pi*evaluate_f(R,n,c)==0
                for t in (F(0),a,R,m,F(2,3)*R):
                    dif=certificate_q(t,a,R,n,c)-evaluate_f(t,n,c)
                    divided=h(n-2,(a,a,t))+(R-c)*h(n-3,(a,a,R,t))
                    count+=2; assert dif == (t-a)**2*(R-t)*divided, (dif,divided)
                    assert dif>=0
    for _ in range(120):
        R=F(1)
        m=F(rng.randint(1,25),100)
        delta=F(rng.randint(1,100-int(100*m)),100)
        s=m+delta
        a,pi=extremals(m,s,R)
        # Lower extremizer {0,s}, upper extremizer {a,R}.
        p0=m/s
        for n in range(1,15):
            count+=1; assert (p0*s**(n+1))/(p0*s**n)==s
            count+=1; assert upper(m,s,R,n)==((1-pi)*a**(n+1)+pi*R**(n+1))/((1-pi)*a**n+pi*R**n)
    return count

if __name__=='__main__':
    print('PASS',run(),'exact rational assertions')
