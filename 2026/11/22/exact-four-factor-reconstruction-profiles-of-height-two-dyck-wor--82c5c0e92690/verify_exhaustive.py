#!/usr/bin/env python3
"""Independent direct enumeration of four-factor histograms of height-two Dyck words."""
from itertools import product

def compositions(n):
    if n == 0:
        yield ()
        return
    for bits in product((0, 1), repeat=n-1):
        cuts = [0] + [i+1 for i,b in enumerate(bits) if b] + [n]
        yield tuple(cuts[i+1]-cuts[i] for i in range(len(cuts)-1))

def word(parts):
    return ''.join('1'+'10'*(p-1)+'0' for p in parts)

def histogram(w):
    return tuple(sum(w[i:i+r] == format(v, f'0{r}b') for i in range(len(w)-r+1))
                 for r in range(1,5) for v in range(1<<r))

def key(parts):
    n=sum(parts); b=parts.count(2); c=sum(p>=3 for p in parts)
    if b+c==0: return (n, 'unit')
    d=sum(parts[i]>=2 and parts[i+1]>=2 for i in range(len(parts)-1))
    f=int(parts[0]==1); g=int(parts[-1]==1)
    return (n,b,c,d,f,g)

def realizable(n,b,c,d,f,g):
    L=b+c
    if L==0 or not(0<=d<L):return False
    k=L-d; a0=k-1+f+g
    if c>0:return n>=2*b+3*c+a0
    if k==1 and f==g==0:return n==2*b
    return n>=2*b+a0

def expected(n):
    ans={(n, 'unit')}
    for b in range(n//2+1):
      for c in range(n//3+1):
        L=b+c
        for d in range(L):
          for f,g in product((0,1),repeat=2):
            if realizable(n,b,c,d,f,g):ans.add((n,b,c,d,f,g))
    return ans

for n in range(1,18):
    by_hist={}; by_key={}; count=0
    for parts in compositions(n):
        h=histogram(word(parts)); k=key(parts); count+=1
        if h in by_hist:assert by_hist[h]==k,(n,parts,'profile collision')
        else:by_hist[h]=k
        if k in by_key:assert by_key[k]==h,(n,parts,'key mismatch')
        else:by_key[k]=h
    assert set(by_key)==expected(n),(n,'incomplete feasibility')
    assert len(by_hist)==len(expected(n))
    assert count==2**(n-1)
    print(n,len(by_hist),count)
print('EXHAUSTIVE_OK')
