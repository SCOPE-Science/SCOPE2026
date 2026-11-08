"""Exact binary linear algebra and finite small-state checks for reversible waves on complete multipartite graphs."""
from itertools import product
from math import comb

def matrix(parts):
    n=sum(parts)
    partof=[i for i,s in enumerate(parts) for _ in range(s)]
    return [sum((1<<j) for j in range(n) if partof[i]!=partof[j]) for i in range(n)]

def rank(vs):
    pivot={}
    for v in vs:
        while v:
            b=v.bit_length()-1
            if b in pivot:v^=pivot[b]
            else:pivot[b]=v;break
    return len(pivot)

def action(x,rows):
    return sum(( ((x & row).bit_count()&1)<<i ) for i,row in enumerate(rows))

def mul(B,C):return [action(row,C) for row in B]
def identity(n):return [1<<j for j in range(n)]

def invariants(parts):
    n=sum(parts);p=sum(a&1 for a in parts);e=len(parts)-p;r=p+e
    s=p-(p&1)
    delta=int(p%2==1 and e>0)
    rho=r-(r&1)
    a3=delta
    a2=rho-s-2*delta
    b2=int(p>0 and p%2==0)
    b1=s-2*b2
    a1=n-2*a2-3*a3-b1-2*b2
    assert min(a1,a2,a3,b1,b2)>=0
    return a1,a2,a3,b1,b2

def dimfix(k,inv):
    a1,a2,a3,b1,b2=inv
    v2=(k&-k)
    return a1*min(v2,2)+a2*min(v2,4)+a3*min(v2,6) + (2*b1+2*b2*min(v2,2) if k%3==0 else 0)

def wave_rows(parts):
    A=matrix(parts);n=len(A)
    # (u,v) -> (v,u+Av), bit row convention
    return [(1<<(n+i)) for i in range(n)]+[ (1<<i)|(A[i]<<n) for i in range(n)]

def divisors(n):return [i for i in range(1,n+1) if n%i==0]

def mobius(n):
    prime=0;k=2
    while k*k<=n:
        if n%k==0:
            n//=k;prime+=1
            if n%k==0:return 0
            while n%k==0:n//=k
        k+=1
    if n>1:prime+=1
    return -1 if prime&1 else 1

def least(k,inv,q=2):
    return sum(mobius(k//d)*q**dimfix(d,inv) for d in divisors(k))

cases=0
for r in range(2,7):
 for parts in product(range(1,5),repeat=r):
  if sum(parts)>14:continue
  n=sum(parts);A=matrix(parts);B=identity(n);powers=[]
  a1,a2,a3,b1,b2=invariants(parts)
  # A ranks for powers 0..4, from predicted Jordan blocks
  for k in range(1,5):
   B=mul(B,A);powers.append(B)
   expected = a2*(k<2)+a3*max(3-k,0)+b1+b2*2
   assert rank(B)==expected,('rank',parts,k,rank(B),expected)
  assert powers[3]==(powers[1] if sum(a%2 for a in parts)%2==0 else powers[2]), ("power_identity", parts)
  W=wave_rows(parts);P=identity(2*n)
  for k in range(1,25):
   P=mul(P,W)
   ker=2*n-rank([row^(1<<i) for i,row in enumerate(P)])
   assert ker==dimfix(k,(a1,a2,a3,b1,b2)),('fix',parts,k,ker,dimfix(k,(a1,a2,a3,b1,b2)))
  assert P==identity(2*n)
  for k in divisors(24):
   assert least(k,(a1,a2,a3,b1,b2))>=0 and least(k,(a1,a2,a3,b1,b2))%k==0
  cases+=1
print('RANK_AND_FIXED_COUNT_OK',cases)

# Independent orbit-by-orbit brute force for all states of small graph sizes
state_cases=0
for r in range(2,6):
 for parts in product(range(1,4),repeat=r):
  n=sum(parts)
  if n>7:continue
  W=wave_rows(parts); inv=invariants(parts)
  counts={d:0 for d in divisors(24)}
  for z in range(1<<(2*n)):
   cur=action(z,W);k=1
   while cur!=z:
    cur=action(cur,W);k+=1
    assert k<=24
   counts[k]+=1
  for k in divisors(24):assert counts[k]==least(k,inv),('orbit',parts,k,counts[k],least(k,inv))
  state_cases+=1
print('STATE_ORBITS_OK',state_cases)

for parts in ([1,2],[1,1,2],[1,1,1,2],[1,1,2,2],[2,2],[1,1,1],[1,1,1,1],[2,2,2]):
 inv=invariants(parts)
 C={d:least(d,inv) for d in divisors(24)}
 print('EXAMPLE',parts,'INV',inv,'ORDER',max(d for d in divisors(24) if C[d]),'CENSUS',C)
