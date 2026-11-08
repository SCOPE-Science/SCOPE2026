"""Numerical matrix and spectral checks for quantum loss on Boolean cubes."""
from math import comb, sqrt, pi
import numpy as np
from scipy.linalg import expm, solve_continuous_lyapunov


def adjacency(d):
    n=1<<d
    A=np.zeros((n,n),dtype=float)
    for v in range(n):
        for j in range(d):
            A[v,v^(1<<j)]=1.0
    return A


def exact_weights(w):
    z=[w-2*j for j in range(w+1)]
    p=[comb(w,j)/2**w for j in range(w+1)]
    W=sum(q for zz,q in zip(z,p) if zz)
    S=sum(q/(zz*zz) for zz,q in zip(z,p) if zz)
    return W,S


def two_level_survival(sigma,kappa,t):
    M=np.array([[-kappa,-1j*sigma],[-1j*sigma,0]],dtype=complex)
    f=expm(M*t)@np.array([0,1],dtype=complex)
    return np.vdot(f,f).real


def explicit_two_level(sigma,kappa,t):
    if sigma==0: return 1.
    D=np.sqrt(complex(kappa*kappa-4*sigma*sigma))
    if abs(D)<1e-10:
        b=np.exp(-kappa*t/2)*(1+kappa*t/2)
        a=-1j*sigma*t*np.exp(-kappa*t/2)
    else:
        b=np.exp(-kappa*t/2)*(np.cosh(D*t/2)+kappa/D*np.sinh(D*t/2))
        a=-2j*sigma/D*np.exp(-kappa*t/2)*np.sinh(D*t/2)
    return abs(a)**2+abs(b)**2


def spectral_survival(w,kappa,t):
    return sum(comb(w,j)/2**w*explicit_two_level(abs(w-2*j),kappa,t) for j in range(w+1))


def check():
    ncases=0
    for w in range(1,8):
        A=adjacency(w); p=np.array([((x.bit_count()%2)==0) for x in range(1<<w)],dtype=float)
        for kappa in (0.7,2.,3.4):
            H=-1j*A-np.diag(kappa*p)
            for t in (0.13,0.64,2.2):
                U=expm(H*t)
                q=spectral_survival(w,kappa,t)
                for x in range(1<<w):
                    if x.bit_count()%2 == 1:
                        actual=np.vdot(U[:,x],U[:,x]).real
                        assert abs(actual-q)<1e-9,(w,kappa,t,x,actual,q)
                        ncases+=1
    # A non-coordinate affine parity hyperplane in a larger cube.
    d=5; mask=(1<<0)|(1<<2)|(1<<4); w=3
    a=adjacency(d)
    for b in (0,1):
        trap=np.array([((x&mask).bit_count()%2)==b for x in range(1<<d)], dtype=float)
        for kappa,t in ((.9,.73),(1.7,1.3)):
            U=expm((-1j*a-np.diag(kappa*trap))*t)
            expected=spectral_survival(w,kappa,t)
            for x in range(1<<d):
                if ((x&mask).bit_count()%2)!=b:
                    actual=np.vdot(U[:,x],U[:,x]).real
                    assert abs(actual-expected)<1e-9,(d,mask,b,x,actual,expected)
                    ncases+=1
    print('full matrix time-law tests',ncases)
    ncase2=0
    for w in range(1,21):
        W,S=exact_weights(w)
        assert W>0
        kappa=sqrt(2*W/S)
        for value in (0.5*kappa,kappa,1.5*kappa):
            mean=1/value+value*S/(2*W)
            assert mean+1e-12 >= 1/kappa+kappa*S/(2*W)
        # independent Lyapunov check for each nonzero singular value
        for j in range(w+1):
            sigma=abs(w-2*j)
            if sigma==0:continue
            M=np.array([[-kappa,-1j*sigma],[-1j*sigma,0]],dtype=complex)
            X=solve_continuous_lyapunov(M.conj().T,-np.eye(2))
            assert abs(X[1,1].real - (1/kappa+kappa/(2*sigma*sigma)))<3e-11,(w,sigma,X[1,1])
            ncase2+=1
    print('independent Lyapunov mean-time tests',ncase2)
    for w in range(2,11):
        A=adjacency(w)
        even=[x for x in range(1<<w) if x.bit_count()%2==0]
        odd=[x for x in range(1<<w) if x.bit_count()%2==1]
        B=A[np.ix_(even,odd)]
        dim=B.shape[1]-np.linalg.matrix_rank(B)
        predicted=comb(w,w//2)//2 if w%2==0 else 0
        assert dim==predicted,(w,dim,predicted)
    print('dark-subspace rank tests 2..10 passed')
    # exact asymptotic ratios grow to one along both parity subsequences
    Codd=pi**1.5/(2*sqrt(2))
    Ceven=pi**1.5/(6*sqrt(2))
    for w in (1000,1001,4000,4001):
        # stable binomial log pmf
        import scipy.stats as stats
        p=stats.binom.pmf(np.arange(w+1),w,.5)
        j=np.arange(w+1);z=w-2*j
        S=np.sum(p[z!=0]/(z[z!=0]*z[z!=0]))
        C=Codd if w%2 else Ceven
        print('S asymptotic',w,round(S*sqrt(w)/C,6))

if __name__=='__main__':check()
