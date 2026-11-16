#!/usr/bin/env python3
"""Independent tree-edge enumeration followed by exact Walsh transform."""
from collections import Counter
from math import gcd

DIM=16
N=1<<DIM
EXPECTED={0:42894,32:7008,-32:7008,64:448,-64:448,128:3504,-128:3504,224:16,-224:16,256:96,-256:96,288:144,-288:144,512:72,-512:72,640:32,-640:32,4096:1,-4096:1}

def tree(mask):
 if mask.bit_count()!=7:return False
 parent=list(range(8))
 def find(x):
  while x!=parent[x]:
   parent[x]=parent[parent[x]]
   x=parent[x]
  return x
 for e in range(16):
  if mask & (1<<e):
   u,v=find(e//4),find(4+e%4)
   if u==v:return False
   parent[u]=v
 return True

def hadamard(vec):
 for k in range(DIM):
  span=1<<k
  for block in range(0,N,span*2):
   for j in range(block,block+span):
    u,v=vec[j],vec[j+span]
    vec[j]=u+v
    vec[j+span]=u-v
 return vec

def main():
 f=[int(tree(mask)) for mask in range(N)]
 assert sum(f)==4096
 W=hadamard(f)
 assert Counter(W)==EXPECTED
 assert sum(t*t for t in W)==N*4096
 assert sum(W)==N*int(tree(0))==0
 assert all(W[s^65535]==-W[s] for s in range(N))
 assert gcd(*W)==32
 assert min(abs(x) for x in W if x)!=0 and min(abs(x) for x in W if x)==32
 assert N-Counter(W)[0]==22642
 P=hadamard([int(x!=0) for x in W])
 assert sum(abs(x) for x in P)==2950060
 assert sum(abs(x) for x in P)/N > 45
 print('TREE_ENUMERATION_WALSH_PASS')

if __name__=='__main__':main()
