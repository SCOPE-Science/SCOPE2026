"""Reproduce symbolic and exact-arithmetic checks for two-cycle tongue formulas.

Dependency: SymPy >= 1.12. Execute: python check.py.
All statements for arbitrary real parameters follow from the proof, not the sampling checks.
"""
from fractions import Fraction as Q
import sympy as s

b,y=s.symbols('b y',real=True)
p=2*(1+b);q=2*(1-b);t=s.expand(1-p*q)
xc=((1+q)*y-q)/(p+1)
ac=b/2+(p*q+t*y)/(p+1)
for j in [0,1]:
    x=xc+j/(p+1);a=ac+j/(p+1)
    assert s.simplify(p*x+a-b/2-j-y)==0
    assert s.simplify(q*y+a+3*b/2-2-x)==0
    assert s.simplify(s.diff(a,y)-t/(p+1))==0
    assert s.simplify(s.diff(x,y)-(1+q)/(p+1))==0
assert s.factor(t)==4*b*b-3
width=s.simplify((ac.subs(y,1)-ac.subs(y,s.Rational(1,2))))
assert s.simplify(width-t/(2*(3+2*b)))==0
bcrit=s.sqrt(3)/2
assert s.simplify(ac.subs({b:bcrit,y:s.Rational(1,4)})-(s.Rational(1,2)+s.sqrt(3)/12))==0
assert s.simplify((ac+1/(p+1)).subs({b:bcrit,y:s.Rational(3,4)})-(1-s.sqrt(3)/12))==0
assert s.simplify(s.diff(width,b).subs(b,bcrit)-(s.sqrt(3)-1))==0
area=s.simplify(2*s.integrate(width,(b,bcrit,1)))
expected=-s.Rational(11,4)+s.Rational(3,2)*s.sqrt(3)+3*s.log(5/(3+s.sqrt(3)))
assert s.simplify(s.expand_log(area-expected,force=True))==0
symbolic=14

# Independent exact-affine test with branch integers and mod-1 evaluations.
count=0
for B in [Q(7,8),Q(9,10),Q(19,20),Q(99,100),Q(1)]:
    P=2*(1+B); C=2*(1-B); T=1-P*C
    lo=B/2+(1-T/Q(2))/(P+1)
    hi=B/2+1/(P+1)
    assert 0<lo<hi<1
    assert hi < lo+1/(P+1)
    for j in [0,1]:
        for Y in [Q(51,100),Q(3,5),Q(3,4),Q(4,5),Q(99,100)]:
            X=((1+C)*Y-C+j)/(P+1)
            A=B/2+(P*C+T*Y+j)/(P+1)
            assert 0<X<Q(1,2)<Y<1 and 0<A<1
            fx=P*X+A-B/2
            fy=C*Y+A+3*B/2
            assert fx-j==Y and fy-2==X
            assert (fx%1)==Y and (fy%1)==X
            assert P*C<1
            count+=1

# Independent full mixed-branch integer-lift search at 255 rational parameters.
search_cases=0
for B in [Q(7,8),Q(9,10),Q(19,20),Q(99,100),Q(1)]:
    P=2*(1+B); C=2*(1-B); T=1-P*C
    lower=B/2+(1-T/Q(2))/(P+1)
    upper=B/2+1/(P+1)
    for k_a in range(1,52):
        A=Q(k_a,52)
        hits=set()
        for K in range(-2,4):
            for L in range(-2,5):
                X=((1+C)*A+Q(3,2)*B-L-C*(B/2+K))/T
                Y=P*X+A-B/2-K
                if 0<X<Q(1,2) and Q(1,2)<Y<1:
                    hits.add((X,Y))
        predicted=(lower<A<upper) or (lower+1/(P+1)<A<upper+1/(P+1))
        assert len(hits)==int(predicted)
        search_cases+=1

# The polynomial identities also verify the exact inverse parametrization.
print(f'VERIFY_OK symbolic_identities={symbolic} exact_rational_cycles={count} '
      f'critical_parameters=2 inverse_lift_search={search_cases} area={float(area):.12f}')
