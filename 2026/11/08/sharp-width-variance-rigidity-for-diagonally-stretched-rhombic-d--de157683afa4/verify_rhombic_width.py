#!/usr/bin/env python3
"""Standalone geometric and Monte Carlo checks for the diagonal rhombic dodecahedron theorem."""
import math
import random
import itertools

T=((1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1))
V={(2,0,0),(-2,0,0),(0,2,0),(0,-2,0),(0,0,2),(0,0,-2)} | set(itertools.product((-1,1),repeat=3))
Z=set()
for signs in itertools.product((-1,1), repeat=4):
    z=tuple(sum(signs[k]*T[k][j] for k in range(4))/2 for j in range(3))
    Z.add(z)
assert Z == V | {(0,0,0)} and len(V)==14

def f(t):
    return math.sqrt(max(0.0,1-t*t))+t*math.asin(max(-1.0,min(1.0,t)))

def moments(a):
    S=sum(v*v for v in a)
    rho=[2*v*v/S-1 for v in a]
    return 2*math.sqrt(S), (4*S/3)+(8*S/(3*math.pi))*sum(f(x) for x in rho)

def width_zono(u,a):
    return sum(abs(sum(u[j]*a[j]*t[j] for j in range(3))) for t in T)

def width_vertex(u,a):
    dots=[sum(u[j]*a[j]*v[j] for j in range(3)) for v in V]
    return max(dots)-min(dots)

rng=random.Random(20261103)
for a in ((1,1,1),(2,.8,1.3),(1,.08,.02)):
    n=80000; total=0.; total2=0.
    for _ in range(n):
        g=[rng.gauss(0,1) for i in range(3)]
        l=math.sqrt(sum(x*x for x in g));u=[x/l for x in g]
        w=width_zono(u,a)
        if _<3000: assert abs(w-width_vertex(u,a))<1e-12
        total+=w;total2+=w*w
    mean,sq=moments(a)
    assert abs(total/n-mean)<.035,(a,total/n,mean)
    assert abs(total2/n-sq)<.18,(a,total2/n,sq)
    print('shape',a,'mean',mean,'empirical',total/n,'square',sq,'empirical',total2/n)
for i in range(30000):
    a=[math.exp(rng.gauss(0,1)) for j in range(3)]
    S=sum(x*x for x in a)
    m,second=moments(a)
    reg=moments([math.sqrt(S/3)]*3)[1]
    excess=second-reg
    anis=sum((x*x-S/3)**2 for x in a)
    assert excess>=16/(3*math.pi*S)*anis-1e-10
    assert second-m*m <4*S/3+1e-10
M,Q=moments((1,1,1))
assert abs(Q-(8+16/math.pi*(math.sqrt(2)-math.asin(1/math.sqrt(3)))))<2e-13
print('regular mean',M,'squared moment',Q,'variance',Q-M*M,'boundary supremum at S=3:',4)
print('RHOMBIC_WIDTH_OK exact_vertices=14 support_consistency=9000 cases=3 stability_samples=30000')
