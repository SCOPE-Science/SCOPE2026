import math, sys
sys.path.insert(0, "/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-1241/output/artifacts")
from kasteleyn import logZ
def logK(n,x,y):
    E=(n*n+1)//2; O=n*n-E
    lD1=E*math.log(2*x*x)+O*math.log(2*y*y)
    p,q=1/(2*x),1/(2*y)
    lD2=(n-1)*(n-1)*math.log(2*p*q)
    X,Y=2*x*y*y/(x*x+y*y), 2*x*x*y/(x*x+y*y)
    m=n-2
    E2=(m*m+1)//2; O2=m*m-E2
    lD3=E2*math.log(2*X*X)+O2*math.log(2*Y*Y)
    P,Q=1/(2*X),1/(2*Y)
    lD4=(m-1)*(m-1)*math.log(2*P*Q)
    lam=4*x*x*y*y/(x*x+y*y)**2
    lg=(n-4)*(n-3)*math.log(lam)
    return lD1+lD2+lD3+lD4+lg
ok=True
for a in [0.3,0.5,0.7]:
    for n in [4,5,6,7,8]:
        pred=logK(n,a,1.0); act=logZ(n,a)-logZ(n-4,a)
        e=abs(pred-act); ok &= e<1e-9
        print(f"a={a} n={n} err={e:.2e}")
print("ALL OK" if ok else "MISMATCH")
