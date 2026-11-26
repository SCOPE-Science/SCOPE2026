from math import sqrt

def w(theta,x):
 k=(1-theta/2)/sqrt(2)
 return (1-k/sqrt(k*k+theta*(1-x)))/theta

def g(theta,x):
 k=(1-theta/2)/sqrt(2)
 u=(sqrt(k*k+theta*(1-x))-k)/theta
 return .5-u*u,.5+u*u

def f(theta,y):
 k=(1-theta/2)/sqrt(2)
 return 1-theta*abs(y-.5)-2*k*sqrt(abs(y-.5))

def U(s):
 return 1-1/sqrt(1+2*s)

def V(s,n=65):
 return sum(2**(-j)*U(s/(2**j)) for j in range(1,n+1))

for theta in (1.2,1.5,1.8,1.95,1.99):
 k=(1-theta/2)/sqrt(2)
 for x in (0.,.01,.24,.55,.91,1.):
  a,b=g(theta,x)
  assert abs(f(theta,a)-x)<1e-12
  assert abs(f(theta,b)-x)<1e-12
  assert 0<=w(theta,x)<1
 assert abs(w(theta,0)-1/(1+theta/2))<1e-12
 assert w(theta,1)==0
for s in (0.,.1,.5,1.,3.,9.):
 v=V(s)
 assert abs(v-(V(s/2)+U(s/2))/2)<1e-13
 assert abs(V(s,15)-v)<2**(-15)
assert abs(sum(4**(-j) for j in range(1,51))-1/3)<1e-15
print('CHECKS_PASS: exact inverse branch, endpoints, bounded profile recursion and slope geometric sum')
