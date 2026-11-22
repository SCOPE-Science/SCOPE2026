#!/usr/bin/env python3
"""Independent finite geometry and equality-family checks (Python standard library)."""
import math, random, itertools

PI=math.pi

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def mul(a,c): return tuple(x*c for x in a)
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def norm(a): return math.sqrt(dot(a,a))
def unit(a): return mul(a,1/norm(a))
def gap(a,b): return math.acos(max(-1.,min(1.,dot(a,b))))
def form_normals(x,y,z):
    w=math.sqrt(x*x+y*y+z*z)
    return [tuple(t/w for t in v) for v in [(x,y,z),(x,-y,-z),(-x,y,-z),(-x,-y,z)]]
def polygon(n,signs):
    signed=[mul(v,s) for v,s in zip(n,signs)]
    verts=[]
    for i,j in itertools.combinations(range(4),2):
        v=unit(cross(n[i],n[j]))
        for s in (-1,1):
            w=mul(v,s)
            if all(dot(w,u)>=-1e-9 for u in signed) and not any(norm(add(w,mul(z,-1)))<1e-7 for z in verts):
                verts.append(w)
    if len(verts)<3: return None
    c=unit(tuple(sum(v[k] for v in verts) for k in range(3)))
    e1=unit(add(verts[0],mul(c,-dot(verts[0],c))))
    e2=cross(c,e1)
    ordered=sorted(verts,key=lambda v:math.atan2(dot(v,e2),dot(v,e1)))
    return sum(gap(ordered[i],ordered[(i+1)%len(ordered)]) for i in range(len(ordered))),len(verts)
def cells(n):
    return {s:polygon(n,s) for s in itertools.product((-1,1),repeat=4) if len(set(s))==2}

def sphere_face_area(u,v,w):
    # Oosterom-Strackee independent area calculation from the normal-triple Gram matrix.
    return 2*math.atan2(abs(dot(u,cross(v,w))),1+dot(u,v)+dot(v,w)+dot(w,u))

def close(a,b,eps=3e-7):
    assert abs(a-b)<eps,(a,b)

def main():
    rng=random.Random(20261117)
    total=0
    for j in range(500):
        xyz=[rng.random()+.01 for _ in range(3)]
        x,y,z=[t/norm(xyz) for t in xyz]
        n=form_normals(x,y,z)
        cc=cells(n)
        assert len(cc)==14 and all(v is not None for v in cc.values())
        tris=[v[0] for s,v in cc.items() if s.count(1) in (1,3)]
        quads=[v[0] for s,v in cc.items() if s.count(1)==2]
        assert len(tris)==8 and len(quads)==6
        for p in tris: close(p,PI)
        close(sum(tris),8*PI)
        close(sum(v[0] for v in cc.values()),16*PI)
        q_theory=[2*PI-4*math.atan(y*z/x),2*PI-4*math.atan(x*z/y),2*PI-4*math.atan(x*y/z)]
        for q in q_theory:
            assert sum(abs(q-v)<1e-7 for v in quads)==2,(q,quads)
        m=min(v[0] for v in cc.values())
        close(m,min(PI,*q_theory))
        feasible=(y*z<=x and x*z<=y and x*y<=z)
        assert (m>=PI-1e-8)==feasible,(xyz,feasible,m)
        total+=1
    # One exact rational nonregular optimizer, a non-optimizer, and a boundary equality.
    for xyz,expected in [((4,4,7),True),((1,2,2),False)]:
        a,b,c=[t/norm(xyz) for t in xyz]
        m=min(v[0] for v in cells(form_normals(a,b,c)).values())
        assert (m>=PI-1e-8)==expected
    a=math.sqrt(2)-1
    b=c=math.sqrt(math.sqrt(2)-1)
    close(a*a+b*b+c*c,1)
    close(b*c,a)
    close(min(v[0] for v in cells(form_normals(a,b,c)).values()),PI)
    for j in range(400):
        n=[unit(tuple(rng.uniform(-1,1) for k in range(3))) for i in range(3)]
        weights=[1+rng.random() for i in range(3)]
        n.append(unit(mul(tuple(sum(n[i][k]*weights[i] for i in range(3)) for k in range(3)),-1)))
        cc=cells(n)
        assert len(cc)==14 and all(v is not None for v in cc.values())
        tris=[v[0] for s,v in cc.items() if s.count(1) in (1,3)]
        assert len(tris)==8 and all(cc[s][1]==3 for s in cc if s.count(1) in (1,3))
        close(sum(tris),8*PI)
        # Compare each triangle with the polar area of its three normals.
        for i in range(4):
            signs=tuple(1 if k==i else -1 for k in range(4))
            complement=[n[k] for k in range(4) if k!=i]
            close(cc[signs][0],2*PI-sphere_face_area(*complement))
        assert min(v[0] for v in cc.values()) <=PI+1e-8
        total+=1
    print('PASS:',total,'nondegenerate configurations; 14-cell polygon reconstructions,',
          'triangular sum, min bound, disphenoid equality and exact 3-quadrilateral formulas')
if __name__=='__main__': main()
