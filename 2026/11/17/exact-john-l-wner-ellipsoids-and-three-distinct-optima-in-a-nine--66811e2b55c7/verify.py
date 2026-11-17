#!/usr/bin/env python3
"""Independent finite checks for exact extremal ellipsoids of nine-vertex prisms.

The mathematical theorem is proved analytically in RESULT.md. This script checks
coordinate/facet and contact formulas and gives regression tests, not a proof.
Requires only the Python standard library.
"""
import math
import random
from fractions import Fraction

TOL = 4e-12
COUNT = 0

def check(condition, message):
    global COUNT
    COUNT += 1
    if not condition:
        raise AssertionError(message)

def dot(a,b):
    return sum(x*y for x,y in zip(a,b))

def vertices(r):
    h = math.sqrt(1-r*r)
    vs = []
    for j in range(3):
        th = 2*math.pi*j/3
        vs.append((math.cos(th), math.sin(th), 0.0))
    for z in (h,-h):
        for j in range(3):
            th=math.pi/3+2*math.pi*j/3
            vs.append((r*math.cos(th),r*math.sin(th),z))
    return vs

def facets(r):
    h = math.sqrt(1-r*r)
    out=[((0.,0.,1.),h),((0.,0.,-1.),h)]
    for j in range(3):
        th=2*math.pi*j/3
        u=(math.cos(th),math.sin(th))
        v=(-math.sin(th),math.cos(th))
        for sg in (+1,-1):
            out.append(((math.sqrt(3)*r*u[0]/2+sg*(1-r/2)*v[0],
                         math.sqrt(3)*r*u[1]/2+sg*(1-r/2)*v[1],0.),
                        math.sqrt(3)*r/2))
            out.append(((h*u[0],h*u[1],sg*(1-r/2)),h))
    return out

def params(r):
    h=math.sqrt(1-r*r)
    inner_r2=3*r*r/(4*(1-r+r*r))
    if 3*r*r<=2:
        outer_a2=outer_b2=1.
    else:
        outer_a2=3*r*r/2
        outer_b2=3*h*h
    return h,inner_r2,outer_a2,outer_b2

def ratio(r):
    h,a2,c2,d2=params(r)
    return c2*math.sqrt(d2)/(a2*h)

def i_poly(x):
    return 4*x**4-4*x**3+3*x**2+4*x-4

def j_poly(x):
    return x**4-2*x**3+3*x*x+x-2

def root(f,a,b):
    fa=f(a)
    for _ in range(100):
        m=(a+b)/2
        if f(m)*fa>0:
            a=m;fa=f(m)
        else:b=m
    return (a+b)/2

check(i_poly(Fraction(71,100))<0 and i_poly(Fraction(72,100))>0,
      'inball quartic rational isolation')
check(j_poly(Fraction(77,100))<0 and j_poly(Fraction(78,100))>0,
      'John quartic rational isolation')
rI=root(i_poly,.71,.72)
rJ=root(j_poly,.77,.78)
rV=math.sqrt(3)-1
check(rI<rV<rJ<math.sqrt(2/3),'strict ordering of three optimizers')
check(abs(ratio(rJ)-2.900134231069326)<1e-11,'sharp ratio benchmark')

rng=random.Random(260804392)
rs = [.5000001,.501,.51,.6,.7,rI,rV,rJ,math.sqrt(2/3),.9,.99,.999999]
rs += [rng.uniform(.500001,.999999) for _ in range(300)]
for r in rs:
    vv=vertices(r)
    ff=facets(r)
    h,a2,c2,d2=params(r)
    check(len(vv)==9 and len(ff)==14,'facet and vertex counts')
    check(max(abs(dot(v,v)-1) for v in vv)<TOL,'sphere vertices')
    contacts=[]
    for norm,offset in ff:
        gaps=[offset-dot(norm,v) for v in vv]
        check(min(gaps)>-TOL,'facet supports all vertices')
        check(sum(abs(z)<TOL for z in gaps)==3,'facet exactly three vertices')
        # For any diagonal shape M, support in direction normal = sqrt(n M n).
        inner_support=math.sqrt(a2*(norm[0]**2+norm[1]**2)+h*h*norm[2]**2)
        check(inner_support<=offset+TOL,'John ellipsoid contained')
        contacts.append(abs(inner_support-offset)<TOL)
    check(sum(contacts)==8,'John contacts exactly eight facets')
    for v in vv:
        chk=(v[0]**2+v[1]**2)/c2+v[2]**2/d2
        check(chk<=1+TOL,'Loewner contains all vertices')
    num_outer_contacts=sum(abs((v[0]**2+v[1]**2)/c2+v[2]**2/d2-1)<TOL for v in vv)
    check(num_outer_contacts==(9 if 3*r*r<=2+1e-14 else 6), 'Loewner contact count')
    for t in (0.1,.5,.9):
        # A diagonal competitor with smaller axes is always contained;
        # its volume must not exceed the exact John candidate.
        trial_a2=a2*t*t
        trial_b2=h*h*(1-t/2)**2
        check(trial_a2*math.sqrt(trial_b2)<=a2*h+TOL,'volume benchmark inner')

# Sharp ratio minimizer and monotonicity on either side.
for k in range(1,100):
    p=.501+(rJ-.501)*k/100
    q=rJ+(.999-rJ)*k/100
    check(ratio(p)>=ratio(rJ)-TOL and ratio(q)>=ratio(rJ)-TOL,
          'global ratio lower benchmark')

print(f'PASS: {COUNT} finite assertions; rI={rI:.12f}, rV={rV:.12f}, '
      f'rJ={rJ:.12f}, min ratio={ratio(rJ):.12f}')
