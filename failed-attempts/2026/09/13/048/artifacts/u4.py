from eisen import *
from u3lib import *
lam3=(-3,-6)
def clean(pi): return edivides(lam3, esub(pi, ONE))
primes=enum_primary_primes(5000)
C=[(pi,N) for pi,N in primes if clean(pi)]
S={}
for i,(p1,n1) in enumerate(C):
    for j,(p2,n2) in enumerate(C):
        if i!=j: S[(i,j)]=cubic_symbol(p1,p2)
pairs=[(i,j) for i in range(len(C)) for j in range(i+1,len(C)) if S[(i,j)]==0 and S[(j,i)]==0]
# order by max norm
pairs.sort(key=lambda ij: max(C[ij[0]][1],C[ij[1]][1]))
print("npairs:",len(pairs))
import time
tested=0
for i,j in pairs[:40]:
    pi1,n1=C[i]; pi2,n2=C[j]
    t0=time.time()
    s=find_theta(pi1,pi2,4)
    dt=time.time()-t0
    tested+=1
    print(f"{e2str(pi1)}({n1}) x {e2str(pi2)}({n2}): {'THETA '+str(list(map(e2str,s[0]))) if s else 'none'} [{dt:.1f}s]")
