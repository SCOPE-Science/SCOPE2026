"""Checks the explicit sharp transient witnesses against the quotient recurrence."""
from class_states import transition

def entry(s,m,n):
  seen={};u=s;t=0
  while u not in seen:
    seen[u]=t;u=transition(u,m,n);t+=1
    if t>8:raise AssertionError('long trajectory')
  return seen[u],t-seen[u]

if __name__=='__main__':
  total=0
  for m in range(3,101):
    for n in range(3,101):
      if m%2 and n%2: s=(0,0,(n-1)//2,1);target=2
      elif m%2 and not n%2: s=((m-1)//2,0,n//2-1,1);target=5
      elif not m%2 and n%2: s=(m//2-1,1,(n-1)//2,0);target=5
      else: s=(0,1,n//2,0);target=4
      got=entry(s,m,n)
      assert got==(target,1),(m,n,s,got,target)
      total+=1
  print('PASS explicit sharp witnesses for',total,'ordered size pairs (3..100 each)')
