"""Finite stress-test for unequal-width multiband phase classification."""
import random, math
R=random.Random(17421)
checks=0

def criterion(widths,x):
 n=len(widths)
 if any(w<=0 for w in widths) or not all(x>(widths[i]+widths[i+1])/2 for i in range(n-1)):return False
 if any(w>1 for w in widths):return False
 ds=[max((widths[i]+widths[i+r])/2 for i in range(n-r)) for r in range(1,n)]
 u=x-math.floor(x)
 return all(ds[r-1]-1e-11<=r*u<=1-ds[r-1]+1e-11 for r in range(1,n))

def brute(widths,x):
 n=len(widths)
 if any(w>1 for w in widths):return False
 if not all(x>(widths[i]+widths[i+1])/2 for i in range(n-1)):return False
 sgn=[]
 for r in range(1,n):
  si=[]
  for i in range(n-r):
   d=(widths[i]+widths[i+r])/2
   a=r*x-d;b=r*x+d
   # If a zero inside the open interval, no consistent sign.
   if math.floor(a+1e-11)!=math.floor(b-1e-11):return False
   t=(a+b)/2
   si.append(1 if math.sin(math.pi*t)>0 else -1)
  if len(set(si))>1:return False
  sgn.append(si[0])
 return all(sgn[r-1]==sgn[0]**r for r in range(1,n))

for N in range(2,11):
 for _ in range(600):
  ws=[R.uniform(.001,1.35) for _ in range(N)]
  x=R.uniform(.001,6.7)
  if abs(x-round(x))<.002:continue
  if any(abs(r*x - round(r*x))<max((ws[i]+ws[i+r])/2 for i in range(N-r))+.001 and abs(r*x - round(r*x))>max((ws[i]+ws[i+r])/2 for i in range(N-r))-.001 for r in range(1,N)):continue
  a=criterion(ws,x);b=brute(ws,x)
  assert a==b,(N,ws,x,a,b)
  checks+=1
for N in range(2,11):
 for _ in range(100):
  ws=[R.uniform(.001,.2/N) for i in range(N)]
  ds=[max((ws[i]+ws[i+r])/2 for i in range(N-r)) for r in range(1,N)]
  low=max(ds[r-1]/r for r in range(1,N))
  high=min((1-ds[r-1])/r for r in range(1,N))
  if low<=high:
   u=R.uniform(low,high)
   assert brute(ws,4+u) and criterion(ws,4+u)
   checks+=1
print('UNEQUAL_MULTIBAND_SIGN_CHECKS_PASS',checks)
