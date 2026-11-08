from fractions import Fraction as F
from math import comb
from collections import defaultdict

def weights(p,n):
 q=1-p
 def B(s):
  if (n+s)%2 or abs(s)>n: return F(0)
  k=(n+s)//2
  return F(comb(n,k))*p**k*q**(n-k)
 def Fm(m,s):
  if m<0 or s>m:return F(0)
  return B(s)-(q/p)**(m+1-s)*B(2*m+2-s)
 W={}
 for m in range(n+1):
  for s in range(-n,m+1):
   v=Fm(m,s)-Fm(m-1,s)
   if v:W[m,s]=v
 return W

def lev(p,N):
 b=2*(1-p)/p; d=(2*p-1)/p
 G=F(1);partial_4=F(0);partial_2=F(0)
 out=[]
 for m in range(N+1):
  v=d*(F(3,4)*partial_4+F(1,12*2**m)*partial_2+(F(1,3)*(F(1,4**m)*G+2**m*(b/F(8))**(m+1)/(1-b/F(8)))))
  out.append(v)
  partial_4+=G/F(4**(m+1));partial_2+=G/F(2**(m+1))
  G+=b**(m+1)
 return out

def stat(p,n):
 W=weights(p,n);L=lev(p,n);mu=(2*p-1)/(3*p-1)
 V=sum(v*F(1,2**(m-s))*L[m] for (m,s),v in W.items());return V-mu**2

# A self-contained series calculator, independent of ballot reflection and dyadic sums.
def series_coeff(p, t, N):
    # Formal power-series solution r(z) = qz + pz r(z)^2,
    # followed by the denominator identity for Phi(z;t).
    q=1-p
    r=[F(0)]*(N+1)
    for k in range(1,N+1,2):
        if k==1:r[k]=q
        else:r[k]=p*sum(r[i]*r[k-1-i] for i in range(1,k-1))
    d=[F(0)]*(N+1);d[0]=1
    for k in range(1,N+1):
        # (1 - p t z - p z r)(1-r/2)
        a_k= -p*t if k==1 else (-p*r[k-1] if k>=2 else F(0))
        b_k=-r[k]/2
        d[k]=a_k+b_k+sum(((-p*t if i==1 else -p*r[i-1]) if i>=1 else F(0))* (-r[k-i]/2) for i in range(1,k))
    c=[F(0)]*(N+1);c[0]=1
    for k in range(1,N+1):c[k]=-sum(d[i]*c[k-i] for i in range(1,k+1))
    return c

def check():
    count=0
    for p in (F(11,20),F(3,5),F(2,3),F(4,5),F(9,10),F(1,1)):
        mu=(2*p-1)/(3*p-1)
        B=(p-1)*(7*p-3)/(4*(3*p-1)*(5*p-1))
        v=(1-p)/(2*p)
        L=lev(p,15)
        for m in range(16):
            assert L[m]==mu/2+F(1,12*2**m)+B*v**m
            count+=1
        K1=series_coeff(p,F(1),16)
        Khalf=series_coeff(p,F(1,2),16)
        Kc=series_coeff(p,v,16)
        for n in range(17):
            cov=mu/F(2)*K1[n]+F(1,12)*Khalf[n]+B*Kc[n]-mu*mu
            assert cov==stat(p,n), (p,n,cov,stat(p,n))
            count+=1
        # original publication's first two lags, including endpoints
        d=2*p-1
        raw1=stat(p,1)+mu*mu
        assert raw1==d*(3*p+25)/(24*(5*p-1)),(p,raw1)
        raw2=stat(p,2)+mu*mu
        assert raw2==d*((3*p+1)**2/(3*(5*p-1))-(11*p+6)/16),(p,raw2)
        count+=2
        if p==1:
            for n in range(17):assert stat(p,n)==F(1,12*2**n)
    print('PASS:',count,'exact rational identities; generating series vs ballot/reflection, 6 p values, n <=16, and published lag-1/2 formulas.')
    import math
    for p,n in [(F(4,5),80),(F(4,5),160),(F(9,10),80),(F(9,10),160)]:
        pf=float(p);c=float(stat(p,n))
        if p==F(4,5): pred=2/(9*math.sqrt(2*math.pi))*.8**n/math.sqrt(n); tolerance=.006
        else: pred=(5*pf-4)/(12*(2*pf-1))*((4-3*pf)/2)**n;tolerance=.0001
        assert abs(c/pred-1)<tolerance,(p,n,c/pred)
        print('PASS asymptotic spot-check:',str(p),'lag',n,'ratio',repr(c/pred))
    print('ALL CHECKS PASSED')

if __name__=='__main__': check()
