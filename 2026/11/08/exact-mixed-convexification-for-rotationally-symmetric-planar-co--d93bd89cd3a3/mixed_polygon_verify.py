"""Supplementary finite tests for a regular-polygon mixed convexification theorem.
All claims for unbounded indices and all real dilations are proved analytically.
Python 3 standard library only; run with python3 mixed_polygon_verify.py.
"""
import math
from random import Random
RNG=Random(20261103)
TAU=2*math.pi

def reg(q,phase=0):
    return [(math.cos(TAU*j/q+phase),math.sin(TAU*j/q+phase)) for j in range(q)]

def hull(points):
    points=sorted(set(points))
    def cross(o,a,b):return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    lo=[]
    for p in points:
        while len(lo)>=2 and cross(lo[-2],lo[-1],p)<=1e-13:lo.pop()
        lo.append(p)
    up=[]
    for p in reversed(points):
        while len(up)>=2 and cross(up[-2],up[-1],p)<=1e-13:up.pop()
        up.append(p)
    return lo[:-1]+up[:-1]

def cross(a,b):return a[0]*b[1]-a[1]*b[0]

def inp(poly,z):
    return all(cross((v[0]-u[0],v[1]-u[1]),(z[0]-u[0],z[1]-u[1]))>=-2e-8 for u,v in zip(poly,poly[1:]+poly[:1]))

def in_union(V,K,L,z):
    for v in V:
        if inp(K,((z[0]-v[0])/L,(z[1]-v[1])/L)):
            return True
    return False

def mix_hull(V,K,L):return hull([(v[0]+L*k[0],v[1]+L*k[1]) for v in V for k in K])

def f_threshold(n,m):
    if m==n: return 1 if n%2==0 else 1/math.cos(math.pi/n)
    return math.sin(math.pi/n)/math.sin(math.pi/m)

checked=0
for n in range(3,15):
    for k in range(1,6):
        m=n*k
        if m>65:continue
        phase=math.pi/n-math.pi/m
        V=reg(n)
        K=reg(m,phase)
        c=f_threshold(n,m)
        H=mix_hull(V,K,c)
        # Boundary and radial filling: all points of P+lambda K checked.
        for j in range(len(H)):
            p=H[j];q=H[(j+1)%len(H)]
            for t in (0,1/13,1/4,1/2,3/4,12/13,1):
                w=(p[0]*(1-t)+q[0]*t,p[1]*(1-t)+q[1]*t)
                for a in (0,0.01,0.17,0.41,0.76,1):
                    z=(a*w[0],a*w[1])
                    assert in_union(V,K,c,z),(n,m,phase,c,j,t,a,z)
                    checked+=1
        # At the two strict subthreshold witnesses, central missing point
        # for n=m odd, or midpoint of one uncovered exposed edge otherwise.
        L=.995*c
        if n==m and n%2:
            assert not in_union(V,K,L,(0,0)),('center',n)
        else:
            # Choose the center of the full exposed edge in a source-normal.
            # For k=1 and even n this is also an uncovered gap.
            N=(math.cos(math.pi/n),math.sin(math.pi/n))
            length=math.cos(math.pi/n)+L*math.cos(math.pi/m)
            w=(length*N[0],length*N[1])
            assert not in_union(V,K,L,w),('facegap',n,m,L,w)
        checked+=1
        # At any rotated nonmatching normal fan, a common P-edge midpoint
        # is absent from the corresponding union boundary even at large L.
        Kr=reg(m,phase+math.pi/(7*m))
        L=7.0*c
        N=(math.cos(math.pi/n),math.sin(math.pi/n))
        support=max((N[0]*p[0]+N[1]*p[1] for p in Kr))
        mid=((math.cos(math.pi/n)+L*support)*N[0],(math.cos(math.pi/n)+L*support)*N[1])
        assert not in_union(V,Kr,L,mid),('misalign',n,m,L,mid)
        checked+=1
print('MIXED_REGULAR_POLYGON_TESTS_OK',checked)

# Supplementary tests for nonsimilar, n-fold symmetric polygonal convexifiers.
def gauge(K,x):
    val=0.0
    for u,v in zip(K,K[1:]+K[:1]):
        edge=(v[0]-u[0],v[1]-u[1])
        normal=(edge[1],-edge[0])
        num=normal[0]*x[0]+normal[1]*x[1]
        den=normal[0]*u[0]+normal[1]*u[1]
        assert den>0.0
        val=max(val,num/den)
    return val

def mink_poly(V,W,a,b):
    return hull([(a*v[0]+b*w[0],a*v[1]+b*w[1]) for v in V for w in W])

for n in range(3,13):
    V=reg(n)
    for j in range(1,8):
        angle=(j+0.37)*math.pi/(13*n)
        K=mink_poly(V,reg(n,angle),.2+.2*j,.08+.13*j)
        N=(math.cos(math.pi/n),math.sin(math.pi/n))
        h=max(p[0]*N[0]+p[1]*N[1] for p in K)
        F=[p for p in K if abs(p[0]*N[0]+p[1]*N[1]-h)<1e-8]
        ell=math.dist(F[0],F[-1])
        assert ell>1e-4
        L=2*math.sin(math.pi/n)
        edge_bound=L/ell
        center_bound=gauge(K,(-1,0))
        c=max(edge_bound,center_bound)
        H=mix_hull(V,K,c)
        for i in range(len(H)):
            p,q=H[i],H[(i+1)%len(H)]
            for t in (0,1/5,1/2,4/5,1):
                z=(p[0]*(1-t)+q[0]*t,p[1]*(1-t)+q[1]*t)
                for a in (0,.27,.77,1):
                    assert in_union(V,K,c,(a*z[0],a*z[1])),('general',n,j,i,t,a)
                    checked+=1
        sub=c*.995
        if center_bound > edge_bound*1.00001:
            assert not in_union(V,K,sub,(0,0)),('general-center',n,j)
        else:
            # The Minkowski exposed edge midpoint is not covered.
            w=(h*sub*N[0]+math.cos(math.pi/n)*N[0],h*sub*N[1]+math.cos(math.pi/n)*N[1])
            # Extra tangential displacement can occur for K with only n-fold
            # symmetry; choose the actual midpoint of the K support facet.
            mid=(.5*(F[0][0]+F[-1][0]),.5*(F[0][1]+F[-1][1]))
            w=(math.cos(math.pi/n)*N[0]+sub*mid[0],math.cos(math.pi/n)*N[1]+sub*mid[1])
            assert not in_union(V,K,sub,w),('general-edge',n,j,w)
        checked+=1
print('N_FOLD_SYMMETRIC_CONVEXIFIER_TESTS_OK',checked)
