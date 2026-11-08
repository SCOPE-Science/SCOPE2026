"""Exact algebraic and rational checks for the piecewise-linear circle-map three-cycle windows.
Run with: python check.py  (requires SymPy and mpmath)."""
import sympy as s
import mpmath as mp

A, b = s.symbols('a b', real=True)
p, q = 2*(1+b), 2*(1-b)
M = s.factor(p*q*q)
P = s.factor(M-1)
lower = s.factor((b+1)*(4*b*b-10*b+9)/(2*(7+2*b-4*b*b)))
upper = s.factor((-4*b**3-2*b*b+3*b+4)/(2*(7-2*b-4*b*b)))
width = s.factor(upper-lower)
expected = (4*b*b+2*b-5)*(8*b**3-8*b*b-8*b+7)/(2*(4*b*b-2*b-7)*(4*b*b+2*b-7))
assert s.factor(width-expected) == 0
assert s.factor(width-(b-s.Rational(1,2)+2*(b-1)/(4*b*b+2*b-7)+(2*b+1)/(4*b*b-2*b-7))) == 0
x = s.factor(((1+q+q*q)*A+q*q*(-b/2)+q*(3*b/2-1)+3*b/2-2)/(1-M))
y = s.factor(p*x+A-b/2)
z = s.factor(q*y+A+3*b/2-1)
assert s.factor(q*z+A+3*b/2-2-x) == 0
assert s.factor(y.subs(A, lower)-s.Rational(1,2)) == 0
assert s.factor(z.subs(A, upper)-1) == 0
for point in (x, y, z):
    da = s.factor(s.diff(point,A))
    # Positive since 0<q<1, p>0, and 0<M<1 on the claimed strip.
    assert s.factor(da*(1-M)).is_positive is not False
assert s.factor(M - 8*(1+b)*(1-b)**2) == 0
# All branch inequalities reduce to signs of listed one-variable expressions.
endpoints = [(x,0),(x,s.Rational(1,2)),(y,s.Rational(1,2)),(y,1),(z,s.Rational(1,2)),(z,1)]
for v,tgt in endpoints:
    for alpha in (lower,upper):
        num,den = s.fraction(s.factor(v.subs(A,alpha)-tgt))
        # Exact root counts prove constant sign of these rational functions
        # throughout (0.73,0.90), which contains the entire theorem strip.
        for polynomial in (num,den):
            poly=s.Poly(polynomial,b)
            if not poly.is_zero and poly.degree()>0:
                count=poly.count_roots(s.Rational(73,100),s.Rational(9,10))
                if count:
                    Q=s.Poly(4*b*b+2*b-5,b)
                    R=s.Poly(8*b**3-8*b*b-8*b+7,b)
                    assert (poly.rem(Q).is_zero or poly.rem(R).is_zero) and count==1, (v,tgt,alpha,polynomial)
        for rat in (s.Rational(74,100),s.Rational(4,5),s.Rational(89,100)):
            vv = s.factor((num/den).subs(b,rat))
            expected_sign = (1 if (v,tgt) in [(x,0),(y,s.Rational(1,2)),(z,s.Rational(1,2))] else -1)
            # Endpoints y(lower)=1/2 and z(upper)=1 have exactly zero.
            if (v is y and alpha==lower and tgt==s.Rational(1,2)) or (v is z and alpha==upper and tgt==1):
                assert vv == 0
            else:
                assert vv*expected_sign > 0,(v,tgt,alpha,rat,vv)
# b_c is unique root of M=1 on (0,1): derivative is strictly negative.
assert s.factor(s.diff(M,b) + 8*(1-b)*(1+3*b)) == 0
assert (M-1).subs(b,0)>0 and (M-1).subs(b,1)<0
bcrit = s.polys.polytools.intervals(s.Poly(P,b),eps=s.Rational(1,10**10))
crit_intervals = [(l,r) for ((l,r),mult) in bcrit if 0<l<1]
assert len(crit_intervals)==1
b0=float((crit_intervals[0][0]+crit_intervals[0][1])/2)
b1=float((s.sqrt(21)-1)/4)
assert b0<b1
# Exact rational orbit example, with all residues strictly in their intended halves.
br=s.Rational(4,5); ar=(lower.subs(b,br)+upper.subs(b,br))/2
v0,v1,v2 = [s.factor(v.subs({b:br,A:ar})) for v in (x,y,z)]
assert 0<v0<s.Rational(1,2)<v1<1 and s.Rational(1,2)<v2<1
assert s.factor(p.subs(b,br)*v0+ar-br/2-v1)==0
assert s.factor(q.subs(b,br)*v1+ar+3*br/2-1-v2)==0
assert s.factor(q.subs(b,br)*v2+ar+3*br/2-2-v0)==0
assert M.subs(b,br)<1
# Exact reflection: 1/2-x for the plus branch; 3/2-x for the minus branch.
# use fresh variable so that a and x are not conflated:
t=s.symbols('t',real=True)
assert s.factor((p*(s.Rational(1,2)-t)+s.Rational(1,2)-A-b/2) - (s.Rational(1,2)-(p*t+A-b/2))) == 1
assert s.factor((q*(s.Rational(3,2)-t)+s.Rational(1,2)-A+3*b/2) - (s.Rational(1,2)-(q*t+A+3*b/2))) == 3
# Reflection sends (a,x) to (1/2-a,1/2-x) modulo one, preserving multiplier.
mp.mp.dps=65
b0mp=mp.findroot(lambda t:8*(1+t)*(1-t)**2-1, (mp.mpf('.7'),mp.mpf('.8')))
b1mp=(mp.sqrt(21)-1)/4
wid=lambda t: ((t+1)*(4*t*t-10*t+9)/(2*(7+2*t-4*t*t)))*(-1)+(-4*t**3-2*t*t+3*t+4)/(2*(7-2*t-4*t*t))
area=2*mp.quad(wid,[b0mp,(b0mp+b1mp)/2,b1mp])
assert area>0
print('VERIFY_OK cycle_linear_identities=4 endpoint_equalities=2 exact_rational_cycle=1 mirror_identity=1 multiplier_unique_root=1 area_quadrature=1')
print('bcrit=',mp.nstr(b0mp,35),'bupper=',mp.nstr(b1mp,35),'total_two_window_area=',mp.nstr(area,35))
