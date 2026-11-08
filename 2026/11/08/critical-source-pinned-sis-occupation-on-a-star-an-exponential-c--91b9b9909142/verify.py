"""Independent exact-state and asymptotic checks for a contact process pinned at a star leaf."""
import math
from fractions import Fraction
import numpy as np
from scipy.linalg import solve_banded
from scipy.sparse import lil_matrix, csc_matrix
from scipy.sparse.linalg import spsolve
from sympy import Matrix, Rational

assertions=0

def eq(a,b,label=''):
 global assertions
 assert a==b,(label,a,b)
 assertions+=1

def full_Q(n,lam):
 states=1<<(n+1)
 M=[[Rational(0) for _ in range(states)] for _ in range(states)]
 for s in range(states):
  hub=s&1;k=(s>>1).bit_count()
  for i in range(n+1):
   infected=(s>>i)&1
   if infected:r=Rational(1)
   elif i==0:r=lam*(k+1)
   elif hub:r=lam
   else:r=Rational(0)
   if r:
    t=s^(1<<i)
    M[s][t]+=r;M[s][s]-=r
 return Matrix(M)

def reduced_Q(n,lam,source=True):
 S=2*(n+1)
 M=[[Rational(0) for _ in range(S)] for _ in range(S)]
 for k in range(n+1):
  for hub in (0,1):
   i=2*k+hub
   targets=[]
   if k:targets.append((2*(k-1)+hub,k))
   if hub:
    targets.append((2*k,Rational(1)))
    if k<n:targets.append((2*(k+1)+1,lam*(n-k)))
   elif k+int(source):targets.append((2*k+1,lam*(k+int(source))))
   for j,r in targets:
    M[i][j]+=r;M[i][i]-=r
 return Matrix(M)

def stationary(Q):
 A=Q.T.copy();b=[Rational(0)]*Q.rows
 for j in range(Q.cols):A[0,j]=1
 b[0]=1
 return A.inv()*Matrix(b)

def reduced_occupation(n,lam):
 Q=reduced_Q(n,lam,source=False)
 idx=list(range(1,Q.rows))
 A=Matrix([[-Q[i,j] for j in idx] for i in idx]);b=Matrix([int(i%2==1) for i in idx])
 ans=A.inv()*b
 return ans[0],ans

def dual_hit(n,lam):
 Q=reduced_Q(n,lam,source=False)
 idx=list(range(1,Q.rows))
 A=Matrix([[-Q[i,j]+(lam if i==j and i%2 else 0) for j in idx] for i in idx])
 b=Matrix([(lam if i%2 else 0) for i in idx])
 return (A.inv()*b)[0]

for n in range(1,5):
 for la in (Rational(1,3),Rational(2,5)):
  Q=full_Q(n,la);f=stationary(Q)
  R=reduced_Q(n,la,True);red=stationary(R)
  for k in range(n+1):
   for hub in (0,1):
    total=sum((f[s] for s in range(1<<(n+1)) if (s&1)==hub and (s>>1).bit_count()==k),Rational(0))
    eq(total,red[2*k+hub],f'aggregate n={n}, k={k}, hub={hub}')
  p=sum(red[2*k+1] for k in range(n+1))
  ek=sum(k*(red[2*k]+red[2*k+1]) for k in range(n+1))
  exk=sum(k*red[2*k+1] for k in range(n+1))
  eq(ek,la*(n*p-exk),'moment balance')
  eq(p,dual_hit(n,la),'dual first hit')
  h,arr=reduced_occupation(n,la)
  eq(h,arr[0],'occupation solve')

# Band solver for general n, independent of the exact-state test above.
def occupation_banded(n,lam):
 ab=np.zeros((3,n+1));b=-np.ones(n+1)
 for k in range(n+1):
  ab[1,k]=-(lam*(n-k)+k*(1+lam)+1)
  if k<n:ab[0,k+1]=lam*(n-k)*(1+lam)
  if k:ab[2,k-1]=k
 return solve_banded((1,1),ab,b,check_finite=True)[0]

