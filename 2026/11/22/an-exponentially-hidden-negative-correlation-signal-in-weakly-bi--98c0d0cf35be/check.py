"""Independent exact-algebra and numerical checks of a three-state transport-memory law.

Run: python check.py
Requires sympy, scipy, mpmath, numpy.
"""
import sympy as s
import numpy as np
from scipy.linalg import expm
import mpmath as mp

z, a, b, k = s.symbols('z a b k')
Q=s.Matrix([[-a-b,1-a,1-b],[a,-1+a-k,k],[b,k,-1+b-k]])
D=1-a*b+k*(2+a+b)
p=s.factor((k*(a+b)+a*(1-b))/D)
q=s.factor((k*(a+b)+b*(1-a))/D)
pi=s.Matrix([1-p-q,p,q]); assert all(s.factor(x)==0 for x in Q*pi)
assert s.factor(Q.charpoly(z).as_expr()-z*((z+1+k)**2-(k-a)*(k-b)))==0
m,d=s.symbols('m d',positive=True)
subs={a:m+d,b:m-d,k:m}
pd=s.factor(p.subs(subs))
A=s.factor(pd*(1-pd))
B=s.factor(pd*((m+d)-(1+m)*pd)/d)
Den=d*d+(1+m)**2
assert s.factor(pd-(d*d+d+m*m+m)/Den)==0
assert s.factor(A-((1+m-d)*(d*d+d+m*m+m))/Den**2)==0
assert s.factor(B-((d*d-d+m*m+m)*(d*d+d+m*m+m))/Den**2)==0
assert s.factor(B/A-(d*d-d+m*m+m)/(1+m-d))==0
assert s.simplify(s.limit(B/A,d,0)-m)==0
assert s.simplify(s.limit(A,d,0)-m/(1+m)**2)==0
assert s.simplify(s.limit(B,d,0)-m*m/(1+m)**2)==0

# Direct matrix exponential checks of autocovariance and negative minimum.
for mm, dd, gamma in ((.5,.3,1),(.37,.12,2.3),(.8,.05,.7)):
    aa,bb,kk=mm+dd,mm-dd,mm
    Qn=np.array(Q.subs({a:aa,b:bb,k:kk}),dtype=float)*gamma
    pp=float(pd.subs({m:mm,d:dd})); aa0=float(A.subs({m:mm,d:dd})); bb0=float(B.subs({m:mm,d:dd}))
    omega=gamma*dd; decay=gamma*(1+mm)
    phi=np.arctan2(bb0,aa0)
    tzero=(np.pi/2+phi)/omega
    tmin=tzero+np.arctan(omega/decay)/omega
    amp=np.hypot(aa0,bb0)
    negative=amp*omega/np.hypot(decay,omega)*np.exp(-decay*tmin)
    for tt in (0.,.1,1.,tzero, tmin, tmin+2/omega):
        exact=pp*(expm(Qn*tt)[1,1]-pp)
        spectral=np.exp(-decay*tt)*(aa0*np.cos(omega*tt)+bb0*np.sin(omega*tt))
        assert abs(exact-spectral)<1e-11, (mm,dd,tt,exact,spectral)
    assert negative>0
    assert abs(np.exp(-decay*tmin)*(aa0*np.cos(omega*tmin)+bb0*np.sin(omega*tmin))+negative)<1e-12

# Stable arbitrary-precision evaluation of the essential singularity.
mp.mp.dps=65
mm=mp.mpf('0.5')
L=-(1+mm)*(mp.pi/2+mp.atan(mm))
errs=[]
for dstr in ('0.04','0.02','0.01','0.005'):
    dd=mp.mpf(dstr); Den=dd**2+(1+mm)**2
    p=(dd**2+dd+mm**2+mm)/Den
    A=p*(1-p)
    B=(dd**2-dd+mm**2+mm)*(dd**2+dd+mm**2+mm)/Den**2
    ph=mp.atan(B/A)
    tmin=(mp.pi/2+ph+mp.atan(dd/(1+mm)))/dd
    M=mp.sqrt(A*A+B*B)*dd/mp.sqrt((1+mm)**2+dd**2)*mp.exp(-(1+mm)*tmin)
    assert M>0
    errs.append(abs(dd*mp.log(M)-L))
assert errs[-1]<errs[0]/3 and errs[-1] < mp.mpf('.04')
print('PASS: generator, stationary solution, spectral polynomial, exact amplitudes, 18 matrix-exponential checks, three global-minimum checks and weak-bias limit')
print('Essential exponent (m=1/2):',mp.nstr(L,25),' last error:',mp.nstr(errs[-1],10))
