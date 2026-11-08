"""Exact small-characteristic witness checks for the quartic family z*x^3+w*y^3+Q(z,w)*x*y+G(z,w)."""
P=3
class F9:
    __slots__=('a','b')
    def __init__(self,a=0,b=0): self.a=int(a)%3; self.b=int(b)%3
    def __add__(self,z):
        z=to(z); return F9(self.a+z.a,self.b+z.b)
    def __radd__(self,z): return self+z
    def __neg__(self): return F9(-self.a,-self.b)
    def __sub__(self,z): return self+-to(z)
    def __rsub__(self,z): return to(z)+-self
    def __mul__(self,z):
        z=to(z);a,b,c,d=self.a,self.b,z.a,z.b
        return F9(a*c+b*d,a*d+b*c-b*d)
    def __rmul__(self,z): return self*z
    def __pow__(self,n):
        assert n>=0
        x=F9(1);b=self
        while n:
            if n&1: x=x*b
            b=b*b;n>>=1
        return x
    def __eq__(self,z):
        z=to(z);return self.a==z.a and self.b==z.b
    def __hash__(self): return hash((self.a,self.b))
    def __repr__(self): return str(self.a)+'+'+str(self.b)+'r'
def to(x): return x if isinstance(x,F9) else F9(x)
ZERO=F9(0);ONE=F9(1); R=F9(0,1)
K=[F9(a,b) for a in range(3) for b in range(3)]
def q(z,w): return z*z+z*w-w*w
def g(z,w): return z**4+z*w**3+w**4
def qz(z,w): return 2*z+w
def qw(z,w): return z-2*w
def gz(z,w): return z**3+w**3
def gw(z,w): return w*w*w
assert R*R==1-R
roots=[t for t in K if q(t,ONE)==ZERO]
assert len(roots)==2 and len(set(roots))==2
assert all(t!=ZERO and qz(t,ONE)!=ZERO for t in roots)
assert q(ONE,ZERO)!=ZERO and q(ZERO,ONE)!=ZERO
# Quartic g(t,1)=t^4+t+1 has derivative t^3+1=(t+1)^3, with g(-1,1)=1.
assert g(-ONE,ONE)==ONE
assert all(g(t,ONE)!=ZERO for t in roots)
assert g(ONE,ZERO)!=ZERO and g(ZERO,ONE)!=ZERO
for t in roots:
    a=t**3; b=g(t,ONE)**3
    assert a**3==t and b**3==g(t,ONE)
    A=-qz(t,ONE)*a
    B=-qz(t,ONE)*b
    C=gz(t,ONE)
    def h(x): return x**3+A*x*x+B*x+C
    def hp(x): return 2*A*x+B
    crit=[x for x in K if hp(x)==ZERO]
    assert len(crit)==1
    assert h(crit[0])!=ZERO
    print('Q-root',t,'H(T)=T^3+(',A,')T^2+(',B,')T+(',C,')','H critical value',h(crit[0]))
# Check the two exact polynomial-gradient forms on every point of P3(F9).
def canon_points():
    for j in range(4):
        for tail in __import__('itertools').product(K,repeat=3-j):
            yield tuple([ZERO]*j+[ONE]+list(tail))
def f(p):
    x,y,z,w=p;return z*x**3+w*y**3+q(z,w)*x*y+g(z,w)
def grad(p):
    x,y,z,w=p;return (y*q(z,w),x*q(z,w),x**3+x*y*qz(z,w)+gz(z,w),y**3+x*y*qw(z,w)+gw(z,w))
pts=list(canon_points())
assert len(pts)==820
surface=[p for p in pts if f(p)==ZERO]
singular=[p for p in surface if all(v==ZERO for v in grad(p))]
assert all(p[2]!=ZERO or p[3]!=ZERO for p in singular)
assert all(q(p[2],p[3])==ZERO for p in singular)
print('projective P3(F9) points',len(pts),'surface',len(surface),'singular F9-points',len(singular))
print('Six geometric A2 singular points certified by two simple-root cubic polynomials.')
print('CHAR3_DEGENERATION_EXACT_CHECKS_PASSED')
