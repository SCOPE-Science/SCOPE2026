"""Second exact Hasse--Witt extraction plus branch and semilinear-rank checks."""
from math import comb, factorial
from collections import defaultdict
p=19
E=((1,1,1,2),(1,1,2,1),(1,2,0,1),(2,1,1,1))

def multi(n,a,b,c):return factorial(n)//(factorial(a)*factorial(b)*factorial(c))

def matrix_entry(a,b):
    u=p*a[3]-b[3]
    if u<0 or u%2 or u>2*(p-1):return {}
    h=p-1-u//2
    tx,ty,tz=[p*a[i]-b[i] for i in range(3)]
    out=defaultdict(int)
    for i in range(p):
      for j in range(p-i):
        l=p-1-i-j
        v=ty-2*i
        if v<0 or v>h:continue
        k=h-v
        if 3*j+l+v!=tx or i+2*l+2*k!=tz:continue
        out[k]=(out[k]+multi(p-1,i,j,l)*(-1)**j*comb(h,v)*comb(p-1,u//2)*(-1)**h)%p
    return {k:v for k,v in out.items() if v}
M=[[matrix_entry(a,b) for b in E] for a in E]
expected=[ [{},{},{},{}], [{},{3:-49,7:-7},{},{5:56,9:7}], [{},{},{},{}], [{},{1:7,5:-7},{},{3:7}] ]
assert M==[[{k:v%p for k,v in d.items()} for d in row] for row in expected]

# Simple polynomial arithmetic over F_19.
def add(a,b):
 c=[0]*max(len(a),len(b))
 for i,v in enumerate(a):c[i]=(c[i]+v)%p
 for i,v in enumerate(b):c[i]=(c[i]+v)%p
 while c and c[-1]==0:c.pop()
 return c
def mult(a,b):
 if not a or not b:return []
 c=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]=(c[i+j]+x*y)%p
 while c and c[-1]==0:c.pop()
 return c
def sub(a,b):return add(a,[(-x)%p for x in b])
def divmodp(a,b):
 assert b
 a=list(a);q=[0]*max(1,len(a)-len(b)+1)
 while len(a)>=len(b) and a:
  j=len(a)-len(b);v=a[-1]*pow(b[-1],-1,p)%p
  q[j]=v
  for i,w in enumerate(b):a[j+i]=(a[j+i]-v*w)%p
  while a and a[-1]==0:a.pop()
 return q,a
def gcd(a,b):
 while b: _,r=divmodp(a,b);a,b=b,r
 return [v*pow(a[-1],-1,p)%p for v in a]
poly=lambda d:([d.get(i,0) % p for i in range(max(d,default=-1)+1)] if d else [])
B=[[poly(M[i][j]) for j in (1,3)] for i in (1,3)]
D=sub(mult(B[0][0],B[1][1]),mult(B[0][1],B[1][0]))
F=[4,0,0,0,6,0,0,0,1]
assert D==mult([0]*6+[11],F)
assert gcd(F,[0,0,0,5,0,0,0,8])==[1]
# The branch discriminant (derived from x^5-x^3-t^2) vanishes if and only if 3125t^4-108=0.
sing=[(-108)%p,0,0,0,3125%p]
assert sing==[6,0,0,0,9]
assert gcd(F,sing)==[1]
assert [pow(t,4,p) for t in [7,9]]==[7,6]
assert 7!=6 and 7!=12 and 6!=12

def calc(poly,t):return sum(v*pow(t,i,p) for i,v in enumerate(poly))%p
for t in [7,9]:
 b=[[calc(v,t) for v in row] for row in B]
 assert (b[0][0]*b[1][1]-b[0][1]*b[1][0])%p==0
 assert sum(b[i][i] for i in range(2))%p in (4,1)
 # Rank-one nonnilpotent over F_19, so its semilinear stable rank is one.
 b2=[[(b[i][0]*b[0][j]+b[i][1]*b[1][j])%p for j in range(2)] for i in range(2)]
 assert any(v for row in b2 for v in row)
 # The four roots in each geometric orbit t^4=u are related by t -> i*t.
print('VERIFY_OK: independent multinomial Hasse coefficients, determinant, 8 simple smooth roots, p-rank via representatives')
print('det(B) coefficients',D,'rank-drop polynomial',F,'singular parameter polynomial',sing)
