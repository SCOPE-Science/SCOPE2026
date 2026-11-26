from fractions import Fraction as F
from functools import lru_cache
import mpmath as mp
mp.mp.dps=45

def cavity_fast(a,x,k):
    a=mp.mpf(a)
    if k==1: return mp.quad(lambda y:mp.exp(-y)*(1-a*(1-y)**(a-1)),[0,x])
    # convolution k-1 on base derivative
    return (-1)**(k-1)/mp.factorial(k-1)*mp.quad(lambda y:mp.exp(-y)*(1-a*(1-y)**(a-1))*(x-y)**(k-1),[0,x])
# For k=1 formula exponent0 correct. For k=2 delta2=-int delta1 = -int derivative*(x-y), yes.
def interaction_integral(a,b,d,j):
    return mp.quad(lambda x: cavity_fast(a,x,j)*cavity_fast(b,x,d-j),[0,1])

def exact_target(m, specials, target):
    rates=[F(specials.get(i,1)) for i in range(m)]
    prefix=[F(0)]
    for rate in rates: prefix.append(prefix[-1]+rate)
    @lru_cache(None)
    def rec(l,r):
        if l>r or not l<=target<=r: return F(0)
        norm=prefix[r+1]-prefix[l]
        out=F(0)
        for i in range(l,r+1):
            if i==target: out+= rates[i]/norm
            elif i<=target-2: out+=rates[i]/norm*rec(i+2,r)
            elif i>=target+2: out+=rates[i]/norm*rec(l,i-2)
        return out
    return rec(0,m-1)

if __name__=='__main__':
    for d in (2,3,4,5):
        for j in range(1,d):
            a,b=2,3
            e=interaction_integral(a,b,d,j)
            # Finite-path first-event recursion, twelve homogeneous edges at each end
            n=2*12+d+1; start=12
            p11=exact_target(n,{start:1,start+d:1},start+j)
            pa1=exact_target(n,{start:a,start+d:1},start+j)
            p1b=exact_target(n,{start:1,start+d:b},start+j)
            pab=exact_target(n,{start:a,start+d:b},start+j)
            ef=pab-pa1-p1b+p11
            print(d,j,mp.nstr(e,15),float(ef),float(ef)-float(e), 'sign', (e>0)==(d%2==0))
            assert abs(float(ef)-float(e)) < 1e-10
    print('PASS')
