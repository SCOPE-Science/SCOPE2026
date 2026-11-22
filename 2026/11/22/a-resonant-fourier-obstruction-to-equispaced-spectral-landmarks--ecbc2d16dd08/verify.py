import math

def mat_inv_solve(a,b):
 n=len(a); z=[list(map(float,a[i]))+list(map(float,b[i])) for i in range(n)]
 for i in range(n):
  p=max(range(i,n),key=lambda j:abs(z[j][i])); z[i],z[p]=z[p],z[i]
  d=z[i][i]; assert abs(d)>1e-14
  for k in range(i,2*n):z[i][k]/=d
  for j in range(n):
   if j==i:continue
   d=z[j][i]
   for k in range(i,2*n):z[j][k]-=d*z[i][k]
 return [r[n:] for r in z]

def kernel(d,m,eps):
 z=complex(math.cos(d),math.sin(d))/2
 return 2+2*math.cos(d)+math.cos(m*d)+2*eps*(z*z/(1-z)).real-2*eps*(2**-m)*math.cos(m*d)

def calc(angles,m,eps):
 a=[[kernel(x-y,m,eps) for y in angles] for x in angles]
 b=[[2+2*math.cos(x-y) for y in angles] for x in angles]
 x=mat_inv_solve(a,b)
 return 3-sum(x[i][i] for i in range(m))
for m in (6,8,10,12):
 q=m//2
 for eps in (.001,.01,.05,.1):
  uniform=[2*math.pi*j/m for j in range(m)]
  stagger=[2*math.pi*j/q+r*math.pi/m for r in range(2) for j in range(q)]
  a,b=calc(uniform,m,eps),calc(stagger,m,eps)
  bound=2.5*eps*(1-2**(1-m))
  print(m,eps,'uniform=',round(a,7),'stagger=',round(b,7),'upper=',round(bound,7))
  assert a>=1/3-1e-6, (m,eps,a)
  assert b<=bound+1e-7,(m,eps,b,bound)
  assert a>b
