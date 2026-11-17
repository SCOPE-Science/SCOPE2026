#!/usr/bin/env python3
"""Independent finite geometric checks for regular antiprism dihedrals and volumes.
Run: python3 verify_antiprism.py. Standard library only. Finite checks are not a proof.
"""
import math

checks = 0

def check(ok, desc):
    global checks
    checks += 1
    if not ok:
        raise AssertionError(desc)

def dot(a,b):
    return sum(x*y for x,y in zip(a,b))

def sub(a,b):
    return tuple(x-y for x,y in zip(a,b))

def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])

def unit(a):
    q=math.sqrt(dot(a,a)); return tuple(v/q for v in a)

def facet_normal(points, face):
    a,b,c=(points[j] for j in face)
    normal=unit(cross(sub(b,a),sub(c,a)))
    # Ensure outward direction: centroid at origin.
    if dot(normal,a)<0: normal=tuple(-v for v in normal)
    return normal

def regular_antiprism(n,t):
    th=math.pi/n
    T=[(math.cos(2*k*th),math.sin(2*k*th),t/2) for k in range(n)]
    B=[(math.cos((2*k+1)*th),math.sin((2*k+1)*th),-t/2) for k in range(n)]
    return T+B

def expected(n,t):
    c=math.cos(math.pi/n); q=1-c
    A=math.pi-math.acos(q/math.hypot(t,q))
    B=math.pi-math.acos((t*t*c-q*q)/(t*t+q*q))
    return A,B

def check_facets(n,t):
    vertices=regular_antiprism(n,t)
    top=[(k,(k+1)%n,n+k) for k in range(n)]
    bottom=[(n+k,n+(k+1)%n,(k+1)%n) for k in range(n)]
    up=[facet_normal(vertices,f) for f in top]
    down=[facet_normal(vertices,f) for f in bottom]
    for face,N in zip(top+bottom,up+down):
        support=dot(N,vertices[face[0]])
        check(support>0,(n,t,'positive support'))
        for p in vertices:
            check(dot(N,p)<=support+5e-12,(n,t,'valid supporting plane'))
        for idx in face:
            check(abs(dot(N,vertices[idx])-support)<5e-12,(n,t,'facet incidence'))
    A,B=expected(n,t)
    for k in range(n):
        # rim base/side normal comparisons
        u=math.pi-math.acos(max(-1,min(1,up[k][2])))
        b=math.pi-math.acos(max(-1,min(1,-down[k][2])))
        check(abs(u-A)<3e-12,(n,t,'upper rim dihedral'))
        check(abs(b-A)<3e-12,(n,t,'lower rim dihedral'))
        for j in (k,(k-1)%n):
            dihedral=math.pi-math.acos(max(-1,min(1,dot(up[k],down[j]))))
            check(abs(dihedral-B)<3e-12,(n,t,'slant edge dihedral'))
    return A,B

def volume_formula(n,t):
    th=math.pi/n
    return n*t*(math.sin(2*th)+math.sin(th))/3

def signed_volume_by_facets(n,t):
    pts=regular_antiprism(n,t)
    ans=0.0
    # Two caps triangulated at centroid of each cap.
    for start,z in ((0,t/2),(n,-t/2)):
        C=(0,0,z)
        for k in range(n):
            a,b=pts[start+k],pts[start+(k+1)%n]
            ans+=abs(dot(C,cross(a,b)))/6
    for k in range(n):
        faces=[(k,(k+1)%n,n+k),(n+k,n+(k+1)%n,(k+1)%n)]
        for i,j,l in faces:
            ans+=abs(dot(pts[i],cross(pts[j],pts[l])))/6
    return ans

for n in range(3,31):
    c=math.cos(math.pi/n);q=1-c
    e=q*math.sqrt(1+2*c)/c
    u=math.sqrt(2*q*(1+2*c))
    v=math.sqrt(2)
    check(abs((e*e*c-q*q)/(e*e+q*q)-q/math.hypot(e,q))<2e-12,'equal normal angles')
    check((abs(e-u)<1e-12 and abs(u-v)<1e-12) if n==3 else (0<e<u<v),'optimizer ordering')
    check(abs(math.pi-math.acos(c/(1+c)) - math.acos(-c/(1+c)))<1e-12,'opt formula')
    check(abs((u*u*c-q*q)/(u*u+q*q)-(4*c-1)/3)<1e-12,'uniform side cosine')
    check(abs(volume_formula(n,1)-signed_volume_by_facets(n,1))<1e-10,'volume facets')
    for height in (e,u,v,0.3,0.8,2.6):
        a,b=check_facets(n,height)
        check(abs(max(a,b)-(math.pi-min(math.pi-a,math.pi-b)))<2e-12,'max conversion')
        check(max(a,b)>=math.acos(-c/(1+c))-3e-12,'global dihedral bound')
    for fac in (0.65,0.80,0.92,1.11,1.31):
        for t in (e*fac,v*fac):
            check(max(expected(n,t))>=max(expected(n,e))-3e-12,'minimizer sampled')
    # Fixed circumradius 1: h/R scales with t.
    def circumvolume(x):
        r=1/math.sqrt(1+x*x/4)
        return r**3*volume_formula(n,x)
    for x in (e,u,0.2,0.5,1,2,3,5):
        check(circumvolume(v)>=circumvolume(x)-1e-11,'volume global maximum')
print('PASS:',checks,'finite checks across 28 polygon orders (n=3..30).')
