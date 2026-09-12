import math
from kasteleyn import logZ
def logK(n,x,y):
    E=(n*n+1)//2; O=n*n-E
    lD1=E*math.log(2*x*x)+O*math.log(2*y*y)          # shuffle 1: uniform faces
    p,q=1/(2*x),1/(2*y)
    lD2=(n-1)*(n-1)*math.log(p*p+q*q)                # shuffle 2: cross faces, Delta=p^2+q^2
    X,Y=2*x*y*y/(x*x+y*y), 2*x*x*y/(x*x+y*y)
    m=n-2
    E2=(m*m+1)//2; O2=m*m-E2
    lD3=E2*math.log(2*X*X)+O2*math.log(2*Y*Y)
    P,Q=1/(2*X),1/(2*Y)
    lD4=(m-1)*(m-1)*math.log(P*P+Q*Q)
    lam=4*x*x*y*y/(x*x+y*y)**2
    lg=(n-4)*(n-3)*math.log(lam)
    return lD1+lD2+lD3+lD4+lg
lz={a:{n:logZ(n,a) for n in range(0,13)} for a in [0.2,0.3,0.5,0.7,0.9,1.3]}
ok=True
for a in lz:
    for n in range(4,13):
        e=abs(logK(n,a,1.0)-(lz[a][n]-lz[a][n-4])); ok&=e<1e-9
        print(f"a={a} n={n} err={e:.2e}")
print("ALL OK" if ok else "MISMATCH")
