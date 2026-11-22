import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import spsolve

def check(n,q,a):
 states=q**n
 rows=[]; cols=[]; data=[]
 for s in range(states):
  d=[(s//q**i)%q for i in range(n)];rateout=0.
  for i in range(n):
   new=(d[(i-1)%n]+1)%q
   if new!=d[i]:
    t=s+(new-d[i])*q**i;rows.append(s);cols.append(t);data.append(1.);rateout+=1
   for val in range(q):
    if val!=d[i]:
     t=s+(val-d[i])*q**i; rows.append(s);cols.append(t);data.append(a/q);rateout+=a/q
  rows.append(s);cols.append(s);data.append(-rateout)
 G=coo_matrix((data,(rows,cols)),shape=(states,states)).tocsr(); A=G.T.tolil();A[-1,:]=1.;b=np.zeros(states);b[-1]=1
 p=spsolve(A.tocsc(),b)
 omega=np.exp(2j*np.pi/q);k=np.arccosh(1+a)
 for dist in range(1,n):
  empirical=sum(p[s]*omega**(((s//q**dist)%q)-((s//q**0)%q)) for s in range(states))
  pred=omega**dist*(np.sinh((n-dist)*k)+omega**(-n)*np.sinh(dist*k))/np.sinh(n*k)
  assert abs(empirical-pred)<1e-9,(n,q,a,dist,empirical,pred)
 print('PASS',n,q,a,'all',n-1,'distances',flush=True)
for n,q in [(3,3),(4,3),(5,3),(4,4),(5,4)]:
 check(n,q,0.5)

# Confirm the predicted critical scaling in distinct winding sectors.
for q,r in [(3,0),(3,1),(3,2),(4,1)]:
    n=300+r
    n+=(r-n)%q
    c=2.0
    d=round(0.3*n)
    a=c/n**2
    omega=np.exp(2j*np.pi/q)
    k=np.arccosh(1+a)
    observed=(np.sinh((n-d)*k)+omega**(-n)*np.sinh(d*k))/np.sinh(n*k)
    x=d/n
    h=np.sqrt(2*c)
    limiting=(np.sinh((1-x)*h)+omega**(-r)*np.sinh(x*h))/np.sinh(h)
    assert abs(observed-limiting)<2e-5
    print('PASS winding',q,r,flush=True)
print('CYCLIC_SUCCESSOR_CHECKS_PASSED')
