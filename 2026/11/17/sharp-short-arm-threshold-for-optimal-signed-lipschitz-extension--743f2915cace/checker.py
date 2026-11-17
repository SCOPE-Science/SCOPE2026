"""Finite LP checks for an exact signed Lipschitz-extension formula."""
from fractions import Fraction as F
from itertools import product
import numpy as np
from scipy.optimize import linprog

def predicted(m,t):
    t=F(t)
    critical=F(m-2,m)
    if t<critical: return 1+t,[F(0)]*m+[F(1)],'short'
    if t==critical: return 1+t,[F(1,m)]*m+[F(0)],'segment'
    s=F(m)*t-F(m-2)
    s/=2*(F(m)*t+1)
    return F(m)*(1+t)**2/(2*(F(m)*t+1)),[(1-s)/m]*m+[s],'interior'

def lp(m,t):
    a=np.array([1.0]*m+[float(t)]); n=len(a); d=3*n+1
    # w,u,v,T
    A=[]; b=[]
    for j in range(n):
        z=np.zeros(d);z[j]=1;z[n+j]=-1;A.append(z);b.append(0)
        z=np.zeros(d);z[j]=-1;z[n+j]=-1;A.append(z);b.append(0)
        z=np.zeros(d);z[j]=-1;z[2*n+j]=-1;A.append(z);b.append(-1)
        z=np.zeros(d);z[j]=1;z[2*n+j]=-1;A.append(z);b.append(1)
    for j in range(n):
        z=np.zeros(d);z[n:2*n]=a;z[n+j]=0;z[2*n+j]=a[j];z[-1]=-1;A.append(z);b.append(0)
    A=np.array(A);b=np.array(b)
    eq=np.zeros((1,d));eq[0,:n]=1
    c=np.zeros(d);c[-1]=1
    bounds=[(None,None)]*n+[(0,None)]*(2*n+1)
    res=linprog(c,A_ub=A,b_ub=b,A_eq=eq,b_eq=[1],bounds=bounds,method='highs')
    assert res.success,(m,t,res.message)
    return res,np.array(A),b,eq,bounds

def main():
    tested=0
    for m in range(3,10):
        ts={F(1,20),F(1,5),F(1,3),F(1,2),F(2,3),F(3,4),F(9,10),F(1),F(m-2,m),max(F(1,100),F(m-2,m)-F(1,100)),min(F(1),F(m-2,m)+F(1,100))}
        for t in ts:
            val,w,phase=predicted(m,t)
            sol,A,b,eq,bounds=lp(m,t)
            assert abs(sol.fun-float(val))<1e-8,(m,t,sol.fun,val)
            a=[F(1)]*m+[t]
            actual=[sum(a[j]*abs((F(1) if j==i else F(0))-w[j]) for j in range(m+1)) for i in range(m+1)]
            assert max(actual)==val,(m,t,actual,val)
            # optimizer coordinate bounds on the exact optimal face
            A2=np.vstack([A,np.eye(1,3*(m+1)+1,3*(m+1))[0]])
            b2=np.r_[b,float(val)+1e-8]
            if phase!='segment':
                for j in range(m+1):
                    c=np.zeros(A.shape[1]);c[j]=1
                    for sense in [-1,1]:
                        r=linprog(sense*c,A_ub=A2,b_ub=b2,A_eq=eq,b_eq=[1],bounds=bounds)
                        assert r.success
                        assert abs(r.x[j]-float(w[j]))<2e-5,(m,t,phase,j,r.x[j],w[j])
            else:
                # Test exact threshold face endpoints and absence of asymmetric optimizers.
                for j in range(m+1):
                    c=np.zeros(A.shape[1]);c[j]=1
                    goals=(0.0,1.0) if j==m else (0.0,1.0/m)
                    for sense,goal in zip((1,-1),goals):
                        r=linprog(sense*c,A_ub=A2,b_ub=b2,A_eq=eq,b_eq=[1],bounds=bounds)
                        assert r.success and abs(r.x[j]-goal)<2e-5,(m,t,'segment extremum',j,r.x[j],goal)
                for j in range(1,m):
                    c=np.zeros(A.shape[1]);c[0]=1;c[j]=-1
                    for sign in (-1,1):
                        r=linprog(sign*c,A_ub=A2,b_ub=b2,A_eq=eq,b_eq=[1],bounds=bounds)
                        assert r.success and abs(r.x[0]-r.x[j])<2e-5,(m,t,'asymmetry')
            tested+=1
    print('EXACT_FORMULA_VS_SIGNED_LP_PASS profiles=',tested)
    # Independent tree-dual LP on random signed mass vectors: vertex potential constraints.
    for m in (3,4,5):
        n=m+1
        for t in (F(1,5),F(1,2),F(3,4),F(1)):
            a=np.array([1.0]*m+[float(t)])
            # potential values y_j with pairwise constraints |y_i-y_j|<=a_i+a_j; y0=0
            A=[];b=[]
            for i in range(n):
                for j in range(i+1,n):
                    for sign in (-1,1):
                        z=np.zeros(n);z[i]=sign;z[j]=-sign;A.append(z);b.append(a[i]+a[j])
            for w in ([1.4,-.1,-.1]+[(-.2)/(n-3)]*(n-3) if n>3 else [1.4,-.2,-.2],):
                w=np.array(w);w=w/w.sum();mu=np.eye(n)[0]-w
                res=linprog(-mu,A_ub=A,b_ub=b,A_eq=np.eye(1,n,0),b_eq=[0],bounds=[(None,None)]*n,method='highs')
                assert res.success
                kr=sum(a*np.abs(mu))
                assert abs(-res.fun-kr)<1e-8,(m,t,res.fun,kr)
    print('SEPARATE_METRIC_DUAL_VS_TREE_ABSOLUTE_SUM_PASS')
    print('ONE_DEFECT_STAR_OPTIMAL_EXTENSION_ALL_CHECKS_PASS')
if __name__=='__main__':main()
