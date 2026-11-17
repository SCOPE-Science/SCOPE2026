"""Independent numerical checks of the trace-slice 2x2 Hermitian modulus formulas.
No packages outside the Python standard library are required. The proof is analytic.
"""
from decimal import Decimal, getcontext
from random import Random

getcontext().prec = 75
D = Decimal
ZERO = D(0)
ONE = D(1)
TWO = D(2)
ROOT_TWO = TWO.sqrt()

def rnorm(v):
    return sum((x * x for x in v), ZERO).sqrt()

def output(a, v):
    r = rnorm(v)
    if r <= abs(a):
        sign = ONE if a > 0 else -ONE if a < 0 else ZERO
        return abs(a), tuple(sign * x for x in v)
    return r, tuple((a / r) * x for x in v)

def mat_norm(pair):
    return abs(pair[0]) + rnorm(pair[1])

def diff_norm(p, q):
    return mat_norm((p[0]-q[0], tuple(x-y for x, y in zip(p[1], q[1]))))

def ratio(a, v, w):
    return diff_norm(output(a, v), output(a, w)) / rnorm(tuple(x-y for x,y in zip(v,w)))

# Exact structural checks, in which algebra has only rational operations.
for a in [D('-1'), D('-0.5'), ZERO, D('0.5'), ONE]:
    for z in [D('0'), D('0.2'), D('2.5')]:
        v = (z, ZERO, ZERO)
        s,q=output(a,v)
        if z <= abs(a):
            assert s == abs(a)
            assert q == tuple((ONE if a>0 else -ONE if a<0 else ZERO)*x for x in v)
        elif a == 0:
            assert q == (ZERO, ZERO, ZERO)

rng=Random(2411)
count=0
for a in [ZERO, D('0.5'), D('-0.5'), D('1')]:
    for _ in range(4000):
        v = tuple(D(str(rng.uniform(-3,3))) for _ in range(3))
        w = tuple(D(str(rng.uniform(-3,3))) for _ in range(3))
        gain=ratio(a,v,w)
        assert gain <= (ONE if a==ZERO else ROOT_TWO) + D('1e-55'), (a,v,w,gain)
        count+=1
print('RANDOM_GLOBAL_BOUND_CHECKS_PASS',count)

assert ratio(ZERO, (ONE,ZERO,ZERO), (ZERO,ZERO,ZERO)) == ONE
print('TRACE_ZERO_EXACT_ATTAINMENT_PASS')

previous=ZERO
for exponent in [1,2,3,4,5,6,7,8,9]:
    eps = ONE / (D(10) ** exponent)
    step = eps ** 2
    a = D('0.5')
    r = a + eps
    v=(ZERO,ZERO,r)
    w=(step,ZERO,r+step)
    measured=ratio(a,v,w)
    derivative=(ONE + a/r) / ROOT_TWO
    assert measured < ROOT_TWO and measured > previous, (eps, measured,previous)
    assert abs(measured - derivative) < D('5')*step/eps, (eps, measured,derivative)
    previous=measured
    print('NEAR_BOUNDARY_WITNESS',str(eps),'gain',str(measured)[:28])

for a,r in [(D('0.5'),D('1')),(D('1'),D('2')),(D('-0.5'),D('2'))]:
    local=(ONE+(a/r)**2).sqrt()
    assert ONE < local < ROOT_TWO
    # The analytically optimal trace-preserving direction has
    # parallel/perpendicular components in the proportions r:|a|.
    parallel=ONE
    perp=abs(a)/r
    actual=(parallel+abs(a)/r*perp) / (parallel**2+perp**2).sqrt()
    assert abs(actual-local) < D('1e-60')
print('LOCAL_OPERATOR_NORM_PROFILE_PASS')
print('ALL_TRACE_SLICE_MODULUS_CHECKS_PASS')
