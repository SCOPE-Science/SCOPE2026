from collections import Counter

def formula(p,k):
 n=p**k; m=p**(k-1)*(p+1); C=Counter({m:1});
 for t in range((k-1)//2+1):
  C[2*p**t]+=m*((p-1)//2)*p**(k-2*t-1)
 C[p**(k//2)]+=m
 for v in range(1,k):
  C[2*p**v]+=(p*p-1)//2*p**(2*(k-v)-2)
 C[0]=n*n-sum(C.values())
 return C,3*p**(2*k-2)*(p+1)*(1+k*(p-1))

def value_prediction(p,k,x,y):
    q=p**k
    m=p**(k-1)*(p+1)
    if x==0 and y==0:return m
    def valuation(a):
        if a==0:return k
        v=0
        while a%p==0:
            a//=p
            v+=1
        return v
    v=min(valuation(x),valuation(y))
    if v==0:
        norm=(x*x+y*y)%q
        assert norm%p!=0
        u=(4*pow(norm,-1,q)-1)%q
        if u==0:return p**(k//2)
        r=valuation(u)
        if r%2:return 0
        lead=(u//(p**r))%p
        return 2*p**(r//2) if pow(lead,(p-1)//2,p)==1 else 0
    h=k-v
    w1=(x//(p**v))%(p**h)
    w2=(y//(p**v))%(p**h)
    lead=(w1*w1+w2*w2)%p
    assert lead!=0
    return 2*p**v if pow(lead,(p-1)//2,p)==1 else 0

def check(p,k):
 q=p**k
 circle=[(x,y) for x in range(q) for y in range(q) if (x*x+y*y)%q==1]
 counts=Counter(((x+a)%q,(y+b)%q) for (x,y) in circle for (a,b) in circle)
 hist=Counter(counts.values());hist[0]=q*q-len(counts)
 want,e=formula(p,k)
 for x in range(q):
  for y in range(q):
   assert counts.get((x,y),0)==value_prediction(p,k,x,y), (p,k,x,y,counts.get((x,y),0),value_prediction(p,k,x,y))
 assert len(counts)==q*q-hist[0]
 print(p,k,'circle',len(circle),'observed',sorted(hist.items()),'desired',sorted(want.items()),'energy',sum(z*z*c for z,c in hist.items()),'formula',e)
 assert hist==want and e==sum(z*z*c for z,c in hist.items())
for p,k in [(3,1),(3,2),(3,3),(3,4),(7,1),(7,2),(11,1),(11,2)]:check(p,k)
print('ANISOTROPIC_CIRCLE_PRIME_POWER_HISTOGRAM_PASS')
