"""Independent direct greedy stress checks (finite corroboration, not the proof)."""
from itertools import combinations

def predicted(h,N):
 k=(h-5)//6;m=5*h-1
 C={1,2}
 for j in range(k+1):C.update((h+6*j,h+6*j+1,h+6*j+2))
 C.update((2*h+1,2*h+6))
 B={6*h+6*j-1 for j in range(1,k+2)}|{6*h+6*j for j in range(k+1)}|{6*h+6*j+1 for j in range(-1,k)}
 mask=bytearray(N+1)
 for x in C:
  if x<=N:mask[x]=1
 for shift in range(0,N+1,m):
  for b in B:
   if b+shift<=N:mask[b+shift]=1
 return mask,C,B

def independent_greedy(h,N):
 S=bytearray(N+1);one=pair=triple=0
 for x in (1,2,h):
  S[x]=1;triple|=pair<<x;pair|=one<<x;one|=1<<x
 for x in range(h+1,N+1):
  if not (triple>>x)&1:
   S[x]=1;triple|=pair<<x;pair|=one<<x;one|=1<<x
 return S

def run():
 cnt=0
 for k in range(2,401):
  h=6*k+5;N=12*h
  got=independent_greedy(h,N);want,C,B=predicted(h,N)
  assert got==want,(k, next(i for i in range(N+1) if got[i]!=want[i]))
  cnt+=1
 print('DIRECT_GREEDY_MATCH',cnt,'families; k=2..400; all integers through 12h')
 for k in (2,3,5,11,23,75,250,400):
  h=6*k+5;N=100*h
  got=independent_greedy(h,N);want,_,_=predicted(h,N)
  assert got==want,(k,next(i for i in range(N+1) if got[i]!=want[i]))
 print('LONG_RANGE_MATCH',8,'families; all integers through 100h')
 for k in range(2,13):
  h=6*k+5;E=11*h+3
  want,C,B=predicted(h,E)
  S=[x for x in range(1,E+1) if want[x]]
  tri={sum(t) for t in combinations(S,3) if sum(t)<=E}
  for n in range(h+1,E+1):
   assert (n in tri)==(want[n]==0),(k,n)
 print('INDEPENDENT_TRIPLE_ENUMERATION',11,'families; full base intervals')
 print('GREEDY_VERIFY_OK finite_checks_not_infinite_proof=True')
if __name__=='__main__':run()
