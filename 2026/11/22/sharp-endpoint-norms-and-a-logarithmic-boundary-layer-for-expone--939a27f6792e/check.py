"""Supplementary numerical checks for rank-two exponential least-squares projection.
Run with python check.py; mpmath is required. These checks supplement, not replace, the proof.
"""
import mpmath as mp
mp.mp.dps=70

def data(lam):
    lam=mp.mpf(lam)
    q=mp.exp(-lam)
    m=-mp.expm1(-lam)/lam
    s=-mp.expm1(-2*lam)/(2*lam)
    v=s-m*m
    ks=[(1-m)/v,(q-m)/v]
    zz=[m-1/k for k in ks]
    tt=[-mp.log(z)/lam for z in zz]
    def f(k,t):
        return (1-k*m)*t+k*(-mp.expm1(-lam*t))/lam
    Lplus=2*f(ks[0],tt[0])-1
    Lminus=1-2*f(ks[1],tt[1])
    return q,m,v,ks,tt,zz,Lplus,Lminus

count=0
for x in ['0.02','0.1','0.2','0.5','1','2','3','7','12','30','80']:
    lam=mp.mpf(x)
    q,m,v,k,t,z,Lp,Lm=data(lam)
    assert q<z[0]<m<z[1]<1
    for endpoint,kj,tj,Lj in [(0,k[0],t[0],Lp),(1,k[1],t[1],Lm)]:
        ker=lambda y: 1+kj*(mp.exp(-lam*y)-m)
        num=mp.quad(lambda y: abs(ker(y)),[0,tj,1])
        assert abs(num-Lj)<mp.mpf('1e-50')
        assert abs(mp.quad(ker,[0,1])-1)<mp.mpf('1e-50')
        # Test no interior evaluation has a larger kernel row norm.
        for j in range(1,10):
            xx=mp.mpf(j)/10
            kii=(mp.exp(-lam*xx)-m)/v
            zz2=m-1/kii if abs(kii)>mp.mpf('1e-40') else None
            breaks=[0,1]
            if zz2 is not None and q<zz2<1: breaks=[0,-mp.log(zz2)/lam,1]
            value=mp.quad(lambda y:abs(1+kii*(mp.exp(-lam*y)-m)),breaks)
            assert value <= max(Lp,Lm)+mp.mpf('1e-45')
            count+=1
    count+=3
# Asymptotics; limit of slope and stiff regime from explicit expansions.
for lam in ['0.001','0.0001','0.00001']:
    p=data(lam)
    assert abs((p[-2]-mp.mpf(5)/3)/mp.mpf(lam)-mp.mpf(4)/27)<mp.mpf('0.001')
    assert abs((p[-1]-mp.mpf(5)/3)/mp.mpf(lam)+mp.mpf(4)/27)<mp.mpf('0.001')
    count+=2
for lam in ['500','1000','5000']:
    p=data(lam)
    lam=mp.mpf(lam)
    leading=2*(mp.log(2*lam)-1)/lam
    assert abs((3-p[-2])-leading)<mp.mpf('0.001')
    assert abs(lam*(p[-1]-1)-2*(1-mp.log(2)))<mp.mpf('0.01')
    count+=2
print(f'PASS {count} endpoint, integral, and asymptotic numeric checks')
