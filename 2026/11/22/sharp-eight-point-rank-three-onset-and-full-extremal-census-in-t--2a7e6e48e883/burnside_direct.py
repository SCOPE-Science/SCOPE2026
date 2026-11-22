"""Separate Burnside certificate; construct fixed matrices as unions of cell orbits.
Uses direct finite-extension rank recursion from independent_recursion.py, not
canonical relabelling and not the structural rank criterion.
"""
from itertools import permutations
from collections import Counter
from independent_recursion import direct_rank_three

def cycles(p):
 seen=set(); out=[]
 for i in range(len(p)):
  if i not in seen:
   k=i; c=[]
   while k not in seen:
    seen.add(k);c.append(k);k=p[k]
   out.append(tuple(c))
 return out

def ct(p): return tuple(sorted((len(c) for c in cycles(p))))

def fixed(a,b):
 seen=set(); masks=[]
 for cell in range(16):
  if cell not in seen:
   mask=0; cur=cell
   while cur not in seen:
    seen.add(cur);mask|=1<<cur
    cur=4*a[cur//4]+b[cur%4]
   masks.append(mask)
 n=0
 for z in range(1<<len(masks)):
  bits=0
  for i,cellmask in enumerate(masks):
   if (z>>i)&1:bits|=cellmask
  if direct_rank_three(bits):n+=1
 return n

def main():
 perms=list(permutations(range(4)))
 classes=Counter(ct(p) for p in perms)
 reps={ct(p):p for p in perms}
 values={}
 s=0
 for a,pa in sorted(reps.items()):
  for b,pb in sorted(reps.items()):
   val=fixed(pa,pb)
   values[(a,b)]=val
   s+=classes[a]*classes[b]*val
 assert s==16704, s
 assert s//576==29
 assert values[((1,1,1,1),(1,1,1,1))]==9672
 print('BURNSIDE_DIRECT_OK fixed_sum=',s,'orbits=',s//576)
 print('types_and_multiplicities',sorted(classes.items()))
 for a in sorted(reps): print('row',a,[(b,values[(a,b)]) for b in sorted(reps)])

if __name__=='__main__':main()
