"""Supplementary exact-symbolic and numerical checks for the geodesic covariance theorem.

Run: python checker.py
Requires: sympy and mpmath (see requirements.txt).
The infinite-degree theorem is proved analytically in RESULT.md; finite tests are not its proof.
"""
import math
import sympy as sp
import mpmath as mp

n, y, z = sp.symbols('n y z', real=True)
checks = 0

def insist(condition, message):
    global checks
    if not bool(condition):
        raise AssertionError(message)
    checks += 1

m = n*(n+1)
D = sp.expand((y+(n-2)**2)*(y+(n+3)**2))
R = 1 + 6*(3*m-2*y-8)/D
A = (n+1)*(n+2)/((2*n+1)*(2*n+3))
B = (n+1)**2/((2*n+1)*(2*n+3)) + n**2/((2*n+1)*(2*n-1))
C = n*(n-1)/((2*n+1)*(2*n-1))
R_via_three_terms = 2*(A*(y+n**2)/(y+(n+3)**2) + B + C*(y+(n+1)**2)/(y+(n-2)**2))-1
insist(sp.cancel(R_via_three_terms-R)==0, 'Legendre three-term multiplication')
insist(sp.cancel(R.subs(n,0)-(y-3)/(y+9))==0, 'degree zero')
insist(sp.cancel(R.subs(n,1)-(y+4)/(y+16))==0, 'degree one')
D_cont = (z+y-6)**2 + 25*y
R_cont = 1+6*(3*z-2*y-8)/D_cont
insist(sp.cancel(D-D_cont.subs(z,m))==0, 'Lorentzian denominator')
insist(sp.cancel(R-R_cont.subs(z,m))==0, 'rational profile')
num_deriv = -3*z**2+(4*y+16)*z+7*y**2+31*y+12
insist(sp.cancel(sp.diff(R_cont,z)-6*num_deriv/D_cont**2)==0, 'continuous derivative')
zplus = (2*y+8+5*sp.sqrt((y+1)*(y+4)))/3
insist(sp.simplify(num_deriv.subs(z,zplus))==0, 'critical point')
P = 7*y**2+(4*n**2+8*n+35)*y-3*n**4-12*n**3+n**2+26*n+28
Dnext = D.subs(n,n+1)
insist(sp.cancel(R-R.subs(n,n+1)+12*(n+1)*P/(D*Dnext))==0, 'adjacent crossing')
u = sp.symbols('u', real=True)
insist(sp.expand((-P.subs(y,0)).subs(n,u+2)) == 3*u**4+36*u**3+143*u**2+210*u+60,
       'positive transition constant')
insist(sp.limit(y*(R_cont.subs(z,zplus)-1),y,sp.oo) == sp.Rational(27,10),
       'large-parameter continuous maximum')

mp.mp.dps=45
for aval in ('0.2', '0.5', '1.0', '1.7320508075688772', '2.0', '4.0'):
    a=mp.mpf(aval)
    v=a*a
    E=mp.e**(-mp.pi*a)
    def moment(k):
        return mp.quad(lambda theta: mp.exp(-a*theta)*mp.legendre(k,mp.cos(theta))*mp.sin(theta), [0,mp.pi])
    moments=[moment(j) for j in range(13)]
    insist(mp.almosteq(moments[0],(1+E)/(1+v),rel_eps=mp.mpf('1e-32')), 'I_0')
    insist(mp.almosteq(moments[1],(1-E)/(4+v),rel_eps=mp.mpf('1e-32')), 'I_1')
    for k in range(11):
        insist(mp.almosteq(moments[k+2]/moments[k], (v+k*k)/(v+(k+3)**2),rel_eps=mp.mpf('1e-25')),
               f'Legendre recurrence {aval}, {k}')
    for k in range(13):
        direct=mp.quad(lambda theta: mp.exp(-a*theta)*mp.cos(2*theta)*mp.legendre(k,mp.cos(theta))*mp.sin(theta),[0,mp.pi])
        ratio=1+6*(3*k*(k+1)-2*v-8)/((v+(k-2)**2)*(v+(k+3)**2))
        insist(mp.almosteq(direct/moments[k],ratio,rel_eps=mp.mpf('1e-25')),
               f'modulated coefficient {aval}, {k}')

for j in range(1,81):
    aval=0.035*j + j*j/100
    v=aval*aval
    critical=(2*v+8+5*math.sqrt((v+1)*(v+4)))/3
    k=max(2,int(math.floor((math.sqrt(1+4*critical)-1)/2)))
    def rn(deg):
        return 1+6*(3*deg*(deg+1)-2*v-8)/((v+(deg-2)**2)*(v+(deg+3)**2))
    exact=max(rn(k),rn(k+1))
    insist(abs(exact-max(rn(d) for d in range(180))) < 1e-12, 'two-mode maximizer')
    bmin=-1/exact
    insist(all(1+bmin*rn(d)>-1e-11 for d in range(180)), 'boundary positivity')
    controlled=[d for d in range(180) if abs(1+bmin*rn(d))<1e-10]
    insist(len(controlled) in (1,2) and all(d in (k,k+1) for d in controlled),'spectral notch')
    insist(1+(bmin-0.0001)*rn(controlled[0])<0, 'sharp lower threshold')
    if v<3:
        bmax=(v+9)/(3-v)
        insist(abs(1+bmax*rn(0))<1e-11, 'upper boundary degree zero')
        insist(all(1+bmax*rn(d)>-1e-10 for d in range(180)), 'upper boundary all modes')
        insist(1+(bmax+0.0001)*rn(0)<0, 'upper sharpness')
    else:
        insist(all(rn(d)>0 for d in range(180)), 'positive second harmonic')

for j in range(2,62):
    polynomial=sp.Poly(P.subs(n,j),y)
    roots=[float(sp.re(q)) for q in sp.nroots(polynomial) if abs(float(sp.im(q)))<1e-12 and float(sp.re(q))>0]
    insist(len(roots)==1, 'one adjacent switch')
    val=roots[0]
    Rf=lambda k:1+6*(3*k*(k+1)-2*val-8)/((val+(k-2)**2)*(val+(k+3)**2))
    insist(abs(Rf(j)-Rf(j+1))<1e-9, 'two-mode tie')
    if j>2: insist(val>previous, 'ordered transitions')
    previous=val

print(f'PASS: {checks} supplementary symbolic/numerical assertions.')
print('Universal theorem, strictness, and all-parameter transitions require analytic proof in RESULT.md.')
