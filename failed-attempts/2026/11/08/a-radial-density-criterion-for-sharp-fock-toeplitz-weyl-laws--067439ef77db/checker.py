"""Finite checks for a radial weighted-Fock Toeplitz Weyl criterion.
Standard library only. This checks numerical integral identities and explicit
geometric examples; the infinite-dimensional proof is in RESULT.md.
"""
import math

COUNT = 0

def check(condition, description):
    global COUNT
    if not condition:
        raise AssertionError(description)
    COUNT += 1


def potential(r, kind, c=1.0):
    if kind == 'quadratic':
        return 0.5 * c * r*r
    u = math.log1p(r*r)
    return 0.5 * r*r * (1.0 + 0.1*math.sin(u))


def radial_slope(r, kind, c=1.0):
    if kind == 'quadratic':
        return c
    v = r*r/(1.0+r*r)
    u = math.log1p(r*r)
    return 1.0 + 0.1*(math.sin(u)+v*math.cos(u))


def radial_curvature(r, kind, c=1.0):
    if kind == 'quadratic':
        return c
    v = r*r/(1.0+r*r)
    u = math.log1p(r*r)
    return 1.0 + 0.1*((1.0-2*v*v)*math.sin(u)+(5*v-2*v*v)*math.cos(u))


def mode(k, d, kind, c=1.0):
    q = k+d-0.5
    lo, hi = 0.0, 2*math.sqrt(q/0.5)
    for _ in range(90):
        mid = (lo+hi)*0.5
        if mid*mid*radial_slope(mid,kind,c) < q:
            lo = mid
        else:
            hi = mid
    return (lo+hi)*0.5


def radial_eigenvalue(k,d,beta,kind,c=1.0):
    rho = mode(k,d,kind,c)
    lo, hi = max(1e-9,rho-15), rho+15
    num_steps = 2400
    step = (hi-lo)/num_steps
    height = (2*k+2*d-1)*math.log(rho)-2*potential(rho,kind,c)
    sums = [0.0,0.0]
    for i in range(num_steps+1):
        r = lo+i*step
        logmass = (2*k+2*d-1)*math.log(r)-2*potential(r,kind,c)-height
        weight = (1 if i in (0,num_steps) else (4 if i%2 else 2))*math.exp(logmass)
        sums[0] += weight
        sums[1] += weight * (1+r*r)**(-beta/2)
    return sums[1]/sums[0],rho


def main():
    for d in (1,2,3,5):
        for k in (0,1,2,6,20):
            mult = math.comb(k+d-1,d-1)
            check(math.comb(k+d,d)-math.comb(k+d-1,d)==mult, 'multiplicity')
    for r in (0,0.01,0.1,1,2,5,10,50,500):
        check(.6 <= radial_slope(r,'periodic') <= 1.4, 'tangential Hessian bound')
        check(.6 <= radial_curvature(r,'periodic') <= 1.4, 'radial Hessian bound')
    for kind,c in (('quadratic',1),('quadratic',1.75),('periodic',1)):
        for d in (1,2,3):
            previous=1.1
            for k in (100,400,1600):
                eig,rho=radial_eigenvalue(k,d,1.6,kind,c)
                check(eig < previous, 'radial eigenvalues strictly decreasing')
                check(abs((k+d-0.5)-rho*rho*radial_slope(rho,kind,c))<1e-10,
                      'mode exact equation')
                # Relative Gaussian localization to symbol value at the saddle.
                saddle=(1+rho*rho)**(-0.8)
                check(abs(eig/saddle-1) < 0.055, 'Laplace localization')
                # Direct dimension-free normalized level asymptotic, with 5% margin.
                asym=(k**0.8)*eig
                geom=radial_slope(rho,kind,c)**0.8
                check(abs(asym/geom-1)<0.055, 'geometric eigenvalue coefficient')
                previous=eig
    for d in (1,2,3,4,6):
        for k in (50,100,200,500):
            high=math.comb(k+d,d)
            low=math.comb(k+d-1,d)
            check(low < high, 'degree blocks')
            check(abs(math.factorial(d)*high/k**d-1)<(d*(d+1)+1)/k,
                  'cumulative multiplicity growth')
    eps=.1
    check(1-eps*math.sqrt(2)>.6,'periodic lower cluster')
    check(1+eps*math.sqrt(2)<1.4,'periodic upper cluster')
    print('RADIAL_FOCK_GEOMETRY_CHECK_OK',COUNT,'finite assertions; analytic proof separate')

if __name__=='__main__': main()
