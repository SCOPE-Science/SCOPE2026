"""Exact finite modular corroboration of osculating projection-curve critical degrees.
The unrestricted theorem is proved separately via torus weights and Bertini.
Standard library only; the field of all modular calculations is GF(1009).
"""
from math import comb
from random import Random
P=1009

def strip(a):
 while len(a)>1 and a[-1]%P==0:a.pop()
 return a

def add(a,b):
 c=[0]*max(len(a),len(b))
 for i,x in enumerate(a):c[i]=(c[i]+x)%P
 for i,x in enumerate(b):c[i]=(c[i]+x)%P
 return strip(c)

def mul(a,b):
 c=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  if x:
   for j,y in enumerate(b):c[i+j]=(c[i+j]+x*y)%P
 return strip(c)

def remainder(a,b):
 a=strip(a[:]); b=strip(b[:]); inv=pow(b[-1],-1,P)
 while len(a)>=len(b) and a!=[0]:
  m=a[-1]*inv%P; k=len(a)-len(b)
  for j,x in enumerate(b):a[k+j]=(a[k+j]-m*x)%P
  strip(a)
 return a

def gcd(a,b):
 while b!=[0]:a,b=b,remainder(a,b)
 return strip(a)

def M_coeffs(d):
 # e_j=binom(d,j)*s^(d-j)*u^j ; R(t):s->s+t*u, u->-t*s+u
 M=[[None]*(d+1) for _ in range(d+1)]
 for i in range(d+1):
  for j in range(d+1):
   out=[0]*(d+1)
   for a in range(d-j+1):
    b=i-a
    if 0<=b<=j:
     exp=a+j-b
     coeff=comb(d,j)*comb(d-j,a)*comb(j,b)*(-1)**(j-b)
     coeff=coeff*pow(comb(d,i),-1,P)
     out[exp]=(out[exp]+coeff)%P
   M[i][j]=strip(out)
 return M

def negative(a):return [x*(-1 if i%2 else 1)%P for i,x in enumerate(a)]

def trial(d,r,seed):
 M=M_coeffs(d); N=d+1
 rng=Random(seed)
 S=[[0]*N for _ in range(N)]
 for i in range(N):
  for j in range(i,N):S[i][j]=S[j][i]=rng.randrange(P)
 poly=[0]
 for a in range(r):
  for i in range(N):
   for j in range(N):
    poly=add(poly,[(S[j][i]*x)%P for x in mul(M[i][a],negative(M[a][j]))])
 # f(t)=poly/(1+t²)^d, numerator derivative H=(1+t²)poly'-2dt*poly
 deriv=[(i*poly[i])%P for i in range(1,len(poly))] or [0]
 H=add(mul([1,0,1],deriv),mul([0,-2*d%P],poly))
 sep=(gcd(H,[(i*H[i])%P for i in range(1,len(H))] or [0])==[1])
 # gcd could non-unit const -- normalized gcd is not guaranteed monic
 sep=len(gcd(H,[(i*H[i])%P for i in range(1,len(H))] or [0]))==1
 poles=len(gcd(H,[1,0,1]))==1
 return len(H)-1,sep,poles

if __name__=='__main__':
 count=0
 for d in range(2,10):
  for r in range(1,d+1):
   K=sum((-1)**j*comb(d,j) for j in range(r))
   assert K==(-1)**(r-1)*comb(d-1,r-1) and K!=0
   witnesses=[]
   for trial_id in range(8):
    ans=trial(d,r,17113+199*d+17*r+trial_id)
    if ans==(2*d,True,True):
     witnesses.append(trial_id)
     break
   assert witnesses,(d,r,ans)
   count+=1
 print('OSCULATING_ED_MODULAR_WITNESSES_OK',count,'pairs d=2..9, r=1..d, GF(1009)')
 count=0
 for d in range(2,201):
  for r in range(1,d+1):
   v=sum((-1)**j*comb(d,j) for j in range(r))
   assert v==(-1)**(r-1)*comb(d-1,r-1) and v!=0
   count+=1
 print('EXTREME_WEIGHT_BINOMIAL_IDENTITY_OK',count,'pairs d=2..200')
