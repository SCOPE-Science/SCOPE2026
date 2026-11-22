"""Independent numerical checks for two outward-shifted Fourier quadrature nodes.

Run: python verify.py
This finite test suite supplements, but cannot replace, the analytic proof.
"""
from mpmath import mp

mp.dps=65

def sinv(v):
    return mp.sin(v)

def threshold(n):
    x=mp.pi/n
    def H(a):
        return sinv(a*x)*sum(1/sinv(t*x) for t in (1-a,1+a,2+a))
    lo,hi=mp.mpf('0'),mp.mpf('0.5')
    for _ in range(230):
        mid=(lo+hi)/2
        if H(mid)<1:lo=mid
        else:hi=mid
    return (lo+hi)/2

def closed_weights(n,alpha):
    a=mp.mpf(alpha);x=mp.pi/n
    if a==0: return [mp.mpf(1)/n]*n
    den=1/sinv(a*x)-1/sinv((1+a)*x)
    t=1/(sinv(mp.pi*a)*den)
    return [t if j in (0,1) else (1-(-1)**j*(1/sinv((j+a)*x)+1/sinv((j-1-a)*x))/den)/n for j in range(n)]

def direct_weights(n,alpha):
    a=mp.mpf(alpha)
    angles=[2*mp.pi*(mp.mpf(j)+(-a if j==0 else a if j==1 else 0))/n for j in range(n)]
    ks=list(range(-(n//2),n//2+1))
    A=mp.matrix([[mp.exp(1j*k*t) for t in angles] for k in ks])
    b=mp.matrix([int(k==0) for k in ks])
    z=mp.lu_solve(A,b)
    assert max(abs(mp.im(v)) for v in z)<mp.mpf('1e-54')
    return [mp.re(v) for v in z]

def noise_sum(n,alpha):
    a=mp.mpf(alpha);x=mp.pi/n
    if a==0: return mp.mpf(1)/n
    S=sinv(mp.pi*a)*(1/sinv(a*x)-1/sinv((1+a)*x))
    Q=-sinv(2*mp.pi*a)/(n*sinv((1+2*a)*x))
    return mp.mpf(1)/n+(4+2*Q-4*S/n)/S**2

checks=0
prev=mp.mpf('0')
for n in range(3,32,2):
    crit=threshold(n)
    assert crit>prev
    prev=crit
    for a in ('0.01','0.1','0.2','0.27','0.33','0.38','0.45','0.49'):
        alpha=mp.mpf(a)
        w=closed_weights(n,alpha)
        v=direct_weights(n,alpha)
        assert max(abs(u-z) for u,z in zip(w,v))<mp.mpf('1e-53')
        assert abs(sum(w)-1)<mp.mpf('1e-55')
        assert abs(sum(x*x for x in w)-noise_sum(n,alpha))<mp.mpf('1e-53')
        assert (min(w)>=0)==(alpha<=crit)
        if alpha>crit: assert w[2]<0 and w[n-1]<0
        checks+=3
    at=closed_weights(n,crit)
    assert abs(at[2])<mp.mpf('1e-54')
    assert abs(at[n-1])<mp.mpf('1e-54')
    assert min(at)>=-mp.mpf('1e-54')
    checks+=3
assert abs(threshold(3)-mp.mpf(1)/4)<mp.mpf('1e-54')
assert abs(threshold(5)-mp.mpf(1)/3)<mp.mpf('1e-54')
r=(mp.sqrt(3)-1)/2
for n in [101,501,2001]:
    a=threshold(n)
    assert a<r
    rem=(r-a-mp.sqrt(3)*mp.pi**2/(24*n**2))*n**4
    assert abs(rem)<mp.mpf('1000.0')
    checks+=2
print('PASS:',checks,'high-precision direct/closed/noise/threshold consistency checks')
for n in (3,5,7,11,51,201):
 print('n=',n,'alpha_c=',mp.nstr(threshold(n),19))
print('limit=',mp.nstr(r,19),' coefficient=',mp.nstr(mp.sqrt(3)*mp.pi**2/24,18))
