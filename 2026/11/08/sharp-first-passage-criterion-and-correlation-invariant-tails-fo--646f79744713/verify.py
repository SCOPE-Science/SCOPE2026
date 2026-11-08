"""Standalone arithmetic checks for Markov-modulated Poisson-clock first passage.

All checks use the Python standard library. Finite tests illustrate and test exact
identities used in the analytic theorem; they do not certify infinite limits.
"""
from fractions import Fraction as F
from itertools import product
import math

CHECKS = 0

def check(c, message="verification failed"):
    global CHECKS
    CHECKS += 1
    if not c:
        raise AssertionError(message)

def add(a, b):
    z = dict(a)
    for i, v in b.items():
        z[i] = z.get(i, F(0)) + v
    return {i:v for i,v in z.items() if v}

def scale(a, f):
    return {i:v*f for i,v in a.items() if v*f}

def mul(a, b):
    z = {}
    for i,x in a.items():
        for j,y in b.items():
            z[i+j] = z.get(i+j, F(0)) + x*y
    return {i:v for i,v in z.items() if v}

def pmul(A, B):
    return [[add_many(mul(A[i][k],B[k][j]) for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def add_many(terms):
    z = {}
    for a in terms:
        z = add(z,a)
    return z

def direct_distribution(n, nu, P, emissions):
    # Enumerate state and emission choices independently, conditional on states.
    m = len(P)
    ans = {}
    def step(t, state, total, prob):
        if t == n:
            ans[total] = ans.get(total,F(0)) + prob
            return
        for value, pr in emissions[state]:
            for nxt in range(m):
                step(t+1,nxt,total+value,prob*pr*P[state][nxt])
    for j in range(m):
        step(0,j,0,nu[j])
    return {a:b for a,b in ans.items() if b}

def matrix_distribution(n, nu, P, emissions):
    m=len(P)
    D=[dict((value,prob) for value,prob in emissions[i]) for i in range(m)]
    Q=[[scale(D[i],P[i][j]) for j in range(m)] for i in range(m)]
    v=[{0:x} for x in nu]
    for _ in range(n):
        v=[add_many(mul(v[i],Q[i][j]) for i in range(m)) for j in range(m)]
    return add_many(v)

def evaluate(poly, z):
    return sum((coeff*z**i for i,coeff in poly.items()),F(0))

def solve(A,b):
    n=len(A)
    a=[A[i][:]+[b[i]] for i in range(n)]
    for j in range(n):
        k=next(i for i in range(j,n) if a[i][j])
        a[j],a[k]=a[k],a[j]
        pivot=a[j][j]
        a[j]=[v/pivot for v in a[j]]
        for i in range(n):
            if i!=j:
                v=a[i][j]
                a[i]=[a[i][c]-v*a[j][c] for c in range(n+1)]
    return [a[i][-1] for i in range(n)]

configurations = [
    ([F(1,2),F(1,2)],[[F(3,4),F(1,4)],[F(1,3),F(2,3)]],[[ (1,F(2,3)), (4,F(1,3)) ],[(2,F(1,4)),(3,F(3,4))]]),
    ([F(1,4),F(1,2),F(1,4)],[[F(1,2),F(1,4),F(1,4)],[F(1,5),F(3,5),F(1,5)],[F(1,3),F(1,3),F(1,3)]], [[(1,F(1,2)),(3,F(1,2))],[(2,F(3,4)),(5,F(1,4))],[(1,F(2,5)),(4,F(3,5))]])
]
for nu,P,emissions in configurations:
    for n in range(1,6):
        a=direct_distribution(n,nu,P,emissions)
        b=matrix_distribution(n,nu,P,emissions)
        check(a==b,"matrix-distribution identity")
        check(sum(a.values())==1,"probability normalization")
        for z in [F(1,2),F(1,3),F(2,3),F(3,4)]:
            check(evaluate(a,z)==evaluate(b,z),"Laplace polynomial")
        # Exact fundamental matrix sum of transform powers.
        z=F(1,2)
        D=[sum((p*z**v for v,p in e),F(0)) for e in emissions]
        Q=[[D[i]*P[i][j] for j in range(len(P))] for i in range(len(P))]
        A=[[F(int(i==j))-Q[i][j] for j in range(len(P))] for i in range(len(P))]
        u=solve(A,[F(1)]*len(P))
        full=sum((nu[i]*u[i] for i in range(len(P))),F(0))
        check(full>0,"fundamental matrix positive")
        running=F(0)
        for j in range(n+1):
            running+=evaluate(matrix_distribution(j,nu,P,emissions),z)
        check(running<full,"positive resolvent remainder")

# Check the exact Poissonized simple-walk survival formula at one site.
# For x=1, the embedded walk survives through k steps iff its path never hits 0.
def walk_survival(k, x):
    live={x:1}
    for _ in range(k):
        nxt={}
        for pos,w in live.items():
            if pos+1>0:
                nxt[pos+1]=nxt.get(pos+1,0)+w
            if pos-1>0:
                nxt[pos-1]=nxt.get(pos-1,0)+w
        live=nxt
    return F(sum(live.values()), 2**k)

# Simpson quadrature of the exact spectral formula for the Poissonized walk.
def spectral_survival(u,x):
    num=4000
    acc=0.
    for k in range(num+1):
        th=math.pi*k/num
        if k==0:
            weight=2.*x
        else:
            weight=math.sin(x*th)*math.sin(th)/(1-math.cos(th)) if th<1e-6 else math.sin(x*th)*math.sin(th)/(1-math.cos(th))
        if k==num:
            weight=0.
        coeff=1 if k==0 or k==num else (4 if k%2 else 2)
        acc+=coeff*weight*math.exp(-u*(1-math.cos(th)))
    return acc/(3.*num)

for x in range(1,6):
    for u in [0.2,0.8,2.,4.,8.,16.]:
        terms=[]
        pr=math.exp(-u)
        acc=0.
        for k in range(150):
            acc+=pr*float(walk_survival(k,x))
            pr*=u/(k+1)
        sp=spectral_survival(u,x)
        check(abs(acc-sp)<3e-7,f"Poisson survival vs spectral x={x},u={u}: {acc},{sp}")

# Numerical illustrations of the Perron root first-order perturbation.
def radius2(Q):
    a,b=Q[0];c,d=Q[1]
    return 0.5*((a+d)+math.sqrt((a-d)**2+4*b*c))
P=[[0.82,0.18],[0.27,0.73]]
pi=[0.27/(0.18+0.27),0.18/(0.18+0.27)]
for a1,a2 in [(0.22,0.73),(0.49,0.78),(0.31,0.31)]:
    ratios=[]
    for s in [1.e-4,1.e-6,1.e-8,1.e-10]:
        D=[1/(1+s**a1),1/(1+s**a2)]
        h=sum(pi[i]*(1-D[i]) for i in range(2))
        Q=[[D[i]*P[i][j] for j in range(2)] for i in range(2)]
        r=radius2(Q)
        ratios.append((1-r)/h)
    check(abs(ratios[-1]-1)<0.011,"Perron slope small-s")
    check(abs(ratios[-1]-1)<abs(ratios[0]-1),"Perron slope convergence")

print(f"PASS: {CHECKS} exact-rational and numerical checks")
