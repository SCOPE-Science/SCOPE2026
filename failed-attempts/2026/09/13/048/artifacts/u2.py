from eisen import *
import itertools
lam3=(-3,-6)
def clean(pi): return edivides(lam3, esub(pi, ONE))
primes=enum_primary_primes(5000)
C=[(pi,N) for pi,N in primes if clean(pi)]
print("nclean:",len(C))
# pairwise symbol matrix on C
S={}
for i,(p1,n1) in enumerate(C):
    for j,(p2,n2) in enumerate(C):
        if i!=j: S[(i,j)]=cubic_symbol(p1,p2)
pairs=[(i,j) for i in range(len(C)) for j in range(i+1,len(C)) if S[(i,j)]==0 and S[(j,i)]==0]
print("npairs:",len(pairs))
# show pairs with small norms
sp=[(i,j) for (i,j) in pairs if C[i][1]<300 and C[j][1]<300]
print("small pairs:",len(sp))
for i,j in sp[:30]:
    print(e2str(C[i][0]),C[i][1],"x",e2str(C[j][0]),C[j][1])
