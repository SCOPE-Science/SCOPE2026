#!/usr/bin/env python3
"""Exact rational and independent-stage checks for periodic RK4 heat positivity."""
from fractions import Fraction as F
from math import factorial

checks = 0

def check(b, label="assertion"):
    global checks
    checks += 1
    if not b:
        raise AssertionError(label)


def coefficients(t):
    return [
        (35*t**4-40*t**3+36*t**2-24*t+12)/12,
        t*(6-12*t+15*t**2-14*t**3)/6,
        t*t*(3-6*t+7*t*t)/6,
        t**3*(1-2*t)/6,
        t**4/24,
    ]


def kernel(n, t):
    a = coefficients(t)
    return [sum((a[abs(j)] for j in range(-4, 5) if j % n == i), F(0)) for i in range(n)]


def L(v):
    n = len(v)
    return [v[(i-1) % n] + v[(i+1) % n] - 2*v[i] for i in range(n)]


def rk4_basis(n,t):
    v = [F(int(i == 0)) for i in range(n)]
    def add(x,y,alpha): return [xj+alpha*yj for xj,yj in zip(x,y)]
    k1=L(v)
    k2=L(add(v,k1,t/2))
    k3=L(add(v,k2,t/2))
    k4=L(add(v,k3,t))
    return [v[i]+t*(k1[i]+2*k2[i]+2*k3[i]+k4[i])/6 for i in range(n)]


def g(n,t):
    if n == 3: return 9*t**3-12*t*t+12*t-8
    if n == 4: return 8*t**3-8*t*t+6*t-3
    if n == 5: return 55*t**3-60*t*t+48*t-24
    raise ValueError(n)


def brack(n, digits=15):
    lo,hi=F(0),F(1)
    for _ in range(digits*5):
        mid=(lo+hi)/2
        if g(n,mid)<0: lo=mid
        else: hi=mid
    return lo,hi

# Independently evaluate the RK4 Butcher stages against Fourier-shift expansion.
for n in range(3,31):
    for t in [F(0), F(1,20), F(1,4), F(1,2), F(4,7), F(2,3), F(7,10), F(3,4), F(1), F(5,4), F(2), F(3)]:
        kern=kernel(n,t)
        stage=rk4_basis(n,t)
        for k,(x,y) in enumerate(zip(kern,stage)):
            check(x==y, f'RK4 kernel n={n} t={t} j={k}')
            check(x==kern[(n-k)%n], 'symmetric kernel')
        check(sum(kern)==1, 'mass conservation')

# All display identities, exact rather than float comparisons.
for t in [F(i,48) for i in range(161)]:
    a=coefficients(t)
    check(a[0] + 2*(a[1]+a[2]+a[3]+a[4])==1)
    check(a[2]>0 if t else a[2]==0)
    check(a[4]>=0)
    check(kernel(3,t)[0]==(3*t*t+2)*(3*t*t-4*t+2)/4)
    check(kernel(3,t)[1]==-t*g(3,t)/8)
    check(kernel(4,t)[1]==-t*g(4,t)/3)
    check(kernel(4,t)[2]==t*t*(7*t*t-6*t+3)/3)
    check(kernel(5,t)[1]==-t*g(5,t)/24)
    check(kernel(5,t)[2]==t*t*(5*t*t-5*t+3)/6)
    check(kernel(6,t)[3]==t**3*(1-2*t)/3)
    check(kernel(7,t)[3]==t**3*(4-7*t)/24)
    check(kernel(8,t)[3]==t**3*(1-2*t)/6)

# The monotone cubic isolators are exact fractions.
for n in [3,4,5]:
    lo,hi=brack(n)
    check(g(n,lo)<0<g(n,hi))
    check(hi-lo < F(1,10**15))
    print(f'cycle {n}: threshold in [{float(lo):.15f},{float(hi):.15f}]')

for n in [6,7,8,9,12,21]:
    c=F(4,7) if n==7 else F(1,2)
    for t in [F(1,20),F(1,4),c]:
        check(all(x>=0 for x in kernel(n,t)), f'positive through cutoff n={n} t={t}')
    for t in [c+F(1,1000), c+F(1,10), F(2)]:
        check(any(x<0 for x in kernel(n,t)), f'negative after cutoff n={n} t={t}')

# Strict nonmonotonicity at n=4 to 5 and 6 to 7.
lo4,hi4=brack(4)
lo5,hi5=brack(5)
check(hi4<lo5)
check(F(1,2)<F(4,7))
check(hi5<F(3,4))

# Stability radius polynomial has unique positive root, with a strict gap.
def p(t): return t**3-4*t*t+12*t-24
check(p(F(11,4))<0 and p(F(14,5))>0)
check(F(11,4)/4>F(4,7))
print(f'VERIFICATION_OK {checks} exact-rational assertions')
