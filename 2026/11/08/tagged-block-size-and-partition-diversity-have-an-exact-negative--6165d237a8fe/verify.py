"""Exact rational independent state-space checks of a two-parameter partition moment identity.
Run: python3 verify.py (standard library only).
This finite test supports, but does not replace, the analytic proof.
"""
from collections import defaultdict
from fractions import Fraction as F


def rising(x, m):
    y = F(1)
    for i in range(m):
        y *= x + i
    return y


def closed(n, a, t):
    assert n >= 2 and 0 <= a < 1 and t > -a and t + a > 0
    ux = (1-a) * (t+n) / (t+1)
    es = ux+a
    vy = (t+a)*rising(t+1+a,n-1)/rising(t+1,n-1)
    if a:
        ek = (vy-t)/a
        qy = (t+a)*(t+2*a)*rising(t+1+2*a,n-1)/rising(t+1,n-1)
        vk = (qy-a*vy-vy*vy)/(a*a)
    else:
        ek = 1 + sum((t/(t+j) for j in range(1,n)),F(0))
        vk = sum((t*j/((t+j)*(t+j)) for j in range(1,n)),F(0))
    vs = (n-1)*(1-a)*(t+a)*(n+t)/((t+1)*(t+1)*(t+2))
    cov = -(1-a)*(t+a)*(n-1)*rising(t+2+a,n-2)/((t+1)*rising(t+1,n-1))
    return es,ek,vs,vk,cov


def independent(n,a,t):
    dist = {(1,1):F(1)}
    for j in range(1,n):
        nxt = defaultdict(F)
        for (s,k), p in dist.items():
            z=t+j
            u=(s-a)/z
            v=(t+a*k)/z
            w=1-u-v
            assert u>=0 and v>=0 and w>=0 and u+v+w==1
            nxt[s+1,k] += p*u
            nxt[s,k+1] += p*v
            nxt[s,k] += p*w
        dist=nxt
        assert sum(dist.values())==1
    es=sum((p*s for (s,k),p in dist.items()),F(0))
    ek=sum((p*k for (s,k),p in dist.items()),F(0))
    vs=sum((p*s*s for (s,k),p in dist.items()),F(0))-es*es
    vk=sum((p*k*k for (s,k),p in dist.items()),F(0))-ek*ek
    cov=sum((p*s*k for (s,k),p in dist.items()),F(0))-es*ek
    return es,ek,vs,vk,cov


def main():
    pairs = [(F(0),F(1)),(F(0),F(2)),(F(1,3),F(1)),
             (F(1,2),F(0)),(F(1,2),F(3,2)),(F(3,4),F(-1,2)),
             (F(1,4),F(-1,8)),(F(2,3),F(4))]
    tests=0
    for a,t in pairs:
        for n in range(2,31):
            theory=closed(n,a,t)
            actual=independent(n,a,t)
            for label,x,y in zip(('ES','EK','VarS','VarK','Cov'),theory,actual):
                assert x==y,(n,a,t,label,x,y)
                tests+=1
            assert theory[4]<0
            tests+=1
    print('PASS: %d exact moment-and-sign checks on %d parameter families and 29 sample sizes' % (tests,len(pairs)))

if __name__=='__main__':
    main()
