from itertools import combinations
from collections import Counter

def faces_from_facets(facets):
    result=set()
    for f in facets:
        for k in range(len(f)+1):
            for c in combinations(f,k):result.add(frozenset(c))
    return result

def double2(facets):
    face=faces_from_facets(facets)
    ed=sorted([tuple(sorted(x)) for x in face if len(x)==2]);
    simplices=[[]]
    for k in range(1,4):
        cur=[]
        for inds in combinations(range(len(ed)),k):
            u=[v for i in inds for v in ed[i]]
            if len(set(u))==len(u) and frozenset(u) in face: cur.append(inds)
        simplices.append(cur)
    return ed,simplices



from collections import defaultdict,Counter,deque
stack=[tuple(set(range(7))-{i}) for i in range(6)]+[tuple((set(range(6))-{i})|{7}) for i in range(6)]
E,cs=double2(stack)
assert len(E)==27 and list(map(len,cs[1:]))==[27,165,180]
V=len(E); edges=cs[2];tris=cs[3]
# spanning tree BFS
adj=[[] for _ in range(V)];edge_id={e:i for i,e in enumerate(edges)}
for a,b in edges:adj[a].append(b);adj[b].append(a)
seen={0};todo=deque([0]);tree=set()
while todo:
 a=todo.popleft()
 for b in sorted(adj[a]):
  if b not in seen:
   seen.add(b);todo.append(b);tree.add(tuple(sorted((a,b))))
assert len(seen)==V
non=[e for e in edges if e not in tree];gen={e:i+1 for i,e in enumerate(non)}
def word_edge(a,b):
 e=tuple(sorted((a,b)));return [] if e in tree else [gen[e] if a<b else -gen[e]]
rel=[]
for a,b,c in tris:
 rel.append(word_edge(a,b)+word_edge(b,c)+word_edge(c,a))
def reduce(w):
 stack=[]
 for x in w:
  if stack and stack[-1]==-x:stack.pop()
  else:stack.append(x)
 # cyclic reduce too
 while len(stack)>1 and stack[0]==-stack[-1]:stack=stack[1:-1]
 return stack
rel=[reduce(w) for w in rel]
# greedy search for eliminable generator with smallest replacement, least total operations
sublog=[];active=set(gen.values());step=0
while True:
 cmap=Counter(x for w in rel for x in map(abs,w))
 choices=[]
 for i,w in enumerate(rel):
  cnt=Counter(map(abs,w))
  for g,num in cnt.items():
   if num!=1:continue
   choices.append((len(w)*(cmap[g]+1),len(w),cmap[g],i,g))
 if not choices:break
 _,_,_,i,g=min(choices)
 w=rel[i];j=next(j for j,x in enumerate(w) if abs(x)==g)
 rot=w[j:]+w[:j]; sign=rot[0]//g
 rest=rot[1:]
 if sign==1:repl=[-x for x in reversed(rest)]
 else:repl=rest
 rel.pop(i)
 new=[]
 for w in rel:
  if g not in set(map(abs,w)):new.append(w);continue
  tmp=[]
  for x in w:
   if abs(x)!=g:tmp.append(x)
   elif x>0:tmp.extend(repl)
   else:tmp.extend([-z for z in reversed(repl)])
  new.append(reduce(tmp))
 rel=new
 active.remove(g);step+=1;sublog.append((g,i,len(w),len(repl)))
 if step%20==0:print('step',step,'remain rel',len(rel),'active',len(active),'maxlen',max(map(len,rel)),flush=True)
 if sum(map(len,rel))>200000:break
print('final',step,'active',len(active),'rel_count',len(rel),'nonempty',sum(bool(x) for x in rel),'maxlen',max(map(len,rel)),flush=True)
assert step==134 and len(active)==5 and len(rel)==46
assert sorted(active)==[48,88,91,95,98]
assert sum(bool(x) for x in rel)==20
for w in rel:
 assert all(sum((1 if x>0 else -1) for x in w if abs(x)==g)==0 for g in active)
print('presentation and abelianizations verified')
print('retained words:')
for w in rel:
 if w:print(w)
