from fractions import Fraction as F
from itertools import combinations,product
from scipy.optimize import linprog
import numpy as np

def formula(n,a,b,s):
    a,b,s=map(F,(a,b,s))
    assert min(a,b,s)>0 and abs(a-b)<=min(F(1),s) and F(1)<=min(a+b,2*b) and s<=min(a+b,2*b)
    D=(n-1)*b+a
    theta=F((n-1))*(b-a)/D
    if theta< -F(1,n-1): theta=-F(1,n-1)
    return max(F(1),F(n-1)/D if a<=F(n-1,n-2)*b else F(n-2,(n-1)*b)),theta

def verify(n,a,b,s):
    a,b,s=map(F,(a,b,s))
    lam,theta=formula(n,a,b,s)
    # full unrestricted LP variables T[y_i,x_j] for n^2, t; impose constants preserved
    N=n*n+1;t=N-1;M=2*n
    rows=[]; rhs=[]
    for u,v in combinations(range(M),2):
        d=(F(1) if u<n and v<n else s if u>=n and v>=n else a if u%n==v%n else b)
        for mask in range(1,1<<n):
            z=np.array([(mask>>j)&1 for j in range(n)],float)
            row=np.zeros(N)
            for node,sgn in [(u,1),(v,-1)]:
                if node<n: pass
                else: row[(node-n)*n:(node-n+1)*n]+=sgn*z
            src=(z[u] if u<n else 0)-(z[v] if v<n else 0)
            for sign in (1,-1):
                rr=sign*row; rr[t]=-float(d)
                rows.append(rr);rhs.append(-sign*src)
    Aeq=np.zeros((n,N));
    for j in range(n):Aeq[j,j*n:(j+1)*n]=1
    c=np.zeros(N);c[t]=1
    sol=linprog(c,A_ub=np.array(rows),b_ub=np.array(rhs),A_eq=Aeq,b_eq=np.ones(n),bounds=[(None,None)]*(N-1)+[(0,None)],method='highs')
    assert sol.success,sol.message
    assert abs(sol.x[t]-float(lam))<2e-8,(n,a,b,s,sol.x[t],lam)
    # exact candidate pair norm via binary values and rational coefficients
    T=[[theta*(i==j)+(1-theta)/n for j in range(n)] for i in range(n)]
    worst=F(0)
    for u,v in combinations(range(2*n),2):
        d=F(1) if u<n and v<n else F(s) if u>=n and v>=n else F(a) if u%n==v%n else F(b)
        coeff=[(F(int(u==j)) if u<n else T[u-n][j])-(F(int(v==j)) if v<n else T[v-n][j]) for j in range(n)]
        assert sum(coeff)==0
        q=sum(abs(x) for x in coeff)/2/d
        if q>worst:worst=q
    assert worst==lam, (worst,lam)
    return float(lam),str(theta)

cases=[(3,'3/5','4/5','1'),(4,'3/5','13/20','1'),(4,'11/10','13/20','1'),(5,'11/10','13/20','1'),(5,'7/10','7/10','1/10'),(7,'3/5','3/5','1/10'),(3,'1','1/2','1'),(6,'1','3/5','1/2'),(4,'9/10','1/2','1/2'),(8,'3/5','3/5','6/5'),(4,'3/5','13/20','1/20'),(4,'3/5','13/20','6/5'),(4,'11/10','13/20','9/20'),(4,'11/10','13/20','13/10')]
for n,a,b,s in cases:
 try: print('PASS',n,a,b,s,verify(n,a,b,s))
 except Exception as e:print('FAIL',n,a,b,s,str(e));raise
print('TWINNED_METRIC_EXTENSION_EXACT_OK',len(cases))
