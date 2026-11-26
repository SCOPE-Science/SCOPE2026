#!/usr/bin/env python3
"""Independent reproducibility checks for a joint cube-section law.
Uses only the Python standard library; finite tests do not prove the theorem.
"""
import math
import random

PI=math.pi
Z0=1/math.sqrt(6)
Z1=1/math.sqrt(3)

def theta(z):
    return math.asin(z/math.sqrt(1-z*z))

def phi(z):
    return math.asin(z/math.sqrt(2*(1-z*z)))

def joint(z):
    if z<0 or z>=Z1: return (0.0,0.0)
    h=PI/4-theta(z)
    six=phi(z) if z<Z0 else h
    return ((12/PI)*max(0,h-six),(12/PI)*six)

def simpson(f,a,b,n=4000):
    step=(b-a)/n
    return step/3*(f(a)+f(b)+4*sum(f(a+step*j) for j in range(1,n,2))+2*sum(f(a+step*j) for j in range(2,n,2)))

def vertices(u):
    verts=[]
    for k in range(3):
        if abs(u[k])<1e-12: continue
        js=[i for i in range(3) if i!=k]
        for s in (-1.0,1.0):
            for t in (-1.0,1.0):
                q=-(u[js[0]]*s+u[js[1]]*t)/u[k]
                if abs(q)<=1+1e-12:
                    x=[0.,0.,0.];x[k]=max(-1.,min(1.,q));x[js[0]]=s;x[js[1]]=t
                    if not any(sum((x[i]-v[i])**2 for i in range(3))<1e-20 for v in verts):verts.append(tuple(x))
    return verts

def polygon_stats(u):
    v=vertices(u)
    e=(1.,0.,0.) if abs(u[0])<0.8 else (0.,1.,0.)
    a=(e[0]-e[0]*u[0]**2-e[1]*u[0]*u[1]-e[2]*u[0]*u[2],
       e[1]-e[0]*u[0]*u[1]-e[1]*u[1]**2-e[2]*u[1]*u[2],
       e[2]-e[0]*u[0]*u[2]-e[1]*u[1]*u[2]-e[2]*u[2]**2)
    t=math.sqrt(sum(z*z for z in a));a=tuple(z/t for z in a)
    b=(u[1]*a[2]-u[2]*a[1],u[2]*a[0]-u[0]*a[2],u[0]*a[1]-u[1]*a[0])
    p=sorted((sum(x[i]*a[i] for i in range(3)),sum(x[i]*b[i] for i in range(3))) for x in v)
    def cross(o,q,r):return (q[0]-o[0])*(r[1]-o[1])-(q[1]-o[1])*(r[0]-o[0])
    lower=[]
    for x in p:
        while len(lower)>1 and cross(lower[-2],lower[-1],x)<=1e-12: lower.pop()
        lower.append(x)
    upper=[]
    for x in reversed(p):
        while len(upper)>1 and cross(upper[-2],upper[-1],x)<=1e-12: upper.pop()
        upper.append(x)
    hull=lower[:-1]+upper[:-1]
    r=min(abs(x[0]*y[1]-x[1]*y[0])/math.hypot(y[0]-x[0],y[1]-x[1]) for x,y in zip(hull,hull[1:]+hull[:1]))
    return len(hull),r

rng=random.Random(24681357)
for _ in range(2500):
    g=[rng.gauss(0,1) for _ in range(3)]
    t=math.sqrt(sum(x*x for x in g));u=[x/t for x in g]
    a,b,c=sorted((abs(x) for x in u),reverse=True)
    n,r=polygon_stats(u)
    assert n==(6 if a<b+c else 4),(u,n)
    assert abs(r-1/math.sqrt(1-c*c))<1e-10,(u,r)
    if n==4: assert c<Z0+1e-12

f4=lambda z:joint(z)[0]
f6=lambda z:joint(z)[1]
q4=simpson(f4,0,Z0)
q6=simpson(f6,0,Z0)+simpson(f6,Z0,Z1)
known=1-6/PI*math.asin(1/3)
assert abs(q6-known)<1e-8,(q6,known)
print("normalization",q4,q6,q4+q6,known); assert abs(q4+q6-1)<1e-8
for j in range(1,100):
    z=Z0*j/100
    _,d6=joint(z);d4,_=joint(z)
    assert 0<d6/(d4+d6)<1
    if j>1:
        zprevious=Z0*(j-1)/100
        ap,bp=joint(zprevious)
        assert d6/(d4+d6)>bp/(ap+bp)
print('VERIFY_OK: 2500 independently reconstructed plane sections, exact combinatorial thresholds, continuous density, normalizations, monotonic conditional law')
