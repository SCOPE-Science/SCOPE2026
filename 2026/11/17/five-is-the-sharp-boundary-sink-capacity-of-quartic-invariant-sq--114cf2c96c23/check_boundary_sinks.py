"""Exact rational-quadratic witness checker for an invariant-square flow.

Only uses the Python standard library; all signs and identities are exact.
"""
from fractions import Fraction as Q


class Quad:
    """An exact element of Q(sqrt(d)), with rational a,b."""
    def __init__(self, a=0, b=0, d=1):
        self.a, self.b, self.d = Q(a), Q(b), d
    def cv(self, other):
        if isinstance(other, Quad):
            assert self.d == other.d or self.b == 0 or other.b == 0
            if other.d != self.d and other.b == 0:
                return Quad(other.a, 0, self.d)
            return other
        return Quad(other, 0, self.d)
    def __add__(self, other):
        t = self.cv(other)
        return Quad(self.a + t.a, self.b + t.b, self.d)
    __radd__ = __add__
    def __neg__(self):
        return Quad(-self.a, -self.b, self.d)
    def __sub__(self, other):
        return self + (-self.cv(other))
    def __rsub__(self, other):
        return (-self) + other
    def __mul__(self, other):
        t = self.cv(other)
        return Quad(self.a*t.a + self.b*t.b*self.d, self.a*t.b + self.b*t.a, self.d)
    __rmul__ = __mul__
    def sign(self):
        a, b = self.a, self.b
        if b == 0: return (a > 0) - (a < 0)
        if a == 0: return (b > 0) - (b < 0)
        if a*b > 0: return (a > 0) - (a < 0)
        c = a*a - self.d*b*b
        if c > 0: return (a > 0) - (a < 0)
        if c < 0: return (b > 0) - (b < 0)
        return 0
    def __repr__(self):
        return '(%s)+(%s)*sqrt(%s)' % (self.a,self.b,self.d)


def f(x, y):
    return 3600*x*x - 720*x + 3025*y*y - 1053


def g(x, y):
    return 5625*x*x + 4225*y*y - 1690*y - 1352


u_minus = Quad(Q(1,10), -Q(11,120), 11)
u_plus = Quad(Q(1,10), Q(11,120), 11)
v_minus = Quad(Q(1,5), -Q(3,130), 51)
v_plus = Quad(Q(1,5), Q(3,130), 51)

assert all((u + Q(1,2)).sign() > 0 and (Q(1,2) - u).sign() > 0 for u in (u_minus,u_plus,v_minus,v_plus))
assert all(f(u,y).sign() == 0 for u in (u_minus,u_plus) for y in (-Q(1,2), Q(1,2)))
assert all(g(x,v).sign() == 0 for v in (v_minus,v_plus) for x in (-Q(1,2), Q(1,2)))

counts = {'sink':0, 'saddle':0, 'source':0}

def classify(lam1, lam2):
    s1 = lam1.sign() if isinstance(lam1, Quad) else (lam1>0)-(lam1<0)
    s2 = lam2.sign() if isinstance(lam2, Quad) else (lam2>0)-(lam2<0)
    assert s1 != 0 and s2 != 0
    cls = 'sink' if s1<0 and s2<0 else 'source' if s1>0 and s2>0 else 'saddle'
    counts[cls]+=1
    return cls

for y in (-Q(1,2), Q(1,2)):
    for x in (u_minus,u_plus):
        tangent = (4*x*x-1)*(7200*x-720)
        normal = 8*y*g(x,y)
        cls = classify(tangent, normal)
        assert (cls == 'sink') == (x is u_plus)
for x in (-Q(1,2), Q(1,2)):
    for y in (v_minus,v_plus):
        tangent = (4*y*y-1)*(8450*y-1690)
        normal = 8*x*f(x,y)
        cls = classify(tangent, normal)
        assert (cls == 'sink') == (y is v_plus)
for x in (-Q(1,2), Q(1,2)):
    for y in (-Q(1,2), Q(1,2)):
        cls = classify(8*x*f(x,y), 8*y*g(x,y))
        assert (cls == 'sink') == (x<0 and y<0)

assert counts == {'sink':5,'saddle':6,'source':1}, counts
assert f(-Q(1,2),-Q(1,2)) == Q(3853,4)
assert g(-Q(1,2),-Q(1,2)) == Q(3911,2)
print('INVARIANT_SQUARE_SHARP_FIVE_BOUNDARY_SINKS_OK',counts)
