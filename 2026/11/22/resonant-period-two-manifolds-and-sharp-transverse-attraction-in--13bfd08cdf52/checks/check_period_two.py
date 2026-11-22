"""Independent exact algebraic spot checks for quadratic companion-map period-two statements."""
from fractions import Fraction as F
import random
import sympy as s

u,v,a,b,c,delta,sigma,alpha,lam=s.symbols('u v a b c delta sigma alpha lam')
Q=lambda x,y: a*x*x+b*x*y+c*y*y
L=lambda x,y,z:s.Matrix([delta*z+alpha-sigma*y+Q(x,y),x,y])
J=lambda x,y:s.Matrix([[2*a*x+b*y, b*x+2*c*y-sigma,delta],[1,0,0],[0,1,0]])
S=1+sigma-delta; B=1+sigma+delta; d=a-c; e=b-a-c
E1=s.expand((1+sigma)*v-delta*u-alpha-Q(u,v))
E2=s.expand((1+sigma)*u-delta*v-alpha-Q(v,u))
assert s.expand(E1-E2-(v-u)*(B+d*(u+v)))==0
assert s.expand(E1+E2-(S*(u+v)-2*alpha-(a+c)*(u+v)**2-2*e*u*v))==0
ex={a:s.Rational(1,2), b:s.Rational(1,2), c:0, delta:s.Rational(1,4), sigma:-s.Rational(5,4),alpha:0}
for n in list(range(-20,21)) + [s.Rational(1,2),s.Rational(7,3)]:
    pt=s.Matrix([n,-n,n]); neg=s.Matrix([-n,n,-n]);
    assert s.simplify(L(*pt).subs(ex)-neg)==s.zeros(3,1)
    assert s.simplify(L(*neg).subs(ex)-pt)==s.zeros(3,1)
    P=s.simplify((J(-n,n)*J(n,-n)).subs(ex))
    check=(lam-1)*(lam**2-(s.Rational(3,2)-n*n/4)*lam+s.Rational(1,16))
    assert s.expand(P.charpoly(lam).as_expr()-check)==0

rng=random.Random(29)
for _ in range(160):
    av=F(rng.randint(-5,5),rng.randint(1,4));cv=F(rng.randint(-5,5),rng.randint(1,4));
    bv=1-av-cv; dv=F(rng.choice([-3,-1,1,3]),4)
    sv=F(rng.randint(-6,6),4); alp=F(rng.randint(-6,6),3)
    D=av-cv;E=bv-av-cv;BB=1+sv+dv;SS=1+sv-dv
    if D and E:
        t=-BB/D; h=(SS*t-2*alp-(av+cv)*t*t)/(2*E); disc=t*t-4*h
        if disc>0:
            uu=(s.Rational(t.numerator,t.denominator)+s.sqrt(s.Rational(disc.numerator,disc.denominator)))/2
            vv=(s.Rational(t.numerator,t.denominator)-s.sqrt(s.Rational(disc.numerator,disc.denominator)))/2
            pars={a:s.Rational(av.numerator,av.denominator), b:s.Rational(bv.numerator,bv.denominator),c:s.Rational(cv.numerator,cv.denominator),delta:s.Rational(dv.numerator,dv.denominator),sigma:s.Rational(sv.numerator,sv.denominator),alpha:s.Rational(alp.numerator,alp.denominator)}
            assert s.simplify(E1.subs(pars).subs({u:uu,v:vv}))==0
            assert s.simplify(E2.subs(pars).subs({u:uu,v:vv}))==0
print('PASS: symbolic sum/difference, exact two-cycle curve and Jacobian characteristic polynomial, 160 rational parameter cases.')
