import sympy as s
A,B,U,V,W,M,N=s.symbols('a b alpha beta gamma mu nu')
r2=s.Rational(1,2);r3=s.Rational(1,3);r6=s.Rational(1,6)
cols=[
{0:A,2:A*U,7:M},
{0:(A-B)*r3,1:B,2:V,3:-U*B,4:W,5:U**2*B*r2,6:-U*W-U**3*B*r6,7:N},
{2:A*B},
{3:B**2,4:B*(V+U*(B-A)*r3),5:-U*B**2,6:A*U**2*B*r3-U*B*V+B*W+U**2*B**2*r6,7:-A*U**3*B*r6-A*U*W+U**2*B*V*r2+3*V*W},
{4:A*B**2,6:-U*A*B**2,7:3*A*B*W+A*B**2*U**2*r2},
{4:(A*B**2-B**3)*r3,5:B**3,6:2*B**2*V-U*A*B**2,7:-2*A*B*U*V+A*B*W+A*B**2*U**2*r6+A**2*B*U**2*r3+3*B*V**2},
{6:A*B**3,7:3*A*B**2*V-U*A**2*B**2},
{7:A**2*B**3}
]
C=s.zeros(8,8)
for j,col in enumerate(cols):
 for i,v in col.items(): C[i,j]=v
pairs = {(0,1):[(2,-1)],(1,0):[(2,1)],(1,1):[(3,1)],(1,2):[(4,1)],(3,0):[(4,1)],(3,1):[(5,1)],(3,2):[(6,1)],(4,1):[(6,1)],(5,0):[(6,2)],(5,1):[(6,1)],(4,2):[(7,3)],(5,2):[(7,1)],(6,0):[(7,3)],(6,1):[(7,1)]}
def prod(x,y):
 z=s.zeros(8,1)
 for (i,j),out in pairs.items():
  for k,c in out:z[k] += c*x[i]*y[j]
 return z
for i in range(8):
 for j in range(8):
  v=prod(C[:,i],C[:,j]) - C*prod(s.eye(8)[:,i],s.eye(8)[:,j])
  for e in v:
   t=s.cancel(e)
   assert t==0, (i,j,t)
print('SYMBOLIC_OK all 64 basis-pair multiplication identities over Q(a,b,alpha,beta,gamma,mu,nu)')
