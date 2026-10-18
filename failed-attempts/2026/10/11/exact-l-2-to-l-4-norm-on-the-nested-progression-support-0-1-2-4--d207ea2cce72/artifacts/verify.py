import sympy as sp
from fractions import Fraction

# Exact fourth-moment identity for support {0,1,2,4}.
a,b,c,d=sp.symbols('a b c d', complex=True)
x,y,z,w=sp.symbols('x y z w', positive=True, real=True)
# Magnitude-maximized quartic on the unit L2 sphere.
H=2-(x**4+y**4+z**4+w**4)+4*x*z*y**2+4*x*w*z**2

# Boundary certificate: if y=0 or w=0, write q for the middle squared mass.
q=sp.symbols('q', real=True)
bound=sp.expand(2-(1-q)**2/sp.Integer(2)-q**2+2*(1-q)*q)
assert sp.expand(sp.factor(bound) + sp.Rational(1,2)*(7*q**2-6*q-3)) == 0
assert sp.expand(bound-sp.Rational(15,7)+sp.Rational(7,2)*(q-sp.Rational(3,7))**2)==0
# x=0 or z=0 has no collision gain and is <= 5/3 by sum fourth >= 1/3.
assert sp.Rational(5,3) < sp.Rational(15,7) < sp.Rational(9,4)
# Equal magnitudes witness 9/4, so every global maximizer is interior.
assert sp.simplify(H.subs({x:sp.Rational(1,2),y:sp.Rational(1,2),z:sp.Rational(1,2),w:sp.Rational(1,2)})) == sp.Rational(9,4)

# Interior stationary equations for G=H-2. Scale x=1 and let k=delta/x^2.
r,s,t,k=sp.symbols('r s t k')
eqs=[
 -1+s*r**2+t*s**2-k,
 -r**2+2*s-k,
 -s**3+r**2+2*t*s-k*s,
 -t**3+s**2-k*t,
]
G=sp.groebner(eqs,r,s,t,k,order='lex')
P_expected=1152*k**9+10770*k**8+36224*k**7+56126*k**6+25235*k**5-47027*k**4-84801*k**3-63648*k**2-28469*k-6889
assert sp.expand(G.polys[-1].as_expr()-P_expected)==0
# Extract r^2,s,t as rational polynomials of k from the triangular Groebner basis.
gr=[p.as_expr() for p in G.polys]
R2=sp.solve(gr[0],r**2)[0]
S=sp.solve(gr[1],s)[0]
T=sp.solve(gr[2],t)[0]
N=sp.cancel(1+R2+S**2+T**2)
numN,denN=sp.fraction(N)
numN=sp.rem(numN,P_expected,k)
denN=sp.rem(denN,P_expected,k)
D=sp.symbols('D')
rel=sp.expand(D*numN-k*denN)
Qraw=sp.resultant(P_expected,rel,k)
Q=7405408*D**9+29910288*D**8+50188768*D**7+43830564*D**6+19545666*D**5+2647793*D**4-1203370*D**3-539404*D**2-84328*D-6889
assert sp.rem(Qraw,Q,D)==0
# Descartes: one coefficient-sign change, while Q(0)<0<Q(1), so exactly one positive root.
coeff=sp.Poly(Q,D).all_coeffs()
signs=[1 if cc>0 else -1 if cc<0 else 0 for cc in coeff]
signs=[s0 for s0 in signs if s0]
assert sum(signs[i]!=signs[i+1] for i in range(len(signs)-1))==1
assert Q.subs(D,0)<0 and Q.subs(D,1)>0
lo=sp.Rational(1497,5000); hi=sp.Rational(599,2000)
assert Q.subs(D,lo)<0<Q.subs(D,hi)
root=sp.nroots(Q,n=30,maxsteps=200)
pos=[rr for rr in root if abs(sp.im(rr))<sp.Float('1e-25') and sp.re(rr)>0]
assert len(pos)==1
delta=float(sp.re(pos[0])); C=(2+delta)**0.25
assert 0.2994<delta<0.2995
assert 1.2314<C<1.2315
print(f'VERIFY_OK delta={delta:.15f} C4={C:.15f} groebner_degree=9 positive_roots=1 boundary={float(sp.Rational(15,7)):.15f}')
