"""Standalone finite consistency checks for cyclic exponentially tapered Gabor bounds.
Run with python3 CHECK.py; standard library only. Finite checks supplement the proof.
"""
import cmath
import math
from fractions import Fraction


def block(m, r, j):
    """Direct two-translation Gram block on paired coordinates."""
    n = 2 * m
    def g(t):
        t %= n
        return r ** min(t, n - t)
    i, k = j, j + m
    u = (g(i), g(k))
    v = (g(i - 1), g(k - 1))
    return (u[0]**2 + v[0]**2,
            u[0]*u[1] + v[0]*v[1],
            u[1]**2 + v[1]**2)


def formula(m, r):
    a = m - 1
    d = r**(2*a) * (1-r*r)**2
    t = (1+r*r)*(1+r**(2*a))
    discr = math.sqrt((t-2*math.sqrt(d))*(t+2*math.sqrt(d)))
    low = m*2*d/(t+discr) # m*(t-discr)/2, stabilized
    high = m*(t+discr)/2
    return low, high


def exact_formula(m, r):
    """Exact rational checks on all 2-by-2 determinants/traces."""
    rr = Fraction(r)
    rows = [block(m, rr, j) for j in range(m)]
    d = rr**(2*m-2) * (1-rr*rr)**2
    tmax = (1+rr*rr)*(1+rr**(2*m-2))
    for j, (aa, bb, cc) in enumerate(rows):
        assert aa*cc-bb*bb == d, ('det',m, r, j)
        assert aa+cc <= tmax, ('trace',m, r, j)
    assert rows[0] == rows[1]


def dense_check(m, r):
    """Construct every Gabor atom independently from the block formula."""
    n = 2*m
    g = [r**min(j,n-j) for j in range(n)]
    atoms = []
    for shift in (0,1):
        for a in range(m):
            atoms.append([cmath.exp(2j*math.pi*a*j/m)*g[(j-shift)%n]
                          for j in range(n)])
    actual = [[sum(atom[j]*atom[k].conjugate() for atom in atoms)
               for k in range(n)] for j in range(n)]
    maxerr = 0.0
    for j in range(n):
        for k in range(n):
            same = (j % m == k % m)
            if same:
                aa, bb, cc = block(m, r, j % m)
                target = m * (aa if j < m and k < m else
                              cc if j >= m and k >= m else bb)
            else:
                target = 0
            maxerr = max(maxerr, abs(actual[j][k] - target))
    assert maxerr < 2e-11 * n, (m, r, maxerr)
    aa, bb = formula(m, r)
    assert aa > 0 and aa < bb
    return maxerr


def taper_equation(a, s):
    return a*math.tanh(a*s)*math.sinh(2*s)-2


def root_optimum(m):
    a=m-1
    lo,hi=0.,1.
    while taper_equation(a,hi)<0:
        hi*=1.5
    for _ in range(95):
        mid=(lo+hi)/2
        if taper_equation(a,mid)>0: hi=mid
        else:lo=mid
    return (lo+hi)/2


def opt_condition(m,s):
    a=m-1
    x=2*math.cosh(a*s)/math.tanh(s)
    return ((x+math.sqrt(x*x-4))/2)**2


def check():
    count = 0
    for m in range(2,13):
        for r in (Fraction(1,5),Fraction(2,5),Fraction(3,5),Fraction(4,5)):
            exact_formula(m,r)
            count += 1
    print('Exact fraction determinant/trace certificates:',count)
    n_dense=0
    for m in range(2,13):
        for r in (0.17,0.41,0.68,0.91):
            dense_check(m,r)
            n_dense+=1
    print('Independent full synthesis-frame matrices:',n_dense)
    zlo,zhi=1.,2.
    for _ in range(100):
        z=(zlo+zhi)/2
        if z*math.tanh(z)>1: zhi=z
        else:zlo=z
    z=(zlo+zhi)/2
    constant=4/(z*z-1)
    for m in (2,3,4,5,7,12,23,100,1000,10000):
        s=root_optimum(m)
        assert taper_equation(m-1,s) < 1e-11
        eps=min(s/200,1e-4)
        assert opt_condition(m,s) < opt_condition(m,s-eps)
        assert opt_condition(m,s) < opt_condition(m,s+eps)
        if m>100:
            assert abs((m-1)*s-z)<.02
        print('m=%d s=%.13f kappa=%.9f normalized=%.9f'%
              (m,s,opt_condition(m,s),opt_condition(m,s)/(m-1)**2))
    assert abs(opt_condition(2,root_optimum(2))-(2+math.sqrt(3))**2)<1e-10
    assert abs(opt_condition(10000,root_optimum(10000))/9999**2/constant-1)<1e-5
    print('z*=%.13f; coefficient=%.13f; all tests PASS'%(z,constant))

if __name__=='__main__':
    check()
