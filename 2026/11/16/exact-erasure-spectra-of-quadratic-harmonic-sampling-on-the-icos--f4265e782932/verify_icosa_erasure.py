"""Standalone numerical cross-check of a quadratic icosahedral sampling theorem.
The mathematical proof, not this finite checker, establishes the stated classification.
Run: python3 verify_icosa_erasure.py
"""
from itertools import combinations, product
from math import sqrt
from collections import Counter

PHI=(1+sqrt(5))/2
D=sqrt(1+PHI**2)
V=[]
for s,t in product((-1,1),repeat=2):
    V.extend(((0,s/D,t*PHI/D),(s/D,t*PHI/D,0),(t*PHI/D,0,s/D)))
assert len(V)==12

def dot(u,v): return sum(a*b for a,b in zip(u,v))
def close(x,y,tol=3e-12): assert abs(x-y)<tol,(x,y)
def feat(v):
    x,y,z=v
    return (1.,sqrt(3)*x,sqrt(3)*y,sqrt(3)*z,
            sqrt(15)/2*(x*x-y*y),sqrt(5)/2*(3*z*z-1),
            sqrt(15)*x*y,sqrt(15)*y*z,sqrt(15)*z*x)
F=[tuple(x/sqrt(12) for x in feat(v)) for v in V]
assert all(len(row)==9 for row in F)
nchecks=0
for i in range(9):
  for j in range(9):
    close(sum(row[i]*row[j] for row in F),float(i==j))
    nchecks+=1
for i in range(12):
 for j in range(12):
    t=dot(V[i],V[j])
    kernel=(1+3*t+5*(3*t*t-1)/2)/12
    close(dot(F[i],F[j]),kernel)
    if i==j: close(kernel,.75)
    elif t<-.99: close(kernel,.25)
    else: close(abs(kernel),1/(4*sqrt(5)))
    nchecks+=3

def det(A):
 if len(A)==1:return A[0][0]
 if len(A)==2:return A[0][0]*A[1][1]-A[0][1]*A[1][0]
 if len(A)==3:
  a,b,c=A[0];d,e,f=A[1];g,h,i=A[2]
  return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)
 raise AssertionError('only small matrices')

def check_eigs(A,vals):
 # Compare all characteristic polynomial coefficients via principal minors.
 n=len(A)
 close(sum(A[i][i] for i in range(n)),sum(vals))
 for k in range(2,n+1):
  lhs=sum(det([[A[i][j] for j in I] for i in I]) for I in combinations(range(n),k))
  rhs=sum(__import__('math').prod(x) for x in combinations(vals,k))
  close(lhs,rhs)
 return n

a=1/(4*sqrt(5))
ct=Counter()
for r in range(4):
 for E in combinations(range(12),r):
  A=[[dot(F[i],F[j]) for j in E] for i in E]
  has_pair=any(dot(V[i],V[j])<-.99 for i,j in combinations(E,2))
  if r==0:
    ct['zero']+=1
  if r==1:
    check_eigs(A,[.75]);ct['one_good']+=1
  if r==2:
    eig=[1,.5] if has_pair else [.75+a,.75-a]
    check_eigs(A,eig)
    ct['two_bad' if has_pair else 'two_good']+=1
  if r==3:
    if has_pair:
      vals=[1,5/8+sqrt(65)/40,5/8-sqrt(65)/40]
      ct['three_bad']+=1
    else:
      P=__import__('math').prod(dot(V[i],V[j]) for i,j in combinations(E,2))
      if P>0:
        vals=[.75+2*a,.75-a,.75-a]
        ct['three_balanced']+=1
      else:
        vals=[.75-2*a,.75+a,.75+a]
        ct['three_unbalanced']+=1
    check_eigs(A,vals)
    assert (max(vals)<1)==(not has_pair)
  nchecks+=r
assert ct==Counter({'zero':1,'one_good':12,'two_good':60,'two_bad':6,
                   'three_bad':60,'three_balanced':80,'three_unbalanced':80}),ct
assert sum(ct[k] for k in ('zero','one_good','two_good','three_balanced','three_unbalanced'))==233
# The signed Seidel matrix of the six antipodal axes has balanced triangles.
axes=[]
for i,v in enumerate(V):
 if all(dot(v,u)>-.99 for u in axes):axes.append(v)
assert len(axes)==6
seidel=[[0 if i==j else (1 if dot(axes[i],axes[j])>0 else -1) for j in range(6)] for i in range(6)]
triangles=Counter('+' if seidel[i][j]*seidel[j][k]*seidel[k][i]>0 else '-' for i,j,k in combinations(range(6),3))
assert triangles==Counter({'+':10,'-':10}),triangles
print('PASS: independently reconstructed quadratic harmonic frame, kernel, spectral certificates and all 299 erasure patterns up to size three.')
print('counts:',dict(ct),'signed-axis triangles:',dict(triangles),'checks:',nchecks)
print('worst successful squared singular value:',.25-2*a,'condition number:',1/sqrt(.25-2*a))
