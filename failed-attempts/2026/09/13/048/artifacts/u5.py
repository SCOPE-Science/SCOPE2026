# For each solved pair, scan pi3 (clean, pairwise-sym 1 with both) and compute central value. Seek nontriv.
from eisen import *
from u3lib import *
import itertools
lam3=(-3,-6)
def clean(pi): return edivides(lam3, esub(pi, ONE))
primes=enum_primary_primes(5000)
C=[(pi,N) for pi,N in primes if clean(pi)]
S={}
for i,(p1,n1) in enumerate(C):
    for j,(p2,n2) in enumerate(C):
        if i!=j: S[(i,j)]=cubic_symbol(p1,p2)
pairs=[(i,j) for i in range(len(C)) for j in range(i+1,len(C)) if S[(i,j)]==0 and S[(j,i)]==0]
pairs.sort(key=lambda ij: max(C[ij[0]][1],C[ij[1]][1]))
found=[]
for i,j in pairs[:14]:
    pi1,n1=C[i]; pi2,n2=C[j]
    s=find_theta(pi1,pi2,4)
    if not s: print("nosol",e2str(pi1),e2str(pi2)); continue
    Th=s[0]
    N=knormXYZ(*Th,pi1)
    print(f"=== pi1={e2str(pi1)}({n1}) pi2={e2str(pi2)}({n2}) Th={list(map(e2str,Th))} N={e2str(N)}")
    nnon=0; examples=[]
    for k,(pi3,n3) in enumerate(C):
        if k==i or k==j: continue
        if enorm(pi3)==n1 or enorm(pi3)==n2: continue
        if S[(i,k)]!=0 or S[(k,i)]!=0 or S[(j,k)]!=0 or S[(k,j)]!=0: continue
        v=central_value(Th,pi1,pi3)
        if v==1 or v==2:
            nnon+=1
            if len(examples)<4: examples.append((e2str(pi3),n3,v))
    print(f"    nontriv pi3 count: {nnon} e.g. {examples}")
