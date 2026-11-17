from itertools import combinations
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
import sys,time

def mat(n):
 W=list(combinations(range(1,n),3)); D=list(combinations(range(n),3)); ws={x:i for i,x in enumerate(W)}; ds={x:len(W)+i for i,x in enumerate(D)}
 C=list(combinations(range(n),4)); A=s.zeros(len(W)+len(D),2*len(C))
 for j,(a,b,c,d) in enumerate(C):
  if a==0:
   A[ws[(b,c,d)],2*j]+=1
   A[ws[(b,c,d)],2*j+1]+=1
  else:
   for f,coef in [((b,c,d),1),((a,c,d),-1),((a,b,d),1),((a,b,c),-1)]:
    A[ws[f],2*j]+=coef
    A[ws[f],2*j+1]+=coef
  A[ds[(b,c,d)],2*j]+=1
  A[ds[(a,b,d)],2*j]+=1
  A[ds[(a,c,d)],2*j+1]-=1
  A[ds[(a,b,c)],2*j+1]-=1
 return A

# Fix W part: for a>0, the 4-boundary has W_bcd-W_acd+W_abd-W_abc. For a=0, W_bcd only.
for n in [5,6,7,8]:
 A=mat(n)
 t=time.time(); print('n',n,'matrix',A.shape,'started',flush=True)
 B=smith_normal_form(A,domain=ZZ)
 diag=[abs(B[i,i]) for i in range(min(A.shape)) if B[i,i]]
 nonunits=[int(x) for x in diag if x!=1]
 print('n',n,'rank',len(diag),'nonunits',nonunits, 'H2free',A.rows-len(diag),flush=True)
 if n>=7:
  assert nonunits==[3]*(n-2)+[6], (n,nonunits)
  assert A.rows==len(diag)
 else:
  assert (n,A.rows-len(diag),nonunits) in [(5,5,[]),(6,5,[3])]
print('PASS: integral boundary presentation and Wilson-predicted invariant factors in tested cases')
