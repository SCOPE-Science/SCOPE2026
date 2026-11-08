"""Symbolic checks for the sharp Jacobi gap on isosceles SPD correlations.
These finite checks supplement but do not replace the analytic inequalities.
Requirements: Python 3.10+, sympy 1.13+.
"""
import math
import random
import sympy as S

a,u,s,r,t=S.symbols('a u s r t',real=True)
passed=0
def eq(x,y,label):
    global passed
    d=S.factor(x-y)
    if d!=0: raise AssertionError(f'{label}: {d}')
    passed+=1

def check(b,label):
    global passed
    if not b: raise AssertionError(label)
    passed+=1

# The two nontrivial upper-bound regions are algebraically certified.
F2=3*a*(1+a-2*u)*(2+a-s)-2*(a-u)*(1-a)*(2+a+s)
H2=(1+2*a)*s**2-6*a*(a+2)*s+a*(4*a*a+19*a+4)
eq(F2.subs(u,(s*s-a*a)/8),(a+s+2)*H2/4,'middle-region factorization')
center=3*a*(a+2)/(1+2*a)
eq(H2,(1+2*a)*(s-center)**2+a*(4-a)*(1-a)**2/(1+2*a),'completed square')
Fsquared=(2+a)**2*(1+5*r)**2-(a*a+4*(1+a)*r*r)*(5+r)**2
H3=(1+a)*(1+10*r+r*r)-6*a*a
eq(Fsquared,4*(1-r*r)*H3,'large-coupling factorization')
# First region: exact difference, and comparison to the simple positive lower bound.
F1=3*a*(1+a-2*u)-(2+a+s)*(a-u)
eq(F1,a+2*a*a+(2-5*a)*u-s*(a-u),'small-coupling difference')
eq(F1.subs(s,3*a),(1-a)*(a+2*u),'small-coupling lower bound')
# Sharp family verifies algebraic branch and closed-form optimal condition.
aw=1-t*t
uw=1-t
kw=aw*(1+aw-2*uw)/((aw-uw)*(1-aw))
eq(kw,(1+t)*(2-t)/t**2,'sharp family optimum')
# Rational special instance, in the first branch.
A=S.Rational(1,2);B=S.Rational(1,4);U=B*B
xopt=(A-U)/(A*(1-A))
check(xopt==S.Rational(7,4),'rational square scaling')
C=S.Matrix([[1,A,B],[A,1,B],[B,B,1]])
D=S.diag(S.sqrt(xopt),S.sqrt(xopt),1)
W=S.simplify(D*C*D)
check(W.eigenvals()=={S.Rational(11,4):1,S.Rational(7,8):2},'rational optimal spectrum')
check(S.simplify((S.Rational(11,4)/S.Rational(7,8))-(S.Rational(22,7)))==0,'rational optimal condition')
# Finite stress points: the analytic proof handles the continuum, not these checks.
rng=random.Random(20261104)
for i in range(220):
 aa=0.001+0.998*rng.random()
 bb=(0.001+0.998*rng.random())*math.sqrt((1+aa)/2)
 uu=bb*bb
 xx=max(1/(1+aa),(aa-uu)/(aa*(1-aa)))
 rho=math.sqrt(2/(1+aa))*bb
 kk=(aa*(1+aa-2*uu)/((aa-uu)*(1-aa)) if uu<=2*aa*aa/(1+aa) else (1+rho)/(1-rho))
 sr=math.sqrt(aa*aa+8*uu)
 lplus=(2+aa+sr)/2
 lminus=(2+aa-sr)/2
 kj=lplus/min(lminus,1-aa)
 check(1-1e-10<=kj/kk<1.5+1e-10,f'ratio bounds point {i}')
 # Verify optimal equal-pair diagonal scaling at randomly perturbed x.
 for j in range(30):
    y=xx*math.exp(rng.uniform(-5,5))
    plus=((1+aa)*y+1+math.sqrt(((1+aa)*y-1)**2+8*uu*y))/2
    minus=((1+aa)*y+1-math.sqrt(((1+aa)*y-1)**2+8*uu*y))/2
    check(plus/min(minus,(1-aa)*y)>=kk*(1-2e-10),f'scale {i}:{j}')
print(f'PASS {passed} symbolic, exact and numerical assertions')
print('For C(1/2,1/4), optimal diagonal-square x=7/4, eigenvalues 7/8,7/8,11/4.')
print('For a=1-t^2, b=sqrt(1-t), the ratio tends to 3/2 as t tends to zero.')
print('Universal inequalities are proved analytically in RESULT.md, not by randomized tests.')
