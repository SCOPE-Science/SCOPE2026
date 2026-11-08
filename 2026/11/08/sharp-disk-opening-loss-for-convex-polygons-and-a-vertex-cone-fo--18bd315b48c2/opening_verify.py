"""Independent numerical checks of the planar opening-loss theorem.
Uses half-plane clipping, segment distances, and linear programming. 
All universal claims in the accompanying proof are analytic, not inferred from samples.
"""
import numpy as np
from math import acos, pi, sin, cos, sqrt
from scipy.spatial import ConvexHull
from scipy.optimize import linprog

EPS=1e-10

def polygon(points):
    x=np.asarray(points, dtype=float)
    h=ConvexHull(x)
    return x[h.vertices]

def normals(P):
    e=np.roll(P,-1,axis=0)-P
    length=np.linalg.norm(e,axis=1)
    N=np.stack([e[:,1],-e[:,0]],axis=1)/length[:,None]
    return N, np.einsum('ij,ij->i',N,P)

def inradius(N,b):
    res=linprog([0,0,-1],A_ub=np.c_[N,np.ones(len(N))],b_ub=b,bounds=[(None,None)]*3,method='highs')
    assert res.success and res.x[2]>0
    return res.x[2]

def clip_halfplane(vertices, normal, bound):
    out=[]
    if len(vertices)==0: return []
    for i in range(len(vertices)):
        a=np.asarray(vertices[i]);c=np.asarray(vertices[(i+1)%len(vertices)])
        fa=float(normal@a-bound);fb=float(normal@c-bound)
        ina=fa<=1e-11;inb=fb<=1e-11
        if ina:out.append(a)
        if ina!=inb:
            t=fa/(fa-fb)
            out.append(a+t*(c-a))
    return out

def inner_poly(P,N,b,r):
    out=list(P)
    for n,bb in zip(N,b):out=clip_halfplane(out,n,bb-r)
    return np.array(out)

def distance_to_polygon(v,P):
    if len(P)==0: return float('inf')
    # Vertex is outside P_r in all tests here.
    ds=[]
    for a,b in zip(P,np.roll(P,-1,axis=0)):
        e=b-a;s=np.dot(e,e)
        if s<1e-24: ds.append(float(np.linalg.norm(v-a)));continue
        t=max(0,min(1,np.dot(v-a,e)/s))
        ds.append(float(np.linalg.norm(v-(a+t*e))))
    return min(ds)

def metrics(P):
    N,b=normals(P)
    th=[];Z=[];r0=float('inf')
    n=len(P)
    for i,v in enumerate(P):
        before=P[(i-1)%n]-v;after=P[(i+1)%n]-v
        before=before/np.linalg.norm(before);after=after/np.linalg.norm(after)
        theta=acos(float(np.clip(np.dot(before,after),-1,1)))
        th.append(theta)
        z=(before+after)/np.linalg.norm(before+after)/sin(theta/2)
        Z.append(z)
        for j in range(n):
            if j in ((i-1)%n,i):continue
            gap=b[j]-N[j]@v
            denom=1+N[j]@z
            if denom>1e-12:r0=min(r0,gap/denom)
    return np.array(th),np.array(Z),r0,N,b

def check(P):
    th,Z,r0,N,b=metrics(P)
    R=inradius(N,b);m=len(P)
    local=min(R/7,r0/5)
    assert local>0
    ideal=1/sin(min(th)/2)-1
    bound=1/cos(pi/m)-1
    for r in (local,.75*R):
        ir=inner_poly(P,N,b,r)
        assert len(ir)>0
        actual=max(distance_to_polygon(v,ir)-r for v in P)
        assert actual/r>=ideal-5e-7,(r,actual/r,ideal)
        assert actual/r>=bound-5e-7
        if r==local:
            assert abs(actual/r-ideal)<5e-7,(actual/r,ideal)
        defect=max(0,actual/r-bound)
        low=2*np.arcsin(1/(1+actual/r))
        assert all(t>low-3e-7 for t in th)
    return m

rng=np.random.default_rng(4141)
checks=0
for _ in range(220):
    k=int(rng.integers(4,13))
    points=rng.uniform(-2,2,size=(k,2))
    P=polygon(points)
    checks+=check(P)
for n in range(3,19):
    theta=np.linspace(0,2*pi,n,endpoint=False)
    P=polygon(np.c_[np.cos(theta),np.sin(theta)])
    N,b=normals(P);R=inradius(N,b)
    for a in [.005,.02,.1,.33,.7,.99,1.0]:
        r=a*R
        ir=inner_poly(P,N,b,r)
        assert len(ir)>0
        err=max(distance_to_polygon(v,ir)-r for v in P)
        assert abs(err/r-(1/cos(pi/n)-1)) < 2e-7,(n,a,err/r)
        checks+=1
for a,b in [(1,1),(1,2),(4,1),(1.37,3.28)]:
    P=np.array([[-a,-b],[a,-b],[a,b],[-a,b]])
    N,B=normals(P)
    for f in [.01,.2,.7,.999]:
        r=f*min(a,b)
        Q=inner_poly(P,N,B,r)
        err=max(distance_to_polygon(v,Q)-r for v in P)
        assert abs(err/r-(sqrt(2)-1))<1e-8
        checks+=1
print('OPENING_GEOMETRY_NUMERIC_OK 220 random convex polygons x 2 radii; 112 regular-polygon radii; 16 rectangle radii')
