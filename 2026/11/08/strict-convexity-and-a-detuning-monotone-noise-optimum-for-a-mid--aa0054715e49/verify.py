"""Independent reproducible checks of mean capture time and convex optimization.
Run: python verify.py (requires sympy, numpy)."""
from fractions import Fraction
import sympy as S
import numpy as np

x,z=S.symbols('x z',nonnegative=True,real=True)
Q=4*x**3+4*x**2+9*x+2
F=2*(2*x*x+x+1)/Q
T=S.Rational(7,2)+x+1/(2*x+1)+z*F
P=16*x**5-36*x**3+16*x**2+6*x+21
assert S.factor(S.diff(F,x,2)-4*(2*x+3)*P/Q**3)==0
assert S.factor(S.diff(F,x)+2*(8*x**4+8*x**3-2*x*x+7)/Q**2)==0
assert S.factor(S.diff(T,x,2) - (8/(2*x+1)**3 + z*4*(2*x+3)*P/Q**3))==0

# Exact Bernstein positivity on [0,3/2]; positive monomial coefficients on [3/2,infty).
y=S.symbols('y'); aa=S.Rational(3,2)
c=list(reversed(S.Poly(S.expand(P.subs(x,aa*y)),y).all_coeffs()))
b=[S.factor(sum(c[k]*S.binomial(i,k)/S.binomial(5,k) for k in range(i+1))) for i in range(6)]
assert b==[21,S.Rational(114,5),S.Rational(141,5),S.Rational(501,20),S.Rational(6,5),66], b
assert all(t>0 for t in S.Poly(S.expand(P.subs(x,y+aa)),y).all_coeffs())

# Reconstruct the physical no-click generator independently, not by using the T formula.
# Off-diagonal density entries rho_ij decay at rate x; sink rate = coupling = 1.
H=S.Matrix([[0,1,0],[1,S.symbols('d',real=True),1],[0,1,0]])
d=H[1,1]
vars=S.symbols('p0 p1 p2 u01 u02 u12 v01 v02 v12',real=True)
rho=S.diag(*vars[:3]); pairs=[(0,1),(0,2),(1,2)]
for (i,j),u,v in zip(pairs,vars[3:6],vars[6:9]):
    rho[i,j]=u+S.I*v;rho[j,i]=u-S.I*v
L=-S.I*(H*rho-rho*H)
for i in range(3):
    for j in range(3):
        if i!=j:L[i,j]-=x*rho[i,j]
        if i==2 or j==2:L[i,j]-=S.Rational(int(i==2)+int(j==2),2)*rho[i,j]
comps=[L[i,i] for i in range(3)]+[S.re(L[i,j]) for i,j in pairs]+[S.im(L[i,j]) for i,j in pairs]
A=S.linear_eq_to_matrix(comps,vars)[0]
source=S.zeros(9,1);source[1]=-1
# Prove exact generator formula with exact inverses for 7 rational witnesses.
for rate,gap in [(S.Rational(0),0),(S.Rational(1,5),0),(S.Rational(3,7),S.Rational(1,2)),(S.Rational(1),2),(S.Rational(5,2),S.Rational(13,4)),(S.Rational(17,3),7),(S.Rational(23),11)]:
    B=A.subs({x:rate,d:gap}); obs=B.inv()*source
    exact=S.factor(sum(obs[i] for i in range(3)))
    assert S.simplify(exact-T.subs({x:rate,z:gap**2}))==0,(rate,gap,exact)

# Independent complex Liouvillian reconstruction through vectorization and Kronecker products.
for rate,gap in [(0.04,0.3),(0.3,3),(1.0,1.4),(2.5,9),(10,20)]:
    mat=np.array([[0.,1.,0.],[1.,gap,1.],[0.,1.,0.]],complex)
    proj=np.diag([0.,0.,1.]); eye=np.eye(3)
    Lc=-1j*(np.kron(eye,mat)-np.kron(mat.T,eye)) -0.5*(np.kron(eye,proj)+np.kron(proj.T,eye))
    for i in range(3):
        for j in range(3):
            if i!=j:Lc[i+3*j,i+3*j]-=rate
    start=np.zeros(9,complex);start[1+3*1]=-1
    integrated=np.linalg.solve(Lc,start).reshape(3,3,order='F')
    actual=float(np.trace(integrated).real)
    predicted=float(T.subs({x:rate,z:gap**2}))
    assert abs(actual-predicted)<1e-8*max(1,abs(predicted)),(rate,gap,actual,predicted)

# Unique minimizer and strictly increasing dependence on detuning, numerical sanity witnesses.
roots=[]
for gap in [0,0.1,1,2,4,10,20,50]:
    zz=gap**2
    deriv=S.lambdify(x,S.diff(T,x).subs(z,zz),'numpy')
    lo,hi=0.,max(10.,4*gap)
    assert deriv(lo)<0 and deriv(hi)>0
    for _ in range(80):
        m=(lo+hi)/2
        if deriv(m)<0:lo=m
        else:hi=m
    roots.append((gap,(lo+hi)/2))
assert roots[0][1]>0.2 and all(roots[i][1]<roots[i+1][1] for i in range(len(roots)-1))
print('PASS: exact generator reconstruction, independent complex resolvent, Bernstein certificates, derivatives, monotone root witnesses')
print('Bernstein certificates:',b)
print('Optima (detuning, dephasing):',roots)
