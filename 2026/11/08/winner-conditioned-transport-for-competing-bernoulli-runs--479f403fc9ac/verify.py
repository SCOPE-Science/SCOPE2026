"""Independent exact checks for winner-conditioned equal-length Bernoulli-run races.

The finite dynamic program evolves live suffix states without using the
run-block generating-function proof. All comparisons use Fraction arithmetic.
"""
from fractions import Fraction as F
from itertools import product
from math import factorial

def dp(p,r,N):
    q=1-p
    live={(0,0):F(1)}
    hits=[(F(0),F(0)) for _ in range(N+1)]
    for t in range(1,N+1):
        new={}; h=tails=F(0)
        for (last,ell),prob in live.items():
            for sym,weight in ((1,p),(-1,q)):
                k=ell+1 if last==sym else 1
                if k==r:
                    if sym==1:h+=prob*weight
                    else:tails+=prob*weight
                else:
                    key=(sym,k)
                    new[key]=new.get(key,F(0))+prob*weight
        hits[t]=(h,tails)
        live=new
    return hits

def polys(p,r,N):
    q=1-p
    a=[F(0)]*N;b=[F(0)]*N
    for j in range(1,r): a[j]=p**j;b[j]=q**j
    ab=[F(0)]*N
    for i in range(1,r):
        for j in range(1,r):
            if i+j<N:ab[i+j]+=a[i]*b[j]
    den=[F(0)]*N;den[0]=F(1)
    for t in range(1,N):den[t]=sum(ab[j]*den[t-j] for j in range(1,t+1))
    out=[]
    for t in range(N+1):
        h=tail=F(0)
        if t>=r:
            v=t-r
            h=p**r*sum(den[v-j]*(F(1) if j==0 else b[j]) for j in range(min(v,r-1)+1))
            tail=q**r*sum(den[v-j]*(F(1) if j==0 else a[j]) for j in range(min(v,r-1)+1))
        out.append((h,tail))
    return out

def mu(s,r):
    return sum(F(j)*s**j for j in range(r))/sum(s**j for j in range(r))

def checks():
    count=0
    for r in range(2,8):
        for p in (F(1,11),F(1,4),F(2,5),F(1,2),F(3,5),F(3,4),F(10,11)):
            N=34
            x=dp(p,r,N);y=polys(p,r,N+1)
            for t in range(N+1):
                assert x[t]==y[t],(r,p,t,x[t],y[t]);count+=2
            q=1-p
            a=sum(p**j for j in range(1,r)); b=sum(q**j for j in range(1,r))
            ph=p**r*(1+b)/(1-a*b);pt=q**r*(1+a)/(1-a*b)
            assert ph+pt==1;count+=1
            w1=abs(mu(p,r)-mu(q,r))
            if p!=q:
                assert 0<w1<F(r-1,2), (p,r,w1);count+=1
            else:
                assert w1==0;count+=1
            # CDF order at every enumerated step; expectation bound is analytical.
            hc=tc=F(0)
            for h,tail in x:
                hc+=h/ph;tc+=tail/pt
                if p>q: assert hc>=tc,(p,r,hc,tc)
                elif p<q: assert hc<=tc,(p,r,hc,tc)
                else: assert hc==tc
                count+=1
    # Independently enumerate complete short binary words for small horizons.
    for r in range(2,5):
      for p in (F(1,3),F(1,2),F(3,5)):
        D=dp(p,r,10)
        for t in range(r,11):
            h=tt=F(0)
            for seq in product((0,1),repeat=t):
                k=0;prev=-1;first=None
                for i,b in enumerate(seq):
                    k=k+1 if b==prev else 1
                    prev=b
                    if k==r:
                        first=(i+1,b)
                        break
                if first is not None and first[0]==t:
                    w=p**sum(seq)* (1-p)**(t-sum(seq))
                    if first[1]:h+=w
                    else:tt+=w
            assert (h,tt)==D[t],(p,r,t,(h,tt),D[t]);count+=2
    # Exact rational version of the finite-r limiting sharp constant.
    for r in range(2,21):
      a=mu(F(999999,1000000),r)-mu(F(1,1000000),r)
      assert a>F(r-1,2)-F(1,3000), (r,a);count+=1
    print('PASS:',count,'exact assertions; independent state DP and word enumeration')

if __name__=='__main__':checks()
