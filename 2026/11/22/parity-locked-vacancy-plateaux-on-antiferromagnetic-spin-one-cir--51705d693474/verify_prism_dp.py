from collections import defaultdict
from fractions import Fraction
S=[(x,y) for x in (-1,0,1) for y in (-1,0,1)]
N=9;K=[(a!=0)+(b!=0) for a,b in S]
H=[[a*c+b*d for c,d in S] for a,b in S]
def exact_dp(n,r,d):
  V=[r*a*b+d*(a*a+b*b) for a,b in S]
  energy=None;count=0;by_K={}
  for first in range(N):
    states={(first,K[first]):(V[first],1)}
    for _ in range(1,n):
      new={}
      for (prev,k),(e,c) in states.items():
        for nxt in range(N):
          key=(nxt,k+K[nxt]);val=e+H[prev][nxt]+V[nxt]
          if key not in new or val<new[key][0]:new[key]=(val,c)
          elif val==new[key][0]:new[key]=(val,new[key][1]+c)
      states=new
    for (last,k),(e,c) in states.items():
      val=e+H[last][first]
      if k not in by_K or val<by_K[k][0]:by_K[k]=(val,c)
      elif val==by_K[k][0]:by_K[k]=(val,by_K[k][1]+c)
  energy=min(e for e,c in by_K.values())
  return energy, {k:c for k,(e,c) in by_K.items() if e==energy}

def predicted(n,r,d):
  if n%2==0:
    vals=[(2*n*d-(2+r)*n,{2*n:2}),(Fraction(0),{0:1})]
    # lower energy branch may tie
  else:
    vals=[(2*n*d-(2+r)*n+4,{2*n:2*n}),((2*n-2)*d-(2+r)*n+4+r,{2*n-2:2*n}),(Fraction(0),{0:1})]
  low=min(v for v,_ in vals)
  counts={}
  for val,ks in vals:
    if val==low:counts.update(ks)
  return low,counts

if __name__=='__main__':
  test=0
  for n in range(3,13):
    for r in [Fraction(1,5),Fraction(2,3),Fraction(1),Fraction(3),Fraction(9)]:
      lo=r/2; hi=r/2+Fraction(n-2,n-1) if n%2 else 1+r/2
      choices=[lo-Fraction(1,3),lo,lo+Fraction(1,9),hi-Fraction(1,9),hi,hi+Fraction(1,5)]
      for d in choices:
        actual=exact_dp(n,r,d);expected=predicted(n,r,d)
        assert actual==expected,(n,r,d,actual,expected)
        test+=1
  print('PASS exact DP crosscheck',test,'parameterized instances n=3..12')
