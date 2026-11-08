"""Exact-rational checks for triangular-indicator jittered quadrature.

Run with Python 3: python verify.py. No dependencies outside the standard library.
The analytic infinite statements are proved separately, not by this finite checker.
"""
from fractions import Fraction as F
from math import gcd

checks = 0

def check(condition, msg):
    global checks
    assert condition, msg
    checks += 1


def cell_phases(alpha, i):
    q = (alpha * i) % 1
    if q <= 1 - alpha:
        p = q + alpha / 2
        return (p,)
    t = 1 - q
    return (1 - t*t/(2*alpha), (alpha-t)**2/(2*alpha))


def variance_phase(alpha, q):
    if q <= 1 - alpha:
        p = q + alpha / 2
        return p*(1-p)
    t = 1-q
    p0 = 1-t*t/(2*alpha)
    p1 = (alpha-t)**2/(2*alpha)
    return p0*(1-p0) + p1*(1-p1)


def finite_sum(alpha, n):
    return sum((variance_phase(alpha, (alpha*i) % 1) for i in range(n)), F(0)) / n**4


def exact_coefficient(a, b):
    z = F(a,b)
    return F(1,6)+z*z/12-z*z*z/60+F(1,60*a*b**3)


def halfplane_cell_area(alpha, i, j):
    # Independent polygon clipping of each unit-scaled grid square, for y <= alpha*x.
    poly = [(F(i),F(j)),(F(i+1),F(j)),(F(i+1),F(j+1)),(F(i),F(j+1))]
    def signed(p):
        return alpha*p[0]-p[1]
    new = []
    for ix in range(len(poly)):
        p, q = poly[ix-1],poly[ix]
        dp,dq = signed(p),signed(q)
        if (dp < 0 and dq > 0) or (dp > 0 and dq < 0):
            u = dp/(dp-dq)
            new.append((p[0]+u*(q[0]-p[0]), p[1]+u*(q[1]-p[1])))
        elif dp == 0 and dq != 0:
            new.append(p)
        if dq >= 0:
            new.append(q)
    if len(new) < 3:
        return F(0)
    return abs(sum((new[k][0]*new[(k+1)%len(new)][1] - new[k][1]*new[(k+1)%len(new)][0] for k in range(len(new))),F(0)))/2


def direct_geometry(alpha,n):
    var=F(0)
    mean=F(0)
    for i in range(n):
        for j in range(n):
            p=halfplane_cell_area(alpha,i,j)
            check(F(0)<=p<=F(1),f'area bounds {alpha=} {i=} {j=} {p=}')
            mean+=p
            var+=p*(1-p)
    return mean/n**2, var/n**4

for b in range(1,36):
    for a in range(1,b+1):
        if gcd(a,b)!=1: continue
        alpha=F(a,b)
        expected=exact_coefficient(a,b)
        avg=sum((variance_phase(alpha,F(r,b)) for r in range(b)),F(0))/b
        check(avg==expected,f'period coefficient {a}/{b}: {avg} != {expected}')
        for k in range(1,4):
            n=k*b
            check(finite_sum(alpha,n)*n**3==expected,f'grid period exact {a}/{b}, {n}')
        for n in (1,2,3,5,9,20):
            if n > 2*b and n != 20: continue
            var=finite_sum(alpha,n)
            check(F(0)<=var<=F(1,4*n**3), f'positive variance and simple bound {a}/{b} {n}')
            for i in range(min(n,10)):
                check(sum(cell_phases(alpha,i), F(0)) <= 2, 'phase means bounded')

# Independent geometric checks; no use of the phase formula to calculate cell areas.
for b in range(1,10):
    for a in range(1,b+1):
        if gcd(a,b)!=1: continue
        alpha=F(a,b)
        for n in range(1,10):
            exact_mean, geom_var=direct_geometry(alpha,n)
            check(exact_mean==alpha/2,f'unbiased geometry {a}/{b}, n={n}')
            check(geom_var==finite_sum(alpha,n),f'variance geometry {a}/{b}, n={n}')

# Boundary cases and independently evaluated benchmark.
check(exact_coefficient(1,1)==F(1,4),'diagonal coefficient')
check(exact_coefficient(1,2)==F(3,16),'slope 1/2 coefficient')
check(exact_coefficient(2,3)==F(43,216),'slope 2/3 coefficient')
check(exact_coefficient(1,3)==F(19,108),'slope 1/3 coefficient')
print(f'PASS: {checks} exact-rational assertions.')
print('Examples: slope 1 -> 1/4; 1/2 -> 3/16; 2/3 -> 43/216; 1/3 -> 19/108.')
print('The irrational-slope coefficient and continuity proof use Weyl equidistribution, not finite checking.')
