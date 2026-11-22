"""Independent finite numerical/symbolic checks for exact trapped-area theorem.
No network access or external data; mpmath and sympy are used.
"""
import mpmath as mp
import sympy as sp
mp.mp.dps=65
s,r=sp.symbols('s r',real=True)
b=s**3*(1-s)
Es=-s**2/2+s+b/(2*s**2)
P=sp.expand(r**4-2*r**3+2*Es*r**2-b)
assert sp.simplify(P-(r-s)**2*(r**2+2*(s-1)*r+s*(s-1)))==0
# At s=3/4, and delta=beta_* - beta, local cubic normal form.
t,z=sp.symbols('t z',positive=True)
C=sp.Rational(128,81)*sp.sqrt(2)
c=sp.Rational(2,3)*sp.sqrt(2)
star=sp.Rational(3,4)
V=lambda x, bb:-x**2/2+x+bb/(2*x**2)
E=sp.series(V(star+c*t*z,sp.Rational(27,256)-t*t)-V(star,sp.Rational(27,256)-t*t),t,0,4).removeO()
assert sp.simplify(sp.expand(E).coeff(t,3)-C*(z-z**3/3))==0
Ashape=sp.integrate(2*(1-z)*sp.sqrt((z+2)/3),(z,-2,1))
assert sp.simplify(Ashape-sp.Rational(24,5))==0
K=sp.simplify(Ashape*c*sp.sqrt(2*C))
assert sp.simplify(K-sp.Rational(256,45)*2**sp.Rational(3,4))==0
w=sp.symbols('w',nonnegative=True)
f=(sp.Rational(15,4)*sp.sqrt(w)*(1-w))
assert sp.simplify(sp.integrate(f,(w,0,1))-1)==0
assert sp.simplify(sp.integrate(w*f,(w,0,1))-sp.Rational(3,7))==0
# Exact factorization-integral area, separate energy quadrature, and limits.
def compute(S):
    B=S**3*(1-S)
    L=1-S+mp.sqrt(1-S)
    N=1-S-mp.sqrt(1-S)
    Es=-S*S/2+S+B/(2*S*S)
    area=2*mp.quad(lambda rr:(S-rr)/rr*mp.sqrt((rr-L)*(rr-N)),[L,(L+S)/2,S])
    # direct energy integration uses same turning points but no factorization
    def Eminus(rr):
        return Es+rr*rr/2-rr-B/(2*rr*rr)
    area2=2*mp.sqrt(2)*mp.quad(lambda v: mp.sqrt(max(mp.mpf('0'),Eminus(L+(S-L)*v*v)))*(S-L)*2*v,[0,mp.mpf('.5'),1])
    return B,area,area2
samples=[mp.mpf(v) for v in ['0.98','0.93','0.88','0.82','0.78','0.765','0.755','0.751']]
prev=mp.mpf('2')
for S in samples:
    B,a,a2=compute(S)
    assert 0<a<prev
    prev=a
    assert abs(a-a2)/a<mp.mpf('1e-29'),(S,a,a2)
    d=mp.mpf(27)/256-B
    rat=a/(mp.mpf(str(K.evalf(60)))*d**mp.mpf('1.25'))
    print('s',mp.nstr(S,6),'beta',mp.nstr(B,10),'area',mp.nstr(a,16),'fold-ratio',mp.nstr(rat,12))
assert abs((compute(mp.mpf('.75001'))[1])/(mp.mpf(str(K.evalf(60)))*(mp.mpf(27)/256-mp.mpf('.75001')**3*(1-mp.mpf('.75001')))**mp.mpf('1.25'))-1)<mp.mpf('3e-4')
assert abs(compute(mp.mpf('0.999999'))[1]-1)<mp.mpf('.012')
print('PASS: exact polynomial identity, fold coefficient, shape area, Beta normalization, eight area quadratures, monotonicity, critical coefficient and beta-zero endpoint')