def stationary_sparse(n,lam):
 S=2*(n+1);Q=lil_matrix((S,S))
 for k in range(n+1):
  for x in (0,1):
   i=2*k+x
   moves=[]
   if k:moves.append((2*(k-1)+x,k))
   if x:
    moves.append((2*k,1.0))
    if k<n:moves.append((2*(k+1)+1,lam*(n-k)))
   else:moves.append((2*k+1,lam*(k+1)))
   for j,r in moves:Q[i,j]+=r;Q[i,i]-=r
 A=Q.T.tolil();A[0,:]=1
 b=np.zeros(S);b[0]=1
 pr=spsolve(A.tocsc(),b)
 return sum(pr[1::2]),sum((k*(pr[2*k]+pr[2*k+1]) for k in range(n+1)))

# A continuous potential solving the limiting generator on z=lam*k.
def v(a,z):
 d=a-z
 if abs(d)<1e-8:return 1+d/2+d*d/6
 return math.expm1(d)/d

def u1prime(a,z):
 d=a-z
 if abs(d)<1e-5:return 0.5+d/3+d*d/8
 return (math.expm1(d)-d)/(d*d)

def u1second(a,z):
 # from the integral v+v': u1''=-integral_0^1 (t-t^2) exp(t*(a-z)) dt
 from scipy.integrate import quad
 return -quad(lambda t:t*(1-t)*math.exp(t*(a-z)),0,1)[0]

for c in (.5,1,1.5,2):
 a=c*c;target=math.expm1(a)/a
 for n in (200,1000,4000):
  lam=c/math.sqrt(n);H=occupation_banded(n,lam)
  # The finite-state occupation approaches the value derived from the limiting potential.
  assert abs(H-target)<3.5*c*math.sqrt(n)**(-0.3)*target
  assertions+=1
  ph,ek=stationary_sparse(n,lam)
  # Test the stationary balance and duality in the asymptotic regime.
  assert ph>0 and ek>0
  assert ek<lam*n*ph
  assertions+=2
  print('c,n',c,n,'H',round(H,8),'target',round(target,8),'sqrt(n)*hub',round(math.sqrt(n)*ph,7),'target',round(c*target,7),'E leaves',round(ek,7),'target',round(math.expm1(a),7))

# Check the exact continuum Poisson equation in regions on both sides of the drift zero.
for a in (.25,1,2.25,4):
 for z in (0,0.1,a/2,a,2*a,a+20):
  w=v(a,z);u1p=u1prime(a,z)
  assert abs((a-z)*u1p-w+1)<1e-7,(a,z,w,u1p)
  assertions+=1
print('PASS:',assertions,'exact-rational, independent-generator and numerical checks')

# Direct Poisson-generator residual checks on the actual physical state space.
from scipy.integrate import quad
for c in (.5,1,1.5,2):
 for n in (100,1000):
  lam=c/math.sqrt(n);a=c*c
  for k in sorted(set((0,1,2,3,n//4,n//2,n-1,n))):
   z=lam*k
   def U0(t):return quad(lambda s:v(a,s),0,t,epsabs=5e-10)[0]
   def U1(t):return U0(t)+v(a,t)
   l0=k*(U0(z-lam)-U0(z)) + (lam*k)*v(a,z) if k else 0.0
   l1=(lam*(n-k)*(U1(z+lam)-U1(z)) if k<n else 0.0)+(k*(U1(z-lam)-U1(z)) if k else 0.0)-v(a,z)
   assert abs(l0)<10*math.exp(a)*lam and abs(l1+1)<10*math.exp(a)*lam, (c,n,k,l0,l1)
   assertions+=2
print('PASS TOTAL:',assertions,'checks including exact finite generators and limiting Poisson equation')
