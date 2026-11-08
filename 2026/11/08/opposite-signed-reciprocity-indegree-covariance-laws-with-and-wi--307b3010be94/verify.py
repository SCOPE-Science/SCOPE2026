from itertools import combinations,product
from collections import defaultdict
from fractions import Fraction as F
from math import comb

def polynomial(n,k,looped):
    p=F(k,n if looped else n-1)
    q=1-p
    out={}
    for j in range(n+1):
        def b(r,i):return F(comb(r,i))*q**(r-i)*p**i if 0<=i<=r else 0
        if looped:
            A=-F(k*k,2*(n-1))*q*q
            out[j]=A*(b(n-2,j)-2*b(n-2,j-1)+b(n-2,j-2))
        else:
            A=F(comb(n,2))*p*p*q*q/F(n-2)
            out[j]=A*(b(n-3,j)-2*b(n-3,j-1)+b(n-3,j-2))
    return out

def exhaustive(n,k,looped):
    v=tuple(range(n))
    cand=[list(combinations(v if looped else tuple(w for w in v if w!=i),k)) for i in v]
    counts=defaultdict(int)
    tots=[0]*(n+1)
    cross=[0]*(n+1)
    mr=0; t=0
    for choices in product(*cand):
        inc=[0]*n
        for i,edges in enumerate(choices):
            for j in edges:inc[j]+=1
        R=sum((j in choices[i] and i in choices[j]) for i in v for j in range(i+1,n))
        hist=[inc.count(j) for j in range(n+1)]
        mr+=R;t+=1
        for j in range(n+1):
            tots[j]+=hist[j];cross[j]+=R*hist[j]
    return {j:F(cross[j],t)-F(mr,t)*F(tots[j],t) for j in range(n+1)},t

def main():
    checks=0
    for looped in (False,True):
     for n in range(3,6):
      for k in range(1,min(n if looped else n-1,3)+1):
       pred=polynomial(n,k,looped)
       if (len(list(combinations(range(n if looped else n-1),k))))**n>700000:continue
       exact,count=exhaustive(n,k,looped)
       assert pred==exact,(n,k,looped,pred,exact)
       checks+=n+1
       print('PASS', 'loops' if looped else 'loopless',n,k,'graphs',count,'cov0',exact[0])
    print('PASS total coefficient assertions',checks)
if __name__=='__main__':main()
