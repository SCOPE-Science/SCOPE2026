"""Independent zeta numerator verification by point counting over F_p, F_{p^2}, F_{p^3}.
No Hasse-Witt coefficient routines are used. All smooth F_p parameter pairs are tested.
Requires Python 3 only.
"""
from itertools import product


def irreducible(p,n):
    if n==1:return (0,1)
    for cs in product(range(p),repeat=n):
        if cs[0]==0:continue
        if n==2 and all((x*x+cs[1]*x+cs[0])%p for x in range(p)):
            return cs+(1,)
        if n==3 and all((x*x*x+cs[2]*x*x+cs[1]*x+cs[0])%p for x in range(p)):
            return cs+(1,)
    raise RuntimeError
class GF:
 def __init__(self,p,n):self.p=p;self.n=n;self.q=p**n;self.mod=irreducible(p,n);self.arr=list(product(range(p),repeat=n));self.index={a:i for i,a in enumerate(self.arr)};self.zero=self.index[(0,)*n];self.one=self.index[(1,)+(0,)*(n-1)]
 def add(self,i,j):return self.index[tuple((a+b)%self.p for a,b in zip(self.arr[i],self.arr[j]))]
 def mul(self,i,j):
  a=self.arr[i];b=self.arr[j];p=self.p;n=self.n;v=[0]*(2*n-1)
  for ii in range(n):
   for jj in range(n):v[ii+jj]+=a[ii]*b[jj]
  for k in range(2*n-2,n-1,-1):
   t=v[k]%p
   for j2 in range(n):v[k-n+j2]-=t*self.mod[j2]
  return self.index[tuple(x%p for x in v[:n])]
 def const(self,x):return self.index[(x%self.p,)+(0,)*(self.n-1)]
 def power(self,a,k):
  res=self.one
  while k:
   if k&1:res=self.mul(res,a)
   a=self.mul(a,a);k>>=1
  return res
 def count(self,a,b):
  cuberoot_counts={}
  for y in range(self.q):
   z=self.power(y,3);cuberoot_counts[z]=cuberoot_counts.get(z,0)+1
  N=1
  for x in range(self.q):
   x2=self.power(x,2);x4=self.mul(x2,x2)
   f=self.add(self.add(x4,self.mul(a,x2)),b)
   N+=cuberoot_counts.get(f,0)
  return N

def counts(p,a,b):
 ns=[]
 for n in range(1,4):
  K=GF(p,n)
  ns.append(K.count(K.const(a),K.const(b)))
 return ns

def Lmodp(p,ns):
 # Newton: n a_n = -sum_{k=1}^n a_{n-k} S_k, S_k=q^k+1-N_k
 a=[1]
 for n in range(1,4):
  S=[pow(p,i)+1-ns[i-1] for i in range(1,n+1)]
  nA=-sum(a[n-j]*S[j-1] for j in range(1,n+1))
  assert nA%n==0
  a.append(nA//n)
 return tuple(v%p for v in a)

# Exhaust every smooth coefficient pair over the prime fields.
for p in (11,13):
    fields=[GF(p,n) for n in range(1,4)]
    rows={}
    for a in range(p):
        for b in range(p):
            if b*(a*a-4*b)%p==0: continue
            ns=[K.count(K.const(a),K.const(b)) for K in fields]
            observed=Lmodp(p,ns)
            if p==11:
                c=3*a%p
                d=(-a*b*b*pow((a*a-4*b)%p,2,p))%p
                expected=(1,0,(-c*d)%p,0)
                r=0 if a==0 else 2
            else:
                Delta=(a*a-4*b)%p
                L0=(2*b*b*Delta*Delta*(a*a+5*b))%p
                L1=(5*Delta*Delta)%p
                L2=(6*(a*a+5*b))%p
                expected=(1,-(L0+L1+L2)%p,(L0*L1+L0*L2+L1*L2)%p,-L0*L1*L2%p)
                r=1 if (a*a+5*b)%p==0 else 3
            assert observed==expected,(p,a,b,observed,expected)
            assert max(i for i,x in enumerate(observed) if x%p)==r
            rows[r]=rows.get(r,0)+1
    print('PICARD_PRIME_FIELD_ZETA_PASS',p,rows)
