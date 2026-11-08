from itertools import product
from collections import Counter

def field(q):
 # prime q=2,3; alpha^2=alpha+1 q2, alpha^2=-1 q3
 def mul(x,y):
  a,b=x%q,x//q;c,d=y%q,y//q
  if q==2:return ((a*c+b*d)%q)+q*((a*d+b*c+b*d)%q)
  return ((a*c-b*d)%q)+q*((a*d+b*c)%q)
 def bar(x):return mul(x,x) if q==2 else (x%q+q*(-(x//q)%q))
 return mul,bar

def enum(q):
 mul,bar=field(q)
 add=lambda x,y:(x%q+y%q)%q+q*((x//q+y//q)%q)
 sub=lambda x,y:(x%q-y%q)%q+q*((x//q-y//q)%q)
 ff=q*q
 def det2(a,b,c,d):return sub(mul(a,d),mul(b,c))
 def rank(a):
  if all(v==0 for row in a for v in row):return 0
  for i,j in [(0,1),(0,2),(1,2)]:
   for u,v in [(0,1),(0,2),(1,2)]:
    if det2(a[i][u],a[i][v],a[j][u],a[j][v]):
     break
   else:continue
   break
  else:return 1
  # determinant
  t1=mul(a[0][0], det2(a[1][1],a[1][2],a[2][1],a[2][2]))
  t2=mul(a[0][1], det2(a[1][0],a[1][2],a[2][0],a[2][2]))
  t3=mul(a[0][2], det2(a[1][0],a[1][1],a[2][0],a[2][1]))
  return 3 if add(sub(t1,t2),t3) else 2
 counters={s:[[0]*q for r in range(4)] for s in range(4)}
 for (a,b,c) in product(range(q),repeat=3):
  for (x,y,z) in product(range(ff),repeat=3):
   M=[[a,x,y],[bar(x),b,z],[bar(y),bar(z),c]]
   r=rank(M)
   for s in range(4):counters[s][r][(a+b+c if s==3 else sum([a,b,c][:s]))%q]+=1
 L=q**4+q**2+1
 for s in range(4):
  z=1 if s==0 else q**(2*s-1)+(-1)**s*(q-1)*q**(s-1)
  I=(q**(2*(3-s))*z-1)//(q*q-1)
  J={0:L,1:1,2:q+1,3:0}[s]
  P1=q*I-L;P2=q**4*J-L-(q*q+1)*P1;P3=(q**9 if s==0 else 0)-1-P1-P2
  expected=[1,P1,P2,P3]
  got=[arr[0]-arr[1] if q==3 else arr[0]-arr[1] for arr in counters[s]]
  print('q',q,'frequency rank',s,'expected',expected,'got',got,'RAW',counters[s])
  assert got==expected

if __name__=='__main__':
 enum(2)
 enum(3)
 print('HERMITIAN_3_RANK_FOURIER_PASS')
 from math import log
 for q in [2,3,4,5,7,11]:
  f=lambda t:q**3*3**t-q*(q*q-q+1)*2**t-q*q+q-1
  lo,hi=0.,1.
  for _ in range(100):
   mid=(lo+hi)/2
   if f(mid)>0:hi=mid
   else:lo=mid
  beta=(lo+hi)/2
  assert 0<beta<1 and f(beta-1e-6)<0<f(beta+1e-6)
  s1=(-q**4+q**3-q**2+q-1,q*(q-1)*(q*q+1)**2,-q**3*(q-1)*(q*q+1))
  s2=((q-1)*(q*q+1),q*(q**3-2*q*q+q-1),-q**3*(q-1))
  for s in [s1,s2]:
   for t in [0,beta,1,2]:assert s[0]+s[1]*2**t+s[2]*3**t<0
  lost=q**3*(q-1)**2*(q*q+1)*(q*q+q+1)
  assert 0<lost<q**9
  print(f'order {q}: beta={beta:.12f}, endpoint dimension={q**9-1-lost}')
 print('HERMITIAN_THREE_NEGATIVE_TYPE_PASS')
