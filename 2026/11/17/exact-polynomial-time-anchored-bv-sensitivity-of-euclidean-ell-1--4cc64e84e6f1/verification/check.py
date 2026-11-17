"""Exact arithmetic checks for anchored-variation norm of Euclidean l1-ball projection."""
from fractions import Fraction as Q
from itertools import product
import random

def anchored(a):
    old=Q(0); score=Q(0)
    for v in a:
        score+=abs(v-old);old=v
    return score

def projection(x,r=Q(1)):
    x=list(map(Q,x));r=Q(r)
    if sum(map(abs,x))<=r:return x[:]
    mags=sorted((abs(v) for v in x),reverse=True)
    t=None
    for m in range(1,len(x)+1):
        candidate=(sum(mags[:m])-r)/m
        if candidate>=0 and mags[m-1]>candidate and (m==len(x) or mags[m]<=candidate):
            t=candidate;break
    assert t is not None
    return [(1 if v>0 else -1 if v<0 else 0)*max(abs(v)-t,0) for v in x]

def direct(q,k):
    n=len(q);m=sum(bool(x) for x in q)
    if not m: return Q(0)
    t=sum(q[k:]); arr=[Q(m*(i>=k)-t*q[i],m) if q[i] else Q(0) for i in range(n)]
    return anchored(arr)

def dyn(n):
    winner=(Q(1),None,None,None)
    for m in range(2,n+1):
        for k in range(n):
            for t in range(-m,m+1):
                dp={(0,0,0):0}
                for i in range(n):
                    nd={}
                    for (a,b,p),sc in dp.items():
                        old=(m*(i-1>=k)-t*p) if p else 0
                        for q in (-1,0,1):
                            aa=a+(q!=0);bb=b+(q if i>=k else 0)
                            if aa>m or abs(t-bb)>m-aa: continue
                            new=(m*(i>=k)-t*q) if q else 0
                            key=(aa,bb,q); vv=sc+abs(new-old)
                            if vv>nd.get(key,-1):nd[key]=vv
                    dp=nd
                    if not dp:break
                val=max((sc for (a,b,p),sc in dp.items() if a==m and b==t),default=0)
                f=Q(val,m)
                if f>winner[0]:winner=(f,m,k,t)
    return winner

def brute(n):
    best=Q(1)
    for q in product((-1,0,1),repeat=n):
        if sum(bool(t) for t in q)<2:continue
        for k in range(n): best=max(best,direct(q,k))
    return best

def patterned(n):
    m=(n+1)//2
    q=[0]*n
    for j in range(m):q[2*j]=1 if j<m//2 else -1
    if m%2==0:pass
    # when m odd, choose one more negative than positive, so t=-1
    # for odd n, final active sign matches t, ensuring deficit 1/m
    return q

if __name__=='__main__':
    expected={2:Q(3,2),3:Q(3),4:Q(4),5:Q(14,3),6:Q(16,3),7:Q(7),8:Q(8),9:Q(44,5),10:Q(48,5),11:Q(11),12:Q(12),13:Q(90,7),14:Q(96,7),15:Q(15)}
    for n in range(2,16):
        v,_,_,_=dyn(n);assert v==expected[n],(n,v)
        if n<=8:assert brute(n)==v,(n,brute(n),v)
        print(f'EXACT_DYNAMIC_N{n}_PASS_{v}',flush=True)
    for n in range(3,101):
        q=patterned(n);m=(n+1)//2
        target=(Q(n) if m%2==0 else Q(n)-(Q(1,m) if n%2 else Q(2,m)))
        assert direct(q,0)==target,(n,direct(q,0),target)
    print('ANALYTIC_PATTERN_WITNESSES_N3_TO_N100_PASS',flush=True)
    for n in range(2,18):
        for i in range(90):
            q=[random.Random(1093*n+i+j).choice((-1,0,1)) for j in range(n)]
            m=sum(bool(t) for t in q)
            if m<2:continue
            k=(13*i+n)%n;R=Q(1);rho=Q(2)
            x=[Q(v)*(rho+R/m) for v in q]; eps=Q(1,100*n)
            xx=[xi+(eps if j>=k else 0) for j,xi in enumerate(x)]
            z=projection(x);zz=projection(xx)
            assert anchored([a-b for a,b in zip(zz,z)])/eps==direct(q,k)
    print('FINITE_INPUT_PAIR_KKT_WITNESSES_PASS')
    print('ALL_ANCHORED_BV_CROSSPOLYTOPE_CHECKS_PASS')
