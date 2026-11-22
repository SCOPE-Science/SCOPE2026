import math, numpy as np
from scipy.special import logsumexp

def logkl_perm(z,b):
    z=np.asarray(z,float); b=np.asarray(b,float)
    p=np.argsort(-z,kind='stable'); s=z[p]
    w=np.log(np.sort(b)[::-1]); blocks=[]
    for i in range(len(s)):
        blocks.append([i,i+1,s[i]-w[i]])
        while len(blocks)>1 and blocks[-2][2]<blocks[-1][2]-1e-13:
            a,_,_=blocks[-2]; _,c,_=blocks[-1]
            blocks[-2:]=[[a,c,logsumexp(s[a:c])-logsumexp(w[a:c])]]
    v=np.empty_like(s)
    for a,c,t in blocks: v[a:c]=t
    ret=np.empty_like(s); ret[p]=s-v
    return ret

def test():
    rng=np.random.default_rng(2026)
    for n in range(2,9):
        b=np.exp(np.arange(1,n+1,dtype=float)); B=sum(b); L=2*(1-min(b)/B)
        for i in range(1000):
            z=rng.normal(size=n)*rng.uniform(.01,15)
            h=rng.choice([-1,1],size=n)*rng.uniform(1e-7,1e-3)
            x=logkl_perm(z,b); y=logkl_perm(z+h,b)
            rat=max(abs(x-y))/max(abs(h))
            assert rat<L+1e-6, (n,rat,L,z,h)
        mu=(1-1e-6)*b+1e-6*B/n
        z=np.log(mu)
        j=0
        h=np.ones(n); h[j]=-1
        y=logkl_perm(z+1e-8*h,b)
        x=logkl_perm(z,b)
        ratio=max(abs(y-x))/1e-8
        assert abs(ratio-L)<1e-3,(n,ratio,L)
        print(n,round(L,9),round(ratio,9))
if __name__=='__main__':test()
