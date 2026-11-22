from fractions import Fraction
import json,sys
import numpy as np
from numpy.polynomial.legendre import leggauss
from verify import BASE_VERTICES

base=np.array(BASE_VERTICES,float)
t,w=leggauss(16);t=(t+1)/2;w=w/2

def pts(V):
 p=[];wt=[]
 for j in range(6):
  a,b=V[j],V[(j+1)%6];det=np.linalg.det(np.stack((a,b)))
  for i,si in enumerate(t):
   zi=t*(1-si)
   p.append(si*a[None,:]+zi[:,None]*b[None,:])
   wt.extend(w[i]*w*(1-si)*det)
 return np.concatenate(p),np.array(wt)

def E(V,k):
 pp,ww=pts(V)
 J=0
 for i in range(0,len(pp),128):
  diff=pp[i:i+128,None,:]-pp[None,:,:]
  d2=diff[:,:,0]**2+3*diff[:,:,1]**2
  J+=np.sum(d2**(k//2)*(ww[i:i+128,None]*ww[None,:]))
 return J/(sum(ww)**((k+4)//2))
cert=json.load(open('certificate.json'))
for k in (8,16,24):
 d=next(x for x in cert['certificates'] if x['exponent']==k)
 A=6;B=(k+4)//2
 J=float(Fraction(d['energy_numerator']));E0=J/A**B
 q=E(base,k);print(k,'E0',E0,'gauss',q,'relerror',abs(E0-q)/E0)
 eps=0.002
 plus=base.copy();minus=base.copy();plus[1,0]+=eps;minus[1,0]-=eps
 fd=(E(plus,k)+E(minus,k)-2*q)/(eps*eps)
 theo=float(Fraction(d['hessian_K'][0][0]))/(A**(B+2))
 print('num second deriv',fd,'exact',theo,'relative error',abs(theo-fd)/theo)
