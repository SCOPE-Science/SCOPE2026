from itertools import combinations,product

def model(n,edges,rvec):
 one={}
 for qty in set(rvec):
  opts=[]
  for k in range(min(qty,len(edges))+1):
   for ee in combinations(range(len(edges)),k):
    endpoints=set(sum(([edges[i][0],edges[i][1]] for i in ee),[]))
    if len(endpoints)!=2*k:continue
    for vv in combinations(sorted(set(range(n))-endpoints),qty-k):
     if len(vv)!=qty-k:continue
     opts.append((tuple(vv),tuple(ee)))
  one[qty]=opts
 cells={k:[] for k in range(len(rvec)+1)}
 for c in product(*(one[x] for x in rvec)):
  v=set(sum((list(a) for a,b in c),[]))
  if len(v)!=n:continue
  k=sum(len(b) for a,b in c)
  cells[k].append(c)
 return cells

def homology2(cells, edges, rvec):
 def facets(cell):
  for col,(vs,es) in enumerate(cell):
   for ei in es:
    for v in edges[ei]:
     aa=list(cell);bb=(tuple(sorted(vs+(v,))),tuple(e for e in es if e!=ei));aa[col]=bb
     yield tuple(aa)
 def rank2(vecs):
  piv={}
  for z in vecs:
   while z:
    i=z.bit_length()-1
    if i in piv:z^=piv[i]
    else:piv[i]=z;break
  return len(piv)
 ranks=[0];ks=sorted(cells)
 for k in ks[1:]:
  idx={c:i for i,c in enumerate(cells[k-1])}
  ranks.append(rank2([sum(1<<idx[f] for f in facets(c)) for c in cells[k]]))
 ranks.append(0)
 return {k:len(cells[k])-ranks[k]-ranks[k+1] for k in ks}
if __name__=='__main__':
 for typ,edges in [('C4',[(i,(i+1)%4) for i in range(4)]),('P4',[(i,i+1) for i in range(3)]),('K4',list(combinations(range(4),2)))]:
  for rs in [(2,2,2),(2,2,1),(2,2,2,2)]:
   x=model(4,edges,rs);print(typ,rs,[(k,len(c)) for k,c in x.items()],homology2(x,edges,rs),flush=True)
