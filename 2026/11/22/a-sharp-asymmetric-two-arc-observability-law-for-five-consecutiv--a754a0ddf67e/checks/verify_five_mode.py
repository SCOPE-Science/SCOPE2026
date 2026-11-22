"""Exact algebra and high-precision numerical checks for a two-arc Fourier-frame theorem.
Scientific checks only; this program is supplementary to the proof.
Run: python checks/verify_five_mode.py (requires sympy and mpmath).
"""
import mpmath as mp
import sympy as sp

mp.mp.dps = 65
c=sp.symbols('c', real=True)
S=34+32*c+4*c*c
R=4*(1-c)**2/S
assert sp.simplify(R.subs(c,-1)-sp.Rational(8,3))==0
assert sp.simplify(S.subs(c,-1)-6)==0
assert sp.simplify(sp.together(sp.diff(R,c))*S**2-80*(c-1)*(2*c+5)) == 0
# Prove the derivative is negative on [-1,1): its numerator is
# -8(1-c)[(34+32c+4c^2)+(1-c)(16+4c)].
num=sp.factor(sp.together(sp.diff(R,c))*S**2)
print('Derivative numerator of R times S^2:',num)
assert sp.simplify(num.subs(c,-1))<0
assert sp.simplify(num.subs(c,0))<0
assert sp.simplify(num.subs(c,sp.Rational(1,2)))<0
x=sp.symbols('x',real=True)
assert sp.integrate((x*x-sp.Rational(1,3))**2,(x,-1,1)) == sp.Rational(8,45)
assert sp.integrate(x*x*(x*x-sp.Rational(1,3)),(x,-1,1)) == sp.Rational(8,45)
q=(sp.Symbol('z')**2-1)**2
assert sp.expand(q)==sp.Symbol('z')**4-2*sp.Symbol('z')**2+1
assert sp.diff(q,sp.Symbol('z')).subs(sp.Symbol('z'),1)==0
assert sp.diff(q,sp.Symbol('z')).subs(sp.Symbol('z'),-1)==0
C=mp.mpf(1024)/(135*mp.pi)
assert abs(C-mp.mpf('2.4144394329792713'))<mp.mpf('1e-14')
print('Sharp constant',mp.nstr(C,35))

# Independent exact integration of Fourier coefficients, then eigenspectrum.
def gram(a1,a2,delta):
    # windows centered at 0 and delta; all five Fourier frequencies k=0,..,4
    G=mp.matrix(5)
    for i in range(5):
        for j in range(5):
            k=i-j
            if k==0: G[i,j]=(a1+a2)/mp.pi
            else: G[i,j]=(mp.sin(k*a1)+mp.e**(1j*k*delta)*mp.sin(k*a2))/(mp.pi*k)
    return G

def eigmin(a1,a2,delta):
    G=gram(a1,a2,delta)
    eigs=mp.eig(G,left=False,right=False)
    return min(mp.re(v) for v in eigs)

checks=12
for aS in ('0.15','0.08','0.04','0.02','0.01'):
    a=mp.mpf(aS); a2=a**mp.mpf('1.5'); a1=2*a-a2
    new=eigmin(a1,a2,mp.pi)
    equal=eigmin(a,a,mp.pi)
    assert new>equal
    print('a',aS,'unequal/a^5=',mp.nstr(new/a**5,22),'equal/a^5=',mp.nstr(equal/a**5,22))
    checks+=1
# Test convergence to predicted sharp constant at much finer scales.
prev=mp.mpf(0)
for aS in ('0.025','0.0125','0.00625','0.003125','0.0015625'):
    a=mp.mpf(aS); a2=a**mp.mpf('1.5'); a1=2*a-a2
    lam=eigmin(a1,a2,mp.pi)
    ratio=lam/a**5
    assert prev<ratio<C
    prev=ratio
    checks+=2
# Independent quadrature of every Gram coefficient for a non-antipodal example.
a1=mp.mpf('0.13'); a2=mp.mpf('0.04'); delta=mp.mpf('2.3')
G=gram(a1,a2,delta)
for i in range(5):
 for j in range(5):
    k=i-j
    z=mp.quad(lambda t:mp.e**(1j*k*t),[-a1,a1])/(2*mp.pi)
    z+=mp.quad(lambda t:mp.e**(1j*k*t),[delta-a2,delta+a2])/(2*mp.pi)
    assert abs(G[i,j]-z)<mp.mpf('1e-58')
    checks+=1
# Test the separated-centers upper coefficient against the numerical asymptotics.
for deltaS in ('1.2','2.0','3.14159265358979323846264338327950288419716939937510'):
 delta=mp.mpf(deltaS)
 e=mp.e**(1j*delta)
 qcoeff=[e**2,-2*e*(1+e),1+4*e+e**2,-2*(1+e),1]
 RR=abs(1-e)**4/sum(abs(v)**2 for v in qcoeff)
 assert abs(RR-(4*(1-mp.cos(delta))**2/(34+32*mp.cos(delta)+4*mp.cos(delta)**2)))<mp.mpf('1e-45')
 checks+=1
print('TWO_ARC_FIVE_MODE_CHECKS_PASS',checks)
