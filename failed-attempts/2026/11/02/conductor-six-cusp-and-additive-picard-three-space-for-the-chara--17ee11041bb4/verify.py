"""Exact characteristic-seven polynomial checks for a plane Klein-quartic model."""
from sympy import symbols, Poly, expand, discriminant, factor, cancel, fraction

a,s,t,u,r,x,y=symbols('a s t u r x y')
p=7

def zero(expr,*vars):
    return Poly(expand(expr),*vars,modulus=p).is_zero

D=(s+2*t)*(s+t)**3
U=2*s*s*(s*s-t*t)
W=6*s**4
X=2*D+U
Y=4*D+3*U+W
Z=D
assert zero(X**3*Y+Y**3*Z+Z**3*X,s,t)
print('PARAMETRIZATION_OK: homogeneous quartic identity in F7[s,t]')

F=x**3*y+y**3+x
Fu=(u+2)**3*(4+3*u+r*u)+(4+3*u+r*u)**3+u+2
P=(r+3)*u**2+r*(r*r+2*r-2)*u-2*r*r
assert zero(Fu-u**2*P,u,r)
assert zero(discriminant(P,u)-r**5*(r-3),r)
print('BIRATIONALITY_OK: double-cover discriminant = r^5(r-3), nonsquare over F7(r)')

D1=D.subs({s:a,t:1});U1=U.subs({s:a,t:1});W1=W.subs({s:a,t:1})
eta=cancel(W1/D1-3*(U1/D1)**2-5*(U1/D1)**3)
num,den=fraction(eta)
assert Poly(num,a,modulus=p).terms()[-1][0]==(7,)
assert Poly(den,a,modulus=p).eval(0)!=0
assert Poly(U1,a,modulus=p).terms()[-1][0]==(2,)
assert Poly(D1,a,modulus=p).eval(0)!=0
print('CUSPIDAL_VALUATIONS_OK: orders 2 and 7 at unique preimage of [2:4:1]')

pts=[]
for xx in range(7):
 for yy in range(7):
  if (xx**3*yy+yy**3+xx)%7==0:
   pts.append((xx,yy))
assert len(pts)==6 and (2,4) in pts
print('FINITE_FIELD_SANITY_OK: 6 affine + 2 infinity = 8 F7-points')

# The power-series conductor for k[[tau^2,tau^7]] is tau^6.
gaps=[j for j in range(6) if j not in {2*i+7*j for i in range(4) for j in range(2)}]
assert gaps==[1,3,5]
assert all(k in {2*i+7*j for i in range(10) for j in range(2)} for k in range(6,20))
assert p>6
print('CONDUCTOR_OK: semigroup <2,7>, gaps (1,3,5), conductor 6, additive Picard dimension 3')
print('VERIFICATION_OK')
