from collections import Counter
from itertools import product
from math import comb

def spectrum_counts(n):
    out=Counter()
    for t0 in range(n+1):
      for t1 in range(n-t0+1):
        for t2 in range(n-t0-t1+1):
          t3=n-t0-t1-t2
          t=(t0,t1,t2,t3)
          w=2*sum(x*x for x in t)-n*(n+3)//2
          m=comb(n,t0)*comb(n-t0,t1)*comb(n-t0-t1,t2)
          out[w]+=m
    assert sum(out.values())==4**n
    assert sum(v*c for v,c in out.items())==0
    assert sum(v*v*c for v,c in out.items())==4**n*3*comb(n,2)
    return out

def direct(n):
    out=Counter()
    for bits in product((1,-1),repeat=3*n):
      w=sum(bits[3*i+r]*bits[3*j+r]*bits[3*i+s]*bits[3*j+s]
            for i in range(n) for j in range(i+1,n)
            for r in range(3) for s in range(r+1,3))
      out[w]+=1
    return out

for n in range(2,9):
 hist=spectrum_counts(n)
 z=hist[0]
 if n<=5:
    d=direct(n)
    assert all(d.get(k,0)==v*2**n for k,v in hist.items()),(n,d,hist)
 print('n',n,'zero_4type',z,'full_support',z==0,'Eabs_num',sum(abs(w)*c for w,c in hist.items()))
for n in range(2,81):
 z=spectrum_counts(n)[0] if n<=22 else None
 if n<=22:
    if n%8==1 and n>=9: theoretical=True
    elif n%8==0 and n>=8:
       k=n//8
       x=6*k
       while x%4==0: x//=4
       theoretical=x%8 !=7
    else:theoretical=False
    assert (z>0)==theoretical,(n,z,theoretical)
print('ALL_C4_CHECKS_PASS')
