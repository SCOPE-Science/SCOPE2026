from collections import Counter
from math import gcd

def theor(p,k):
    q=p**k;N=q-q//p
    r=Counter({N:1})
    for j in range(1,k):
        nj=p**(k-j-1)*(p-1)
        r[2*p**j]+=nj*nj//2
    r[2]+=N*((p-3)//2)*p**(k-1)
    for v in range(1,(k-1)//2+1):
        r[2*p**v]+=N*(p-1)*p**(k-2*v-1)//2
    r[p**(k//2)]+=N
    return {m:c for m,c in sorted(r.items()) if c>0}

def check(p,k):
 q=p**k; U=[x for x in range(q) if x%p]; inv={x:pow(x,-1,q) for x in U}; r=Counter(((x+y)%q,(inv[x]+inv[y])%q) for x in U for y in U)
 obs=Counter(r.values());pred=theor(p,k)
 E=sum(v*v for v in r.values());N=len(U)
 m=(k-1)//2
 E2=(2*k-1)*N*N + N*(2*(p-3+(p-1)*m)*p**(k-1)+p**(2*(k//2)))
 assert dict(sorted(obs.items()))==pred,(p,k,obs,pred)
 assert E==E2,(p,k,E,E2)
 assert sum(cnt*mult for mult,cnt in pred.items())==N*N
 print('PASS',p,k,'N',N,'sumset',len(r),'levels',pred,'energy',E)
for p,k in [(3,1),(3,2),(3,3),(3,4),(5,1),(5,2),(5,3),(7,1),(7,2),(11,1),(11,2)]: check(p,k)
if __name__=='__main__':
 import cmath, math
 for q in (3,5,9,15,25,27):
  U=[u for u in range(q) if gcd(u,q)==1]
  kk=lambda a,b:sum(cmath.exp(2j*math.pi*((a*u+b*pow(u,-1,q))%q)/q) for u in U)
  m4=sum(abs(kk(a,b))**4 for a in range(q) for b in range(q))
  m2=sum(abs(kk(a,b))**2 for a in range(q) for b in range(q))
  rr=Counter(((u+v)%q,(pow(u,-1,q)+pow(v,-1,q))%q) for u in U for v in U)
  E=sum(x*x for x in rr.values())
  assert abs(m4/(q*q)-E)<1e-6*max(1,E)
  assert abs(m2/(q*q)-len(U))<1e-6*max(1,len(U))
  print('FOURIER_PASS',q,'E',E,'M4',round(m4),'M2',round(m2))
