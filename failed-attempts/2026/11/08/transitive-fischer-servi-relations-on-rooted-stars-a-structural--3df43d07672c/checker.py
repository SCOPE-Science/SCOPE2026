import itertools,math
from collections import Counter

def transitive(mat,n):
 for i in range(n):
  for j in range(n):
   if mat[i]>>j&1 and (mat[j]&~mat[i]):return False
 return True

def works(mat,m):
 n=m+1
 if not transitive(mat,n):return False
 # r=0; i>=1 leaf
 # forward: 0<=i, 0Rz => exists t>=z iRt
 for i in range(1,n):
  for z in range(n):
   if mat[0]>>z&1:
    if z==0:
     if not mat[i]:return False
    elif not(mat[i]>>z&1):return False
 # backward: xRroot, root<=leaf j => exists y>=x yRj
 for x in range(n):
  if mat[x]&1:
   for j in range(1,n):
    if x==0:
     if not any(mat[y]>>j&1 for y in range(n)):return False
    else:
     if not(mat[x]>>j&1):return False
 return True

def generate(m):
 n=m+1; L=set(range(1,n))
 all_T = {}
 for size in range(m+1):
  cidx=range(size)
  all_T[size]=[]
  for z in range(1<<(size*size)):
   rows=[sum((1<<j) for j in cidx if (z>>(i*size+j))&1) for i in cidx]
   if transitive(rows,size):all_T[size].append(rows)
 out=set()
 for av in (0,1):
  for Amask in range(1<<m):
   A={i+1 for i in range(m) if Amask>>i&1}
   AA=sum(1<<j for j in A)
   for Emask in range(1<<m):
    E={i+1 for i in range(m) if Emask>>i&1}
    # E is leaves with R to root
    if av==0:
     if A&E:continue
    elif A==L:
     if E not in (set(),L):continue
    elif A&E:continue
    C=sorted(L-A-E)
    for T in all_T[len(C)]:
     rows=[0]*n
     rows[0]=AA | av
     for i in A: rows[i]=AA | (1 if i in E else 0)
     for i in E: rows[i]=((1<<n)-1)
     for p,i in enumerate(C):
      rows[i]=AA | sum(1<<j for q,j in enumerate(C) if T[p]>>q&1)
     if av==1 and A!=L:
      if not E:
       # every complement vertex needs an incoming from any row
       if any(not any(rows[i]>>j&1 for i in range(n)) for j in C):continue
      if not A:
       # rRr requires leaf rows nonempty
       if any(rows[i]==0 for i in C):continue
     out.add(tuple(rows))
 return out

for m in range(0,4):
 n=m+1
 brute=set()
 for z in range(1<<(n*n)):
  rows=tuple(sum((1<<j) for j in range(n) if z>>(i*n+j)&1) for i in range(n))
  if works(rows,m):brute.add(rows)
 family=generate(m)
 print('m',m,'brute',len(brute),'family',len(family),'miss',len(brute-family),'extra',len(family-brute))
 if brute!=family:
  print('miss',list(brute-family)[:5]); print('extra',list(family-brute)[:5]);break
