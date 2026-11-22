"""Numerical and exact-rational checks for a star normalized-adjacency sensitivity formula.

This code verifies examples, elementary certificates and finite tests. It is
not a substitute for the analytic all-dimensional proof in RESULT.md.
"""
import math
import random
from fractions import Fraction


def g(m, x):
    return (m-1)*(x+1)/(2*math.sqrt(x)*(x+m-1)**1.5)


def exact_constant(m, a=1.0):
    if m == 1:
        return 0.0
    if m <= 18:
        return (m-1)/(m**1.5*a)
    root = (m-5+math.sqrt(m*m-18*m+33))/4
    return g(m, root)/a


def derivative_row_sum(weights, i):
    W = sum(weights)
    x = weights[i]
    return (W+(len(weights)-2)*x)/(2*math.sqrt(x)*W**1.5)


def normalized_star(weights):
    W = sum(weights)
    return [math.sqrt(w/W) for w in weights]


def derivative(weights, h):
    W = sum(weights)
    dh = sum(h)
    return [(h[i]-weights[i]*dh/W)/(2*math.sqrt(weights[i]*W))
            for i in range(len(weights))]


def exact_poly_certificates():
    # 4*x*(x+17)^3 - 18^3*(x+1)^2 =
    # 4*(x-1)*(x^3+52*x^2-539*x+1458).
    # The cubic is nonnegative on x>=1 by explicit SOS decomposition.
    for k in range(1, 80):
        x = Fraction(k, 7)
        cub = x**3+52*x*x-539*x+1458
        sos = (x-Fraction(19,4))**2*(x+Fraction(123,2)) + Fraction(363,16)*x + Fraction(2253,32)
        assert cub == sos
        lhs = 4*x*(x+17)**3-18**3*(x+1)**2
        assert lhs == 4*(x-1)*cub
        if x>=1:
            assert lhs>=0
    # The following rational strict witness proves nonuniformity by m=19.
    assert 4*4*(4+18)**3 - 19**3*(4+1)**2 == -1107


def run():
    random.seed(230734)
    exact_poly_certificates()
    assertions = 1
    for m in list(range(2, 55))+[60,80,100,250]:
        K = exact_constant(m)
        for _ in range(120):
            weights = [math.exp(random.uniform(0, 7)) for _ in range(m)]
            i = random.randrange(m)
            d = derivative_row_sum(weights, i)
            assert d <= K+5e-12,(m,i,d,K)
            assertions += 1
        if m <= 18:
            assert abs(g(m, 1)-K) < 1e-12
        else:
            x=(m-5+math.sqrt(m*m-18*m+33))/4
            assert abs(g(m,x)-K)<1e-12
            assert g(m,x)>g(m,1)
        assertions+=1
    # Exact Jacobian versus finite differences and direct sign extremization.
    for m in [2,3,4,12,18,19,20,35,50]:
        for _ in range(250):
            weights=[random.uniform(1.5, 25.0) for _ in range(m)]
            h=[random.choice([-1.0,1.0]) for _ in range(m)]
            i=random.randrange(m)
            eps=2e-6
            fd=(normalized_star([w+eps*t for w,t in zip(weights,h)])[i]-normalized_star(weights)[i])/eps
            jac=derivative(weights,h)[i]
            assert abs(fd-jac)<1.2e-6,(m,fd,jac)
            assert abs(jac)<=derivative_row_sum(weights,i)+1e-13
            assertions+=2
    # Finite pairs: the global Lipschitz estimate, not only differential.
    for m in [2,3,5,18,19,25,50]:
        K=exact_constant(m)
        for _ in range(400):
            v=[random.uniform(1.0, 200.0) for _ in range(m)]
            w=[max(1., z+random.uniform(-3,3)) for z in v]
            if max(abs(z-t) for z,t in zip(w,v))==0:continue
            ratio=max(abs(x-y) for x,y in zip(normalized_star(w),normalized_star(v)))/max(abs(x-y) for x,y in zip(w,v))
            assert ratio<=K+1e-12,(m,ratio,K)
            assertions+=1
    for m in [100,1000,10000,100000]:
        assert abs(exact_constant(m)-1/(3*math.sqrt(3))) < 0.02
        assertions+=1
    print('PASS',assertions,'supplementary checks')
    for m in [3,18,19,20,50,100,1000]:
        x=1 if m<=18 else (m-5+math.sqrt(m*m-18*m+33))/4
        print(f'm={m}, extremal heavy-to-floor ratio={x:.8f}, sharp coefficient for a=1: {exact_constant(m):.12f}')

if __name__=='__main__':
    run()
