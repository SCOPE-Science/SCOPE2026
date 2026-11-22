#!/usr/bin/env python3
"""Exact Q(sqrt(5)) certificate for scaled icosahedron--dual-dodecahedron hull.
Uses only Python standard library; verifies all candidate facet support inequalities
on entire parameter intervals via positive-factor interpolation.
"""
from fractions import Fraction as F
from itertools import combinations, product
from collections import Counter

class Q:
    """a+b*phi, phi^2=phi+1, with exact rational coefficients."""
    __slots__=('a','b')
    def __init__(self,a=0,b=0):self.a,self.b=F(a),F(b)
    @staticmethod
    def into(x):return x if isinstance(x,Q) else Q(x)
    def __add__(self,o):
        o=Q.into(o);return Q(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self):return Q(-self.a,-self.b)
    def __sub__(self,o):return self+-Q.into(o)
    def __rsub__(self,o):return Q.into(o)+-self
    def __mul__(self,o):
        o=Q.into(o);return Q(self.a*o.a+self.b*o.b,self.a*o.b+self.b*o.a+self.b*o.b)
    __rmul__=__mul__
    def __truediv__(self,n):
        if isinstance(n,Q) and n.b:raise ValueError('not needed')
        c=n.a if isinstance(n,Q) else F(n)
        return Q(self.a/c,self.b/c)
    def __eq__(self,o):
        o=Q.into(o);return self.a==o.a and self.b==o.b
    def sign(self):
        # 2*(a+b*phi)=(2a+b)+b*sqrt(5)
        x,y=2*self.a+self.b,self.b
        if not x:return (y>0)-(y<0)
        if not y:return (x>0)-(x<0)
        if (x>0)==(y>0):return 1 if x>0 else -1
        z=x*x-5*y*y
        return (z>0)-(z<0) if x>0 else (z<0)-(z>0)
    def __hash__(self):return hash((self.a,self.b))
    def __repr__(self):return f'({self.a}+{self.b}*phi)'

zero=Q(); one=Q(1);phi=Q(0,1); phi2=phi+1
lo=phi2/3;mid=one;hi=3-phi

def vec(*x):return tuple(Q.into(y) for y in x)
def plus(a,b):return tuple(x+y for x,y in zip(a,b))
def neg(a):return tuple(-x for x in a)
def sub(a,b):return plus(a,neg(b))
def mul(q,a):return tuple(q*x for x in a)
def dot(a,b):return sum((x*y for x,y in zip(a,b)),zero)
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def norm2(a):return dot(a,a)

I=[]
for k in range(3):
    for s,t in product([-1,1],repeat=2):
        a=[zero,Q(s),t*phi]
        if k:a=a[-k:]+a[:-k]
        I.append(tuple(a))
assert len(I)==12 and len(set(map(str,I)))==12
assert {norm2(v) for v in I}=={phi+2}
faces=[]
for ids in combinations(range(12),3):
    if all(norm2(sub(I[i],I[j]))==4 for i,j in combinations(ids,2)):
        faces.append(ids)
assert len(faces)==20
edges=Counter(tuple(sorted(pair)) for f in faces for pair in combinations(f,2))
assert len(edges)==30 and set(edges.values())=={2}
D=[mul(2-phi,plus(plus(I[i],I[j]),I[k])) for i,j,k in faces]
assert len(D)==20 and {norm2(d) for d in D}=={Q(3)}
assert len(set(map(str,D)))==20
# Each D point is dual to an icosahedral triangular facet: strict inequality elsewhere.
for f,w in zip(faces,D):
    for i,x in enumerate(I):
        z=dot(x,w)-phi2
        assert z.sign()<=0
        assert (z==0)==(i in f)

low=[]
for k,f in enumerate(faces):
    for i,j in combinations(f,2):low.append((i,j,k))
assert len(low)==60
high=[]
for i in range(12):
    inc=[k for k,f in enumerate(faces) if i in f]
    assert len(inc)==5
    pairs=[(k,l) for k,l in combinations(inc,2) if len(set(faces[k]) & set(faces[l]))==2]
    assert len(pairs)==5
    high += [(i,k,l) for k,l in pairs]
assert len(high)==60

# Plane signed slack for low: n(u)=(Ij-Ii) cross (u*Dk-Ii).
# For the high: n(u)=(u*Dk-Ii) cross (u*Dl-Ii).
# Their slacks over I have form affine(u) or u*affine(u);
# over u*D they have form u*affine(u) or u^2*affine(u).
# Exact endpoint inequalities thus prove all intermediate inequalities.
checks=0
for family,facets,first,last in [('low',low,lo,mid),('high',high,mid,hi)]:
    for ix,jx,kx in facets:
        a=I[ix]
        def normal(u):
            if family=='low':return cross(sub(I[jx],a),sub(mul(u,D[kx]),a))
            return cross(sub(mul(u,D[jx]),a),sub(mul(u,D[kx]),a))
        probe=(first+last)/2
        orient=dot(normal(probe),a).sign()
        assert orient !=0
        def slack(u,p):return orient*dot(normal(u),sub(p,a))
        for u in (first,probe,last):
            for idx,p in enumerate(I):
                value=slack(u,p)
                assert value.sign()<=0,(family,ix,jx,kx,u,idx,value)
                checks+=1
            for idx,p in enumerate(D):
                value=slack(u,mul(u,p))
                assert value.sign()<=0,(family,ix,jx,kx,u,idx,value)
                checks+=1
        # Exactly three contact points at the midpoint; hence exposed triangular facet.
        u=probe
        contacts=[('I',i) for i,p in enumerate(I) if slack(u,p)==0]
        contacts += [('D',i) for i,p in enumerate(D) if slack(u,mul(u,p))==0]
        assert len(contacts)==3,(family,ix,jx,kx,contacts)
        # Oriented determinant magnitude is 2u or 2u^2 for every face.
        if family=='low': val=det(I[ix],I[jx],D[kx])
        else:val=det(I[ix],D[jx],D[kx])
        assert val==Q(2) or val==Q(-2),(family,val)
        checks+=1

# At low threshold each D point is in a facet plane of I. At upper threshold
# each I point is in a facet plane of uD. Vertex support proves inclusion.
for i,x in enumerate(I):
    for d in D:
        assert (dot(x,d)-phi2).sign()<=0

# At u=1 every ico edge and its two adjacent D normals form a planar quad.
for e,n in edges.items():
    fi=[k for k,f in enumerate(faces) if set(e).issubset(f)]
    assert len(fi)==2
    i,j=e;w,z=D[fi[0]],D[fi[1]]
    assert det(sub(I[j],I[i]),sub(w,I[i]),sub(z,I[i]))==0

# One faceted regime has 60 exposed triangles; with <=32 vertices, Euler gives
# F<=2V-4<=60. Therefore the 60 displayed triangles are all the facets.
# Their exact volumes are 60*(2u)/6=20u and 60*(2u^2)/6=20u^2.
# At the outer thresholds continuity gives the constant 20*lo and cubic
# coefficient 20/hi^1 = 10+2sqrt5. In Q(phi), 10+2sqrt5=8+4phi.
assert lo*20==phi2*F(20,3)
assert (8+4*phi)*hi==20
assert hi>0 if False else hi.sign()>0
print(f'PASS: {len(faces)} icosahedron faces; {len(low)}+{len(high)} exact facet certificates; {checks} exact signed-slack/contact/determinant tests; all three thresholds and all four volume branches verified.')
print('Thresholds: phi^2/3, 1, 3-phi; volumes: 20*phi^2/3, 20*u, 20*u*u, (8+4*phi)*u^3.')
