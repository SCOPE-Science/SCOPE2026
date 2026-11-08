"""Direct independent enumeration of matrix Jordan product fibers over prime fields."""
import itertools
from collections import Counter

def mm(A,B,q):
  a,b,c,d=A; e,f,g,h=B
  return ((a*e+b*g)%q,(a*f+b*h)%q,(c*e+d*g)%q,(c*f+d*h)%q)
def anti(A,B,q):
  x,y=mm(A,B,q),mm(B,A,q)
  return tuple((u+v)%q for u,v in zip(x,y))
def predict(C,q):
  a,b,c,d=C
  I=(1,0,0,1)
  scalar=b==0 and c==0 and a==d
  e=z=0
  for x in range(q):
    for y in range(q):
      if not x and not y:continue
      # canonical lines
      if x and x!=1:continue
      if not x and y!=1:continue
      xx=(a*x+b*y)%q; yy=(c*x+d*y)%q
      if (xx*y-yy*x)%q==0:
        e+=1
        if xx==0 and yy==0:z+=1
  U=(q-1)*q*(q*q-q-1)
  H=q**3-1 if scalar else q-1
  return U+q*(q-1)*(q+1-e+q*z)+q*q*H+(q**4 if C==(0,0,0,0) else 0)
def run(q):
  mats=list(itertools.product(range(q),repeat=4))
  freq=Counter()
  for A in mats:
    for B in mats:
      freq[anti(A,B,q)]+=1
  assert sum(freq.values())==q**8
  for C in mats:
    exp=predict(C,q)
    assert freq[C]==exp,(q,C,freq[C],exp)
  print('q',q,'targets',q**4,'ordered_pairs',q**8,'Nzero',freq[(0,0,0,0)],'distinct_fibers',sorted(set(freq.values())), 'TOTAL_OK')
if __name__=='__main__':
  for q in (3,5):run(q)
  print('ALL_DIRECT_CHECKS_PASS')
