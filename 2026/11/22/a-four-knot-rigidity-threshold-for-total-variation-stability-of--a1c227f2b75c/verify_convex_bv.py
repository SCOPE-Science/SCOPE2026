#!/usr/bin/env python3
"""Exact-rational checks for variation stability of finite convex regression.
Only Python standard library is required. All identities are over Q.
"""
from fractions import Fraction as F
from itertools import product
from random import Random

def dot(a,b): return sum((x*y for x,y in zip(a,b)), F(0))
def tr(a): return list(map(list,zip(*a)))
def mul(a,b):
    bt=tr(b)
    return [[dot(row,col) for col in bt] for row in a]
def eye(n): return [[F(int(i==j)) for j in range(n)] for i in range(n)]
def sub(a,b): return [[x-y for x,y in zip(row,s)] for row,s in zip(a,b)]
def inv(a):
    n=len(a)
    t=[list(row)+e for row,e in zip(a,eye(n))]
    for j in range(n):
        k=next(k for k in range(j,n) if t[k][j]);t[j],t[k]=t[k],t[j]
        p=t[j][j];t[j]=[x/p for x in t[j]]
        for k in range(n):
            if k==j:continue
            p=t[k][j]
            t[k]=[v-p*w for v,w in zip(t[k],t[j])]
    return [row[n:] for row in t]
def mv(a,v):return [dot(row,v) for row in a]
def cols(c):return tr(c)

def constraints(xs):
    n=len(xs);C=[]
    for i in range(n-2):
        h=xs[i+1]-xs[i];g=xs[i+2]-xs[i+1]
        row=[F(0)]*n
        row[i]=1/h;row[i+1]=-1/h-1/g;row[i+2]=1/g
        C.append(row)
    return C

def projector(xs,ms,subset):
    n=len(xs); C=constraints(xs)
    ca=[C[i] for i in subset]
    if not ca:return eye(n)
    t=[[c[j]/ms[j] for c in ca] for j in range(n)]
    gram=mul(ca,t)
    return sub(eye(n),mul(mul(t,inv(gram)),ca))

def edge_matrix(P):
    n=len(P);D=[];E=[]
    for i in range(n-1):
        row=[F(0)]*n;row[i]=-1;row[i+1]=1;D.append(row)
    for i in range(n):E.append([F(int(i>j)) for j in range(n-1)])
    return mul(mul(D,P),E)
def seminorm(z):return sum(abs(z[i+1]-z[i]) for i in range(len(z)-1))
def norm(P):
    J=edge_matrix(P);return max(sum(abs(row[j]) for row in J) for j in range(len(J[0])))

def affine_coeff(xs,ms):
    M=sum(ms);mu=dot(xs,ms)/M
    S=sum(m*(x-mu)**2 for m,x in zip(ms,xs))
    c=[sum((ms[i]*(xs[i]-mu) for i in range(j+1,len(xs))),F(0))/S for j in range(len(xs)-1)]
    return mu,S,c

def all_active_witness(xs,ms):
    n=len(xs);C=constraints(xs);t=[[c[j]/ms[j] for c in C] for j in range(n)]
    base=[-sum(row) for row in t]
    P=projector(xs,ms,list(range(n-2)))
    J=edge_matrix(P)
    j=max(range(n-1),key=lambda k:sum(abs(row[k]) for row in J))
    step=[F(int(i>j)) for i in range(n)]
    G=mul(C,t);Ginv=inv(G)
    change=mv(Ginv,mv(C,step))
    eps=F(1)
    while any(1-eps*q<=0 for q in change):eps/=2
    second=[b+eps*v for b,v in zip(base,step)]
    mult=[F(1)-eps*q for q in change]
    assert all(m>0 for m in mult)
    # P(base)=0 and P(second)=eps*P(step); the KKT multiplier is strictly positive.
    assert mv(P,base)==[0]*n
    predicted=mv(P,second)
    assert mv(C,predicted)==[0]*(n-2)
    assert all(x==0 for x in mv(C,mv(P,step)))
    ratio=seminorm([p for p in predicted])/seminorm([a-b for a,b in zip(second,base)])
    return ratio,j,base,second

# n=2 identity, n=3 both active sets and the exact mass-spacing condition.
assert norm(projector([F(0),F(1)],[F(3),F(2)],[]))==1
for h1 in range(1,6):
 for h2 in range(1,6):
  for m1,m2,m3 in product(range(1,5),repeat=3):
   xs=[F(0),F(h1),F(h1+h2)];ms=list(map(F,[m1,m2,m3]))
   mu,S,c=affine_coeff(xs,ms)
   k=(h1+h2)*max(c)
   assert norm(projector(xs,ms,[0]))==k
   assert (k==1)==(m3*h2==m1*h1)
print('THREE_KNOT_EXACT_WEIGHTED_FORMULA_PASS',5*5*4**3)

xs=list(map(F,range(4)));ms=[F(1)]*4
want={():F(1),(0,):F(7,6),(1,):F(7,6),(0,1):F(6,5)}
for mask,k in want.items():
 assert norm(projector(xs,ms,mask))==k
print('FOUR_KNOT_ALL_ACTIVE_FACES_EXACT_PASS',len(want))
ratio,j,base,second=all_active_witness(xs,ms)
assert ratio==F(6,5) and j==1
print('FOUR_KNOT_ATTAINED_SHARP_SIX_FIFTHS_PASS')

# The affine face norm is L*max c and is strictly >1 for n>=4.
rng=Random(20261115);tests=0
for n in range(4,10):
 for attempt in range(25):
  h=[F(rng.randrange(1,14),rng.randrange(1,6)) for i in range(n-1)]
  xs=[F(0)]
  for item in h:xs.append(xs[-1]+item)
  ms=[F(rng.randrange(1,12),rng.randrange(1,5)) for i in range(n)]
  mu,S,c=affine_coeff(xs,ms)
  L=xs[-1]-xs[0]
  assert all(z>0 for z in c)
  assert dot(h,c)==1
  bound=L*max(c)
  assert bound>1
  ratio,j,base,second=all_active_witness(xs,ms)
  assert ratio==bound
  tests+=1
print('ARBITRARY_MESH_MASS_ALL_AFFINE_FACE_SHARPNESS_PASS',tests)

# Equally spaced, equal-mass formula and universal lower bound.
for n in range(3,40):
 xs=list(map(F,range(n)));ms=[F(1)]*n
 _,_,c=affine_coeff(xs,ms)
 assert c==[F(6*j*(n-j),n*(n*n-1)) for j in range(1,n)]
 assert (n-1)*max(c)==F(6*(n*n//4),n*(n+1))
print('EXACT_BALANCED_JUMP_LOWER_BOUND_PASS',37)
print('ALL_CONVEX_REGRESSION_BV_CHECKS_PASS')
