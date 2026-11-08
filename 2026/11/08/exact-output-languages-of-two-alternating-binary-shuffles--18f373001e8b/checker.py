from itertools import combinations,product

def sh(u,v):
 m=len(u); n=len(v); out=set()
 for indices in combinations(range(m+n),m):
  s=set(indices); i=j=0; w=[]
  for t in range(m+n):
   if t in s:w.append(u[i]); i+=1
   else:w.append(v[j]); j+=1
  out.add(''.join(w))
 return out

def good(w):
 h=0
 for c in w:
  h+=1 if c=='0' else -1
  if h<0 or h>2: return False
 return h==0
for n in range(1,6):
 a='01'*n;b='10'*n
 x=sh(a,a); y=sh(a,b)
 p={''.join(w) for w in product('01',repeat=4*n) if good(w)}
 q={''.join(w) for w in product(('01','10'),repeat=2*n)}
 assert x==p,(n,len(x),len(p),len(x^p))
 assert y==q,(n,len(y),len(q),len(y^q))
 assert len(x)==2**(2*n-1)
 assert len(y)==2**(2*n)
 assert x&y=={a*2},(n,x&y)
 print(n,len(x),len(y),len(x&y))
print('PASS')
