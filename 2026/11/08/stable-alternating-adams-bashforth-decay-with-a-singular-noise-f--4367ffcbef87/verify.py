"""Exact checks for alternating-step Adams--Bashforth scalar decay.

Requires Python 3.10+ and SymPy 1.14.0. This script checks algebraic
identities and finite rational examples; the analytic proof covers
all admissible real parameters.
"""
from fractions import Fraction
from sympy import symbols, Matrix, Rational, eye, factor, simplify, limit, solve, oo
from sympy import zeros

a,b=symbols('a b', positive=True)

def T(h,old):
    return Matrix([[1-h-h*h/(2*old),h*h/(2*old)],[1,0]])

def eq(x,y):
    assert simplify(x-y)==0, (x,y)

H,L=T(a,b),T(b,a)
M=L*H
Mswap=H*L
tr=1-(a+b)+(a+b)**2/2+a*b/4
de=a*b/4
assert simplify(M.trace()-tr)==0
assert simplify(M.det()-de)==0
eq(1-tr+de,(a+b)*(2-a-b)/2)
eq(1+tr+de,((a+b-1)**2+a*b+3)/2)

c=1-b+b*b/2
M0=Matrix([[c,0],[1,0]])
assert M.applyfunc(lambda x: limit(x,a,0,dir='+'))==M0
N=Matrix([[-1,1],[-1,1]])
assert (a*Mswap).applyfunc(lambda x: limit(x,a,0,dir='+'))==b*b*N/2
v=L*Matrix([1,0])
assert (a*v).applyfunc(lambda x: limit(x,a,0,dir='+'))==Matrix([-b*b/2,0])
assert simplify((1-c*c)-(b-b*b/2)*(2-b+b*b/2))==0

# Stationary covariance P solves the periodic Lyapunov equation.
# For b=1 solve exactly and verify the rational closed form.
z=symbols('z',positive=True)
Hb,Lb=T(z,Rational(1)),T(Rational(1),z)
Mb=Lb*Hb
vb=Lb*Matrix([1,0])
W=vb*vb.T+Matrix([[1,0],[0,0]])
X,Y,Z=symbols('X Y Z')
P=Matrix([[X,Y],[Y,Z]])
E=Mb*P*Mb.T+W-P
sol=solve([E[0,0],E[0,1],E[1,1]], [X,Y,Z], simplify=False)
Px=factor(sol[X])
expected=(z**7-4*z**6-4*z**5-8*z**4+4*z**3+16*z**2+z+4)/(z**2*(z-4)*(z-1)*(z+1)*(z**2+z+3))
eq(Px, expected)
eq(limit(z*z*Px,z,0,dir='+'),Rational(1,3))

# Independently construct numerical covariance from Kronecker and
# an exact rational linear solve for 3x3 reduced symmetric system.
tests=0
for va in [Rational(1,1000),Rational(1,100),Rational(1,10),Rational(1,3)]:
    for vb in [Rational(1,2),Rational(1),Rational(3,2)]:
        if va+vb>=2: continue
        h,l=T(va,vb),T(vb,va)
        m=l*h;vv=l*Matrix([1,0]);w=vv*vv.T+Matrix([[1,0],[0,0]])
        u,v,wz=symbols('u v wz')
        q=Matrix([[u,v],[v,wz]])
        f=m*q*m.T+ w-q
        so=solve([f[0,0],f[0,1],f[1,1]], [u,v,wz], simplify=False)
        q1=q.subs(so)
        assert q1==q1.T
        assert q1[0,0]>0 and q1.det()>0
        assert (m*q1*m.T+vv*vv.T+Matrix([[1,0],[0,0]])-q1).applyfunc(simplify)==zeros(2)
        assert simplify(m.det()-va*vb/4)==0
        assert simplify(m.trace()-(1-(va+vb)+(va+vb)**2/2+va*vb/4))==0
        tests+=1

# Covariance limit from convergence of a^2 W and M0. Limit solution
# of P0=M0 P0 M0^T + diag(b^4/4,0) (noise variance set to 1).
p=b**4/(4*(1-c**2))
P0=Matrix([[p,p*c],[p*c,p]])
# The exact limiting solution is [[p,p*c^{-1}?], ...] determined here
# directly from the recurrence: Y=p/c? Solve: M0P0M0.T has
# (1,1)=c^2 p, (1,2)=c*p, (2,2)=p, so P0_12=c*p, P0_22=p.
assert (M0*P0*M0.T+Matrix([[b**4/4,0],[0,0]])-P0).applyfunc(simplify)==zeros(2)
print('PASS: AB2 transfer, Schur factorization, singular monodromy, Lyapunov law; %d rational stationary cases' % tests)
print('b=1 stationary variance exactly:',Px)
print('b=1 scaled small-a stationary variance:',limit(z*z*Px,z,0,dir='+'))
