from itertools import combinations, product, combinations_with_replacement
from collections import defaultdict
from time import monotonic
import json, math, sys

def octgraph():
    # antipodal pairs 0/1,2/3,4/5
    return [(u,v) for u in range(6) for v in range(u+1,6) if u//2!=v//2]
E=octgraph(); nv=6; ne=len(E)
incident=[[j for j,(u,v) in enumerate(E) if v==i or u==i] for i in range(nv)]
refs=[ar[0] for ar in incident]
choices=[ar[1:] for ar in incident]


def make_basis(k):
   basis=[]
   for d in range(k+1):
      bs=[]
      for vs in combinations(range(nv),d):
       for ch in product(*(choices[v] for v in vs)):
        for mon in combinations_with_replacement(range(ne),k-d):
         bs.append((vs,ch,mon))
      basis.append(bs)
   return basis

def differential(basis):
   lookup=[{x:i for i,x in enumerate(bs)} for bs in basis]
   cols=[None]
   for d in range(1,len(basis)):
      out=[]
      for vs,ch,mon in basis[d]:
       column={}
       for i,(v,edge) in enumerate(zip(vs,ch)):
          nvs=vs[:i]+vs[i+1:]; nch=ch[:i]+ch[i+1:]
          for ee,sgn in ((edge,1),(refs[v],-1)):
           newmon=tuple(sorted(mon+(ee,)))
           target=lookup[d-1][(nvs,nch,newmon)]
           column[target]=column.get(target,0)+sgn*(-1 if i&1 else 1)
       out.append({r:a for r,a in column.items() if a})
      cols.append(out)
   return cols

def rank_mod_p(columns,p):
   piv={}; tot=0; nnz_sum=0; greatest=0
   for col in columns:
      x={k:v%p for k,v in col.items() if v%p}
      while x:
         key=max(x)
         if key not in piv:
            v=x[key]; inv=pow(v,-1,p)
            x={r:(a*inv)%p for r,a in x.items() if a%p}
            piv[key]=x; greatest=max(greatest,len(x));break
         b=piv[key]
         factor=x[key]
         for r,a in b.items():
             v=(x.get(r,0)-factor*a)%p
             if v:x[r]=v
             else:x.pop(r,None)
      if len(piv)%300==0 and len(piv)>0 and len(piv)!=tot: pass
   return len(piv),greatest,sum(len(x) for x in piv.values())

def main():
 s=monotonic(); bas=make_basis(3); print('basis',list(map(len,bas)),flush=True)
 col=differential(bas); print('columns',list(map(lambda x:None if x is None else len(x),col)),flush=True)
 print('boundary squared check',flush=True)
 for d in (2,3):
   for one in col[d]:
     boundary=defaultdict(int)
     for mid,c in one.items():
       for row, cc in col[d-1][mid].items():boundary[row]+=c*cc
     if any(boundary.values()):raise RuntimeError('d2 nonzero')
 print('d^2=0',flush=True)
 ranks={}
 for p in [2,3,5,1009]:
   rr=[]
   for d in (1,2,3):
     r=rank_mod_p(col[d],p)
     rr.append(r)
     print('p',p,'d',d,'rank, max, totalnnz',r,flush=True)
   ranks[p]=[x[0] for x in rr]
 print('BETTI', {p:[len(bas[0])-r[0]]+[len(bas[i])-r[i-1]-r[i] for i in (1,2)]+[len(bas[3])-r[2]] for p,r in ranks.items()},flush=True)
if __name__=='__main__': main()
