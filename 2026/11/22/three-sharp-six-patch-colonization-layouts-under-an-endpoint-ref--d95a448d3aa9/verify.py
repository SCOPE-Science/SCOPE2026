"""Self-contained rational algebra and numerical checks for two-arm colonization."""
from fractions import Fraction as F
from math import exp, factorial

checks = 0

def ck(flag, message):
    global checks
    checks += 1
    if not flag:
        raise AssertionError(message)

def poly(*coeff):
    return tuple(F(x) for x in coeff)

def add(a,b):
    return tuple((a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b))))

def neg(a):
    return tuple(-v for v in a)

def sub(a,b):
    return add(a,neg(b))

def mul(a,b):
    res=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            res[i+j]+=x*y
    return tuple(res)

def scalar(a,c):
    return tuple(F(c)*x for x in a)

def eq(a,b):
    n=max(len(a),len(b))
    return all((a[i] if i<len(a) else 0)==(b[i] if i<len(b) else 0) for i in range(n))

one=poly(1)
t=poly(0,1)
a=[scalar(tuple([F(0)]*i+[F(1)]),F(1,factorial(i))) for i in range(7)]
Q=[poly(0)]
for i in range(1,7):
    Q.append(add(Q[-1],a[i-1]))
N=[];D=[]
for m in (1,2):
    n=6-m
    numer=poly(0)
    for j in range(m+1,n):
        numer=add(numer,a[j])
    denom=sub(mul(Q[m+1],Q[n-1]),mul(Q[m],Q[n]))
    N.append(numer);D.append(denom)
ck(eq(N[0],scalar(mul(mul(t,t),poly(12,4,1)),F(1,24))),"A1 polynomial")
ck(eq(D[0],scalar(mul(mul(t,poly(2,1)),poly(4,2,1)),F(1,8))),"B1 polynomial")
ck(eq(N[1],scalar(mul(mul(t,t),t),F(1,6))),"A2 polynomial")
ck(eq(D[1],scalar(mul(mul(t,t),poly(6,4,1)),F(1,12))),"B2 polynomial")
G=sub(mul(N[0],D[1]),mul(N[1],D[0]))
want=scalar(mul(mul(mul(t,t),mul(t,t)),poly(24,24,10,2,1)),F(1,288))
ck(eq(G,want),"strict ordered threshold gap certificate")
ck(all(c>=0 for c in want) and any(c>0 for c in want),"positive coefficient certificate")

# Direct CTMC pure-birth dynamics via independent closed-form Poisson probabilities.
def objective(k,tau,reward):
    p=[exp(-tau)*tau**j/factorial(j) for j in range(7)]
    q=[sum(p[:j]) for j in range(7)]
    occupied=sum(1-q[j] for j in range(1,k+1))+sum(1-q[j] for j in range(1,7-k))
    target=1-q[k]*q[6-k]
    return occupied+reward*target

def thresholds(tau):
    R12=exp(tau)*tau*(tau**2+4*tau+12)/(3*(tau+2)*(tau**2+2*tau+4))
    R23=exp(tau)*2*tau/(tau**2+4*tau+6)
    return R23,R12

for tau in (0.01,0.07,0.2,0.5,1.0,1.3,2.0,4.0,8.0):
    lo,hi=thresholds(tau)
    ck(0<lo<hi,"two distinct positive reward thresholds")
    for reward,winners in ((0,(3,)),(lo/2,(3,)),(lo,(2,3)),((lo+hi)/2,(2,)),(hi,(1,2)),(hi+1,(1,))):
        vals={k:objective(k,tau,reward) for k in (1,2,3)}
        best=max(vals.values())
        ck(all(abs(vals[k]-best)<1e-8*(1+best) for k in winners),"winners meet maximum")
        ck(all(vals[k]<best-1e-8*(1+best) for k in (1,2,3) if k not in winners),"nonwinners excluded")

# At tau=1 and reward 3/5, the strictly intermediate (2,4) geometry wins.
v=[objective(k,1,3/5) for k in (1,2,3)]
ck(v[1]>max(v[0],v[2]),"intermediate optimum at unit time")
print("PASS: exact polynomial identities; positive coefficient gap; numeric complete design tests")
print("Assertions:",checks)
print("At tau=1, reward=0.6: (1,5),(2,4),(3,3) objectives",*[f"{x:.12f}" for x in v])
print("At tau=1: R23,R12=",*[f"{x:.12f}" for x in thresholds(1)])
