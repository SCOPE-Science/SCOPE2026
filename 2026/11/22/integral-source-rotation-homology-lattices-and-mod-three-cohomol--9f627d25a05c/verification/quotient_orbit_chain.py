from itertools import product, combinations
from collections import defaultdict
import math,sys

def rotate(c,k):
    for _ in range(k): c = (c[1],c[2],c[0])
    return c

def rot_sign(c):
    a,b,cc=[len(x)-1 for x in c]
    return (-1)**(a*(b+cc))

def coeff_to_can(cell):
    best=min(rotate(cell,k) for k in range(3))
    s=1;t=cell
    for k in range(3):
        if t==best:return best,s
        s*=rot_sign(t);t=rotate(t,1)
    raise AssertionError

def faces(c):
    offset=0
    for k,A in enumerate(c):
      if len(A)>1:
        for i,_ in enumerate(A):
          yield (c[:k]+(A[:i]+A[i+1:],)+c[k+1:]),(-1)**(offset+i)
      offset+=len(A)-1

def rank_mod_p(cols,p):
    basis={}
    for sparse in cols:
      cur={i:x%p for i,x in sparse.items() if x%p}
      while cur:
        i=min(cur)
        if i not in basis:
          coef=pow(cur[i],-1,p)
          basis[i]={j:(x*coef)%p for j,x in cur.items() if (x*coef)%p}
          break
        v=basis[i]; a=cur[i]
        for j,x in v.items():
          z=(cur.get(j,0)-a*x)%p
          if z:cur[j]=z
          else:cur.pop(j,None)
    return len(basis)

def main(n):
  orbit_cells={}
  # tuple of label->0 unused or 1/2/3 assigned
  for assign in product(range(4),repeat=n):
    if set(assign)>=set((1,2,3)):
      c=tuple(tuple(i for i,z in enumerate(assign) if z==j) for j in (1,2,3))
      can,_=coeff_to_can(c)
      orbit_cells[can]=sum(map(len,can))-3
  groups=defaultdict(list)
  for c,d in orbit_cells.items():groups[d].append(c)
  index={d:{c:i for i,c in enumerate(group)} for d,group in groups.items()}
  ranks={}
  zero_checks={}
  for d in sorted(groups):
    if d==0:continue
    cols=[]
    for c in groups[d]:
      acc=defaultdict(int)
      for f,sg in faces(c):
        t,sg2=coeff_to_can(f)
        acc[index[d-1][t]]+=sg*sg2
      cols.append(dict(acc))
    ranks[d]=rank_mod_p(cols,3)
  betti={d:len(groups[d])-ranks.get(d,0)-ranks.get(d+1,0) for d in groups}
  print('n',n,'cells',dict(sorted((d,len(v)) for d,v in groups.items())),'ranks',ranks,'mod3 Betti',betti,'chi',sum((-1)**d*len(v) for d,v in groups.items()))
  d=n-3
  predicted=(2**n-3-2*(-1)**d)//3
  pred={0:1}
  for j in range(1,d): pred[j]=1
  pred[d]=predicted+(1 if d%2==0 else 0)
  if n>=5:assert betti==pred,(betti,pred)
  else:
    if n==4: assert betti=={0:1,1:5}
    if n==3: assert betti=={0:2}

if __name__=='__main__':
  for n in list(map(int,sys.argv[1:])) or [3,4,5,6,7]:main(n)
