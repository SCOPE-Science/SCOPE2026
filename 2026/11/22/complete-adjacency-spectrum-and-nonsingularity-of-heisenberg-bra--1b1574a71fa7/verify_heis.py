import numpy as np
import sympy as S
from itertools import product

def direct(n,p):
  G=list(product(range(p),repeat=3));m=len(G)
  I=list(product(range(n),G,range(n)))
  A=np.zeros((len(I),len(I)),dtype=np.float64)
  for a,(i,g,j) in enumerate(I):
    for b,(k,h,l) in enumerate(I[:a]):
      if j==k and l==i:
        # product nonzero both; commute only same diagonal i=j=k=l and g,h commute
        ok=(i==j==k==l and (g[0]*h[1]-h[0]*g[1])%p==0)
      elif j==k or l==i: ok=False
      else: ok=True
      if ok: A[a,b]=A[b,a]=1
  return A

def predict(n,p):
  z=p;s=p*(p-1);t=p+1;m=p**3;d=(n-1)*(n-2)
  Q=S.Matrix([[n*z-1,n*t*s,m*d],[n*z,s-1+(n-1)*t*s,m*d],[(n-2)*z,(n-2)*t*s,(m-1)+m*d]])
  R=S.Matrix([[-1,0,-2*m*(n-2)],[0,s-1-t*s,-2*m*(n-2)],[-z,-t*s,(m-1)-m*(n-2)]])
  x=S.symbols('x');pol=S.expand((x+1)**(n*(n-1)*(m-1)+n*(z-1+t*(s-1)))*(x-(s-1))**(n*(t-1))*(x-(m-1))**(n*(n-3)//2)*(x+m+1)**((n-1)*(n-2)//2)*(x-(m*(n-1)-1))**(n-1)*R.charpoly(x).as_expr()**(n-1)*Q.charpoly(x).as_expr())
  ev=[]
  for root,mult in [(-1,n*(n-1)*(m-1)+n*(z-1+t*(s-1))),(s-1,n*(t-1)),(m-1,n*(n-3)//2),(-m-1,(n-1)*(n-2)//2),(m*(n-1)-1,n-1)]:ev += [root]*mult
  ev+=list(np.linalg.eigvals(np.array(Q).astype(float)))
  ev+=list(np.linalg.eigvals(np.array(R).astype(float)))*(n-1)
  return Q,R,np.sort(np.array(ev)),S.factor(Q.det()),S.factor(R.det())
for n,p in [(3,2),(4,2),(5,2),(3,3),(4,3)]:
 A=direct(n,p);Q,R,ev,dq,dr=predict(n,p)
 obs=np.linalg.eigvalsh(A)
 print('p',p,'n',n,'vertices',len(obs),'expected',len(ev),'maxdiscrep',max(abs(obs-ev)),'detQ',dq,'detR',dr)
 assert len(obs)==len(ev) and max(abs(obs-ev))<1e-7
print('ALL DIRECT COMPARISONS PASS')
q,h=S.symbols('q h',integer=True,positive=True)
n=h+2; z=q; s=q*(q-1);t=q+1;m=q**3;d=(n-1)*(n-2)
Q=S.Matrix([[n*z-1,n*t*s,m*d],[n*z,s-1+(n-1)*t*s,m*d],[(n-2)*z,(n-2)*t*s,m-1+m*d]])
R=S.Matrix([[-1,0,-2*m*(n-2)],[0,s-1-t*s,-2*m*(n-2)],[-z,-t*s,m-1-m*(n-2)]])
C=2*q**4-q**3+q**2-1
D=3*q**4-q**3+q**2-q-1
E=q**3-q**2+1
assert S.expand(Q.det()+(q-1)*(q**2+q+1)*C+h*q**3*D+h**2*q**3*C)==0
assert S.expand(R.det()-(q-1)*(q**2+q+1)*E-h*q**3*C)==0
print('SYMBOLIC DETERMINANT IDENTITIES PASS')
