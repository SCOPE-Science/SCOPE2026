"""Independent numerical and symbolic checks for a two-state Robin-gated absorber.
Requires numpy, scipy and sympy. The exact theorem is proved separately.
"""
import math
import numpy as np
import sympy as sp
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve

def exact(D,L,r,alpha,beta,kappa):
    g=alpha+beta
    mu=math.sqrt(r/D); nu=math.sqrt((r+g)/D)
    fresh=(math.expm1(mu*L)/r+math.exp(mu*L)*(beta/(alpha*math.sqrt(r*(r+g)))+g*math.sqrt(D/r)/(alpha*kappa)))
    gap=beta*math.sqrt(r/(r+g))*math.exp(-(nu-mu)*L)/(alpha*g)
    return np.array([fresh,fresh+gap,gap])

def grid(D,L,r,alpha,beta,kappa,refresh,N=1300):
    length=L+12*math.sqrt(D/r)
    idx=max(100,int(round(N*L/length)))
    dx=L/idx
    N=int(math.ceil(length/dx))
    nn=N+1; Q=lil_matrix((2*nn,2*nn))
    rhs=np.full(2*nn,-1.0)
    pi=[beta/(alpha+beta),alpha/(alpha+beta)]
    for j in range(2):
        offset=j*nn
        for i in range(1,N):
            p=offset+i
            Q[p,p-1]+=D/dx**2
            Q[p,p]+=-2*D/dx**2 - r-(alpha if j==0 else beta)
            Q[p,p+1]+=D/dx**2
            Q[p,(1-j)*nn+i]+=(alpha if j==0 else beta)
            if refresh:
                for j0 in range(2): Q[p,j0*nn+idx]+=r*pi[j0]
            else:
                Q[p,offset+idx]+=r
        p=offset
        Q[p,p]=-3
        Q[p,p+1]=4
        Q[p,p+2]=-1
        if j==1:
            Q[p,p]+=-2*dx*kappa/D
        rhs[p]=0
        p=offset+N
        Q[p,p-2]=1;Q[p,p-1]=-4;Q[p,p]=3
        rhs[p]=0
    sol=spsolve(Q.tocsr(),rhs)
    return pi[0]*sol[idx]+pi[1]*sol[nn+idx]

def check_symbolic():
    alpha,beta,r,h0,h1 = sp.symbols('alpha beta r h0 h1', positive=True)
    g=alpha+beta
    Q=sp.Matrix([[-alpha,alpha],[beta,-beta]])
    h=sp.Matrix([h0,h1]); e=sp.Matrix([[0,1]])
    renewal_kernel=(sp.eye(2)-h*e)*(r*sp.eye(2)-Q).inv()
    wait=(sp.ones(2,1)-h)/r
    pi=sp.Matrix([[beta/g,alpha/g]])
    retained=(pi*(sp.eye(2)-r*renewal_kernel).inv()*wait)[0]
    refreshed=(pi*wait)[0]/(pi*h)[0]
    target=beta*(h1-h0)/(g*(beta*h0+alpha*h1))
    assert sp.simplify(retained-refreshed-target)==0
    x,y,z,kappa,D,L=sp.symbols('x y z kappa D L', positive=True)
    # x=mu, y=nu, z=alpha+beta; impose the boundary coefficients.
    B=-kappa/(D*z*y+kappa*(alpha*y/x+beta))
    A=-alpha*y*B/x
    hh0=A*sp.exp(-x*L)+alpha*B*sp.exp(-y*L)
    hh1=A*sp.exp(-x*L)-beta*B*sp.exp(-y*L)
    target_gap=beta*x*sp.exp(-(y-x)*L)/(alpha*z*y)
    assert sp.simplify(target.subs({h0:hh0,h1:hh1,g:z})-target_gap)==0
    f=sp.symbols('f',positive=True)
    cp0=alpha*(y*sp.exp(-x*L)-x*sp.exp(-y*L))/(alpha*y+beta*x)
    cp1=(alpha*y*sp.exp(-x*L)+beta*x*sp.exp(-y*L))/(alpha*y+beta*x)
    universal=beta*x*sp.exp(-(y-x)*L)/(alpha*(alpha+beta)*y)
    assert sp.simplify(target.subs({h0:f*cp0,h1:f*cp1})-universal)==0
    return True

def arbitrary_threshold_checks():
    # Distribution-independent matrix renewal check, for exponential, deterministic,
    # and two-point mixtures of boundary-local-time reaction thresholds.
    count=0
    for D,L,r,alpha,beta,_ in [(1.2,1.1,0.9,0.7,1.5,2.5),(0.85,0.6,1.8,1.4,0.3,7)]:
        g=alpha+beta;mu=math.sqrt(r/D); nu=math.sqrt((r+g)/D)
        q=g*mu*nu/(alpha*nu+beta*mu)
        c0=alpha*(nu*math.exp(-mu*L)-mu*math.exp(-nu*L))/(alpha*nu+beta*mu)
        c1=(alpha*nu*math.exp(-mu*L)+beta*mu*math.exp(-nu*L))/(alpha*nu+beta*mu)
        pi=np.array([beta/g,alpha/g]); Q=np.array([[-alpha,alpha],[beta,-beta]])
        target_gap=exact(D,L,r,alpha,beta,1.0)[2]
        for phi in [1.0,2.0/(2+q),math.exp(-2.0*q),1/(1+q/2)**3,
                    0.2*math.exp(-.1*q)+0.8*math.exp(-3*q)]:
            H=phi*np.array([c0,c1]); R=(np.eye(2)-np.outer(H,[0,1]))@np.linalg.inv(r*np.eye(2)-Q)
            t=(1-H)/r
            mk=pi@np.linalg.solve(np.eye(2)-r*R,t)
            mf=(1-pi@H)/(r*(pi@H))
            assert abs((mk-mf)-target_gap) < 1.e-8*max(1,mk)
            count+=1
    print('PASS',count,'direct matrix-renewal tests across nonexponential reaction laws')

if __name__=='__main__':
    assert check_symbolic()
    arbitrary_threshold_checks()
    cases=[(1.2,1.1,0.9,0.7,1.5,0.25),(1.2,1.1,0.9,0.7,1.5,2.5),(1.2,1.1,0.9,0.7,1.5,25.0),(0.85,0.6,1.8,1.4,0.3,0.8),(0.85,0.6,1.8,1.4,0.3,7.0)]
    for par in cases:
        f,k,delta=exact(*par)
        fn=grid(*par,refresh=True)
        kn=grid(*par,refresh=False)
        print('parameters',par,'analytic',f,k,'FD',fn,kn,'errors',fn-f,kn-k)
        assert abs(fn-f)/f < .0035
        assert abs(kn-k)/k < .0035
        assert abs((kn-fn)-delta) < .025
    print('PASS 1 symbolic Markov-renewal identity, 1 symbolic kappa cancellation, 5 pairs of independent finite-difference checks')
