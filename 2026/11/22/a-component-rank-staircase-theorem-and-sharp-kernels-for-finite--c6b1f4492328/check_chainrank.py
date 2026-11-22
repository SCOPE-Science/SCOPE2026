from functools import lru_cache

def parts(n,cap=None):
 if n==0: yield ()
 else:
  for k in range(min(n,cap or n),0,-1):
   for rest in parts(n-k,k): yield (k,)+rest

def check(part,t,report=False):
 cls=[]
 for i,n in enumerate(part):cls.extend([i]*n)
 positions=[[] for i in part]
 for v,i in enumerate(cls):positions[i].append(v)
 @lru_cache(None)
 def actual(mask,s):
  if not s:return True
  # one new unrelated component type
  newcs=[i for i,P in enumerate(positions) if not any(mask>>v&1 for v in P)]
  if not any(actual(mask | (1<<v),s-1) for i in newcs for v in positions[i]):return False
  # each occupied component each induced order gap
  for i,P in enumerate(positions):
   marked=[j for j,v in enumerate(P) if mask>>v&1]
   if not marked:continue
   for lo,hi in zip([-1]+marked,marked+[len(P)]):
    if not any(actual(mask|(1<<P[j]),s-1) for j in range(lo+1,hi)):return False
  return True
 def predicted(mask,s):
  if not s:return True
  a=(1<<s)-1
  unused=[]
  for P in positions:
   marked=[j for j,v in enumerate(P) if mask>>v&1]
   if not marked:unused.append(len(P));continue
   for lo,hi in zip([-1]+marked,marked+[len(P)]):
    if hi-lo-1<a:return False
  unused.sort(reverse=True)
  return len(unused)>=s and all(unused[j]>=(1<<(s-j))-1 for j in range(s))
 for mask in range(1<<len(cls)):
  for s in range(t+1):
   if actual(mask,s)!=predicted(mask,s):return (part,mask,s,actual(mask,s),predicted(mask,s))
 return None

def main():
 tested=0
 for n in range(11):
  for p in parts(n):
   z=check(p,4)
   if z:
    print('COUNTEREXAMPLE',z);return
   tested+=2**n
 print('ALL_CHECKS_OK',tested,'marked host configurations (each through 4 thresholds)')
 for t in range(1,5):
  N=(1<<(t+1))-t-2
  types_min=[];types_next=[]
  for p in parts(N):
   if len(p)>=t and all(p[j]>=(1<<(t-j))-1 for j in range(t)):types_min.append(p)
  for p in parts(N+1):
   if len(p)>=t and all(p[j]>=(1<<(t-j))-1 for j in range(t)):types_next.append(p)
  assert len(types_min)==1 and len(types_next)==t+1,(t,types_min,types_next)
  print('EXTREMIZERS_OK',t,N,len(types_min),len(types_next))
if __name__=='__main__':main()
