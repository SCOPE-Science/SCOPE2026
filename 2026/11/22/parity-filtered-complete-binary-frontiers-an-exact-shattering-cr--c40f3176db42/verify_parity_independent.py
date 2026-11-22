from functools import lru_cache
def cuts(h,K):
 def f(d,v):
  if d==0:return {1:[1<<v]}
  a=f(d-1,2*v);b=f(d-1,2*v+1)
  out={1:[1<<v]}
  for i,aa in a.items():
   for j,bb in b.items():
    if i+j<=K:out.setdefault(i+j,[]).extend(x|y for x in aa for y in bb)
  return out
 return f(h,1)

def shat_sets(cs,h):
 n=(1<<(h+1));m=len(cs)
 col=[sum((1<<j) for j,c in enumerate(cs) if c&(1<<i)) for i in range(1,n)]
 full=(1<<m)-1
 q=[(0,(full,),0)]; out={0}
 while q:
  new=[]
  for mask,buckets,last in q:
   for v in range(last+1,n):
    pos=col[v-1];newb=[]
    for b in buckets:
     x=b&pos;y=b&~pos
     if not x or not y:break
     newb.extend((x,y))
    else:
     M=mask|(1<<v);new.append((M,tuple(newb),v));out.add(M)
  q=new
  print('layer',len(q),flush=True)
 return out

def antichains(v,h):
 if h==0:return [0,1<<v]
 a=antichains(2*v,h-1);b=antichains(2*v+1,h-1)
 return [1<<v]+[x|y for x in a for y in b]

def criterion(S,h,p):
 nodes=[v for v in range(1,1<<(h+1)) if S>>v&1]
 for i,u in enumerate(nodes):
  for v in nodes[:i]:
   x=u;y=v
   if (x.bit_length()>=y.bit_length() and (x>>(x.bit_length()-y.bit_length()))==y) or (y.bit_length()>=x.bit_length() and (y>>(y.bit_length()-x.bit_length()))==x):return False
 # sibling leaves
 if any(((S>>v)&3)==3 for v in range(1<<h,(1<<(h+1)),2)):return False
 for w in range(1<<(h-1),1<<h):
  if not any((w==s or ((s> w) and (s//2==w)) or (w>s and (w//(2**(w.bit_length()-s.bit_length()))==s))) for s in nodes):
   return True
 # no free bottom parents
 return bool(nodes) and all(v<(1<<(h-1)) for v in nodes) and len(nodes)%2==p
for h in range(2,5):
 allc=cuts(h,2**h)
 for p in (0,1):
  cs=[v for k,vs in allc.items() if k%2==p for v in vs]
  q=shat_sets(cs,h)
  ant=antichains(1,h)
  predicted={S for S in ant if criterion(S,h,p)}|{0}
  print('h,p',h,p,'actual',len(q),'predicted',len(predicted),'miss',len(predicted-q),'extra',len(q-predicted))
  assert q==predicted
print('PY_PASS')
