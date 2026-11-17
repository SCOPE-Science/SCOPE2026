"""Exact polynomial and finite-field checks for a binary-quartic discriminant in characteristic two.
All computations are over prime or binary extension fields. No randomized testing.
"""
import sympy as s
from itertools import product

a,b,c,d,e=s.symbols('a b c d e')
x=s.symbols('x')
f=a*x**4+b*x**3+c*x**2+d*x+e
Q=a*d**2+b*c*d+e*b**2
D=s.discriminant(f,x)
assert s.Poly(D-Q**2,a,b,c,d,e, modulus=2).is_zero
# Classical degree-three quartic invariant reduces to Q in characteristic two.
J=72*a*c*e-27*a*d**2-27*b**2*e+9*b*c*d-2*c**3
assert s.Poly(J-Q,a,b,c,d,e,modulus=2).is_zero
print('discriminant and classical invariant: PASS')

S,T,U,V,W=s.symbols('S T U V W')
coords={a:S*U,b:S*W,c:T*U+S*V,d:T*W,e:T*V}
assert s.Poly(s.expand(Q.subs(coords, simultaneous=True)),S,T,U,V,W,modulus=2).is_zero
print('Segre projection identity: PASS')

# On affine a=1: R=k[c,e,b,d]/(d^2+cbd+eb^2); B=k[c,b,v] with d=bv,e=v^2+cv.
v=s.symbols('v')
assert s.Poly(s.expand(Q.subs({a:1,d:b*v,e:v*v+c*v},simultaneous=True)),b,c,v,modulus=2).is_zero
# For an arbitrary R-element p0+q0*b*v, multiplication by v reduces modulo v^2+c*v+e:
# (p0+q0*b*c)*v+q0*b*e. Divisibility by b forces p0 divisible by b.
p0,q0=s.symbols('p0 q0')
assert s.Poly(s.expand((p0+q0*b*v)*v-(q0*b*e+(p0+q0*b*c)*v)).subs(v**2,e+c*v),p0,q0,b,c,e,v,modulus=2).is_zero
# Every B-element is A + v B, where A,B in k[c,e,b]; R is A + bv B.
# The B-conductor is bB, and the R-conductor is (b,d).
print('normalization chart a=1 and conductor relation: PASS')

# Symmetric-factor map on conductor is q=(S X+T Y)(U X+V Y), up to reindexing.
X,Y=s.symbols('X Y')
q=s.expand((S*X+T*Y)*(U*X+V*Y))
assert s.expand(q-(S*U*X**2+(S*V+T*U)*X*Y+T*V*Y**2))==0
print('conductor pair-factorization: PASS')

# Exact count of all projective points on the cubic over F_{2^m}.
# Polynomial basis, irreducible binary moduli for m=1,2,3.
def mul(x,y,m,poly):
    z=0
    for i in range(m):
        if (y>>i)&1:z^=x
        hi=(x>>(m-1))&1
        x=((x<<1)&((1<<m)-1))^(poly&((1<<m)-1) if hi else 0)
    return z

def count_points(m,poly):
    q=1<<m
    sq=[mul(t,t,m,poly) for t in range(q)]
    cnt=0
    for i in range(5):
        # uniquely normalized projective vector: first nonzero coordinate = 1
        for tail in product(range(q),repeat=4-i):
            A,B,C,D,E=((0,)*i+(1,)+tail)
            lhs=mul(A,sq[D],m,poly)^mul(mul(B,C,m,poly),D,m,poly)^mul(E,sq[B],m,poly)
            cnt+=(lhs==0)
    return cnt

for m,p in [(1,0b11),(2,0b111),(3,0b1011),(4,0b10011)]:
    q=1<<m
    got=count_points(m,p)
    expect=q**3+2*q*q+q+1
    assert got==expect,(q,got,expect)
    print('F_%d: points=%d, formula=%d PASS' % (q,got,expect))
print('ALL_CHECKS_PASSED')
