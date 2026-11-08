"""Recompute exact transverse Floquet polynomials and the sharp threshold.

Requires Python 3 and SymPy. No external data are needed.
"""
import sympy as sp

x, lam = sp.symbols('g lam', real=True)
r = sp.sqrt(5)
ct = (r-1)/4
st = sp.sqrt((5+r)/8)

def quartic_for(n,k):
    theta = 2*sp.pi/n
    c=sp.cos(theta)
    s=sp.sin(theta)
    eta=sp.exp(sp.I*k*theta)-1
    P=sp.expand(lam**2+2*(x-c*eta)*lam+eta**2-2*x*c*eta)
    Q=sp.Poly(sp.expand(sp.expand_complex(P*sp.conjugate(P))),lam)
    assert Q.degree()==4
    _,a,b,cc,d=[sp.simplify(q) for q in Q.all_coeffs()]
    return [a,b,cc,d,sp.simplify(a*b-cc),sp.factor(a*b*cc-a*a*d-cc*cc)]

actual1=quartic_for(5,1)
actual2=quartic_for(5,2)
A1=(8*x-5+3*r)/2
B1=(8*x**2+(-15+9*r)*x+15-7*r)/2
C1=(3*r-5)*x**2+(15-7*r)*x+5*r-10
D1=((10-4*r)*x**2+(10*r-20)*x+15-5*r)/2
E1=(32*x**3+(-70+42*r)*x**2+(135-59*r)*x-70+30*r)/2
H1=((-160+96*r)*x**5+(1300-580*r)*x**4+(-3640+1620*r)*x**3+(5075-2295*r)*x**2+(-3600+1600*r)*x+1000-450*r)/2
A2=4*x+r
B2=4*x**2+3*r*x+5+r
C2=(4*r*x**2+(4*r+20)*x+5+5*r)/2
D2=((5-r)*x**2+(5*r+5)*x+15+5*r)/2
E2=(32*x**3+28*r*x**2+(4*r+50)*x+5+5*r)/2
H2=x*(64*r*x**4+(80*r+520)*x**3+(360+340*r)*x**2+(105*r+475)*x+50+50*r)/2
for act,expected in [(actual1,[A1,B1,C1,D1,E1,H1]),(actual2,[A2,B2,C2,D2,E2,H2])]:
    for a,b in zip(act,expected):
        assert sp.simplify(a-b)==0,('wrong quartic',a,b)

# For g>=6/5, A1,B1,C1,D1,E1 positive by exact elementary inequalities.
q0=sp.Rational(6,5)
for f in [A1,B1,C1,D1,E1]:
    assert sp.simplify(f.subs(x,q0))>0
    deriv=sp.diff(f,x)
    assert sp.simplify(deriv.subs(x,q0))>0
    # derivatives monotonic for x>=6/5: every nonconstant coefficient of derivative Taylor expansion about 6/5 is nonnegative.
    t=sp.symbols('t',nonnegative=True)
    coeff=sp.Poly(sp.expand(deriv.subs(x,t+q0)),t).all_coeffs()
    assert all(sp.simplify(v)>=0 for v in coeff)
# The degree-five Hurwitz determinant has exactly one positive zero by Descartes, not just a numerically guessed root.
coeff=sp.Poly(2*H1,x).all_coeffs()
assert [sp.sign(f) for f in coeff]==[1,1,-1,-1,-1,-1]
assert H1.subs(x,0)<0 and H1.subs(x,sp.Rational(6,5))<0 and H1.subs(x,sp.Rational(121,100))>0
# k=2 mode all Hurwitz coefficients have nonnegative monomial coefficients, strictly positive on g>0.
for f in [A2,B2,C2,D2,E2,H2]:
    poly=sp.Poly(f,x)
    assert all(sp.simplify(c)>=0 for c in poly.all_coeffs())
    assert any(sp.simplify(c)>0 for c in poly.all_coeffs())
# n=3,4 unidirectional directed rotations are never stable for any g>0.
for n in [3,4]:
    a,b,c,d,e,h=quartic_for(n,1)
    if n==3:
        assert sp.factor(h+3*x*(4*x*x-6*x+3)*(8*x*x-21*x+18))==0
        assert sp.discriminant(4*x*x-6*x+3,x)<0
        assert sp.discriminant(8*x*x-21*x+18,x)<0
    else:
        assert sp.simplify(h+64*x*x)==0
# For N=5, winding number +/-2 is never stable: the cubic Hurwitz coefficient
# of the k=1 real quartet is strictly negative at every g>0.
q=2
angle=2*sp.pi*q/5
c=sp.cos(angle)
etak=sp.exp(2*sp.pi*sp.I/5)-1
p=sp.expand(lam**2+2*(x-c*etak)*lam+etak**2-2*x*c*etak)
coeff=[sp.simplify(f) for f in sp.Poly(sp.expand(sp.expand_complex(p*sp.conjugate(p))),lam).all_coeffs()]
Cbad=coeff[3]
assert sp.simplify(Cbad-(-4*r*x**2+(20-4*r)*x+5-5*r)/2)==0
assert sp.discriminant(Cbad,x)==20*(1-r)<0
assert sp.LC(sp.Poly(Cbad,x))<0
# n=2: alternating wave has an expanding real phase eigenvalue +2.
assert sp.cos(sp.pi)*(sp.exp(sp.I*sp.pi)-1)==2
# Monotonic conversion and location of the unique critical relaxation parameter.
root=float(sp.nroots(H1,maxsteps=300)[0]); tau=1/(root+1-float(ct))
assert 1.2074<root<1.2076 and .5266<tau<.5269
w=float(sp.sqrt(C1/A1).subs(x,root));assert .711<w<.714
print('VERIFY_OK five_cycle_fourier_blocks=2 exact_hurwitz_identites=12 unique_positive_root=1 first_stable_size=5 full_five_winding_classes=5 critical_g=%.12f critical_tau=%.12f transverse_frequency=%.12f'%(root,tau,w))
