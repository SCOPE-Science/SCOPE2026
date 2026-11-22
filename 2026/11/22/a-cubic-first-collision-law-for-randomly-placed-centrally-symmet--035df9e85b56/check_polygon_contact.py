"""Numerical verification of polygonal lattice-contact asymptotics.
No external packages required. Floats test geometry, not infinite proof.
"""
from math import sin,cos,pi,tan,hypot

def area(poly):
    return abs(sum(x*y1-y*x1 for (x,y),(x1,y1) in zip(poly,poly[1:]+poly[:1])))/2

def signed_area(poly):
    return sum(x*y1-y*x1 for (x,y),(x1,y1) in zip(poly,poly[1:]+poly[:1]))/2

def clip(poly, edge_a, edge_b):
    if not poly:return []
    a,b=edge_a,edge_b
    def cross(p):return (b[0]-a[0])*(p[1]-a[1])-(b[1]-a[1])*(p[0]-a[0])
    ans=[]
    for p,q in zip(poly,poly[1:]+poly[:1]):
        fp,fq=cross(p),cross(q)
        if fp>=0:ans.append(p)
        if (fp<0<=fq) or (fq<0<=fp):
            t=fp/(fp-fq)
            ans.append((p[0]+t*(q[0]-p[0]),p[1]+t*(q[1]-p[1])))
    return ans

def intersection(poly, other):
    o=other if signed_area(other)>0 else other[::-1]
    q=poly[:]
    for p,r in zip(o,o[1:]+o[:1]):q=clip(q,p,r)
    return area(q) if q else 0.

def regpoly(n,eps,theta):
    return [((1+eps)/2*cos(theta+2*pi*j/n),(1+eps)/2*sin(theta+2*pi*j/n)) for j in range(n)]

def cone(n,eps,theta):
    m=1/tan(pi/n)
    dx=(1+eps)-cos(theta); dy=-sin(theta)
    return max(0.,(m*m*dx*dx-dy*dy)/(2*m)) if abs(dy)<=m*dx else 0.

def simpson(f,a,b,N=1200):
    assert N%2==0
    h=(b-a)/N;s=f(a)+f(b)
    for k in range(1,N):s+=(4 if k%2 else 2)*f(a+k*h)
    return s*h/3

def test(n,eps):
    m=1/tan(pi/n); lim=min(2*m*eps,pi/n*.49)
    def cov(theta):
        p=regpoly(n,eps,theta)
        return intersection(p,[(x+1,y) for x,y in p])
    I=simpson(cov,-lim,lim)
    C=n/ pi*I/eps**3  # each vertex alignment appears n times, P2=1/pi * all angle integral
    pred=2*n*m*m/(3*pi)
    maxerr=max(abs(cov(t)-cone(n,eps,t)) for t in [lim*(j-20)/20 for j in range(41)])
    print('n',n,'eps',eps,'C_num',round(C,9),'C_theory',round(pred,9),'ratio',round(C/pred,8),'cone_area_error',maxerr)
    assert maxerr<2e-11
    assert abs(C/pred-1)<0.16

for n in (4,6,8,12):
 for eps in (0.01,0.005):test(n,eps)
print('PASS numerical cone geometry and cubic scaling')
