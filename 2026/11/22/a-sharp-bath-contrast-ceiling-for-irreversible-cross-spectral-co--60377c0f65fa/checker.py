"""Independent symbolic identities and exact arithmetic checks for a two-bath harmonic Langevin spectrum."""
import sympy as s

a,k,w,Tx,Ty=s.symbols('a k w Tx Ty', positive=True, real=True)
K=s.Matrix([[a,k],[k,a]]);D=s.diag(Tx,Ty)
S=2*(K+s.I*w*s.eye(2)).inv()*D*(K-s.I*w*s.eye(2)).inv()
Den=((a-k)**2+w**2)*((a+k)**2+w**2)
expect=s.Matrix([[2*((a*a+w*w)*Tx+k*k*Ty),-2*k*(a*(Tx+Ty)+s.I*w*(Tx-Ty))],[-2*k*(a*(Tx+Ty)-s.I*w*(Tx-Ty)),2*((a*a+w*w)*Ty+k*k*Tx)]])/Den
for i in range(2):
 for j in range(2):assert s.simplify(s.factor(S[i,j]-expect[i,j]))==0
v,z,t=s.symbols('v z t',positive=True,real=True)
I=v*z*(t-1)**2/((1+z+v*t)*(t*(1+z)+v))
dz=s.factor(s.diff(I,z))
assert s.simplify(dz/((t-1)**2*v)- (t*(1+v*t)*(1+v/t)-t*z*z)/((1+z+v*t)**2*(t*(1+z)+v)**2))==0
# Derivative of v/(A+t v)(tA+v) has sign t(A^2-v^2).
A=s.symbols('A',positive=True)
J=v/((A+t*v)*(t*A+v))
assert s.simplify(s.diff(J,v)-t*(A*A-v*v)/((A+t*v)**2*(t*A+v)**2))==0
# Boundary v=1 optimum square root thermal ratio.
rho=s.sqrt(t)
zb=(1+t)/rho
bound=(rho-1)**2/(t+1)
assert s.simplify(s.powdenest((I.subs({v:1,z:zb})-bound),force=True))==0
for tt in [s.Rational(1,9),s.Rational(1,4),s.Rational(1,2),s.Rational(2),s.Rational(4),s.Rational(9)]:
 for vv in [s.Rational(1,16),s.Rational(1,4),s.Rational(3,4),s.Rational(15,16)]:
  zz=s.sqrt((1+vv*tt)*(1+vv/tt))
  for factor in [s.Rational(1,4),s.Rational(1,2),s.Rational(3,2),s.Rational(4)]:
   assert bool((I.subs({t:tt,v:vv,z:zz})-I.subs({t:tt,v:vv,z:factor*zz})).evalf(40)>0)
  assert bool((bound.subs(t,tt)-I.subs({t:tt,v:vv,z:zz})).evalf(40)>0)
  assert bool((s.diff(I,v).subs({t:tt,v:vv,z:zz})).evalf(40)>0)
print('PASS: exact spectral matrix and derivatives; sharp boundary identity; 144 exact finite parameter comparisons')
