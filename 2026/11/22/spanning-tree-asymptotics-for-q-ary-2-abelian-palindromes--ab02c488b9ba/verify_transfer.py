from collections import defaultdict
from math import pi,sqrt

def count(q,L):
 es=[(i,j) for i in range(1,q) for j in range(i+1,q)]
 index={e:k for k,e in enumerate(es)};D=len(es)
 total=0
 for start in range(q):
  st={(start,(0,)*D):1}
  for step in range(L):
   nxt=defaultdict(int)
   for (last,current),cnt in st.items():
    for new in range(q):
     if new!=last and new and last:
      a,b=sorted((last,new));ii=index[(a,b)]
      nxtcurr=list(current);nxtcurr[ii]+=1 if last<new else -1
      nc=tuple(nxtcurr)
     else:nc=current
     nxt[(new,nc)]+=cnt
   st=nxt
  total+=st.get((start,(0,)*D),0)
 return total
for q,N in [(3,22),(4,20)]:
 d=(q-1)*(q-2)//2
 constant=q**(d+(q-2)/2-1)/(2*sqrt(pi))**d
 for n in ([3,4,5,8,10,15,20,22] if q==3 else [4,6,8,10,12,14,16,18,20]):
  if n>N:continue
  a=count(q,n-1)
  frac=a/q**n
  scaled=frac*(n-1)**(d/2)
  print('q',q,'n',n,'count',a,'scaled',round(scaled,7),'limit',round(constant,7),'ratio',round(scaled/constant,7),flush=True)
