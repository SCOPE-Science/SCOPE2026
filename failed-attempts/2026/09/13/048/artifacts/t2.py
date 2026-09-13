from eisen import *
import itertools
primes=enum_primary_primes(5000)
print("nelig:",len(primes))
# restrict to small norms for search
S=[(pi,N) for pi,N in primes if N<1000]
print("small:",len(S))
# pairwise symbol matrix (directed); for primary both, reciprocity says equal
import time
t0=time.time()
sym={}
for i,(p1,n1) in enumerate(S):
    for j,(p2,n2) in enumerate(S):
        if i==j: continue
        sym[(i,j)]=cubic_symbol(p1,p2)
print("matrix done",time.time()-t0)
pairs=[(i,j) for i in range(len(S)) for j in range(len(S)) if i<j and sym[(i,j)]==0 and sym[(j,i)]==0]
print("npairs small:",len(pairs))
# count triples pairwise 1
count=0; examples=[]
for i,j,k in itertools.combinations(range(len(S)),3):
    if sym[(i,j)]==0 and sym[(j,i)]==0 and sym[(i,k)]==0 and sym[(k,i)]==0 and sym[(j,k)]==0 and sym[(k,j)]==0:
        count+=1
        if len(examples)<20:
            examples.append((S[i],S[j],S[k]))
print("ntriples small:",count)
for a,b,c in examples[:20]:
    print(e2str(a[0]),a[1],"|",e2str(b[0]),b[1],"|",e2str(c[0]),c[1])
