import time,collections,sys,random
from try_k33_4 import differential

def cancel_unit(d, max_sec=150,verbose=True):
 cols={j:dict(c) for j,c in enumerate(d) if c}
 rows={}
 for j,c in cols.items():
  for i,v in c.items():rows.setdefault(i,{})[j]=v
 start=time.time();tlast=start
 pivots=0; maxv=1;maxlen=0
 while cols:
  # choose sparsest entry unit with minimal fill score; optimize sampling all cols
  best=None; key=(10**100,10**100)
  for j,c in cols.items():
   sz=len(c)
   if sz>maxlen:maxlen=sz
   for i,v in c.items():
    if abs(v)!=1:continue
    score=(sz-1)*(len(rows[i])-1)
    rank=(score,sz+len(rows[i]))
    if rank<key:
     key=rank;best=(i,j,v)
     if score==0:break
   if key[0]==0:break
  if best is None:break
  r,c,p=best
  # Schur complement
  crow=rows[r].copy(); ccol=cols[c].copy()
  for j,b in crow.items():
   if j==c:continue
   jc=cols[j]
   for i,a in ccol.items():
    if i==r:continue
    z=jc.get(i,0)-a*b*p
    if z:
     jc[i]=z;rows[i][j]=z
     if abs(z)>maxv:maxv=abs(z)
    else:
     jc.pop(i,None);rows[i].pop(j,None)
   jc.pop(r,None)
  for i in ccol:
   if i!=r:rows[i].pop(c,None)
  del rows[r];del cols[c];pivots+=1
  # remove empty columns
  for j in crow:
   if j!=c and j in cols and not cols[j]:del cols[j]
  if verbose and (pivots%100==0 or time.time()-tlast>6):
   print('UNIT',pivots,'cols',len(cols),'rows',len(rows),'nnz',sum(map(len,cols.values())),'maxval',maxv,'maxlen',maxlen,'sec',round(time.time()-start,1),flush=True);tlast=time.time()
  if time.time()-start>max_sec:
   print('STOP time',flush=True);break
  if maxv.bit_length()>1000:
   print('STOP size',flush=True);break
 return pivots,cols,rows

if __name__=='__main__':
 for k in (1,4,3,2):
  t=time.time();print('\nDEG',k,flush=True)
  p,rem,rows=cancel_unit(differential(k),120)
  vals=collections.Counter(abs(x) for c in rem.values() for x in c.values())
  print('DONE',k,'units',p,'remcols',len(rem),'remrows',len(rows),'entries',sum(map(len,rem.values())),'coeffs',vals.most_common(15),'elapsed',round(time.time()-t,2),flush=True)
