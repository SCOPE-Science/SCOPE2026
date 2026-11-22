"""Reproducible numerical diagnostics for planar central cylinder sections.

Only the Python standard library is required. Numerical tests supplement,
but do not replace, the analytical arguments in RESULT.md.
"""
import math
import random

PI = math.pi
N = 1_200
count = 0

def require(ok, description):
    global count
    count += 1
    if not ok:
        raise AssertionError(description)

def simpson(f, lo, hi, n=N):
    assert n % 2 == 0
    step = (hi - lo) / n
    total = f(lo) + f(hi)
    for j in range(1, n):
        total += (4 if j % 2 else 2) * f(lo + step*j)
    return total * step / 3

def perimeter(h, theta, R=1.0):
    if theta <= 0:
        return 2*PI*R
    if theta >= PI/2:
        return 4*R*(1+h)
    t = math.tan(theta)
    k = min(1.0, h/t)
    alpha = math.asin(k)
    return 4*R*(simpson(lambda p: math.sqrt(1+t*t*math.cos(p)**2), 0, alpha)
                + math.sqrt(max(0.0,1-k*k)))

def independent_polygon_perimeter(h, theta, n=1_500):
    """Direct Euclidean polyline length on the sliced cylinder boundary."""
    if theta <= 0:
        return 2*PI
    if theta >= PI/2:
        return 4*(1+h)
    t = math.tan(theta)
    k = min(1.0, h/t)
    alpha = math.asin(k)
    stretch = math.hypot(1,t)
    x0,y0 = 0.0,1.0
    length = 0.0
    for j in range(1,n+1):
        p=alpha*j/n
        x1,y1=stretch*math.sin(p),math.cos(p)
        length += math.hypot(x1-x0,y1-y0)
        x0,y0=x1,y1
    return 4*(length+math.sqrt(max(0.0,1-k*k)))

rng=random.Random(461209)
h_values=[0.025,0.1,0.3,PI/2-1-0.005,PI/2-1,PI/2-1+0.005,0.8,0.99,1,1.01,1.5,3,8]
for h in h_values:
    critical=math.atan(h)
    angles=[0,critical/5,critical/2,critical,
            critical+(PI/2-critical)*.001,
            critical+(PI/2-critical)*.3,
            critical+(PI/2-critical)*.7,
            PI/2-0.002,PI/2]
    for theta in angles:
        q=perimeter(h,theta)
        direct=independent_polygon_perimeter(h,theta)
        require(abs(q-direct)<2e-5*max(1,q),f'polygon mismatch h={h} angle={theta}')
        bound=min(2*PI,4*(1+h))
        require(q+2e-9>=bound,f'global bound failed h={h} angle={theta}')
    require(abs(perimeter(h,0)-2*PI)<1e-12,'disk endpoint')
    require(abs(perimeter(h,PI/2)-4*(1+h))<1e-12,'rectangle endpoint')

for _ in range(1_000):
    h=math.exp(rng.uniform(-5,3))
    theta=rng.random()*PI/2
    q=perimeter(h,theta)
    require(q>=min(2*PI,4*(1+h))-1e-8,'random global bound')

# Tangency regularity: full ellipse minus clipped section has 3/2 contact.
for h in [0.1,0.4,PI/2-1,0.85,1.0,1.7,3.0]:
    for delta in [1e-3,3e-4,1e-4]:
        t=h+delta
        theta=math.atan(t)
        circle_alpha=PI/2
        ellipse=4*simpson(lambda p:math.sqrt(1+t*t*math.cos(p)**2),0,circle_alpha)
        deficit=ellipse-perimeter(h,theta)
        coef=(2/3)*(1+h*h)*(2/h)**1.5
        asymptotic=coef*delta**1.5
        require(deficit>0,'contact deficit should be positive')
        require(abs(deficit/asymptotic-1)<max(0.06,5*delta/h),
                f'contact coefficient h={h} delta={delta}')

# The side-on local asymptotics are in w=cot(theta)^2.
for h in [0.2,0.58,0.85,0.99,1.0,1.01,1.3]:
    for w in [1e-3,3e-4,1e-4]:
        theta=math.atan(1/math.sqrt(w))
        deviation=perimeter(h,theta)-4*(1+h)
        leading=2*h*(1-h)*w + (2*h**3/3-h/2-h**4/2)*w*w
        require(abs(deviation-leading)<1.0*w*w*w+1e-10,
                f'side-on expansion h={h} w={w}')
        if h<1:
            require(deviation>0,'side-on expected strict local minimum')
        else:
            require(deviation<0,'side-on expected strict local maximum')

print(f'PASS: {count} independent numerical assertions')
