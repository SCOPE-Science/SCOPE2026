from fractions import Fraction as F
import math

def coeffs(a,b,nmax):
 A=1-F(1)/a; B=(b-1)/(a*b)
 c=[F(0)]*(nmax+1)
 if nmax>=1:c[1]=1/a
 if nmax>=2:c[2]=(a-b)/(a*a*b)
 for n in range(3,nmax+1):c[n]=A*c[n-1]+B*c[n-2]
 return c

checks=0
for a in [F(1,2),F(3,4),F(1),F(11,10),F(3,2),F(2),F(4),F(10),F(50)]:
 beta=4*a/(a+1)**2
 for b in [F(1,10),F(1,2),F(4,5),F(8,9),F(9,10),F(1),F(11,10),F(3,2),F(2),F(3),F(4),beta]:
  if b<=0:continue
  pred=a>=1 and beta<=b<=a
  cs=coeffs(a,b,200)
  if pred:
   assert all(x>=0 for x in cs[1:]),(a,b,[i for i,x in enumerate(cs) if x<0][:4])
  else:
   # Only need finite detection for selected not too close to threshold.
   if abs(float(b-beta))>0.001:
    assert any(x<0 for x in cs[1:]),(a,b,float(beta))
  checks+=1
# near critical negative-index scaling
for a in [2,4,10]:
 ast=4*a/(a+1)**2
 for eps in [1e-3,2e-4,5e-5,1e-5]:
  b=ast-eps; A=1-1/a; B=(b-1)/(a*b)
  q=math.sqrt(-B);theta=math.acos(A/(2*q));u=((a-b)/(a*b*q)-math.cos(theta))/math.sin(theta)
  phi=math.atan(1/u)
  nfirst=math.floor((math.pi-phi)/theta)+2
  cons=2*math.pi*math.sqrt(a)*(a-1)/(a+1)**2
  print('a',a,'eps',eps,'n',nfirst,'scaled',round(nfirst*math.sqrt(eps),3),'const',round(cons,3))
  assert nfirst>2
  checks+=1
print('TWO_DEFECT_EXACT_CHECK_OK',checks)
