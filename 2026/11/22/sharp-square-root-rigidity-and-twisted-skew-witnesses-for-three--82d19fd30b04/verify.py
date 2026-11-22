"""Reproduce weighted three-cylinder upper bound and skew near-optimal witnesses.
Finite numerical tests are supporting evidence only; the accompanying proof is analytic.
Python >= 3.9; no third-party imports.
"""
import math
import random

EPS = 1e-9

def dot(x, y):
    return sum(a*b for a,b in zip(x,y))

def cross(x, y):
    return (x[1]*y[2]-x[2]*y[1], x[2]*y[0]-x[0]*y[2], x[0]*y[1]-x[1]*y[0])

def norm(x):
    return math.sqrt(dot(x,x))

def vsub(x,y):
    return tuple(a-b for a,b in zip(x,y))

def vsum(x,y):
    return tuple(a+b for a,b in zip(x,y))

def mul(s,x):
    return tuple(s*a for a in x)

def threshold(b):
    inv = [1/x for x in b]
    return sum(inv) + 2*math.sqrt(sum(inv[i]*inv[j] for i in range(3) for j in range(i+1,3)))

def alpha(i,j,l,b):
    z=(l*l*b[i]*b[j])/((1+l*b[i])*(1+l*b[j]))
    return 2*math.asin(math.sqrt(z))

def frame(b):
    l=threshold(b)
    a=alpha(0,1,l,b)
    c=alpha(1,2,l,b)
    theta=[0,a,a+c]
    q=[(math.cos(u),math.sin(u),0.0) for u in theta]
    return l,q

def point_lines(b,l,q,t):
    p=[mul(1+l*b[i],q[i]) for i in range(3)]
    directions=[(-t*point[1],t*point[0],1.0) for point in p]
    return p, directions

def line_distance(x,u,y,v):
    d=vsub(y,x); uv=cross(u,v)
    if norm(uv)<1e-13:
        return norm(cross(d,u))/norm(u)
    return abs(dot(d,uv))/norm(uv)

def jdet(a,b):
    return a[0]*b[1]-a[1]*b[0]

def case(b):
    lstar,q=frame(b)
    pair=((0,1),(0,2),(1,2))
    assert abs(sum(alpha(i,j,lstar,b) for i,j in pair)-2*math.pi) < 2e-11
    for i,j in pair:
        p,_=point_lines(b,lstar,q,0.0)
        assert abs(norm(vsub(p[i],p[j]))-lstar*(b[i]+b[j]))<3e-10*max(1,lstar*(b[i]+b[j]))
    # Test the closed-form formula for the first variation of each pair slack.
    eps=1e-5*lstar
    le=lstar-eps
    p,_=point_lines(b,le,q,0)
    for i,j in pair:
        D=(1+lstar*b[i])*(1+lstar*b[j])
        analytic=4*lstar*b[i]*b[j]*(2+lstar*(b[i]+b[j]))/D
        slack=norm(vsub(p[i],p[j]))**2-(le*(b[i]+b[j]))**2
        assert slack>0
        assert abs(slack/eps-analytic) < .001*max(1,analytic)
    # Find a nonzero twist t ~ sqrt(epsilon) that maintains all clearances.
    eps=1e-6*lstar
    le=lstar-eps
    p,_=point_lines(b,le,q,0)
    k=1.0
    for i,j in pair:
        h=jdet(p[i],p[j])/norm(vsub(p[i],p[j]))
        slack=norm(vsub(p[i],p[j]))**2-(le*(b[i]+b[j]))**2
        k=min(k, math.sqrt(slack/max(1e-50,(le*(b[i]+b[j]))**2*h*h*eps))/4)
    t=k*math.sqrt(eps)
    p,d=point_lines(b,le,q,t)
    axis_spread=0.0
    for i,j in pair:
        dist=line_distance(p[i],d[i],p[j],d[j])
        h=jdet(p[i],p[j])/norm(vsub(p[i],p[j]))
        formula=norm(vsub(p[i],p[j]))/math.sqrt(1+t*t*h*h)
        assert abs(dist-formula) <= 1e-8*max(1,dist)
        assert dist>=le*(b[i]+b[j])*(1-1e-10), (b,i,j,dist,le*(b[i]+b[j]))
        ui=mul(1/norm(d[i]),d[i]); uj=mul(1/norm(d[j]),d[j]);
        axis_spread=max(axis_spread,norm(vsub(ui,uj)))
    assert axis_spread>0.05*k*math.sqrt(eps)*min(1,min(1+lstar*x for x in b))
    return axis_spread/math.sqrt(eps)

if __name__=='__main__':
    random.seed(29)
    weights=[(1.,1.,1.),(1.,2.,3.),(0.25,1.,10.),(1.,100.,100.),(1.,1.,100.)]
    weights += [tuple(math.exp(random.uniform(-2.5,2.5)) for _ in range(3)) for _ in range(200)]
    estimates=[case(b) for b in weights]
    print(f'PASS {len(weights)} unequal/equal weight triples; twisted witnesses have angular spread/sqrt(epsilon) in [{min(estimates):.6g}, {max(estimates):.6g}]')
