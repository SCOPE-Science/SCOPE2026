"""Finite numerical diagnostics for the stated two-hostile-edge opinion-path theorem.
The analytic proof, not these tests, establishes claims for all network sizes.
"""
import numpy as np
from scipy.optimize import root

checks=0
for K in range(3,13):
    m=K-1
    lam=(K+np.sqrt((K-2)**2+4))/2
    critical=1/lam
    M=np.array([[m,1],[1,1]],dtype=float)
    assert abs(max(np.linalg.eigvals(M))-lam)<1e-11
    for alpha_scale in [0.5,1.0,1.01,1.1,1.5,3,10]:
        alpha=alpha_scale*critical
        A=np.ones(m)
        minenergy=[]
        for j in range(m):
            e=np.zeros(m); e[j]=1
            C=np.outer(A,A)+np.outer(e,e)
            H0=np.eye(m)-alpha*C
            assert abs(np.linalg.eigvalsh(H0)[0]-(1-alpha*lam))<1e-10
            if alpha_scale<=1.0:
                assert np.linalg.eigvalsh(H0)[0]>-1e-9
            else:
                assert np.linalg.eigvalsh(H0)[0]<0
                h=np.ones(2)*0.99
                for _ in range(50000):
                    new=np.tanh(alpha*M@h)
                    if np.max(np.abs(new-h))<1e-14:break
                    h=new
                u,v=h
                assert u>1e-5 and v>1e-5
                y=np.ones(m)*u; y[j]=u+v
                S=y.sum()
                assert abs(S-(m*u+v))<1e-11
                assert np.linalg.norm(y-np.tanh(alpha*S)*np.ones(m)-np.tanh(alpha*y[j])*e)<1e-9
                H=np.eye(m)-alpha*(1-np.tanh(alpha*S)**2)*np.outer(A,A)-alpha*(1-np.tanh(alpha*y[j])**2)*np.outer(e,e)
                assert np.linalg.eigvalsh(H)[0]>0
                potential=0.5*(y@y)-np.logaddexp(alpha*S,-alpha*S)/alpha+np.log(2)/alpha-np.logaddexp(alpha*y[j],-alpha*y[j])/alpha+np.log(2)/alpha
                assert potential < -1e-9
                minenergy.append((S,potential,u,v))
            checks+=1
        if minenergy:
            for a,b in zip(minenergy,minenergy[1:]):
                assert np.max(np.abs(np.array(a)-np.array(b)))<1e-9
                checks+=1
    eps=0.00002
    alpha=critical*(1+eps)
    h=np.ones(2)*.01
    for _ in range(100000):
        hnew=np.tanh(alpha*M@h)
        if np.max(np.abs(hnew-h))<1e-14:break
        h=hnew
    t=1/(lam-1)
    u_as=np.sqrt(3*(1+t*t)/(1+t**4))*np.sqrt(eps)
    assert abs(h[0]/u_as-1)<0.012,(K,h[0],u_as)
    assert abs(h[1]/h[0]-t)<0.012
    checks+=2
print('PASS:',checks,'finite numerical checks; no numerical test substitutes for the all-size proof.')
