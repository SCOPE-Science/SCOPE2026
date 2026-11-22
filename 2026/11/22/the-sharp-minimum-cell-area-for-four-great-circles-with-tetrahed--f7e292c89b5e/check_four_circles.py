#!/usr/bin/env python3
"""Reproduce finite exact-angle identities and numerical four-great-circle cell geometry.
This numerical checker is corroboration; the theorem is proven analytically.
Standard library only; random seed fixed.
"""
import itertools
import math
import random

PI = math.pi
EPS = 5e-9

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def cross(a,b): return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])
def det(a,b,c): return dot(a,cross(b,c))
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def scale(t,a): return tuple(t*x for x in a)
def norm(a): return math.sqrt(dot(a,a))
def unit(a): return scale(1/norm(a),a)
def angle(a,b): return math.acos(max(-1,min(1,dot(a,b))))
def tri_area(a,b,c): return 2*math.atan2(abs(det(a,b,c)),1+dot(a,b)+dot(b,c)+dot(c,a))

def cells(normals):
    """Compute spherical intersections of oriented hemispheres via pair normals."""
    out = {}
    for signs in itertools.product((-1,1), repeat=4):
        verts=[]
        for i,j in itertools.combinations(range(4),2):
            base=unit(cross(normals[i],normals[j]))
            for x in (base,scale(-1,base)):
                if all(signs[k]*dot(normals[k],x)>=-EPS for k in range(4)):
                    if all(norm(add(x,scale(-1,y)))>1e-7 for y in verts): verts.append(x)
        if len(verts)<3: continue
        center=unit(tuple(sum(x[t] for x in verts) for t in range(3)))
        ax=unit(tuple(verts[0][i]-dot(verts[0],center)*center[i] for i in range(3)))
        ay=cross(center,ax)
        verts.sort(key=lambda v:math.atan2(dot(v,ay),dot(v,ax)))
        ar=sum(tri_area(center,verts[i],verts[(i+1)%len(verts)]) for i in range(len(verts)))
        out[signs]=(len(verts),ar)
    return out


def test_normals(normals):
    f=[tuple(normals[j] for j in range(4) if j!=i) for i in range(4)]
    a=[tri_area(*t) for t in f]
    per=[angle(t[0],t[1])+angle(t[1],t[2])+angle(t[2],t[0]) for t in f]
    assert abs(sum(a)-4*PI)<2e-8, (a,sum(a))
    for i in range(4):
        assert per[i]<2*PI
        assert abs(a[i]-tri_area(*f[i]))<1e-10
    c=cells(normals)
    assert len(c)==14, len(c)
    assert sum(v[0]==3 for v in c.values())==8
    assert sum(v[0]==4 for v in c.values())==6
    assert abs(sum(v[1] for v in c.values())-4*PI)<2e-8
    # The four one-out/three-in cells correspond to spherical polar faces.
    for i in range(4):
        for negative in (False, True):
            signs=tuple((-1 if j!=i else 1) * (-1 if negative else 1) for j in range(4))
            assert c[signs][0]==3
            assert abs(c[signs][1]-(2*PI-per[i]))<2e-8, (i,c[signs],per[i])
    return min(v[1] for v in c.values()),a,per

def main():
    a=math.acos(-1/3)
    exact=2*PI-3*a
    square=4*a-2*PI
    vs=[unit(v) for v in ((1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1))]
    assert abs(sum(dot(x,y) for x,y in itertools.combinations(vs,2))+2)<1e-12
    cells0=cells(vs)
    assert len(cells0)==14
    assert sum(v[0]==3 for v in cells0.values())==8
    assert sum(v[0]==4 for v in cells0.values())==6
    for k,ar in cells0.values():
        assert abs(ar-(exact if k==3 else square))<1e-10
    assert square>exact
    print('tetrahedral area: min=',format(exact,'.15f'),'quadrilateral=',format(square,'.15f'))
    rng=random.Random(20261117)
    success=0
    for _ in range(600):
        basis=[]
        for i in range(3):
            vv=[rng.gauss(0,1) for j in range(3)]
            basis.append(unit(vv))
        if abs(det(*basis))<0.04: continue
        w=[math.exp(rng.uniform(-0.7,0.7)) for i in range(3)]
        v3=unit(scale(-1,tuple(sum(w[k]*basis[k][j] for k in range(3)) for j in range(3))))
        vv=basis+[v3]
        if min(abs(det(*comb)) for comb in itertools.combinations(vv,3))<0.02: continue
        min_cell,areas,pers=test_normals(vv)
        assert max(areas)>=PI-2e-9
        assert max(pers)>=3*a-2e-9
        assert min_cell<=exact+2e-8
        success+=1
    assert success>=300,success
    # Strict pair smoothing in l'Huilier's formula, on the allowed triangle domain.
    count=0
    for _ in range(3000):
        total=rng.uniform(.2,PI-.01)
        frac=[rng.expovariate(1) for k in range(3)]
        X=[total*u/sum(frac) for u in frac]
        x,y,z=X
        product=lambda q,r:math.tan(q/2)*math.tan(r/2)
        avg=product((x+y)/2,(x+y)/2)
        assert product(x,y)<=avg*(1+1e-13)
        count+=1
    print('PASS:',success,'generic arrangements; 14 cells each; 4 face-polar area identities each;',count,'pair-smoothing comparisons.')

if __name__=='__main__': main()
