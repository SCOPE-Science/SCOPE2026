"""Exact identities and independent finite-dimensional Gram checks for quadratic spherical block caps."""
from math import comb
import sympy as sp
import mpmath as mp
import numpy as np
from scipy.linalg import eigh

def symbolic_check():
 a,b,x=sp.symbols('a b x', positive=True)
 s=a+b; m=a/s; v=a*b/(s*s*(s+1))
 w={
  'R':(x-m)**2/v,
  'U':x*x*s*(s+1)/(a*(a+1)),
  'C':x*(1-x)*s*(s+1)/(a*b),
  'V':(1-x)**2*s*(s+1)/(b*(b+1))
 }
 for n,k,troot in [('R','U',(a+1)/s),('R','C',a/s),('R','V',(a-1)/s),('U','C',0),('C','V',1)]:
  H=sp.cancel(w[n]-w[k]);A=sp.factor(H.subs(x,0)/a)
  B=sp.factor(-sp.Poly(H,x).coeff_monomial(x*x)/(s+1))
  assert sp.simplify(H- (a*A+((a+1)*B-s*A)*x-(s+1)*B*x*x))==0
  assert sp.simplify(-A/B-troot)==0
 print('EXACT_SYMBOLIC_FIVE_PAIRWISE_BETA_GAPS_PASS')

def betatail(a,b,t):
 return mp.betainc(a,b,t,1,regularized=True)

def predicted(p,q,t):
 a=mp.mpf(p)/2;b=mp.mpf(q)/2;s=a+b;m=a/s
 u=betatail(a+2,b,t)
 c=betatail(a+1,b+1,t)
 v=betatail(a,b+2,t)
 z=mp.betainc(a,b,t,1,regularized=False)/mp.beta(a,b)
 z1=(a/s)*betatail(a+1,b,t)
 z2=(a*(a+1)/(s*(s+1)))*betatail(a+2,b,t)
 r=(z2-2*m*z1+m*m*z)/(a*b/(s*s*(s+1)))
 return [r,u,c,v]

def direct_gram(p,q,t):
 mp.mp.dps=60
 d=p+q
 a=mp.mpf(p)/2;b=mp.mpf(q)/2
 # Independent conditional fourth-order angular-moment integration.
 tau2=mp.quad(lambda w:w**(a+1)*(1-w)**(b-1),[t,1])/mp.beta(a,b)
 eta2=mp.quad(lambda w:w**(a-1)*(1-w)**(b+1),[t,1])/mp.beta(a,b)
 mix=mp.quad(lambda w:w**a*(1-w)**b,[t,1])/mp.beta(a,b)
 def mm(i,j):
  if i<p and j<p:return float(tau2*(3 if i==j else 1)/(p*(p+2)))
  if i>=p and j>=p:return float(eta2*(3 if i==j else 1)/(q*(q+2)))
  return float(mix/(p*q))
 def build_weight(tlocal):
  pass
 # h_i=x_i^2-x_(d-1)^2, h_ij=x_i x_j.
 K=(d-1)+comb(d,2)
 mat=np.zeros((K,K))
 for i in range(d-1):
  for j in range(d-1):mat[i,j]=mm(i,j)-mm(i,d-1)-mm(d-1,j)+mm(d-1,d-1)
 for j,(i,k) in enumerate((i,k) for i in range(d) for k in range(i+1,d)):
  mat[d-1+j,d-1+j]=mm(i,k)
 return mat

def expected_matrix(p,q,t):
 d=p+q
 M=direct_gram(p,q,t)
 M0=direct_gram(p,q,0)
 vals=np.sort(eigh(M,M0,eigvals_only=True))
 pred=predicted(p,q,mp.mpf(str(t)))
 multiplicities=[1,p*(p+1)//2-1,p*q,q*(q+1)//2-1]
 expect=np.sort(np.concatenate([np.full(k,float(v)) for k,v in zip(multiplicities,pred)]))
 err=max(abs(vals-expect))
 assert err<1e-9,(p,q,t,err)
 assert all(-1e-9<=v<=1+1e-9 for v in vals)
 return err

def main():
 symbolic_check()
 maximum=0;cases=0
 for p,q in [(2,2),(2,4),(3,4),(4,3),(3,5),(4,4)]:
  for t in [0.16,0.36,0.71]:
   err=expected_matrix(p,q,t)
   maximum=max(maximum,err);cases+=1
 print('INDEPENDENT_CONDITIONAL_FOURTH_MOMENT_GRAM_PASS',cases,'cases','max_abs_error=',maximum)
 for p,q in [(3,4),(4,3),(4,4),(5,3),(2,4),(4,2)]:
  a=mp.mpf(p)/2;b=mp.mpf(q)/2;s=a+b
  for t in [mp.mpf('0.01'),mp.mpf('0.24'),mp.mpf('0.61'),mp.mpf('0.93')]:
   r,u,c,v=predicted(p,q,t)
   assert u>c>v
   assert mp.sign(r-u)==mp.sign(t-(a+1)/s)
   assert mp.sign(r-c)==mp.sign(t-a/s)
   assert mp.sign(r-v)==mp.sign(t-(a-1)/s)
  eps=mp.mpf('0.0000001');r,u,c,v=predicted(p,q,1-eps)
  k=max(r,u,c,v)/min(r,u,c,v)
  const=b*(b+1)*(b+2)/(a*s)
  assert abs(k*eps**2/const-1)<mp.mpf('0.000002')
 print('EXTREMAL_TRANSITIONS_AND_SHARP_THIN_CAP_PASS')
if __name__=='__main__': main()
