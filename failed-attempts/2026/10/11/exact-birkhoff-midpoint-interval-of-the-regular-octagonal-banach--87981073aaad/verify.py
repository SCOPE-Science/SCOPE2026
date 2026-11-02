from fractions import Fraction as F

class Q2:
    __slots__=("a","b")
    def __init__(self,a=0,b=0):
        if isinstance(a,Q2) and b==0:
            self.a,self.b=a.a,a.b
        else:
            self.a=F(a); self.b=F(b)
    def __add__(self,o):
        o=q(o); return Q2(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return Q2(-self.a,-self.b)
    def __sub__(self,o): return self+(-q(o))
    def __rsub__(self,o): return q(o)-self
    def __mul__(self,o):
        o=q(o); return Q2(self.a*o.a+2*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def inv(self):
        d=self.a*self.a-2*self.b*self.b
        assert d
        return Q2(self.a/d,-self.b/d)
    def __truediv__(self,o): return self*q(o).inv()
    def __rtruediv__(self,o): return q(o)/self
    def sign(self):
        a,b=self.a,self.b
        if a==0 and b==0:return 0
        if b==0:return 1 if a>0 else -1
        if a==0:return 1 if b>0 else -1
        if a>0 and b>0:return 1
        if a<0 and b<0:return -1
        c=a*a-2*b*b
        if a>0 and b<0:return 1 if c>0 else -1
        if a<0 and b>0:return -1 if c>0 else 1
        raise AssertionError
    def __lt__(self,o): return (self-q(o)).sign()<0
    def __le__(self,o): return (self-q(o)).sign()<=0
    def __eq__(self,o):
        try:o=q(o)
        except Exception:return False
        return self.a==o.a and self.b==o.b
    def __repr__(self): return f"Q2({self.a},{self.b})"

def q(x): return x if isinstance(x,Q2) else Q2(x)

rt2=Q2(0,1)
r=rt2-1
qv=rt2/2
d=2-rt2
L=3*rt2/2-1
U=1+rt2/2

facets=[
    (Q2(1),Q2(0)),
    (rt2/2,rt2/2),
    (Q2(0),Q2(1)),
    (-rt2/2,rt2/2),
    (Q2(-1),Q2(0)),
    (-rt2/2,-rt2/2),
    (Q2(0),Q2(-1)),
    (rt2/2,-rt2/2),
]

def dot(f,v): return f[0]*v[0]+f[1]*v[1]
def add(u,v): return (u[0]+v[0],u[1]+v[1])
def sub(u,v): return (u[0]-v[0],u[1]-v[1])

def norm(v):
    vals=[dot(f,v) for f in facets]
    m=vals[0]
    for z in vals[1:]:
        if m<z:m=z
    return m

a=(Q2(1),r)
b=(r,Q2(1))
diag=(rt2/2,rt2/2)
axis=(Q2(1),Q2(0))
k=(qv,-qv)
down=(Q2(0),Q2(-1))

assert norm(a)==norm(b)==norm(k)==norm(down)==1
assert dot(axis,a)==1 and dot(diag,a)==1
assert dot(diag,k)==0
assert dot(axis,down)==0

def cert_segment(z0,z1,g0,g1,active):
    # For z(t)=(1-t)z0+t z1 and g(t)=(1-t)g0+t g1,
    # every signed facet is <= g at both endpoints, hence throughout.
    for f in facets:
        assert dot(f,z0)<=g0
        assert dot(f,z1)<=g1
    assert dot(active,z0)==g0
    assert dot(active,z1)==g1

# Smooth edge, y=k and y=-k.
cert_segment(add(a,k),add(b,k),U,L,axis)
cert_segment(sub(a,k),sub(b,k),L,U,(Q2(0),Q2(1)))

# Vertex support sector C1: y=(s,-1), s:0 -> r.
c10=(Q2(0),Q2(-1))
c11=(r,Q2(-1))
cert_segment(add(a,c10),add(a,c11),L,rt2,(rt2/2,-rt2/2))
cert_segment(sub(a,c10),sub(a,c11),U,rt2,diag)

# Vertex support sector C2: y=(s,s-sqrt2), s:r -> 1/sqrt2.
c20=(r,r-rt2)
c21=(qv,qv-rt2)
assert c20==c11
cert_segment(add(a,c20),add(a,c21),rt2,U,axis)
cert_segment(sub(a,c20),sub(a,c21),rt2,L,(Q2(0),Q2(1)))

# Algebra and endpoint witnesses.
assert U-L==d
assert norm(add(a,down))==L
assert norm(add(a,k))==U

delta=1-U/2
rho=1-L/2
assert delta==(2-rt2)/4
assert rho==3*(2-rt2)/4
assert rho==3*delta

print("VERIFY_OK facets=8 segment_certificates=6 interval=[3sqrt2/2-1,1+1/sqrt2]")
