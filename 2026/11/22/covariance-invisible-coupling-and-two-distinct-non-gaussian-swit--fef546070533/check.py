"""Reproducible moment-identity checks for a telegraph-coupled harmonic pair.

Requires Python 3 and sympy. Tests exact stationary generator equations,
optimization identities, and independent rational substitutions.
"""
from fractions import Fraction
from math import sqrt
import sympy as s

a,g,q,D=s.symbols('a g q D', positive=True)
b=a*a-g*g
m2=D*(a+q)/(b+a*q)
p=g*m2/(a+q)
A,B,C=s.symbols('A B C')
# Generator on X^4, sign*X^3*Y, X^2*Y^2, respectively.
equations=[-4*a*A+4*g*B+12*D*m2,
           -(4*a+2*q)*B+g*(3*C+A)+6*D*p,
           -4*a*C+4*g*B+4*D*m2]
solution=s.solve(equations,(A,B,C),dict=True)[0]
A_exact=s.factor(solution[A]); C_exact=s.factor(solution[C]); B_exact=s.factor(solution[B])
k4=s.factor(A_exact-3*m2**2)
k4_expected=3*D**2*g**4*q/(a*(b+a*q)**2*(2*b+a*q))
assert s.simplify(k4-k4_expected)==0
checks=1
assert s.simplify(-2*a*m2+2*g*p+2*D)==0; checks+=1
assert s.simplify(-(2*a+2*q)*p+2*g*m2)==0;checks+=1
assert s.simplify(C_exact-(D*m2/a+g*B_exact/a))==0;checks+=1
for eq in equations:
    assert s.simplify(eq.subs(solution))==0
    checks+=1
K=s.factor(k4/m2**2)
assert s.simplify(K-3*g**4*q/(a*(2*b+a*q)*(a+q)**2))==0;checks+=1
phi=(1+s.sqrt(5))/2
raw=b/(a*phi)
raw_val=3*D**2*g**4/(a*a*b*b*phi**5)
assert s.simplify(k4.subs(q,raw)-raw_val)==0;checks+=1
# Scale x=aq/b; the raw fourth-cumulant shape is x/[(1+x)^2(2+x)].
x=s.symbols('x',positive=True)
f=x/((1+x)**2*(2+x))
assert s.simplify(s.diff(f,x)-(s.Integer(2)*(1-x-x*x))/((1+x)**3*(2+x)**2))==0;checks+=1
r,t=s.symbols('r t', positive=True)
ft=t/((t+2*r)*(1+t)**2)
assert s.simplify(s.diff(ft,t)-(2*(r-r*t-t*t))/((2*r+t)**2*(1+t)**3))==0;checks+=1
te=(s.sqrt(r*r+4*r)-r)/2
assert s.simplify(te**2+r*te-r)==0;checks+=1
assert s.simplify(((r/phi)**2+r*(r/phi)-r)-r*(r-1))==0;checks+=1
# Independent Fraction exact arithmetic, without substituting the solved A expression.
def frac_matrix_solve(M,y):
    n=len(y); a2=[list(row)+[rhs] for row,rhs in zip(M,y)]
    for col in range(n):
        pivot=next(k for k in range(col,n) if a2[k][col])
        a2[col],a2[pivot]=a2[pivot],a2[col]
        t0=a2[col][col];a2[col]=[x/t0 for x in a2[col]]
        for row in range(n):
            if row!=col:
                factor=a2[row][col]
                a2[row]=[z-factor*w for z,w in zip(a2[row],a2[col])]
    return [row[-1] for row in a2]
for ai in range(2,9):
    for gi in range(1,ai):
        for qi in [Fraction(1,7),Fraction(1,2),Fraction(1,1),Fraction(5,3),Fraction(7,2),Fraction(13,1)]:
            for Di in [Fraction(1,5),Fraction(4,3)]:
                aa=Fraction(ai);gg=Fraction(gi);qq=qi;dd=Di
                mm=dd*(aa+qq)/(aa*(aa+qq)-gg*gg)
                pp=gg*mm/(aa+qq)
                # [A,B,C] equations from the uncoupled generator.
                MM=[[-4*aa,4*gg,0],[gg,-(4*aa+2*qq),3*gg],[0,4*gg,-4*aa]]
                yy=[-12*dd*mm,-6*dd*pp,-4*dd*mm]
                Am,Bm,Cm=frac_matrix_solve(MM,yy)
                kk=Am-3*mm*mm
                expected=3*dd*dd*gg**4*qq/(aa*(aa*aa+aa*qq-gg*gg)**2*(2*aa*aa+aa*qq-2*gg*gg))
                assert kk==expected and kk>0
                checks+=3
                # Low-order stationary identities and physical covariance positivity
                assert -4*aa*Am+4*gg*Bm+12*dd*mm==0;checks+=1
                assert -(4*aa+2*qq)*Bm+gg*(Am+3*Cm)+6*dd*pp==0;checks+=1
                assert -4*aa*Cm+4*gg*Bm+4*dd*mm==0;checks+=1
                assert Am>0 and Cm>0 and mm>0;checks+=1
# Two distinct optima for every 0<r<1, and expected tail behavior
for j in range(1,300):
    rr=j/300
    tr=rr/((1+sqrt(5))/2)
    te_num=(sqrt(rr*rr+4*rr)-rr)/2
    assert 0<tr<te_num<1
    checks+=1
assert s.limit(k4,q,0)==0;checks+=1
assert s.limit(k4,q,s.oo)==0;checks+=1
assert s.limit(K,q,0)==0;checks+=1
assert s.limit(K,q,s.oo)==0;checks+=1
print('PASS',checks,'exact-rational, symbolic, and deterministic numerical assertions')
print('m2=',m2)
print('k4=',k4)
print('excess=',K)
