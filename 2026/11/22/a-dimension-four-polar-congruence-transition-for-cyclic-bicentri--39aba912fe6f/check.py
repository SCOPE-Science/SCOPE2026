import math
import numpy as np
for n in range(3,13):
 m=n+1
 H=np.eye(m)-np.ones((m,m))/m
 x=np.arange(m)
 q=np.cos(2*np.pi*x/m); s=np.sin(2*np.pi*x/m)
 P=(2/m)*(np.outer(q,q)+np.outer(s,s))
 for t in (.18,.5,.87,1.7,3.2):
  N=math.sqrt((2+(n-2)*t*t)/m); Nr=math.sqrt((2+(n-2)/t**2)/m)
  U=(P+t*(H-P))/N
  Urec=(P+(H-P)/t)/Nr
  normals=-(P+(H-P)/t)/Nr
  assert np.max(np.abs(normals+Urec))<2e-13
  gram=U.T@U
  for j in range(m):
   for i in range(m):
    if i!=j:
     h=1/math.sqrt((2+(n-2)*t*t)*(2+(n-2)/t**2))
     assert abs(gram[i,i]-1)<2e-13
     assert abs(np.dot(normals[:,j],U[:,i])-h)<2e-13
  C=math.sqrt(m)/math.factorial(n)
  V=C*t**(n-2)*(m/(2+(n-2)*t*t))**(n/2)
  W=C*(1/t)**(n-2)*(m/(2+(n-2)/t**2))**(n/2)
  actual=math.sqrt(np.linalg.det((U[:,1:]-U[:,:1]).T@(U[:,1:]-U[:,:1])))/math.factorial(n)
  assert abs(V-actual)<1e-10
  if n==4:
   perm=[(2*i)%5 for i in range(5)]
   assert np.max(np.abs(gram-(Urec[:,perm].T@Urec[:,perm])))<2e-13
   assert abs(V-W)<1e-12
  elif n==3 and t<1: assert V>W
  elif n>=5 and t<1: assert V<W
print('PASS: 10 dimensions x 5 parameters, polar identities, volume determinants, 4D congruence, strict ratios')
