import numpy as np
from math import sin,cos,pi,sqrt
n=5; th=2*pi/n;s=sin(th)
z=np.array([[cos(i*th),sin(i*th)] for i in range(n)])
star=25*s*s/24

def V(t,dir):
 a=np.zeros((n,4));b=np.zeros((n,4));
 for i in range(n):
  a[i,:2]=z[i]+t*dir[i,0]*np.array([-z[i,1],z[i,0]])
  a[i,2:]=t*dir[i,1:3]
  a[i]/=np.linalg.norm(a[i])
  b[i,:2]=t*dir[i,4:6]
  b[i,2:]=z[i]+t*dir[i,3]*np.array([-z[i,1],z[i,0]])
  b[i]/=np.linalg.norm(b[i])
 mats=np.stack([np.stack([a[i],a[(i+1)%5],b[j],b[(j+1)%5]],axis=1) for i in range(5) for j in range(5)])
 return np.linalg.det(mats).sum()/24
h=0.0015
basis=np.eye(30).reshape(30,5,6)
Q=np.zeros(30)
for k in range(30):Q[k]=(2*star-V(h,basis[k])-V(-h,basis[k]))/(2*h*h)
H=np.zeros((30,30))
for k in range(30):
 H[k,k]=2*Q[k]
 for j in range(k):
  b=basis[k]+basis[j]
  q=(2*star-V(h,b)-V(-h,b))/(2*h*h)
  H[k,j]=H[j,k]=q-Q[k]-Q[j]
eig=np.linalg.eigvalsh(H)
root5=sqrt(5)
expected=np.array([0]*6+[25/96]*4+[(25+5*root5)/96]*12+[25*(3+root5)/192]*4+[(25+5*root5)/48]*4)
print('numeric eigenvalues:',np.round(eig,8))
print('exact eigenvalues:',np.round(expected,8))
print('max error:',np.max(np.abs(eig-expected)))
assert np.max(np.abs(eig-expected))<4e-5
