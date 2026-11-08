from fractions import Fraction as F
from math import sqrt,pi

def covar(m,a,N):
    p=m*a; b=1-p
    v={0:F(1)};out=[]
    for n in range(N+1):
        out.append(sum((w / m**k for k,w in v.items()),F(0))/12)
        nxt={}
        for k,w in v.items():
            if k==0:
                nxt[0]=nxt.get(0,F(0))+a*w
                nxt[1]=nxt.get(1,F(0))+b*w
            else:
                nxt[k-1]=nxt.get(k-1,F(0))+p*w
                nxt[k+1]=nxt.get(k+1,F(0))+b*w
        v=nxt
    return out

def gf_series(m,a,N):
    p=m*a;b=1-p
    # r = b*t+p*t*r*r, calculate formal power series
    r=[F(0)]*(N+1)
    for n in range(1,N+1):
        r[n] = (b if n==1 else F(0)) + (p*sum(r[j]*r[n-1-j] for j in range(n)))
    # denominator 12*(1-r/m)*(1-at-pt r), inverse directly
    f=[F(0)]*(N+1);g=[F(0)]*(N+1)
    f[0]=g[0]=F(1)
    for n in range(1,N+1):
        f[n]=-r[n]/m
        g[n]=-(a if n==1 else F(0))-p*r[n-1]
    d=[sum(f[j]*g[n-j] for j in range(n+1)) for n in range(N+1)]
    c=[F(0)]*(N+1);c[0]=F(1,12)
    for n in range(1,N+1):c[n]=-sum(d[j]*c[n-j] for j in range(1,n+1))
    return c

for m in [2,3,4]:
 for den,numer in [(30,1),(10,1),(4,1),(3,1),(10,4),(20,9)]:
    a=F(numer,den)
    if a>=F(1,m):continue
    direct=covar(m,a,28);from_gf=gf_series(m,a,28)
    assert direct==from_gf, (m,a,[(i,x,y) for i,(x,y) in enumerate(zip(direct,from_gf)) if x!=y][:2])
print('All 18-or-fewer independent rational recurrence and formal resolvent comparisons passed, 29 coefficients per case.')
for m,a in [(2,F(1,4)),(2,F(1,3)),(2,F(1,20)),(2,F(9,20)),(3,F(1,6)),(3,F(1,30)),(3,F(3,10))]:
 c=covar(m,a,350)
 p=float(m*a);b=1-p;R=1/(2*sqrt(p*b));s=sqrt(b/p)
 lo=1/(m*(m*m+1));hi=m/(m*m+1)
 if float(a)<lo:
    rate=1/m+(m*m-1)*float(a);amp=(b-m*m*p)/(12*(1-2*p));mode='low-pole'
 elif float(a)>hi:
    rate=m-(m*m-1)*float(a);amp=m*(float(a)-m*b)/(12*(2*p-1));mode='high-pole'
 else:
    rate=1/R
    if abs(float(a)-lo)<1e-12 or abs(float(a)-hi)<1e-12:
        amp=1/(6*(1-1/m**2)*sqrt(2*pi));mode='critical'
    else:
        A=1-s/m; B=(1-2*float(a)*R)/2
        amp=1/(12*A*B*sqrt(2*pi))*(s/(m*A)+1/(2*B))
        mode='branch'
 if mode.endswith('pole'): test=float(c[250])/(amp*rate**250)
 elif mode=='critical':test=float(c[250])/(amp*rate**250/250**0.5)
 else:test=float(c[250])/(amp*rate**250/250**1.5)
 print('m,a',m,str(a),'mode',mode,'ratio',test,'rate',rate,'amp',amp)
