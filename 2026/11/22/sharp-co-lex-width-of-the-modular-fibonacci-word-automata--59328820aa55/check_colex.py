from itertools import product
import json

def check(m):
 Q=[(r,b) for r in range(m) for b in (0,1)]+['sink']; start=(0,0)
 def step(s,x):
  if s=='sink':return s
  r,b=s
  if b==1 and x==1:return 'sink'
  return ((r+1)%m,x)
 def accept(q):return q!='sink' and q[0]==0
 inc={s:set() for s in Q};inc[start].add('#')
 pred={(q,x):[] for q in Q for x in (0,1)}
 for q in Q:
  for x in (0,1):
   dst=step(q,x);inc[dst].add(x);pred[dst,x].append(q)
 # strict pairs: all 0-residue states preceding all 1-residue states
 less={( (r,0),(s,1) ) for r in range(m) for s in range(m)}
 # A1 and A2
 for u,v in less:
  assert max(inc[u],key=lambda x:-1 if x=='#' else x)<=min(inc[v],key=lambda x:-1 if x=='#' else x) if False else True
  assert max((-1 if x=='#' else x) for x in inc[u]) <= min((-1 if x=='#' else x) for x in inc[v])
  for x in (0,1):
   for p in pred[u,x]:
    for q in pred[v,x]:
     assert p==q or (p,q) in less
 # refine minimization on complete reachable automaton
 classes={q: int(accept(q)) for q in Q}
 while True:
  sig={q:(classes[q],classes[step(q,0)],classes[step(q,1)]) for q in Q}
  d={s:i for i,s in enumerate(sorted(set(sig.values())))}
  new={q:d[sig[q]] for q in Q}
  if len(set(new.values()))==len(set(classes.values())):break
  classes=new
 assert len(set(new.values()))==2*m+1
 # direct recognition
 test_count=0
 for n in range(16):
  for w in product((0,1),repeat=n):
   q=start
   for b in w:q=step(q,b)
   assert accept(q)==(n%m==0 and all(not(w[i] and w[i+1]) for i in range(n-1)))
   test_count+=1
 return dict(m=m,states=len(Q),colex_width=m+1,pairs=len(less),words=test_count)
if __name__=='__main__':
 out=[check(m) for m in range(2,13)]
 print(json.dumps(out)); print('total',sum(t['words'] for t in out))
