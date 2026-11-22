"""Exact finite checks for the complete-tripartite Kemeny optimizer.
Run: python check.py (Python standard library only).
Universal optimality is established by analytical KKT inequalities in RESULT.md;
finite tests are regression checks, not substitutes for that proof.
"""
from fractions import Fraction as F
from itertools import product

def optimal(a,b,c):
    assert 1 <= a <= b <= c
    X=max(F(0),F(a+b-c,2))
    return (X,F(b)-X,F(a)-X)

def score_gradient(a,b,c,x):
    X,Y,Z=x
    N=a+b+c
    QA=X*Y+Y*Z+Z*X
    S=(X+Z)/a+(X+Y)/b+(Y+Z)/c
    C=F(a*b*c,N)
    V=F(a*(a-1),1)/(X+Z)+F(b*(b-1),1)/(X+Y)+F(c*(c-1),1)/(Y+Z)+C*S/QA
    gX=F(a*(a-1),1)/(X+Z)**2+F(b*(b-1),1)/(X+Y)**2+C*(S*(Y+Z)/QA**2-(F(1,a)+F(1,b))/QA)
    gY=F(b*(b-1),1)/(X+Y)**2+F(c*(c-1),1)/(Y+Z)**2+C*(S*(X+Z)/QA**2-(F(1,b)+F(1,c))/QA)
    gZ=F(a*(a-1),1)/(X+Z)**2+F(c*(c-1),1)/(Y+Z)**2+C*(S*(X+Y)/QA**2-(F(1,a)+F(1,c))/QA)
    return V,(gX,gY,gZ)

def inv(M):
    n=len(M)
    A=[[F(v) for v in r]+[F(i==j) for j in range(n)] for i,r in enumerate(M)]
    for i in range(n):
        j=next(k for k in range(i,n) if A[k][i])
        A[i],A[j]=A[j],A[i]
        p=A[i][i]
        A[i]=[v/p for v in A[i]]
        for j in range(n):
            if j!=i:
                q=A[j][i]
                A[j]=[x-q*y for x,y in zip(A[j],A[i])]
    return [r[n:] for r in A]

def full_score(a,b,c, x):
    X,Y,Z=x; N=a+b+c
    A=range(0,a);B=range(a,a+b);C=range(a+b,N)
    P=[[F(0) for _ in range(N)] for _ in range(N)]
    for U,V,w in [(A,B,X/F(a*b)),(B,C,Y/F(b*c)),(C,A,Z/F(a*c))]:
        for i in U:
            for j in V:P[i][j]=P[j][i]=w
    for i in range(N):P[i][i]=1-sum(P[i])
    assert all(v>=0 for row in P for v in row)
    M=[[F(i==j)-P[i][j]+F(1,N) for j in range(N)] for i in range(N)]
    W=inv(M)
    return sum(W[i][i] for i in range(N))-1

checks=0
for a in range(1,19):
 for b in range(a,19):
  for c in range(b,19):
    X,Y,Z=x=optimal(a,b,c)
    assert X>=0 and Y>0 and Z>0 and X+Z<=a and X+Y<=b and Y+Z<=c
    V,(gX,gY,gZ)=score_gradient(a,b,c,x)
    if c<a+b:
        ua=(gX+gZ-gY)/2;ub=(gX+gY-gZ)/2;uc=(gY+gZ-gX)/2
        assert ua>0 and ub>0 and uc>0
        assert X+Z==a and X+Y==b and Y+Z==c
        Q=X*Y+Y*Z+Z*X
        assert ua==1-F(1,a)+F(b*c,(a+b+c))* (3*a*Y-Q)/Q**2
    else:
        assert X==0 and Y==b and Z==a
        assert gX==2 and gY==gZ and gY>1
    checks+=7
for a,b,c in product(range(1,4),repeat=3):
    if not a<=b<=c or a+b+c>8:continue
    x=optimal(a,b,c)
    v,_=score_gradient(a,b,c,x)
    assert v==full_score(a,b,c,x), (a,b,c,v,full_score(a,b,c,x))
    checks+=1
print('PASS:',checks,'exact-rational checks; triangle, boundary, and asymmetric-size regimes')
