"""Independent discretized-generator and asymptotic checks for blinking-target reset counts."""
import numpy as np
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve

def theorem(z, alpha, beta, r, x0, D):
    lam=alpha+beta
    T=r+lam
    q=np.sqrt(r/T)
    h=np.exp(-x0*np.sqrt(r/D))
    k=np.exp(-x0*np.sqrt(T/D))
    t=alpha/beta
    L=h*z*(T-r*z)+(1-z)*((T-r*z)+t*q*(T-r*z+r*z*k))
    return np.array([(h*(T-r*z)+t*q*T*k*(1-z))/L,
                     (h*(T-r*z)-q*T*k*(1-z))/L])

def discretized(z, alpha, beta, r, x0, D, dx=0.04, radius=9):
    m=int(round(radius/dx)); x_index=int(round(x0/dx)); dx=radius/m
    X=2*m+1; n=2*X; C=D/dx**2
    M=lil_matrix((n,n)); rhs=np.zeros(n)
    idx=lambda state,i: state*X+i
    for state in (0,1):
      rate=alpha if state==0 else beta
      for i in range(X):
        row=idx(state,i)
        if state==0 and i==m:
            M[row,row]=1;rhs[row]=1;continue
        M[row,row]=r+rate
        M[row,idx(1-state,i)]-=rate
        M[row,idx(state,m+x_index)]-=r*z
        if i==0:
            M[row,row]+=2*C;M[row,idx(state,1)]-=2*C
        elif i==X-1:
            M[row,row]+=2*C;M[row,idx(state,i-1)]-=2*C
        else:
            M[row,row]+=2*C
            M[row,idx(state,i-1)]-=C
            M[row,idx(state,i+1)]-=C
    u=spsolve(M.tocsc(),rhs)
    return np.array([u[idx(0,m+x_index)],u[idx(1,m+x_index)]])

if __name__=='__main__':
    comparisons=[]
    for par in [(0.7,1.4,1.,1.,1.),(2.,0.3,0.7,1.0,1.),(0.2,1.,1.3,1.,1.)]:
        alpha,beta,r,x0,D=par
        for z in (0.,0.25,0.6,0.92):
            exact=theorem(z,*par)
            check=discretized(z,*par)
            err=float(np.max(np.abs(exact-check)))
            comparisons.append(err)
            print('parameters',par,'z',z,'PGF',exact.tolist(), 'discretized',check.tolist(),'error',err)
    assert max(comparisons)<0.010
    for alpha,beta,r,x0,D in [(0.7,1.4,1.,1.,1.),(3.,0.1,0.8,1.,1.),(0.1,5.,4.0,1.,1.)]:
        lam=alpha+beta;T=r+lam;q=np.sqrt(r/T);h=np.exp(-x0*np.sqrt(r/D));k=np.exp(-x0*np.sqrt(T/D));t=alpha/beta
        c0=T*(1+t*q)
        c1=T*(1+t*q-h)+r*(1+t*q*(1-k))
        c2=r*(1+t*q*(1-k)-h)
        delta=c1*c1-4*c0*c2
        target=(T*(1+t*q-h-(r/T)*(1+t*q*(1-k))))**2+4*T*T*t*q**3*h*k
        assert abs(delta-target) <=1e-10 * max(1,abs(delta))
        roots=np.array([(c1+np.sqrt(delta))/(2*c0),(c1-np.sqrt(delta))/(2*c0)])
        assert 0<roots[1]<roots[0]<1
        print('positive spectral modes:',roots.tolist(),'discriminant',delta)
    # Geometric active limit, and inactive slow-gating rescaled law.
    for scale in (0.1,0.01,0.001):
        r=1.3;x0=0.8;D=0.9;alpha=2*scale;beta=scale
        h=np.exp(-x0*np.sqrt(r/D));z=0.7
        act=theorem(z,alpha,beta,r,x0,D)[0]
        print('slow gate active to geometric',scale,act, h/(1-(1-h)*z))
        for s in (0.5,2.0):
            inactive=theorem(np.exp(-s*beta/r),alpha,beta,r,x0,D)[1]
            print('slow gate inactive Exp(1)',scale,s,inactive,1/(1+s))
    for scale in (10.,100.,1000.):
        alpha=2*scale;beta=scale;r=0.9;x0=1.0;D=1.0;z=0.6
        h=np.exp(-x0*np.sqrt(r/D));print('fast gate',scale,theorem(z,alpha,beta,r,x0,D),h/(1-(1-h)*z))
