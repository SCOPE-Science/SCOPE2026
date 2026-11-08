#!/usr/bin/env python3
"""Independent matrix-algebra check for the eight Tallini-quartic pencils over F2."""
from itertools import product, permutations, combinations
I=(1,0,0,0,1,0,0,0,1)
ZERO=(0,)*9

def plus(A,B):return tuple(a^b for a,b in zip(A,B))
def mm(A,B):return tuple(sum(A[3*i+k]*B[3*k+j] for k in range(3))%2 for i in range(3) for j in range(3))
def det(A):
 return sum(A[i]*A[3+j]*A[6+k] for i,j,k in permutations(range(3)))%2
def powers(A):
 m=I; res=[I]
 while True:
  m=mm(m,A)
  if m==I:return res
  res.append(m)
  assert len(res)<200
ALL=[tuple(a) for a in product(range(2),repeat=9)]
GL=[A for A in ALL if det(A)]
assert len(GL)==168
IRR={A for A in ALL if det(A) and det(plus(A,I))}
assert len(IRR)==48
for A in IRR:assert len(powers(A))==7
GROUPS={frozenset(powers(A)) for A in IRR}
assert len(GROUPS)==8
# Matrix cosets by scalar identity give curves. Distinctness is checked via explicit forms.
CAN={min(A,plus(A,I)) for A in IRR}
assert len(CAN)==24
group_triples=[]
for H in GROUPS:
 c=frozenset(min(A,plus(A,I)) for A in H if A!=I)
 assert len(c)==3
 group_triples.append(c)
assert len(set.union(*(set(g) for g in group_triples)))==24
assert all(len(G.intersection(H))==0 for G,H in combinations(group_triples,2))
for tri in group_triples:
 A,B,C=tuple(tri)
 assert plus(plus(A,B),C) in (ZERO,I)
# No mixed 3-element smooth subspaces: all pairs of distinct cosets checked.
triples={frozenset((A,B,min(plus(A,B),plus(plus(A,B),I)))) for A,B in combinations(sorted(CAN),2) if plus(A,B) in IRR or plus(plus(A,B),I) in IRR}
assert len(triples)==8 and triples==set(group_triples)

# Explicit matrix-to-quartic linear map in the Tallini basis.
mon=[(i,j,4-i-j) for i in range(5) for j in range(5-i)]
idx={m:k for k,m in enumerate(mon)}
# U=Y^2Z+YZ^2; V=Z^2X+ZX^2; W=X^2Y+XY^2.
U=[(0,2,1),(0,1,2)]; V=[(1,0,2),(2,0,1)]; W=[(2,1,0),(1,2,0)]
BASIS=[U,V,W]
def form(A):
 mask=0
 for j,cubic in enumerate(BASIS):
  for i in range(3):
   if A[3*i+j]:
    for exp in cubic:
     m=tuple(exp[t]+(t==i) for t in range(3))
     mask^=1<<idx[m]
 return mask
assert form(I)==0
MASKS={form(A) for A in CAN}
assert len(MASKS)==24
pencils={tuple(sorted(form(A) for A in H)) for H in group_triples}
assert len(pencils)==8
assert pencils=={(6438,10988,13258),(6636,10086,16010),(6922,11948,13734),(7110,9004,14570),(7530,11884,13062),(7596,9190,15946),(8006,10794,13676),(8070,10154,14380)}
print('MATRIX_FIELD_CHECK_PASS 512 168 48 24 8 8')
