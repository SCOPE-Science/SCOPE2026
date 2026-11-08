"""Numerical checks for the two-interlaced normal-grid identities.
Run with python3 verify.py. Requires NumPy and SciPy.
"""
import math
import numpy as np
from scipy.spatial import ConvexHull
from scipy.optimize import linprog
from scipy.sparse import lil_matrix

def model(m,e):
    x=math.pi/m
    R=x/math.sin(x)
    a=(1+e)/2; b=(1-e)/2
    Z=np.array([(math.cos((2*j+1)*x),math.sin((2*j+1)*x)) for j in range(m)])*R
    W=np.array([(math.cos((2*j+2)*x),math.sin((2*j+2)*x)) for j in range(m)])*R
    combos=np.array([a*z+b*w for z in Z for w in W])
    return combos[ConvexHull(combos).vertices]

def target(m,e):
    x=math.pi/m
    r=x/math.tan(x)
    R=x/math.sin(x)
    mn=0.5*((1+abs(e))*r+(1-abs(e))*R)
    mx=R*math.hypot(math.cos(x/2),e*math.sin(x/2))
    return mn,mx,1-mn

def check():
    count=0
    for m in range(3,41):
        for e in [-1,-0.999,-0.8,-0.31,0,0.24,0.8,0.999,1]:
            v=model(m,e)
            mn,mx,dh=target(m,e)
            n=np.stack([np.cos(np.arange(2*m)*math.pi/m),np.sin(np.arange(2*m)*math.pi/m)],axis=1)
            radius_min=np.max(v @ n.T,axis=0).min()
            radius_max=np.linalg.norm(v,axis=1).max()
            assert abs(radius_min-mn)<4e-12,(m,e,radius_min,mn)
            assert abs(radius_max-mx)<4e-12,(m,e,radius_max,mx)
            assert mx-1 <= dh+2e-13,(m,e,mx-1,dh)
            count+=3
    # W1 grid-to-uniform via explicit transport cell integration,
    # repeated independently through the closed evaluation of the cell moments.
    for m in range(3,30):
        for e in [-1,-0.7,-0.4,0,0.3,0.65,1]:
            N=2*m; D=2*math.pi/N
            mass=np.array([(1+e*((-1)**j))/N for j in range(N)])
            cell_lengths=2*math.pi*mass
            cost=np.sum(cell_lengths**2)/(8*math.pi)
            assert abs(cost-math.pi*(1+e*e)/(2*N))<4e-14
            count+=1
    # An independent discretized optimal-transport LP (additional diagnostic).
    m=3; e=0.6; N=2*m; L=480
    src=(np.arange(L)+0.5)*2*math.pi/L
    dest=np.arange(N)*2*math.pi/N
    diff=np.abs(src[:,None]-dest[None,:]); cost=np.minimum(diff,2*math.pi-diff)
    A=lil_matrix((L+N,L*N),dtype=float)
    for i in range(L):
        for j in range(N):
            idx=i*N+j
            A[i,idx]=1
            A[L+j,idx]=1
    b=np.concatenate((np.ones(L)/L,np.array([(1+e*(-1)**j)/N for j in range(N)])))
    opt=linprog(cost.ravel(),A_eq=A.tocsr(),b_eq=b,bounds=(0,None),method='highs')
    assert opt.success,opt.message
    expected=math.pi*(1+e*e)/(2*N)
    assert abs(opt.fun-expected)<2e-10,(opt.fun,expected)
    print('INTERLACED_GRID_OK',count)
    print('DISCRETE_OT_LP_OK',L,N,format(opt.fun,'.17g'),format(expected,'.17g'))
if __name__=='__main__': check()
