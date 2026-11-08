#!/usr/bin/env python3
"""Independent checks for inverse partner-degree theorem of isotone transformations."""
import itertools,math,random
from collections import Counter

def isotone(n):return list(itertools.combinations_with_replacement(range(n),n))
def mult(f,g):return tuple(g[x] for x in f)
def are_inverse(f,g):return mult(mult(f,g),f)==f and mult(mult(g,f),g)==g

def degree_formula(f):
 n=len(f)
 blocks=[len(list(gr)) for _,gr in itertools.groupby(f)]
 image=sorted(set(f))
 return math.prod(blocks)*math.prod(b-a for a,b in zip(image,image[1:]))

def poly_mul(A,B,N):
 Z=[0]*(N+1)
 for i,a in enumerate(A):
  if not a:continue
  for j,b in enumerate(B[:N+1-i]):
   if b:Z[i+j]+=a*b
 return Z

def moment_poly(n,r,k):
 G=[0]+[j**k for j in range(1,n+1)]
 A=[1]+[0]*n
 for _ in range(r):A=poly_mul(A,G,n)
 B=[1]+[0]*n
 for _ in range(r-1):B=poly_mul(B,G,n)
 P=[j+1 for j in range(n+1)]
 B=poly_mul(B,P,n)
 return A[n]*B[n-1]

def max_product(N,k):
 if k==0:return 1
 d,t=divmod(N,k)
 return d**(k-t)*(d+1)**t

for n in range(1,7):
 fs=isotone(n)
 degs=Counter()
 for f in fs:
  d=sum(are_inverse(f,g) for g in fs)
  assert d==degree_formula(f),(n,f,d,degree_formula(f))
  degs[len(set(f)),d]+=1
 for r in range(1,n+1):
  Ds=[d for (r2,d),c in degs.items() for _ in range(c) if r2==r]
  assert min(Ds)==n-r+1,(n,r,min(Ds))
  assert max(Ds)==max_product(n,r)*max_product(n-1,r-1),(n,r,max(Ds))
  for k in range(4):
   direct=sum(d**k for d in Ds)
   predicted=moment_poly(n,r,k)
   assert direct==predicted,(n,r,k,direct,predicted)
 print('n=%d total_maps=%d all_degree_moments_match=True' %(n,len(fs)))

print('DEGREE_VERIFY_OK')

# Asymptotic diagnostic: independent uniform kernel composition and image subset.
p=0.5
probs=[p*(1-p)**(k-1) for k in range(1,160)]
m=sum(t*math.log(i) for i,t in enumerate(probs,1))
ez=sum(i*t for i,t in enumerate(probs,1))
vz=sum((i-ez)**2*t for i,t in enumerate(probs,1))
vl=sum((math.log(i)-m)**2*t for i,t in enumerate(probs,1))
cv=sum((i-ez)*(math.log(i)-m)*t for i,t in enumerate(probs,1))
v=vl-cv**2/vz
assert v>0
random.seed(20261102)
n=120;r=60
zs=[]
for _ in range(5000):
    cuts=(0,)+tuple(sorted(random.sample(range(1,n),r-1)))+(n,)
    parts=[b-a for a,b in zip(cuts,cuts[1:])]
    B=sorted(random.sample(range(1,n+1),r))
    gaps=[b-a for a,b in zip(B,B[1:])]
    logdeg=sum(map(math.log,parts))+sum(map(math.log,gaps))
    zs.append((logdeg-(2*r-1)*m)/math.sqrt(2*r*v))
mean=sum(zs)/len(zs)
vari=sum((z-mean)**2 for z in zs)/len(zs)
print('conditional-log-degree diagnostic n=120,r=60, draws=5000 centered_mean=%.4f variance=%.4f theory=0,1'%(mean,vari))
print('ASYMPTOTIC_DIAGNOSTIC_OK')
