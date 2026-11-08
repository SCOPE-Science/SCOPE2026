"""Reproduce the complete cyclic symbol-pair generation ladder for binary RM(2,m).
Standard library only. Evaluates the actual codewords, not merely predicted ranks.
"""
from itertools import combinations

def rows(m):
 n=1<<m
 subsets=[()]+[(i,) for i in range(m)]+list(combinations(range(m),2))
 return [sum((int(all((x>>i)&1 for i in I)))<<x for x in range(n)) for I in subsets],subsets

def rank(items):
 piv={}
 for a in items:
  while a:
   b=a.bit_length()
   if b not in piv:
    piv[b]=a
    break
   a^=piv[b]
 return len(piv)

def pw(w,n):
 mask=(1<<n)-1
 return (w | ((w<<1)|(w>>(n-1))) & mask).bit_count()

def expected(m,alpha):
 n=1<<m
 if alpha<n//4+1:return 0
 for s in range(m-3):
  if alpha<n//4+(1<<(s+1)):
   h=s+3
   return 1+h+h*(h-1)//2
 return 1+m+m*(m-1)//2

def exhaustive(m):
 rs,subsets=rows(m);n=1<<m;k=len(rs); tcode=0
 low=[[] for _ in range(n+1)]
 for t in range(1,1<<k):
  tcode^=rs[(t & -t).bit_length()-1]
  low[pw(tcode,n)].append(tcode)
 accum=[];seen={}
 for alpha in range(n+1):
  accum+=low[alpha]
  got=rank(accum);want=expected(m,alpha)
  assert got==want,(m,alpha,got,want)
  seen[alpha]=got
 return {z:seen[z] for z in range(n+1) if z==0 or seen[z]!=seen[z-1]},(1<<k)-1

def polynomial_bits(m,func):
 return sum(int(func([(t>>j)&1 for j in range(m)]))<<t for t in range(1<<m))

def constructors(m):
 n=1<<m
 for j in range(m-3,-1,-1):
  target=n//4 + (1<<(m-j-3));cand=[]
  for i in range(j+2,m):
   for b in (0,1):
    cand.append(polynomial_bits(m,lambda x,i=i,b=b,j=j:(x[j]^x[j+1]) & (x[i]^b)))
  bfun=polynomial_bits(m,lambda x,j=j: int(x[j]==x[j+1]==x[j+2]))
  cand.append(bfun)
  if m-j==3:
   # 8 adjacent pairs of 2^j blocks: valid RM(2,m) words.
   cand=[polynomial_bits(m,lambda x,t=t,j=j: int((((sum(x[i]<< (i-j) for i in range(j,m))) - t)%8) in (0,1))) for t in range(8)]
   assert rank(cand)==7
  else:
   # add previously constructed words depending only on x_{j+1},...,x_{m-1}
   for I in [()]+[(i,) for i in range(j+1,m)]+list(combinations(range(j+1,m),2)):
    cand.append(polynomial_bits(m,lambda x,I=I: int(all(x[i] for i in I))))
  assert all(pw(x,n)<=target for x in cand[:8 if m-j==3 else (2*(m-j-2)+1)]),(m,j)
  dim=rank(cand)
  want=1+(m-j)+(m-j)*(m-j-1)//2
  assert dim==want,(m,j,dim,want)
 return True

if __name__=='__main__':
 total=0
 for m in (3,4,5):
  changes,count=exhaustive(m)
  total+=count
  print('EXHAUSTIVE m=',m,'count=',count,'changes=',changes)
 for m in range(3,9):
  assert constructors(m)
  print('CONSTRUCTION m=',m,'PASS')
 print('ALL PASS, exhaustive nonzero words =',total)
