"""Numerical cross-checks for the three-vertex sigmoidal opinion theorem.

Uses only standard-library Decimal arithmetic.  Infinite assertions are proved
in the accompanying mathematical argument, not established by sampling.
"""
from decimal import Decimal, getcontext

getcontext().prec = 72
D = Decimal
ONE = D(1)
TWO = D(2)
EPS = D('1e-56')


def cosh(z):
    return (z.exp() + (-z).exp()) / TWO


def sinh(z):
    return (z.exp() - (-z).exp()) / TWO


def tanh(z):
    return sinh(z) / cosh(z)


def Q(x):
    x = D(x)
    if x == 0:
        return ONE
    return (x*x).exp() * (sinh(TWO*x)/x - cosh(TWO*x))


def H(x):
    x = D(x)
    return TWO*x*(ONE-x*x) - tanh(TWO*x)


def w(s, delta):
    return ONE/(ONE + (s*s-delta).exp())


def direct(x, delta):
    a, b = w(ONE-x, delta), w(ONE+x, delta)
    return ((ONE-x)*a-(ONE+x)*b)/(a+b)


def reduced(x, delta):
    a = ONE + ((ONE-x)**2-delta).exp()
    b = ONE + ((ONE+x)**2-delta).exp()
    return TWO*x*((ONE-delta).exp()*Q(abs(x))-ONE)/(a+b)


def bisect(f, a, b, steps=220):
    assert f(a)*f(b) < 0, (a, b, f(a), f(b))
    sa = f(a)>0
    for _ in range(steps):
        c = (a+b)/TWO
        if (f(c)>0)==sa:
            a=c
        else:
            b=c
    return (a+b)/TWO


count = 0
m = bisect(H, D('0.1'), D('0.9'))
delta_star = ONE + Q(m).ln()
assert D('0.457314620422499') < m < D('0.457314620422501')
assert D('1.037743156221735') < delta_star < D('1.037743156221738')
assert Q(m) > 1 and Q(0) == 1 and Q(1) < 0
count += 5

# Two completely different evaluations of the original model's vector field.
for d in [D('0'), D('0.5'), D('1'), D('1.01'), D('1.02'), delta_star, D('1.05'), D('2.0')]:
    for i in range(-45,46):
        x=D(i)/D(40)
        err=abs(direct(x,d)-reduced(x,d))
        assert err < D('1e-57'), (d, x, err)
        count += 1

# Ground the four equilibrium regimes in the independently computed Q profile.
for delta, mode in [(D('0.5'),1),(ONE,1),(D('1.01'),2),(D('1.02'),2),(D('1.05'),0)]:
    v=(delta-ONE).exp()
    if mode==1:
        b=bisect(lambda x:Q(x)-v,m,ONE)
        assert m<b<ONE and Q(b)-v< D('1e-56') and Q(b)-v> -D('1e-56')
        assert direct(b-D('0.00001'),delta)>0
        assert direct(b+D('0.00001'),delta)<0
        count+=4
    if mode==2:
        a=bisect(lambda x:Q(x)-v,D('0'),m)
        b=bisect(lambda x:Q(x)-v,m,ONE)
        assert 0<a<m<b<1
        assert direct(a-D('0.00001'),delta)<0
        assert direct((a+b)/TWO,delta)>0
        assert direct(b+D('0.00001'),delta)<0
        count+=4
    if mode==0:
        for i in range(1,50):
            assert direct(D(i)/D(50),delta)<0
            count+=1

# The neutral boundary is cubic-repelling, and the saddle-node is semistable.
for x in [D('0.000001'), D('0.0000001')]:
    coeff=direct(x,ONE)/(x*x*x)
    assert abs(coeff-ONE/D(6)) < D('0.000000001')
    count+=1
for x in [m-D('0.001'),m+D('0.001')]:
    assert direct(x,delta_star)<0
    count+=1
for d in [D('0.99'),D('1.0'),D('1.01'),D('1.05')]:
    slope=((ONE-d).exp()-ONE)/((ONE-d).exp()+ONE)
    assert (slope>0)==(d<ONE) if d!=ONE else slope==0
    count+=1

print('VERIFY_OK', count, 'checks', 'm=',m, 'delta_star=',delta_star)
