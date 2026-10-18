#!/usr/bin/env python3
import math
checks=0
for s in range(1,21):
  for t in range(-s+1,s):
    if math.gcd(s,t)!=1: continue
    for n in range(1,13):
      for r in range(1,13):
        h0=r+s-1
        assert h0-s==r-1<r
        for h in range(r,h0):
          assert (h-h0)%s!=0
        for k in range(1,7):
          xs=[s*i+t for i in range(n,n+h0)]
          assert min(xs)>0 and all(xs[j]<xs[j+1] for j in range(len(xs)-1))
          if s>1:
            rr={pow(a,k,s) for a in xs}
            assert rr=={pow(t,k,s)}
          M=sum(a**k for a in xs); M1=sum(xs)
          assert M>=M1
          assert 1-s+M>=1-s+M1
          checks+=1
print("VERIFY_OK",f"parameter_checks={checks}","s<=20 n<=12 r<=12 k<=6")
