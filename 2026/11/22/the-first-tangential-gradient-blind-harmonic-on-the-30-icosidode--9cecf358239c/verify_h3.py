# Reproduce exact modular minor certificates for tangent-gradient sampling.
# Python 3; dependency: sympy. No internet, documents, or external files needed.
# All symmetries and the zonal-harmonic argument are proved in RESULT.md.
import sympy as s
from itertools import combinations
from math import lcm
x,y,z=s.symbols('x y z')
vars=[x,y,z]
phi=s.Symbol('phi')
p=101  # sqrt5: find phi root
phivals=[i for i in range(p) if (i*i-i-1)%p==0]
assert phivals==[23,79]
print('phi mod',p,phivals)
P=phivals[0]
# all icosa vertices coordinates in Z[phi]
V=[]
for a in [-1,1]:
 for b in [-1,1]:
  V +=[(0,a,b*phi),(a,b*phi,0),(b*phi,0,a)]
assert len(V)==12
reduced=lambda e:s.rem(s.Poly(s.expand(e),phi),s.Poly(phi**2-phi-1,phi)).as_expr().expand()
assert all(reduced(sum(t*t for t in v))==phi+2 for v in V)
E=[]
for i,j in combinations(range(12),2):
 if reduced(sum(V[i][k]*V[j][k] for k in range(3))-phi)==0: E.append((i,j))
print('edges',len(E))
assert len(E)==30
Vmod=[[int(t.subs(phi,P))%p if hasattr(t,'subs') else int(t)%p for t in v] for v in V]
wm=[]
for i,j in E:
 wm.append([((Vmod[i][k]+Vmod[j][k])*pow(2*P,-1,p))%p for k in range(3)])
assert all(sum(a*a for a in w)%p==1 for w in wm)

def harmonics(l):
 mon=[(a,b,l-a-b) for a in range(l+1) for b in range(l-a+1)]
 lower=[(a,b,l-2-a-b) for a in range(l-1) for b in range(l-1-a)] if l>=2 else []
 M=s.zeros(len(lower),len(mon))
 lowidx={u:i for i,u in enumerate(lower)}
 for j,(a,b,c) in enumerate(mon):
  for k,e in enumerate([a,b,c]):
   if e>=2:
    u=[a,b,c];u[k]-=2
    M[lowidx[tuple(u)],j]=e*(e-1)
 B=M.nullspace() if lower else [s.eye(len(mon))[:,j] for j in range(len(mon))]
 basis=[]
 for v in B:
  den=lcm(*(int(q.q) for q in v))
  basis.append([int(q*den) for q in v])
 assert len(basis)==2*l+1
 return mon,basis

def eval_monomial_grad(l,mon,basis,w):
 rows=[]
 for k in range(3):rows.append([])
 for v in basis:
  f=0; grad=[0,0,0]
  for (a,b,c),coeff in zip(mon,v):
   if not coeff:continue
   f+=coeff*pow(w[0],a,p)*pow(w[1],b,p)*pow(w[2],c,p)
   for j,exp in enumerate((a,b,c)):
    if exp:
     e=[a,b,c];e[j]-=1
     grad[j]+=coeff*exp*pow(w[0],e[0],p)*pow(w[1],e[1],p)*pow(w[2],e[2],p)
  f%=p
  for k in range(3):rows[k].append((grad[k]-l*f*w[k])%p)
 return rows

def elimination(A):
 A=[row[:] for row in A]
 n=len(A);m=len(A[0]);piv=[];r=0;ids=list(range(n))
 for c in range(m):
  rs=next((i for i in range(r,n) if A[i][c]%p),None)
  if rs is None:continue
  A[r],A[rs]=A[rs],A[r]
  ids[r],ids[rs]=ids[rs],ids[r]
  v=pow(A[r][c],-1,p)
  A[r]=[(t*v)%p for t in A[r]]
  for i in range(n):
   if i==r:continue
   if A[i][c]:
    v=A[i][c];A[i]=[(a-v*b)%p for a,b in zip(A[i],A[r])]
  piv.append(c);r+=1
  if r==n:break
 return r,piv,ids[:r]

expected={1:(3,10),2:(5,46),3:(7,22),4:(9,60),5:(11,5),6:(12,61)}
for l in range(1,7):
 mon,basis=harmonics(l)
 A=[]
 for w in wm:A+=eval_monomial_grad(l,mon,basis,w)
 rank,piv,rows=elimination(A)
 det=1;B=[[A[i][c] for c in piv] for i in rows]
 for j in range(rank):
  ix=next((i for i in range(j,rank) if B[i][j]%p),None)
  assert ix is not None
  if ix!=j: B[j],B[ix]=B[ix],B[j];det=-det
  u=B[j][j]%p;det=det*u%p;inv=pow(u,-1,p)
  for i in range(j+1,rank):
   t=B[i][j]*inv%p
   for k in range(j,rank):B[i][k]=(B[i][k]-t*B[j][k])%p
 assert (rank,det%p)==expected[l]
 print(l, 'dim',2*l+1,'rank',rank,'piv',piv,'rows',rows,'minor_det',det%p)

# invariant construction at e1: sum over ico vertices P6(v dot x / norm v), homogeneous r^6 times q^3
# F=sum 231(vdot)^6 -315 q(vdot)^4 r2 + 105 q^2(vdot)^2 r2^2 -5 q^3 r2^3
q=P+2
f=0
for v in Vmod:
 dot=v[0];f+=231*dot**6-315*q*dot**4+105*q*q*dot**2-5*q**3
assert f%p==85
print('invariant F6(e1) mod p', f%p)

for w in wm:
 r2=sum(z*z for z in w)%p
 tot=0;G=[0,0,0]
 for v in Vmod:
  t=sum(a*b for a,b in zip(v,w))%p
  f=231*t**6-315*q*t**4*r2+105*q*q*t*t*r2*r2-5*q**3*r2**3
  tot=(tot+f)%p
  a=(1386*t**5-1260*q*t**3*r2+210*q*q*t*r2*r2)%p
  b=(-630*q*t**4+420*q*q*t*t*r2-30*q**3*r2*r2)%p
  G=[(g+a*v[k]+b*w[k])%p for k,g in enumerate(G)]
 assert all((G[k]-6*tot*w[k])%p==0 for k in range(3)),(w,G,tot)
print('all invariant tangential gradients zero mod p')
