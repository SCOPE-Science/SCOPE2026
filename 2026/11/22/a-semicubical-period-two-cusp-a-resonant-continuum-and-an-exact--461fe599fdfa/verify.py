"""Standalone symbolic and exact-arithmetic checks for the affine cubic two-cycle theorem.

Requires Python 3 and SymPy. Identity checks are algebraic; the final sample
substitutions are diagnostics, not an enumeration of all real parameters.
"""
from sympy import (symbols, factor, simplify, Rational, sqrt, Matrix, expand, symmetrize)

x, y, c, b, m, s = symbols('x y c b m s', real=True)
L = b + c**2 - 1
N = c*(b-1) - m
p = b - 1 - c*s
Delta = (s+2*c)**2-4*L

a = (c+x)*y**2 + b*x + m - x
z = (c+y)*x**2 + b*y + m - y
assert simplify(a-z-(x-y)*(b-1-c*(x+y)-x*y)) == 0
sum_equation = c*(s*s-2*p)+p*s+(b-1)*s+2*m
assert factor(sum_equation-2*(L*s-N)) == 0
assert simplify(s*s-4*p-Delta)==0
assert simplify((N+2*c*L)**2-L**2*Delta.subs(s,N/L)-4*L**3)==0

jac = lambda u,v: Matrix([[0,1],[v**2+b,2*(c+u)*v]])
return_mat = jac(y,x)*jac(x,y)
raw_trace = expand(return_mat.trace())
raw_det = expand(return_mat.det())
T = s*s-2*p+2*b+4*L*p
D = p*p+b*(s*s-2*p)+b*b
# Reduce symmetric Jacobian invariants by substituting x+y=s, xy=p.
symtrace, symrem, symsubs = symmetrize(raw_trace, [x,y], formal=True)
assert symrem == 0
assert simplify(symtrace.subs({symsubs[0][0]:s, symsubs[1][0]:p})-T)==0
assert simplify(D-((b+c*c)*s*s+2*c*s+1))==0
assert simplify(1-T+D-L*Delta)==0
assert simplify(raw_trace-( (x+y)**2-2*x*y+2*b+4*(c+x)*(c+y)*x*y))==0
assert simplify(raw_det-((x*x+b)*(y*y+b)))==0
assert simplify((c+x)*(c+y)-L-(x*y+c*(x+y)-b+1))==0

# The resonance is an exact continuum of two-cycles, with normal multiplier t^2.
t=symbols('t', real=True)
fr=lambda u,v: (v,(1+u)*v*v-1)
assert fr(-1,t)==(t,-1)
assert fr(t,-1)==(-1,t)
mon=jac(t,-1).subs({c:1,b:0})*jac(-1,t).subs({c:1,b:0})
assert simplify(mon.det()-t*t)==0
assert simplify(mon.trace()-(1+t*t))==0

# At c=1,b=1/2 the claimed inequalities reduce to exact polynomials.
Ts=factor(T.subs({c:1,b:Rational(1,2)}))
Ds=factor(D.subs({c:1,b:Rational(1,2)}))
Dsprime=factor(Delta.subs({c:1,b:Rational(1,2)}))
assert simplify(Ts-(s*s+1))==0
assert simplify(Ds-(3*s*s+4*s+2)/2)==0
assert simplify(Dsprime-(s*s+4*s+2))==0
assert simplify(1+Ts+Ds-(5*s*s+4*s+6)/2)==0
assert simplify(1-Ts+Ds-(s*s+4*s+2)/2)==0
for sm in [Rational(-1,4),Rational(-3,10),Rational(-1,2)]:
    assert Ds.subs(s,sm)<1
    assert Dsprime.subs(s,sm)>0
    assert 1+Ts.subs(s,sm)+Ds.subs(s,sm)>0
    mv=-Rational(1,2)-sm/2
    sv1=(sm+sqrt(Dsprime.subs(s,sm)))/2
    sv2=(sm-sqrt(Dsprime.subs(s,sm)))/2
    def fmap(u,v):return (v,(1+u)*v*v+Rational(1,2)*u+mv)
    o=fmap(sv1,sv2)
    assert simplify(o[0]-sv2)==0
    assert simplify(o[1]-sv1)==0
assert Ds.subs(s,0)==1 and Ts.subs(s,0)==1
assert simplify(Ts.subs(s,-2+sqrt(2))-(1+Ds.subs(s,-2+sqrt(2))))==0
print('AFFINE_CUBIC_PERIOD_TWO_VERIFY_OK')
