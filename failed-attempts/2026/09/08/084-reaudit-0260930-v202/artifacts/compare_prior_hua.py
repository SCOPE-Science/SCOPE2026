"""Exact small-dimension coefficient extraction from Hua's partition formula."""
from collections import Counter
from fractions import Fraction as F
from math import gcd
import json
def partitions(n,limit=None):
 if not n:yield ();return
 for k in range(min(n,limit or n),1-1,-1):
  for p in partitions(n-k,k):yield (k,)+p
def pair(l,m):return sum(min(a,b) for a in l for b in m)
def b(l,q):
 r=F(1)
 for count in Counter(l).values():
  for j in range(1,count+1):r*=1-F(1,q**j)
 return r
def mul(x,y,A,B):
 out={}
 for (i,j),c in x.items():
  for (k,l),d in y.items():
   if i+k<=A and j+l<=B:out[i+k,j+l]=out.get((i+k,j+l),F(0))+c*d
 return out
def logcoef(A,B,q):
 p={}
 for a in range(A+1):
  for bb in range(B+1):
   if not a+bb:continue
   p[a,bb]=sum((F(q)**(3*pair(l,m)-pair(l,l)-pair(m,m))/(b(l,q)*b(m,q)) for l in partitions(a) for m in partitions(bb)),F(0))
 power={(0,0):F(1)};answer=F(0)
 for k in range(1,A+B+1):
  power=mul(power,p,A,B);answer+=F((-1)**(k+1),k)*power.get((A,B),0)
 return answer
def kac(a,b,q):
 d=gcd(a,b);answer=logcoef(a,b,q)
 if d==2:answer-=logcoef(a//2,b//2,q*q)/2
 assert d in (1,2)
 return (q-1)*answer
out={'source':'Hua partition formula as stated in HLRV, arXiv:1204.2375, equation (1.1)','values':{str((a,b)):str(kac(a,b,2)) for a,b in [(2,2),(2,3)]},'ordinary_log_terms':{'(2,2);q=2':str(logcoef(2,2,2)),'(1,1);q=4':str(logcoef(1,1,4)),'(2,3);q=2':str(logcoef(2,3,2))}}
assert out['values']=={'(2, 2)':'91','(2, 3)':'204'}
print(json.dumps(out,indent=2))
print('HUA_COMPARISON_OK')
