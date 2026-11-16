"""Reproducible finite checks for midpoint evaluation on three-frequency spaces.
The global uniqueness inequalities are proved in RESULT.md, not by this script.
Only Python standard library is required.
"""
import cmath
import math
import random


def sinc(x):
    return math.sin(x) / x if x else 1.0


def numbers(w):
    s = sinc(w)
    c = math.cos(w)
    v = 1.0 + s*c - 2.0*s*s
    return s, c, v


def kernel(w, t):
    s, c, v = numbers(w)
    return 1.0 + 2.0*(1.0-s)/v*(math.cos(w*t)-s)


def leverage(w):
    s, c, v = numbers(w)
    return 1.0 + 2.0*(1.0-s)**2/v


def derivative_sign(w):
    s, c, v = numbers(w)
    return 1.0-2*c*c-2*c+(5*c+1)*s+(c-4)*s*s


def integrate_avg(f, n=1000):
    # Simpson rule on [-1,1] (n even)
    h = 2.0/n
    return h/6*(f(-1)+f(1)+4*sum(f(-1+j*h) for j in range(1,n,2))+2*sum(f(-1+j*h) for j in range(2,n,2)))


count = 0
rng = random.Random(76521)
w_list = [0.25, 0.4, 0.75, 1, 2, 3, math.pi, 4,
          1.5*math.pi, 4.904924457138071, 5, 6,
          2*math.pi, 8, 9, 10, 12, 15, 20, 30, 40]
w_list += [rng.uniform(0.35, 40) for _ in range(140)]
for w in w_list:
    s, c, v = numbers(w)
    assert v > 0
    count += 1
    K = leverage(w)
    assert abs(kernel(w, 0) - K) < 2.e-9
    count += 1
    # Independent moments using diagonal basis 1, cos(wt)-s, sin(wt).
    A = (1+s*c)/2-s*s
    B = (1-s*c)/2
    K_orth = 1+(1-s)**2/A
    assert abs(K_orth-K)<2.e-9
    count += 1
    f = lambda t: kernel(w, t)
    assert abs(integrate_avg(lambda t:f(t)**2,n=600)-K)<5.e-6
    count += 1
    a = complex(rng.uniform(-2,2), rng.uniform(-2,2))
    b = complex(rng.uniform(-2,2), rng.uniform(-2,2))
    d = complex(rng.uniform(-2,2), rng.uniform(-2,2))
    # Exact 3-tone energy Gram formula, compare integrated energy.
    g = lambda t: a+b*cmath.exp(1j*w*t)+d*cmath.exp(-1j*w*t)
    energy = abs(a)**2+abs(b)**2+abs(d)**2+2*(a.conjugate()*(b+d)*s).real+2*(b*d.conjugate()*sinc(2*w)).real
    assert energy>0 and abs(integrate_avg(lambda t:abs(g(t))**2,n=600)-energy)<8.e-6
    count += 1
    assert abs(g(0))**2 <= K*energy+2.e-8
    count += 1
for w in [0.8, 1.2, 2.5, 3.2, 4.0, 4.9, 5.2, 5.8, 6.6, 8.3, 11.0, 20.0]:
    h=1.e-5
    kprime=(leverage(w+h)-leverage(w-h))/(2*h)
    s, c, v = numbers(w)
    exact=2*(1-s)*derivative_sign(w)/(w*v*v)
    assert abs(kprime-exact)<1.e-6
    count+=1
# Bisection for the one zero proven analytically to lie in (3*pi/2,2*pi).
lo, hi=1.5*math.pi, 5.05
assert derivative_sign(lo)>0 and derivative_sign(hi)<0
count+=1
for j in range(100):
    mid=(lo+hi)/2
    if derivative_sign(mid)>0: lo=mid
    else: hi=mid
wstar=(lo+hi)/2
assert abs(wstar-4.904924457138071)<1.e-12
count+=1
assert abs(leverage(wstar)-4.267303561395562)<2.e-12
count+=1
for w in [1, 2, 3, 3.5, 4, 4.5, 4.8, 5, 5.2, 5.5, 6, 7, 8, 9, 10, 15, 20, 30, 40]:
    assert leverage(w)<leverage(wstar)+1.e-10
    count+=1
print(f"PASS: {count} finite assertions; omega*={wstar:.15f}; K*={leverage(wstar):.15f}")
