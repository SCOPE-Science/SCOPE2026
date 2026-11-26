from itertools import product
from collections import defaultdict
E=[(0,0),(0,1),(1,2),(1,3),(2,0),(2,1),(3,2),(3,3)]

def trees(mask,root,active):
 opts=[]
 for v in active:
  if v==root:continue
  outs=[i for i,(a,b) in enumerate(E) if a==v and b!=a and mask>>i&1]
  if not outs:return []
  opts.append(outs)
 good=[]
 for choice in product(*opts):
  nxt={E[i][0]:E[i][1] for i in choice}; ok=True
  for v in active:
   if v==root:continue
   x=v;visited=set()
   while x!=root and x not in visited:
    visited.add(x); x=nxt.get(x,-1)
   if x!=root:ok=False;break
  if ok:good.append(choice)
 return good

if __name__=='__main__':
 combos=[]
 for mask in range(1,256):
  active={v for i,(v,w) in enumerate(E) if mask>>i&1 for v in (v,w)}
  for t in active:
   if len([i for i in range(8) if mask>>i&1 and E[i][0]==t])>1:continue
   tree=trees(mask,t,active)
   if len(tree)!=1:continue
   for s in active-{t}:
    combos.append((mask,s,t,tree[0]))
 print('masks+start/end matching structural uniqueness before flow',len(combos))
 for k in combos[:20]:print(format(k[0],'08b'),k[1],k[2],k[3])
