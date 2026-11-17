"""Independent exact Dyck enumeration and Euclidean simplex-face Gram checks.
For each n, U_i=A_i and D_i=B_i. No external packages required.
"""
from functools import lru_cache
from math import comb, factorial, sqrt, isclose
from fractions import Fraction
from collections import Counter

@lru_cache(None)
def cat(n):return comb(2*n,n)//(n+1)

def dyck(n):
 def rec(word,u,d):
  if d==n:
   yield word
  else:
   if u<n:yield from rec(word+'U',u+1,d)
   if d<u:yield from rec(word+'D',u,d+1)
 yield from rec('',0,0)

def facet_counter(n):
 cnt=Counter(); peaks=Counter(); hills=Counter()
 for word in dyck(n):
  u=d=0; labels=[]; height=0; hill=0; peak=0
  for i,ch in enumerate(word):
   if ch=='U':u+=1;labels.append(('A',u))
   else:d+=1;labels.append(('B',d))
   if i>0 and word[i-1:i+1]=='UD':
    peak+=1
    if u==d:hill+=1
  peaks[peak]+=1; hills[hill]+=1
  for a,b in zip(labels,labels[1:]):
   if a[0]==b[0]: assert b[1]==a[1]+1;cnt[(a[0],a[1])]+=1
   elif a[0]=='A' and b[0]=='B' and a[1]==b[1]:cnt[('V',a[1])]+=1
 return cnt,peaks,hills

def det_frac(M):
 n=len(M); D=[[Fraction(t) for t in row] for row in M]; s=Fraction(1)
 for j in range(n):
  p=next((i for i in range(j,n) if D[i][j]!=0),None)
  if p is None: return Fraction(0)
  if p!=j:D[j],D[p]=D[p],D[j];s=-s
  d=D[j][j];s*=d
  for i in range(j+1,n):
   v=D[i][j]/d
   for k in range(j+1,n):D[i][k]-=v*D[j][k]
 return s

def simplex_facet_gram(word,remove):
 N=len(word); coords=[]; u=d=0
 for ch in word:
  if ch=='U':u+=1;coords.append(u-1)
  else:d+=1;coords.append(N//2+d-1)
 verts=[]
 for j in range(N+1):
  v=[0]*N
  for c in coords[N-j:]:v[c]=1
  if j!=remove:verts.append(v)
 basis=[[a-b for a,b in zip(v,verts[0])] for v in verts[1:]]
 gram=[[sum(a*b for a,b in zip(v,w)) for w in basis] for v in basis]
 return det_frac(gram)

def test():
 total_rows=0; total_gram=0
 for n in range(1,11):
  cnt,peaks,hills=facet_counter(n)
  N=2*n; C=cat(n);total_rows+=C
  assert sum(peaks.values())==C and sum(hills.values())==C
  assert sum(v*cnt for v,cnt in peaks.items())==C*Fraction(n+1,2)
  assert sum(v*cnt for v,cnt in hills.items())==C
  assert sum(cnt.values())==n*C,(n,sum(cnt.values()),n*C)
  for i in range(1,n+1):assert cnt['V',i]==cat(i-1)*cat(n-i),(n,i,cnt)
  assert sum(v for k,v in cnt.items() if k[0]=='V')==C
  assert sum(v for k,v in cnt.items() if k[0] in ('A','B'))==(n-1)*C
  if n<=5:
   for word in dyck(n):
    # All simplex boundary faces: min and max, and consecutive comparable facets.
    N=len(word);u=d=0;labs=[]
    for ch in word:
     if ch=='U':u+=1;labs.append(('A',u))
     else:d+=1;labs.append(('B',d))
    # min at first (zero) and max at last (one)
    assert simplex_facet_gram(word,N)==1
    assert simplex_facet_gram(word,0)==1
    total_gram+=2
    for j,(a,b) in enumerate(zip(labs,labs[1:]),start=1):
     if a[0]==b[0] or (a[0]=='A' and b[0]=='B' and a[1]==b[1]):
      g=simplex_facet_gram(word,N-j)
      assert g==2,(n,word,j,g)
      total_gram+=1
  print(f'n={n}, Dyck={C}, cover-adjacent total={sum(cnt.values())}, peaks_mean={sum(k*v for k,v in peaks.items())/C:g}, hills_mean={sum(k*v for k,v in hills.items())/C:g}, vertical_counts={[cnt["V",i] for i in range(1,n+1)]}')
 print('GRID_SURFACE_EXACT_PASS', 'paths',total_rows,'gram_faces',total_gram)

if __name__=='__main__':test()
