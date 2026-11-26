"""Independent finite checks for total domination of two-token complete bipartite graphs."""
from itertools import combinations
from math import comb, factorial


def add(p,q):
 z=[0]*max(len(p),len(q))
 for i,a in enumerate(p):z[i]+=a
 for i,a in enumerate(q):z[i]+=a
 return z

def mul(p,q):
 z=[0]*(len(p)+len(q)-1)
 for i,a in enumerate(p):
  for j,b in enumerate(q): z[i+j]+=a*b
 return z

def scale(p,c):return [c*a for a in p]
def binpower(n):return [comb(n,j) for j in range(n+1)]

def onto(a,b):
 p=[0]*(a*b+1)
 for i in range(a+1):
  for j in range(b+1):
   sign=(-1)**(i+j)*comb(a,i)*comb(b,j)
   v=binpower((a-i)*(b-j))
   for t,w in enumerate(v):p[t]+=sign*w
 return p

def rowcol_poly(m,n):
 p=[0]*(m*n+1)
 for a in (m-1,m):
  for b in (n-1,n):
   z=onto(a,b)
   for k,v in enumerate(z):p[k]+=v*comb(m,a)*comb(n,b)
 return p

def edgecover_poly(s):
 p=[0]*(comb(s,2)+1)
 for j in range(s+1):
  for k,v in enumerate(binpower(comb(s-j,2))):
   p[k]+=(-1)**j*comb(s,j)*v
 return p

def product_formula(m,n):
 cm,cn=edgecover_poly(m),edgecover_poly(n)
 ya=mul(cm,binpower(comb(n,2)))
 yb=mul(cn,binpower(comb(m,2)))
 yy=add(add(ya,yb),scale(mul(cm,cn),-1))
 return mul(rowcol_poly(m,n),yy)

def components_direct(m,n):
 px=[0]*(m*n+1)
 for mask in range(1<<(m*n)):
  active_rows=sum(any((mask>>(i*n+j))&1 for j in range(n)) for i in range(m))
  active_cols=sum(any((mask>>(i*n+j))&1 for i in range(m)) for j in range(n))
  if active_rows>=m-1 and active_cols>=n-1:px[mask.bit_count()]+=1
 py=[0]*(comb(m,2)+comb(n,2)+1)
 ae=list(combinations(range(m),2));be=list(combinations(range(n),2)); ell=len(ae)
 for mask in range(1<<(len(ae)+len(be))):
  ca=set();cb=set()
  for i,ab in enumerate(ae):
   if (mask>>i)&1: ca.update(ab)
  for j,ab in enumerate(be):
   if (mask>>(ell+j))&1:cb.update(ab)
  if len(ca)==m or len(cb)==n:py[mask.bit_count()]+=1
 return mul(px,py)

def graph_bruteforce(m,n):
 verts=list(combinations(range(m+n),2)); vmap={v:i for i,v in enumerate(verts)}
 adj=[0]*len(verts)
 for i,x in enumerate(verts):
  for j,y in enumerate(verts):
   if len(set(x)&set(y))==1:
    p,q=tuple(set(x)^set(y))
    if (p<m)!=(q<m):adj[i]|=1<<j
 p=[0]*(len(verts)+1)
 for mask in range(1<<len(verts)):
  if all(mask & a for a in adj):p[mask.bit_count()]+=1
 return p

def stirling(a,b):
 s=[[0]*(b+2) for _ in range(a+1)];s[0][0]=1
 for i in range(1,a+1):
  for j in range(1,min(i,b)+1):s[i][j]=s[i-1][j-1]+j*s[i-1][j]
 return s[a][b]

def min_edge_covers(s):
 if s%2==0:
  r=s//2;return factorial(s)//(2**r*factorial(r))
 r=(s-1)//2
 return factorial(s)//(2**r*factorial(r-1))

def minimum_count(m,n):
 k=(m+1)//2
 # choose n-1 columns, one selected cell per column, using >=m-1 rows
 a=n*factorial(m)*(stirling(n-1,m-1)+stirling(n-1,m))
 b=min_edge_covers(m)
 if (n+1)//2==k:b+=min_edge_covers(n)
 return a*b

def validate():
 brute=0
 for m,n in [(2,2),(2,3),(2,4),(2,5),(3,3),(3,4)]:
  exact=product_formula(m,n)
  independent=graph_bruteforce(m,n)
  assert exact==independent,(m,n,exact,independent)
  assert min(k for k,v in enumerate(exact) if v)==n-1+(m+1)//2
  assert exact[n-1+(m+1)//2]==minimum_count(m,n)
  brute+=1<<(comb(m+n,2))
  print('GRAPH_ENUM_OK',m,n,'minimum',n-1+(m+1)//2,'min_sets',minimum_count(m,n))
 for m,n in [(3,5),(4,4),(4,5)]:
  exact=product_formula(m,n)
  independent=components_direct(m,n)
  assert exact==independent,(m,n)
  assert exact[n-1+(m+1)//2]==minimum_count(m,n)
  print('COMPONENT_ENUM_OK',m,n,'minimum',n-1+(m+1)//2,'min_sets',minimum_count(m,n))
 for m in range(2,9):
  for n in range(m,13):
   z=product_formula(m,n)
   t=n-1+(m+1)//2
   assert all(v==0 for v in z[:t])
   assert z[t]==minimum_count(m,n),(m,n)
 print('ALL_FORMULA_BOUNDARY_OK',sum(13-m for m in range(2,9)))
 print('GRAPH_MASKS_TESTED',brute)
 print('VERIFY_OK')
if __name__=='__main__':validate()
