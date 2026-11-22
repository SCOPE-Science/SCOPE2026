#!/usr/bin/env python3
"""Exact finite-group Fourier rank verification; standard library plus SymPy."""
import itertools
import sympy as sp

# Coefficients are indexed by r^0,r^1,r^2,s r^0,s r^1,s r^2.
W={
 (1,0):{6:[-2,0,0,0,0,0]},
 (2,0):{4:[-2,2,0,0,0,0],6:[-2,-2,0,0,0,0]},
 (1,1):{3:[-2,0,0,-2,0,0],6:[-2,0,0,-1,0,0]},
 (3,0):{2:[-2,-2,-2,0,0,0],4:[-2,1,1,0,0,0],6:[-2,-2,-1,0,0,0]},
 (2,1):{4:[-2,-2,0,-2,0,0],5:[-2,1,0,-1,0,0],6:[-2,-2,0,-1,0,0]},
 (3,1):{3:[-2,-2,1,-3,0,0],4:[-2,-2,-1,-1,0,0],5:[-2,-2,2,-2,0,0],6:[-2,-2,-2,-2,0,0]},
 (2,2):{2:[-2,2,0,-2,2,0],3:[-2,-2,0,-2,-2,0],4:[-2,-1,0,-1,1,0],5:[1,1,0,3,-1,0],6:[-2,-2,0,-2,-1,0]},
 (3,2):{2:[3,5,-8,7,-7,0],3:[1,1,2,2+sp.I,2-sp.I,0],4:[-2,-2,-1,-1,-1,0],5:[-2,-2,1,-2,-1,0],6:[-2,-2,-2,-2,-2,0]},
 (3,3):{1:[-2,-2,-2,-2,-2,-2],2:[-2,-2,-2,-1,-1,-1],3:[-2,-2,-1,-2,-2,-1],4:[-2,-2,-1,-2,-1,-1],5:[-2,-2,1,-1,-1,-1],6:[-2,-2,-2,-2,-2,-1]},
}
G=list(itertools.product((0,1),range(3)))
def mul(g,h):
    e,j=g; d,k=h
    return ((e+d)%2, ((-1)**d*j+k)%3)
def inv(g):
    e,j=g
    return (e, -j%3 if not e else j)
def rank_regular(v):
    f=dict(zip(G,v))
    m=sp.Matrix([[f[mul(g,inv(h))] for h in G] for g in G])
    return m.rank()
def quad(v):
    return sum(t*t for t in v)-sum(v[i]*v[j] for i in range(3) for j in range(i+1,3))
def rank_fourier(v):
    a,b=v[:3],v[3:]
    std=0 if a[0]==a[1]==a[2] and b[0]==b[1]==b[2] else (1 if sp.simplify(quad(a)-quad(b))==0 else 2)
    p=sum(a);q=sum(b)
    return int(sp.simplify(p+q)!=0)+int(sp.simplify(p-q)!=0)+2*std
count=0
for shape,table in W.items():
    nr,ns=shape
    for rank,v in table.items():
        assert sum(x!=0 for x in v[:3])==nr and sum(x!=0 for x in v[3:])==ns,(shape,rank,'shape')
        assert rank_regular(v)==rank_fourier(v)==rank,(shape,rank,v,rank_regular(v),rank_fourier(v))
        count+=1
print('EXACT_OK witnesses=%d shape_classes=%d' %(count,len(W)))
print('rank_sets='+str({str(k):sorted(v.keys()) for k,v in W.items()}))
# Check every 0/1-supported pattern with 2..5 weighted nonzero options for comparison (no proof of exclusions).
for k in range(1,7):
 for supp in itertools.combinations(range(6),k):
  if k>4:continue
  for weights in itertools.product((1,-1,2),repeat=k):
   v=[0]*6
   for j,x in zip(supp,weights):v[j]=x
   assert rank_regular(v)==rank_fourier(v),(supp,weights)
print('EXACT_OK crosschecks of regular and Fourier ranks for all 1-to-4 support patterns / ternary weights')
