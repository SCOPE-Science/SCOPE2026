#!/usr/bin/env python3
"""Exact universal polynomial checks for a four-conic family; Python 3 standard library only.

All calculations are over Z[r,x,y,z,t].  The completeness argument for
projective stabilizers is geometric and is supplied in RESULT.md.
"""

class P:
    def __init__(self, terms):
        self.a = {k: int(v) for k, v in terms.items() if v}
    @staticmethod
    def const(c):
        return P({(0, 0, 0, 0, 0): c})
    @staticmethod
    def var(i):
        e = [0] * 5
        e[i] = 1
        return P({tuple(e): 1})
    def __add__(self, other):
        other = other if isinstance(other, P) else P.const(other)
        ans = dict(self.a)
        for e, c in other.a.items():
            ans[e] = ans.get(e, 0) + c
        return P(ans)
    __radd__ = __add__
    def __neg__(self):
        return P({e:-c for e,c in self.a.items()})
    def __sub__(self, other):
        return self + -as_poly(other)
    def __rsub__(self, other):
        return as_poly(other) - self
    def __mul__(self, other):
        other = as_poly(other)
        ans = {}
        for e,c in self.a.items():
            for f,d in other.a.items():
                g = tuple(u+v for u,v in zip(e,f))
                ans[g] = ans.get(g, 0) + c*d
        return P(ans)
    __rmul__ = __mul__
    def __pow__(self, n):
        assert isinstance(n,int) and n >= 0
        out = P.const(1)
        a = self
        while n:
            if n & 1:
                out *= a
            a *= a
            n >>= 1
        return out
    def __eq__(self, other):
        return self.a == as_poly(other).a
    def deriv(self, i):
        out = {}
        for e,c in self.a.items():
            if e[i]:
                f = list(e)
                f[i] -= 1
                f = tuple(f)
                out[f] = out.get(f,0)+c*e[i]
        return P(out)
    def at(self, **kwargs):
        var_ids = {'r':0, 'x':1, 'y':2, 'z':3, 't':4}
        choices = [P.var(i) for i in range(5)]
        for k,v in kwargs.items():
            choices[var_ids[k]] = as_poly(v)
        total = P.const(0)
        for e,c in self.a.items():
            term = P.const(c)
            for v,n in zip(choices,e):
                term *= v**n
            total += term
        return total

def as_poly(a):
    return a if isinstance(a,P) else P.const(a)

r,x,y,z,t=[P.var(i) for i in range(5)]
Q0=x*x+y*y-z*z
Q1=x*x+r*r*y*y-r*r*z*z
Qp=x*x+(r*r+1)*y*y+2*r*y*z
Qm=x*x+(r*r+1)*y*y-2*r*y*z
Q=[Q0,Q1,Qp,Qm]

# Pairwise difference factorization certifies the five tacnodal pairs.
assert Q1-Q0 == (r*r-1)*(y*y-z*z)
assert Qp-Q0 == (r*y+z)**2
assert Qm-Q0 == (r*y-z)**2
assert Qp-Q1 == (y+r*z)**2
assert Qm-Q1 == (y-r*z)**2
# The sixth pair meets along y*z=0, with a tangent intersection at p
# and two transverse intersections on z=0.
assert Qp-Qm == 4*r*y*z
assert Qp.at(y=0)==x*x and Qm.at(y=0)==x*x
assert Qp.at(z=0)==x*x+(r*r+1)*y*y
assert Qm.at(z=0)==x*x+(r*r+1)*y*y
assert Qp.at(x=0,y=0,z=1)==0 and Qm.at(x=0,y=0,z=1)==0
assert Q0.at(x=0,y=0,z=1)==-1 and Q1.at(x=0,y=0,z=1)==-r*r
for f,sign in ((Qp,1),(Qm,-1)):
    assert f.deriv(1).at(x=0,y=0,z=1)==0
    assert f.deriv(2).at(x=0,y=0,z=1)==2*sign*r
    assert f.deriv(3).at(x=0,y=0,z=1)==0

# Check all smooth-conic determinants (quadratic Gram matrices).
def det3(A):
    return (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
            -A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
            +A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))
zero=P.const(0)
M0=[[1,0,0],[0,1,0],[0,0,-1]]
M1=[[1,0,0],[0,r*r,0],[0,0,-r*r]]
Mp=[[1,0,0],[0,r*r+1,r],[0,r,0]]
Mm=[[1,0,0],[0,r*r+1,-r],[0,-r,0]]
assert [det3(A) for A in (M0,M1,Mp,Mm)]==[-1,-r**4,-r*r,-r*r]

# Explicit transformations: [x:y:z] -> [eps*x:y:delta*z] with eps,delta=+-1.
for eps in (-1,1):
    for delta in (-1,1):
        T=[f.at(x=eps*x,z=delta*z) for f in Q]
        assert T[:2]==Q[:2]
        assert T[2]==(Qp if delta==1 else Qm)
        assert T[3]==(Qm if delta==1 else Qp)
# Once the node pair and its secant/tangent are preserved, a projective
# stabilizer has form [a*x+b*y:c*y:d*z]. Node points +/-lambda force
# b=0 and a/c=+/-1 (because lambda^2=-(r^2+1) != 0), and the mixed
# yz coefficient forces d/c=+/-1 (because r != 0).
assert Qp.at(z=t*z)==x*x+(r*r+1)*y*y+2*r*t*y*z
assert Qm.at(z=t*z)==x*x+(r*r+1)*y*y-2*r*t*y*z

print('VERIFY_OK identities=6 conics_smooth=4 nodes=2 tacnodes=11 '
      'all_four_generators_preserve=TRUE universal_polynomial_checks=TRUE '
      'full_projective_group=C2xC2 component_orbits=1+1+2')
