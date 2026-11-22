"""Supplementary finite-case checks for a sharp Walsh synthesis formula.

Only standard-library modules are required. The universal theorem uses
analytic character orthogonality and strict convexity, not these tests.
"""
from fractions import Fraction as Q
from math import comb


def moment_formulas(m):
    n = comb(m, 2)
    return n, 6 * comb(m, 3), 3 * n*n - 2*n + 72*comb(m, 4)


def orbit_value(m, u):
    n = comb(m, 2)
    return sum(Q(comb(m, j), 2**m) *
               (1-u+u*Q((m-2*j)**2-m, m*(m-1)))**4
               for j in range(m+1))


def direct_value(m, u):
    d = m-1
    n = comb(m, 2)
    b = u/n
    a = 1-u
    f = {0: a}
    for x in range(1, 2**d):
        if x.bit_count() <= 2:
            f[x] = b
    values=[]
    for xi in range(2**d):
        F = sum(v * (-1 if (x & xi).bit_count() % 2 else 1)
                for x, v in f.items())
        values.append(F**4)
    return sum(values, Q(0))/2**d


def root_u(m):
    n=comb(m,2)
    t=[((m-2*j)**2-m)/(m*(m-1)) for j in range(m+1)]
    w=[comb(m,j)*2.0**(-m) for j in range(m+1)]
    def grad(z):
        return sum(wj*(1-tj)*(1-z+z*tj)**3 for wj,tj in zip(w,t))
    low, high = 0., 4.
    assert grad(low)>0 and grad(high)<0
    for _ in range(90):
        mid=(low+high)/2
        if grad(mid)>0: low=mid
        else: high=mid
    return (low+high)/2


def check():
    tests = 0
    for m in range(2,10):
        n, third, fourth = moment_formulas(m)
        moments=[0,0,0]
        for bits in range(2**m):
            s=m-2*bits.bit_count()
            E=(s*s-m)//2
            moments[0]+=E*E
            moments[1]+=E**3
            moments[2]+=E**4
        assert moments==[2**m*n,2**m*third,2**m*fourth]
        tests+=3
        for u in [Q(0), Q(1,3), Q(2,3), Q(1)]:
            assert direct_value(m,u)==orbit_value(m,u)
            tests+=1
    for m in range(3,80):
        p=2*m**3-21*m*m+67*m-68
        u=root_u(m)
        if m<=5: assert u<1-1e-8 and p<0
        else: assert u>1+1e-8 and p>0
        tests+=2
    assert abs(root_u(4)-Q(6,7))<1e-10
    tests+=1
    v=1.1071475644353317
    for m in [64,128,256]:
        u=root_u(m)
        assert abs((u-1)*m-v)<0.08
        tests+=1
    print('PASS:',tests,'exact or numerical supplementary checks')

if __name__=='__main__':
    check()
