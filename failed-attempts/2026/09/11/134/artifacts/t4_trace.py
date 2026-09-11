import sympy as sp
from fractions import Fraction as F
T,y=sp.symbols('T y')
# trace poly from w=1/(x+1), w^4-5w^3+6w^2-4w+1, w=-T-1
w=-T-1
fT=sp.expand(w**4-5*w**3+6*w**2-4*w+1)
print("fT =", fT)
print("factor(fT) =", sp.factor(fT))
# rational root test
print("fT(1)=",fT.subs(T,1),"fT(-1)=",fT.subs(T,-1))
# fixed point enclosure: f(x)=x^4-x-1 at 1.2207,1.2208 exact
for s in ["1.2207","1.2208"]:
    a=F(s)
    print(s, "f=", (a**4-a-1), float(a**4-a-1))
# T enclosure: T=-1-1/(x+1)
for s in ["1.2207","1.2208"]:
    a=F(s)
    print("T bound at",s,":", -1-F(1,1)/(a+1), float(-1-1/(a+1)))
# totient-8 preimage
from sympy import totient
pre8=[m for m in range(3,500) if totient(m)==8]
print("phi^-1(8) =",pre8)
# candidate minpolys via resultant method: minpoly of 2cos(2pi/m)
# R(t)=resultant_y(Phi_m(y), y^2-t*y+1); minpoly = sqrt factor
ok=True
for m in pre8:
    Ph=sp.npolyroots if False else None
    from sympy import cyclotomic_poly
    Phi=cyclotomic_poly(m,y)
    R=sp.resultant(Phi, y**2-T*y+1, y)
    R=sp.expand(R)
    fac=sp.factor(R)
    # expect perfect square of degree-4 poly
    sq=sp.sqrt(R) if False else None
    # extract: factor returns c*(...)^2 presumably
    print(f"m={m}: deg R={sp.Poly(R,T).degree()} factor={fac}")
