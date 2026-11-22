import math,itertools
import numpy as np

def predicted(ge,go,s):
 h=(1-ge)/2;d=(1+ge)/2
 q=math.atanh(go)
 v=math.cosh((1-2*s)*q)/math.cosh(q)
 return (-3*h-d-1+v+math.sqrt((d+1-v-3*h)**2+12*h*d))/2

def direct(ge,go,s):
 states=list(itertools.product([-1,1],repeat=3));ix={x:i for i,x in enumerate(states)}
 mat=np.zeros((8,8))
 for j,x in enumerate(states):
  for k in range(3):
   y=x[:k]+(-x[k],)+x[k+1:]
   u=x[(k-1)%3];v=x[(k+1)%3]
   w=(1-x[k]*(ge*(u+v)+go*(u-v))/2)/2
   wrev=(1+x[k]*(ge*(u+v)+go*(u-v))/2)/2
   mat[ix[y],j]+=(w**(1-s))*(wrev**s)
   mat[j,j]-=w
 return max(np.linalg.eigvals(mat).real)
count=0
for ge in (-.7,-.35,0,.2,.6,.95):
 for go in (-.91,-.5,-.08,0,.35,.7,.95):
  for s in (-1,-.3,0,.1,.5,.8,1,1.4,2):
   a=predicted(ge,go,s);b=direct(ge,go,s)
   assert abs(a-b)<1e-11,(ge,go,s,a,b)
   count+=1
print('PASS',count,'independent 8-state tilted generator spectral checks')

for ge in (-0.6, -0.2, 0.4, 0.83):
 for go in (-0.8, -0.3, 0.2, 0.7):
  h=(1-ge)/2; d=(1+ge)/2; p=3*h/(3*h+d);eta=math.atanh(go)
  eps=1e-4
  mean=-(predicted(ge,go,eps)-predicted(ge,go,-eps))/(2*eps)
  variance=(predicted(ge,go,eps)+predicted(ge,go,-eps)-2*predicted(ge,go,0))/eps**2
  truth_mean=2*p*eta*go
  truth_var=4*p*eta**2*(1+2*(1-p)*go**2/(3*h+d))
  assert abs(mean-truth_mean)<1e-6,(ge,go,mean,truth_mean)
  assert abs(variance-truth_var)<2e-6,(ge,go,variance,truth_var)
  for s in (-0.5,0.23,0.5,1.3):
   assert abs(predicted(ge,go,s)-predicted(ge,go,1-s))<1e-12
print('PASS 96 cumulant and fluctuation-symmetry checks')
