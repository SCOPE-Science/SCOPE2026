"""Finite exact checks for stationary two-block synchronous noisy-voter identities.

Standard-library only. These confirm finite identities, not asymptotic proof.
"""
from fractions import Fraction as F
from math import comb

checks=0

def test(ok, msg):
    global checks
    assert ok, msg
    checks+=1

def binprob(n, k, p):
    return comb(n,k)*p**k*(1-p)**(n-k)

def row(n, p):
    z=[binprob(n,i,p) for i in range(n+1)]
    test(sum(z)==1, (n,p))
    return z

def matmul(U,V):
    return [[sum(U[i][k]*V[k][j] for k in range(len(V))) for j in range(len(V[0]))] for i in range(len(U))]

def stationary(T):
    n=len(T)
    A=[[T[j][i] - (int(i==j)) for j in range(n)] for i in range(n)]
    A[-1]=[F(1)]*n
    b=[F(0)]*(n-1)+[F(1)]
    for col in range(n):
        pivot=next(i for i in range(col,n) if A[i][col])
        A[col],A[pivot]=A[pivot],A[col]
        b[col],b[pivot]=b[pivot],b[col]
        t=A[col][col]
        A[col]=[x/t for x in A[col]]; b[col]/=t
        for i in range(n):
            if i==col: continue
            t=A[i][col]
            if t:
                A[i]=[x-t*y for x,y in zip(A[i],A[col])]
                b[i]-=t*b[col]
    return b

for a,b in [(2,2),(2,3),(3,2),(3,4),(4,4),(5,3),(3,6)]:
  for eps in [F(1,7),F(1,3),F(2,3)]:
    q=1-eps
    # AB takes an A-count to a B-count; BA reverses it
    AB=[row(b,eps/2+q*F(i,a)) for i in range(a+1)]
    BA=[row(a,eps/2+q*F(j,b)) for j in range(b+1)]
    AA=matmul(AB,BA)
    piA=stationary(AA)
    piB=[sum(piA[i]*AB[i][j] for i in range(a+1)) for j in range(b+1)]
    for i in range(a+1):
        test(sum(piB[k]*BA[k][i] for k in range(b+1))==piA[i], 'marginal A')
    test(sum(piA)==sum(piB)==1,'normalization')
    # Product stationary law of the joint counts, with simultaneous updates.
    for i in range(a+1):
      for j in range(b+1):
        lhs=piA[i]*piB[j]
        rhs=sum(piA[x]*piB[y]*BA[y][i]*AB[x][j]
                for x in range(a+1) for y in range(b+1))
        test(lhs==rhs, ('factorization',a,b,eps,i,j))
    # Both counts are exactly centered and the two side counts uncorrelated.
    test(sum(F(i,a)*piA[i] for i in range(a+1))==F(1,2),'center A')
    test(sum(F(j,b)*piB[j] for j in range(b+1))==F(1,2),'center B')
    # Exact exchangeable pair-spin correlation formula for distinct vertices.
    denom=1-q**4*(1-F(1,a))*(1-F(1,b))
    RA=(q*q/F(b) + q**4*(1-F(1,b))/a)/denom
    RB=(q*q/F(a) + q**4*(1-F(1,a))/b)/denom
    EA2=sum((F(2*i-a,a))**2*piA[i] for i in range(a+1))
    EB2=sum((F(2*j-b,b))**2*piB[j] for j in range(b+1))
    test(EA2==F(1,a)+(1-F(1,a))*RA, ('spin A',a,b,eps))
    test(EB2==F(1,b)+(1-F(1,b))*RB, ('spin B',a,b,eps))
    # Exact two-step mean and variance identities conditional on the A count.
    for i in range(a+1):
        u=F(i,a)
        r=eps/2+q*u
        mu=eps/2+q*r
        m1=sum(F(k,a)*AA[i][k] for k in range(a+1))
        var=sum((F(k,a)-mu)**2*AA[i][k] for k in range(a+1))
        expected_var=mu*(1-mu)/a+q*q*r*(1-r)*(1-F(1,a))/b
        test(m1==mu, ('two-step mean',a,b,eps,i))
        test(var==expected_var, ('two-step var',a,b,eps,i))
# Independently test the entire stationary vertex configuration, not just counts.
from itertools import product
for a,b in [(2,2),(2,3),(3,2),(3,3)]:
  eps=F(2,5); q=1-eps
  AB=[row(b,eps/2+q*F(i,a)) for i in range(a+1)]
  BA=[row(a,eps/2+q*F(j,b)) for j in range(b+1)]
  piA=stationary(matmul(AB,BA))
  piB=[sum(piA[i]*AB[i][j] for i in range(a+1)) for j in range(b+1)]
  configs=list(product((0,1),repeat=a+b))
  weights={s:piA[sum(s[:a])]*piB[sum(s[a:])]/(comb(a,sum(s[:a]))*comb(b,sum(s[a:]))) for s in configs}
  test(sum(weights.values())==1,'full normalization')
  for dst in configs:
    pre=F(0)
    for src in configs:
      pA=eps/2+q*F(sum(src[a:]),b)
      pB=eps/2+q*F(sum(src[:a]),a)
      u=F(1)
      for v in dst[:a]: u*=pA if v else (1-pA)
      for v in dst[a:]: u*=pB if v else (1-pB)
      pre+=weights[src]*u
    test(pre==weights[dst],('full stationarity',a,b,dst))
print('VERIFY_OK',checks,'exact rational assertions')
