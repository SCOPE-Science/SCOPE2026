"""Reproducible numerical checks for a sharp maximum-norm MESOC projection bound.
The proof is analytic; the checks below are not an infinite verification.
"""
import math
import numpy as np
from scipy.optimize import minimize_scalar

def pava_nonincreasing_nonnegative(y):
    blocks = []
    for j, value in enumerate(y):
        blocks.append([float(value), 1, j, j+1])
        while len(blocks)>1 and blocks[-2][0]/blocks[-2][1] < blocks[-1][0]/blocks[-1][1]:
            b=blocks.pop(); a=blocks.pop()
            blocks.append([a[0]+b[0],a[1]+b[1],a[2],b[3]])
    z=np.zeros(len(y))
    for s,n,l,r in blocks:
        z[l:r]=max(0,s/n)
    return z

def project(y,p):
    x=np.asarray(y[:p],float)
    u=np.asarray(y[p:],float)
    r=np.linalg.norm(u)
    z=pava_nonincreasing_nonnegative(np.r_[x,r])
    return np.r_[z[:p], u*z[-1]/r if r>0 else np.zeros_like(u)]

def f_opt(q):
    if q==1:
        return 0.,1.
    fun=lambda a: a*(1+math.sqrt(q-1)*math.sqrt(max(0,1-a*a))-a)
    out=minimize_scalar(lambda a:-fun(a),bounds=(0,1),method='bounded',options={'xatol':1e-14})
    return fun(out.x),out.x

def coefficient(p,q):
    f,a=f_opt(q)
    return max(1.,(1+math.sqrt(q))/2,1+p*f/(p+1)),a

def near_u(p,q,h=1e-8,delta=1e-6):
    L,a=coefficient(p,q)
    n=np.array([a]+[math.sqrt((1-a*a)/(q-1))]*(q-1))
    y=np.r_[np.ones(p)*(1-delta),n]
    E=np.r_[np.ones(p),1.,-np.ones(q-1)]
    return (project(y+h*E,p)[p]-project(y,p)[p])/h

def near_x(p,q,h=1e-8,delta=1e-6):
    n=np.ones(q)/math.sqrt(q)
    x=np.r_[[10.*(p-j) for j in range(1,p)],1-delta]
    y=np.r_[x,n]
    E=np.r_[np.zeros(p-1),1.,np.ones(q)]
    return (project(y+h*E,p)[p-1]-project(y,p)[p-1])/h

if __name__=='__main__':
    rng=np.random.default_rng(120231115)
    checks=0
    for p in [1,2,3,4,7]:
        for q in [1,2,3,4,5,8,12,24]:
            L,a=coefficient(p,q)
            for _ in range(140):
                y=rng.normal(size=p+q)*rng.uniform(.1,10)
                z=rng.normal(size=p+q)*rng.uniform(.1,10)
                py=project(y,p);pz=project(z,p)
                assert np.max(np.abs(py-pz))<=L*np.max(np.abs(y-z))+1e-10
                checks+=1
            if q>=2:
                ul=near_u(p,q)
                assert abs(ul-(1+p*f_opt(q)[0]/(p+1)))<2e-5, (p,q,ul,L)
                checks+=1
            xl=near_x(p,q)
            assert abs(xl-(1+math.sqrt(q))/2)<2e-5,(p,q,xl,L)
            checks+=1
    print('PASS:',checks,'random-pair and near-extremizer assertions')
    for p,q in [(1,2),(2,2),(2,6),(2,10),(2,16),(4,10),(6,24)]:
        L,a=coefficient(p,q)
        print('p,q=',p,q,'L=',format(L,'.12f'),'a_star=',format(a,'.9f'),'axial=',(1+math.sqrt(q))/2,'spatial=',1+p*f_opt(q)[0]/(p+1))
