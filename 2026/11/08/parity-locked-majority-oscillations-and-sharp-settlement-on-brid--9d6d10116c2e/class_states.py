"""Independent exact quotient-state verification, with combinatorial fibre weights."""
from math import comb

def transition(s,m,n):
 a,x,b,y=s
 def local(a,x,y,k):
  r=k-1
  ones_from_ones=int(2*(x+a-1)>=r)
  ones_from_zeros=int(2*(x+a)>r)
  new_a=a*ones_from_ones+(r-a)*ones_from_zeros
  v=a+y
  new_x=int(2*v>k or (2*v==k and x==1))
  return new_a,new_x
 return *local(a,x,y,m),*local(b,y,x,n)

def inspect(m,n):
    maxT=-1; fixed=set(); periodic_states=set(); tally={}
    for a in range(m):
     for x in range(2):
      for b in range(n):
       for y in range(2):
        s=(a,x,b,y);u=s;seen={};timeline=[]
        while u not in seen:
         seen[u]=len(timeline);timeline.append(u);u=transition(u,m,n)
         if len(timeline)>8:raise RuntimeError('bound')
        t=seen[u];p=len(timeline)-t
        w=comb(m-1,a)*comb(n-1,b)
        maxT=max(maxT,t);tally[(t,p)]=tally.get((t,p),0)+w
        if t==0:
         if p==1:fixed.add(u)
         if p==2:periodic_states.add(u)
        assert p in (1,2),(m,n,s,p)
        if p==2:assert t==0,(m,n,s)
    expected=2*comb(m-1,m//2)*comb(n-1,n//2) if not(m%2 or n%2) else 0
    assert len(fixed)==4
    assert sum(v for (t,p),v in tally.items() if p==2)==expected
    assert maxT==(2 if m%2 and n%2 else 4 if not(m%2 or n%2) else 5),(m,n,maxT)
    assert sum(tally.values())==2**(m+n)
    return expected,maxT

if __name__=='__main__':
    tested=0
    for m in range(3,51):
     for n in range(3,51):
      expected,mt=inspect(m,n)
      tested+=1
    print('PASS quotient sizes 3..50 by 3..50; pairs',tested)
    for m,n in [(3,3),(3,4),(4,4),(4,6),(5,8),(6,6),(8,9),(10,10)]:
      print(f'{m},{n}: period2_states={inspect(m,n)[0]} max_entry={inspect(m,n)[1]}')
