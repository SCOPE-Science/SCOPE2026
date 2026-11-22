import collections
cells={};byd=collections.defaultdict(list)
for line in open('residual_cells.txt'):
 left,right=line.strip().split('|');x=left.split();i=int(x[1]);d=int(x[2]);fs=[int(z) for z in x[3:]];b=[(int(v.split(':')[0]),int(v.split(':')[1])) for v in right.strip().split()];cells[i]=(d,fs,b);byd[d].append(i)
# edge endpoints via boundary[0] bottom, boundary[1] top
verts=byd[0];edges=byd[1];tri=byd[2];ad=collections.defaultdict(list)
for e in edges:
 (_,_,b)=cells[e];end=[b[1][0],b[0][0]]
 for v in end:ad[v].append((end[1] if v==end[0] else end[0],e))
root=verts[0];seen={root};qu=collections.deque([root]);tree=set()
while qu:
 v=qu.popleft()
 for w,e in ad[v]:
  if w not in seen:seen.add(w);tree.add(e);qu.append(w)
assert len(seen)==len(verts)
gens={e:i+1 for i,e in enumerate(edges) if e not in tree}
def letter(e,sign):return [] if e in tree else [sign*gens[e]]
rels=[]
for t in tri:
 b=cells[t][2]
 assert [sg for e,sg in b]==[1,-1,1]
 rels.append(letter(b[2][0],1)+letter(b[0][0],1)+letter(b[1][0],-1))
def reduce(w):
 s=[]
 for x in w:
  if s and s[-1]==-x:s.pop()
  else:s.append(x)
 while len(s)>1 and s[0]==-s[-1]:s=s[1:-1]
 return s
rels=[reduce(r) for r in rels if r]
removed=set();nst=0
while True:
 units=[r[0] for r in rels if len(r)==1]
 if not units:break
 for x in units:removed.add(abs(x))
 rels=[reduce([x for x in r if abs(x) not in removed]) for r in rels]
 rels=[r for r in rels if r]
 nst+=1
print('residual pi1: vert',len(verts),'edges',len(edges),'tri',len(tri),'tree',len(tree),'gens',len(gens),'unit waves',nst,'killed',len(removed),'left',len(gens)-len(removed),'rels left',len(rels),'sample',rels[:10])

assert len(removed)==len(gens) and not rels
print("MK_FUNDAMENTAL_GROUP_OK")
