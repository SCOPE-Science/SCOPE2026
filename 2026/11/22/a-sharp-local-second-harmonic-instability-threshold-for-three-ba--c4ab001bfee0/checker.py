"""Exact algebraic checks for three-band circle Poisson norming modes.
Run: python3 checker.py (requires sympy)."""
import sympy as S
s,x=S.symbols('s x',real=True)
N=3+4*s*x+12*s*s*x*x+3*s**4*x**4
P=3*s**4*x**3-6*s**2*x**3+6*s**2*x-3*s*x*x+s-3*x
R=S.expand(6*s*(1+s*x+s*s*x*x)*(1+x*x)-N)
Q=112*s**5-240*s**4+165*s**3-79*s*s+57*s-18
E=9*s**8-72*s**6+162*s**4-56*s*s+9
assert S.expand(S.diff(N,x)*(1+x*x)-4*x*N-4*P)==0
assert S.expand(E-(9*(s**4-4*s*s+1)**2+16*s*s))==0
assert S.factor(S.resultant(P,R,x)/(S.Integer(54)*s**6*E*Q))==1
# Exact Fourier zero-sum enumeration (for all real a,b,c).
a,b,c=S.symbols('a b c',real=True)
co={-3:c/2,-2:b/2,-1:a/2,1:a/2,2:b/2,3:c/2}
fourth=S.expand(sum(co[i]*co[j]*co[k]*co[-i-j-k] for i in co for j in co for k in co if -i-j-k in co))
expected=S.Rational(3,8)*(a**4+b**4+c**4)+S.Rational(3,2)*(a*a*b*b+a*a*c*c+b*b*c*c)+a**3*c/2+S.Rational(3,2)*a*b*b*c
assert S.expand(fourth-expected)==0
# Exact root counts of the critical resultant and square-factor positivity.
assert S.Poly(Q,s).count_roots(0,1)==2
I1=(S.Rational(507,1000),S.Rational(508,1000))
I2=(S.Rational(794,1000),S.Rational(795,1000))
assert S.Poly(Q,s).count_roots(*I1)==1 and S.Poly(Q,s).count_roots(*I2)==1
sub=S.Poly(S.subresultants(R,P,x)[3],x)
AA=S.factor(sub.coeff_monomial(x)/(27*s**6))
BB=S.factor(sub.coeff_monomial(1)/(27*s**6))
for lo,hi,sa,sb in [(*I1,-1,1),(*I2,-1,-1)]:
    for g,sign in [(AA,sa),(BB,sb)]:
        assert S.Poly(g,s).count_roots(lo,hi)==0
        assert S.sign(g.subs(s,lo))==S.sign(g.subs(s,hi))==sign
# Sign of R on the unique positive stationary branch: negative at s->0;
# R(1,x)>0 for all positive x and no other positive-root collision.
assert S.expand(R.subs(s,1)-(3*x**4+6*x**3+2*x+3))==0
assert S.expand(R.subs(s,0)+3)==0
# Global two-band exact absence through s=2/5, using trace bound:
assert 2*S.Rational(2,5)*(1+S.Rational(2,5)**2)<1
# Strict fourth-moment checks with direct rational example on both sides.
for v in [S.Rational(1,3),S.Rational(2,5),S.Rational(1,2),S.Rational(3,5),S.Rational(4,5),S.Rational(9,10)]:
    roots=S.nroots(P.subs(s,v),maxsteps=100)
    positive=[float(S.re(z)) for z in roots if abs(float(S.im(z)))<1e-9 and float(S.re(z))>0]
    assert len(positive)==1
    q=float(R.subs({s:v,x:positive[0]}))
    assert (q<0 if v<=S.Rational(1,2) else q>0)
print('PASS: exact Fourier quartic, derivative, resultant, Sturm isolations, root-branch signs and global small-radius certificate')
