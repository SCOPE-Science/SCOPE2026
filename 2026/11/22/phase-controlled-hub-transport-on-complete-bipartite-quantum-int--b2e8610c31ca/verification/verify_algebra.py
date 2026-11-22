"""Exact independent algebraic certificates for the phase-controlled two-hub family."""
from sympy import Matrix, I, S, symbols, simplify, cos, pi, sqrt, factor, diff, Rational, expand_trig

def coupling(phases):
    m=len(phases)
    H=Matrix.zeros(m+2)
    for j,z in enumerate(phases):
        H[0,j+2]=1
        H[j+2,0]=1
        H[1,j+2]=z
        H[j+2,1]=z.conjugate()
    return H

examples={
  'two-to-one':[Rational(3,5)+I*Rational(4,5),Rational(3,5)-I*Rational(4,5)],
  'three-to-one':[Rational(4,5)+I*Rational(3,5),Rational(4,5)-I*Rational(3,5)],
  'destructive':[S.One,-S.One],
}
for name,z in examples.items():
    H=coupling(z)
    assert H==H.conjugate().T
    m=len(z)
    val=S.Zero
    for v in z: val+=v
    B=H[:2,2:]
    Gram=simplify(B*B.conjugate().T)
    expected=Matrix([[m,val.conjugate()],[val,m]])
    assert Gram==expected
    chi=factor(H.charpoly().as_expr())
    if name=='two-to-one':
        assert chi==factor(symbols('lambda')**(m-2)*(symbols('lambda')**2-S(16)/5)*(symbols('lambda')**2-S(4)/5))
    if name=='three-to-one':
        assert chi==factor(symbols('lambda')**(m-2)*(symbols('lambda')**2-S(18)/5)*(symbols('lambda')**2-S(2)/5))
    if name=='destructive':
        assert chi==factor((symbols('lambda')**2-2)**2)
    print('PASS: exact Gram and characteristic polynomial',name,chi)

x=symbols('x',real=True)
c=symbols('c', real=True)
# When lambda_plus / lambda_minus=3, the transition probability is 4c^2(1-c^2)^2, c=cos(x).
P=factor(((cos(3*x)-cos(x))/2)**2)
assert simplify(expand_trig(P)-4*cos(x)**2*(1-cos(x)**2)**2)==0
U=4*c**2*(1-c**2)**2
assert simplify(diff(U,c)-8*c*(c**2-1)*(3*c**2-1))==0
assert simplify(U.subs(c,1/sqrt(3))-Rational(16,27))==0
# u=c^2 in [0,1]: derivative is 4(1-u)(1-3u); max at u=1/3.
u=symbols('u',real=True)
assert simplify(diff(4*u*(1-u)**2,u)-4*(u-1)*(3*u-1))==0
print('PASS: exact global maximum 16/27 at 3:1 parity resonance')

# A rational a/b reduced with opposite parity gives |S|/m=(a^2-b^2)/(a^2+b^2).
a,b,m=symbols('a b m',positive=True)
s=m*(a*a-b*b)/(a*a+b*b)
assert simplify((m+s)/(m-s)-a*a/b/b)==0
print('PASS: exact parameter-to-frequency-ratio identity')
