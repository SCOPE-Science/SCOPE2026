"""Reproduce determinant identities for nested spherical Fourier interpolation.
Uses only Python's standard library. Numeric checks supplement the analytic proof.
"""
import cmath
import math
import random
from fractions import Fraction

NTEST = 0

def check(assertion, reason):
    global NTEST
    assert assertion, reason
    NTEST += 1

def legendre_derivative(ell, m, x):
    total = 0.0
    for j in range(ell // 2 + 1):
        power = ell - 2*j
        if power < m:
            continue
        coeff = ((-1)**j * math.factorial(2*ell-2*j) /
                 (2**ell * math.factorial(j) * math.factorial(ell-j) *
                  math.factorial(ell-2*j)))
        total += (coeff * math.factorial(power) /
                  math.factorial(power-m) * x**(power-m))
    return total

def spherical_harmonic(ell, m, x, phi):
    if m < 0:
        return (-1)**(-m)*spherical_harmonic(ell, -m, x, phi).conjugate()
    norm = math.sqrt((2*ell+1)/(4*math.pi)*
                     math.factorial(ell-m)/math.factorial(ell+m))
    return ((-1)**m*norm*max(0,1-x*x)**(m/2)*
            legendre_derivative(ell,m,x)*cmath.exp(1j*m*phi))

def abs_det(matrix):
    a = [list(row) for row in matrix]
    size = len(a)
    determinant = 1+0j
    for k in range(size):
        pivot = max(range(k, size), key=lambda i: abs(a[i][k]))
        if abs(a[pivot][k]) < 1e-14:
            return 0.0
        if pivot != k:
            a[pivot], a[k] = a[k], a[pivot]
            determinant = -determinant
        c = a[k][k]
        determinant *= c
        for i in range(k+1, size):
            fac = a[i][k] / c
            for j in range(k+1,size):
                a[i][j] -= fac*a[k][j]
            a[i][k] = 0j
    return abs(determinant)

def leading(ell, m):
    return (math.sqrt((2*ell+1)/(4*math.pi)) *
            math.factorial(2*ell)/
            (2**ell * math.factorial(ell)*
             math.sqrt(math.factorial(ell-m)*math.factorial(ell+m))))

def K(L):
    out = math.prod((2*k+1)**((2*k+1)/2) for k in range(L))
    out *= math.prod(leading(ell,0) for ell in range(L))
    for m in range(1,L):
        out *= math.prod(leading(ell,m)**2 for ell in range(m,L))
    return out

def predicted_det(L, xs):
    full = [-1.0] + list(xs)
    out = K(L)
    for k in range(1,L):
        out *= (1-full[k]**2)**(k*(k+1)/2)
    for i in range(L):
        for j in range(i+1,L):
            out *= abs(full[j]-full[i])**(2*i+1)
    return out

def numerical_det(L, xs, offsets):
    points = [(-1., 0.)]
    for k in range(1,L):
        points += [(xs[k-1], offsets[k-1]+2*math.pi*j/(2*k+1))
                   for j in range(2*k+1)]
    modes = [(ell,m) for ell in range(L) for m in range(-ell,ell+1)]
    return abs_det([[spherical_harmonic(ell,m,x,phi) for ell,m in modes]
                    for x,phi in points])

def exact_pair(a=0,b=0):
    return (Fraction(a), Fraction(b))

def plus(x,y):
    return (x[0]+y[0], x[1]+y[1])

def neg(x):
    return (-x[0],-x[1])

def minus(x,y):
    return plus(x,neg(y))

def times(x,y):
    return (x[0]*y[0]+2305*x[1]*y[1], x[0]*y[1]+x[1]*y[0])

def product(*values):
    z = exact_pair(1)
    for value in values:
        z = times(z,value)
    return z

def power(x,n):
    return product(*([x]*n))

def p(u,v):
    return plus(plus(neg(times(exact_pair(6),power(u,2))), times(exact_pair(3),times(u,v))),
                plus(minus(u,v),exact_pair(3)))

def q(u,v):
    return plus(plus(times(exact_pair(7),times(u,v)), minus(v,u)),
                plus(neg(times(exact_pair(10),power(v,2))),exact_pair(3)))

def F(u,v):
    one=exact_pair(1)
    return product(minus(one,u), power(plus(one,u),2),power(minus(one,v),3),
                   power(plus(one,v),4),power(minus(u,v),3))

def main():
    root = math.sqrt(2305)
    uhi,vlo = (11+root)/78, (15-root)/130
    ulo,vhi = (11-root)/78, (15+root)/130
    up = (Fraction(11,78),Fraction(1,78))
    vp = (Fraction(15,130),Fraction(-1,130))
    um = (Fraction(11,78),Fraction(-1,78))
    vm = (Fraction(15,130),Fraction(1,130))
    for u,v in [(up,vp),(um,vm)]:
        check(p(u,v)==exact_pair(), 'exact first stationarity')
        check(q(u,v)==exact_pair(), 'exact second stationarity')
    check(plus(F(up,vp),F(um,vm)) ==
          exact_pair(Fraction(5992816136935869152,25555087118721346875)),
          'exact positive branch advantage')
    check(uhi>vlo and ulo<vhi and all(-1<t<1 for t in (uhi,vlo,ulo,vhi)),
          'critical latitude chambers')
    check(abs(K(3)-2278125/(32768*math.pi**4.5))<1e-12,
          'closed constant K3')
    check(predicted_det(3,[uhi,vlo])>predicted_det(3,[ulo,vhi]),
          'global chamber comparison')
    rng=random.Random(261116441)
    for L in range(2,6):
        for trial in range(8):
            xs=[rng.uniform(-0.9,0.9) for _ in range(1,L)]
            if trial%2:
                xs.sort(reverse=True)
            phases=[rng.uniform(0,2*math.pi) for _ in xs]
            d1=numerical_det(L,xs,phases)
            d2=predicted_det(L,xs)
            check(abs(d1-d2)/max(d2,1e-15)<3e-7,
                  'complex matrix determinant versus factorization for L=%d'%L)
        if L>2:
            xs=[rng.uniform(-0.7,0.7) for _ in range(1,L)]
            d1=numerical_det(L,xs,[0.]*(L-1))
            d2=numerical_det(L,xs,[.37]*(L-1))
            check(abs(d1-d2)/max(d2,1e-15)<2e-7,
                  'phase independence')
    print('PASS: %d exact and numerical assertions'%NTEST)
    print('L=3 optimum cos(colatitudes) =',uhi,vlo)
    print('L=3 determinant relative to equiangular placement =',
          predicted_det(3,[uhi,vlo])/
          predicted_det(3,[math.cos(math.pi/5),math.cos(3*math.pi/5)]))

if __name__=='__main__':
    main()
