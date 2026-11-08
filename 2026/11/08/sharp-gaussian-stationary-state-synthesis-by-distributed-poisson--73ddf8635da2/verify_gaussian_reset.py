"""Exact-rational checks for Gaussian steady-state synthesis by Poisson resetting.

Dependency: SymPy 1.12 or later. Run: python verify_gaussian_reset.py.
The analytical proof is in RESULT.md; these finite tests are diagnostics only.
"""
from math import comb, factorial
import sympy as s

x, y = s.symbols('x y', real=True)
I = s.eye(2)
D = s.Integer(1)
K = s.diag(1, 4)
Sigma = s.diag(2, s.Rational(1, 2))
m = s.Matrix([1, 0])
z = s.Matrix([x, y])
B = (K * Sigma + Sigma * K)/2 - D*I
c = s.trace(K) - D*s.trace(Sigma.inv())
a = K*m
rmin = s.factor(c + (a.T*B.inv()*a)[0]/4)
v = Sigma.inv()*(z-m)
q = s.expand((v.T*B*v)[0]+(a.T*v)[0]+rmin-c)
ratio = s.expand(q/rmin)
assert B == I and c == s.Rational(5,2)
assert rmin == s.Rational(11,4)
assert s.factor(q - ((v+s.Rational(1,2)*B.inv()*a).T*B*(v+s.Rational(1,2)*B.inv()*a))[0]) == 0

def normal_moment(n, mean, var):
    return sum(s.Integer(comb(n,j))*mean**(n-j)*s.factorial2(j-1)*var**(j//2) for j in range(0,n+1,2))

def ep(expr):
    pol = s.Poly(s.expand(expr), x, y)
    return s.factor(sum(coef*normal_moment(i,1,2)*normal_moment(j,0,s.Rational(1,2)) for (i,j),coef in pol.terms()))

assert ep(ratio) == 1
assert ep(x*ratio)==1+s.Rational(1,rmin)
assert ep(y*ratio)==0
assert ep(x*x*ratio) == ep(x*x)+s.factor((2*B[0,0]+2*a[0]*m[0])/rmin)
assert ep(y*y*ratio) == ep(y*y)+2*B[1,1]/rmin
ncheck = 0
for total in range(0,10):
    for i in range(total+1):
        j = total-i
        f=x**i*y**j
        Lf=-(i+4*j)*f + (i*(i-1)*x**(i-2)*y**j if i>=2 else 0) + (j*(j-1)*x**i*y**(j-2) if j>=2 else 0)
        assert ep(Lf)+rmin*(ep(ratio*f)-ep(f))==0, (i,j)
        ncheck+=1
# A feasible, genuinely noncommuting covariance with a noncentral mean.
Sigma2=s.Matrix([[2,s.Rational(1,4)],[s.Rational(1,4),s.Rational(5,4)]])
m2=s.Matrix([1,s.Rational(1,2)])
B2=(K*Sigma2+Sigma2*K)/2-I
c2=s.trace(K)-s.trace(Sigma2.inv())
a2=K*m2
r2=s.factor(c2+(a2.T*B2.inv()*a2)[0]/4)
assert B2.det()>0 and B2[0,0]>0
assert r2>c2>0
v2=Sigma2.inv()*(z-m2)
quad2=s.expand((v2.T*B2*v2)[0]+(a2.T*v2)[0]+r2-c2)
square2=s.expand(((v2+B2.inv()*a2/2).T*B2*(v2+B2.inv()*a2/2))[0])
assert s.expand(quad2-square2)==0
assert s.simplify(c2-s.trace(B2*Sigma2.inv()))==0
# A Gaussian covariance strictly above the thermal covariance is not sufficient.
Sigma0=K.inv()
Delta=s.Matrix([[1,s.Rational(9,10)],[s.Rational(9,10),1]])
Sigma_bad=Sigma0+Delta
Bbad=(K*Sigma_bad+Sigma_bad*K)/2-I
assert Delta.det()>0 and Delta[0,0]>0
assert Sigma_bad.det()>0 and Sigma_bad[0,0]>0
assert Bbad.det() == -s.Rational(17,16)
# Exact Fourier-side identity for Gaussian reset densities, valid for any d.
t1,t2=s.symbols('t1 t2',real=True)
tvec=s.Matrix([t1,t2])
# Weighted Gaussian characteristic factor: E[(X-m)exp(i t.X)]/phi=i Sigma t.
# Consequently E[v exp(i t.X)]/phi=i t, and E[v v^T exp(i t.X)]/phi=Sigma^-1 -tt^T.
reset_fourier_factor= s.factor((r2-c2+s.I*(a2.T*tvec)[0]+s.trace(B2*Sigma2.inv())-(tvec.T*B2*tvec)[0])/r2)
expected_factor=1+(s.I*(a2.T*tvec)[0]-(tvec.T*B2*tvec)[0])/r2
assert s.simplify(reset_fourier_factor-expected_factor)==0
# Singular Lyapunov defect: shifts in the zero-defect direction are impossible.
Sigmas=s.diag(2,s.Rational(1,4))
Bs=(K*Sigmas+Sigmas*K)/2-I
assert Bs==s.diag(1,0)
assert (K*s.Matrix([0,1]))[1] != 0 and Bs[1,1]==0
print(f'PASS: {ncheck} exact polynomial stationarity identities; threshold {rmin}; noncommuting threshold {r2}; indefinite defect {Bbad.det()}.')
