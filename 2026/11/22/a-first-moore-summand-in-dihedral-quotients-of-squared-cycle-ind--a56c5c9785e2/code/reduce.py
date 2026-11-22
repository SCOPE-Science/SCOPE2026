import sys,collections,time
from quot import qcomplex,modrank
from collapse import collapse

def reduce(n, verbose=False):
 B,D=qcomplex(n)
 alive,pairs=collapse(B,n)
 counts=[sum(x) for x in alive]
 # columns indexed with original numbers, separate degree
 M=[{}]+[{j:{i:v for i,v in col.items() if alive[d-1][i]} for j,col in enumerate(D[d-1]) if alive[d][j]} for d in range(1,len(B))]
 for d in range(1,len(M)):
  for col in M[d].values():assert all(v in (-1,1) for v in col.values())
 C=[{j for j,a in enumerate(vec) if a} for vec in alive]
 # chain complex test
 for d in range(2,len(M)):
  for j,col in M[d].items():
   v=collections.Counter()
   for i,a in col.items():
    for z,b in M[d-1][i].items():v[z]+=a*b
   assert all(a==0 for a in v.values()),(d,j,v)
 ranks=[]; nonunit=[]; ops=[]
 for d in range(len(M)-1,0,-1):
  matrix=M[d]
  # incremental row mapping
  rows=collections.defaultdict(dict)
  for j,col in matrix.items():
   for i,a in col.items():rows[i][j]=a
  k=0
  while True:
   elig=[(len(cols)*len(matrix[j]),i,j) for i,cols in rows.items() for j,a in cols.items() if abs(a)==1]
   if not elig:break
   _,i,j=min(elig)
   pivot=matrix[j][i]
   # eliminate row i from other cols via col minus multiple*pivot col
   for jj,a in list(rows[i].items()):
    if jj==j:continue
    coef=a//pivot
    v=matrix[jj]
    for ii,b in list(matrix[j].items()):
     old=v.get(ii,0);new=old-coef*b
     if new:
      v[ii]=new;rows[ii][jj]=new
     else:
      v.pop(ii,None);rows[ii].pop(jj,None)
   # delete pivot column; all affected row references
   for ii,b in list(matrix[j].items()):
    rows[ii].pop(j,None)
   del matrix[j]
   assert not rows[i]
   C[d].remove(j);C[d-1].remove(i)
   if d-1>0:
    assert i in M[d-1]
    del M[d-1][i]
   k+=1;ops.append((d,i,j))
  ranks.append(k)
  if matrix:nonunit.append((d,len(matrix),sum(bool(col) for col in matrix.values()),sorted({abs(v) for col in matrix.values() for v in col.values()})[:12]))
  if verbose:print('dim',d,'pivots',k,'nonunit',nonunit[-1:] if nonunit and nonunit[-1][0]==d else None,flush=True)
 assert all(not any(M[d].values()) for d in range(1,len(M))) if not nonunit else True
 bet=[len(c) for c in C]
 return {'n':n,'cells':list(map(len,B)),'collapse_remaining':counts,'collapse_pairs':len(pairs),'unit_pivots':list(reversed(ranks)),'residual':bet,'nonunit':nonunit}
if __name__=='__main__':
 for n in range(int(sys.argv[1]),int(sys.argv[2])+1):
  st=time.time();print(reduce(n),round(time.time()-st,2),flush=True)
