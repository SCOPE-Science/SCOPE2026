import itertools, collections, math
from fractions import Fraction

def outputs(w,b):
 return {w[:i]+w[i+b:] for i in range(len(w)-b+1)}

def uv(q,d):
 r=Fraction(-1,q-1)
 return (1+ (q-1)*r**d)/q, (1-r**d)/q

def formula(q,n,b):
 L=n-b
 p=uv(q,b)[0]
 var=L*p*(1-p)
 for d in range(1,min(b,L)):
  u,v=uv(q,d); u2,v2=uv(q,b-d)
  cov=u*u*u2+(q-1)*v*v*v2-p*p
  cv2=Fraction(q-1,q*q)*Fraction(-1,q-1)**(2*d)*(1-Fraction(-1,q-1)**(b-d))*(1+(q-1)*Fraction(-1,q-1)**(b-d))
  assert cov==cv2,(q,b,d,cov,cv2)
  var+=2*(L-d)*cov
 return 1+L*(1-p),var

checks=0
for q in range(2,5):
 for n in range(2,10):
  if q*(q-1)**(n-1)>250000: continue
  for b in range(1,n):
   hist=collections.Counter()
   for rest in itertools.product(range(1,q),repeat=n-1):
    ww=[0]
    for x in rest:ww.append((ww[-1]+x)%q)
    w=tuple(ww)
    actual=len(outputs(w,b))
    theoretical=1+sum(ww[i]!=ww[i+b] for i in range(n-b))
    assert actual==theoretical,(q,n,b,w,actual,theoretical)
    hist[actual]+=1
   total=sum(hist.values())
   mean=sum(Fraction(a*c,total) for a,c in hist.items())
   var=sum(Fraction(c,total)*(a-mean)**2 for a,c in hist.items())
   em,ev=formula(q,n,b)
   assert (mean,var)==(em,ev),(q,n,b,mean,em,var,ev)
   if b==2:
    for s,count in hist.items():
     L=n-b
     p=Fraction(q-2,q-1)
     theoretical=math.comb(L,s-1)*p**(s-1)*(1-p)**(L-s+1)*total
     assert count==theoretical
   checks+=1
print('VERIFY_OK',checks,'(q,n,b) strata; exact moments and sphere counts; n up to 9')
for b in range(2,7):
 e,v=formula(3,50,b)
 print('q=3 b=',b,'E',e,'V',v)
