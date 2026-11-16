"""Independent numerical and combinatorial checks for Möbius-ladder tree sampling.
Run with Python 3 and NumPy. Finite checks supplement, not replace, the proof.
"""
import itertools
import math
import numpy as np


def predicted(n):
    alpha=2-math.sqrt(3)
    s=1/(4*math.sqrt(3))
    half=np.array([s*(alpha**d-alpha**(n-d))/(1+alpha**n) for d in range(n)])
    O=np.concatenate((half,-half))
    N=2*n
    H=np.zeros(N); H[0]=1
    H-=1/N+2*O
    T=2*(O-np.roll(O,-1))
    # From determinantal transfer-current covariance kernels.
    rim=H[0]*np.eye(N)
    chord=4*O[0]*np.eye(n)
    cross=np.zeros((N,n))
    for i in range(N):
        for j in range(N):
            rim[i,j]-=H[(i-j)%N]**2
    for i in range(n):
        for j in range(n):
            chord[i,j]-=16*O[(i-j)%N]**2
    for i in range(N):
        for j in range(n):
            cross[i,j]=-T[(i-j)%N]**2
    return np.block([[rim,cross],[cross.T,chord]]),O,H,T


def direct(n):
    N=2*n
    edges=[(i,(i+1)%N) for i in range(N)]+[(i,i+n) for i in range(n)]
    b=np.zeros((N,3*n))
    for j,(u,v) in enumerate(edges):
        b[u,j]=1; b[v,j]=-1
    L=b@b.T
    K=b.T@np.linalg.pinv(L)@b
    C=-K*K;C[np.diag_indices(3*n)]+=np.diag(K)
    return C,edges


def brute(n):
    N=2*n; E=3*n
    edges=[(i,(i+1)%N) for i in range(N)]+[(i,i+n) for i in range(n)]
    counts=np.zeros(E);pairs=np.zeros((E,E));total=0
    for choice in itertools.combinations(range(E),N-1):
        par=list(range(N))
        def root(x):
            while par[x]!=x:
                x=par[x]
            return x
        for j in choice:
            a,b=edges[j];a=root(a);b=root(b)
            if a==b:break
            par[a]=b
        else:
            total+=1
            ix=np.array(choice)
            counts[ix]+=1
            pairs[np.ix_(ix,ix)]+=1
    C=pairs/total-np.outer(counts,counts)/total**2
    return total,C


def fourier_eigenvalues(n,O,H,T):
    N=2*n
    a=H[0]-np.fft.fft(H**2)
    d=4*O[0]-np.fft.fft((4*O[:n])**2)
    b=-math.sqrt(2)*np.fft.fft(T[:n]**2)
    eig=[]
    for k in range(1,N,2):eig.append(a[k].real)
    for l in range(n):
        x=(a[2*l].real+d[l].real)/2
        y=math.hypot((a[2*l].real-d[l].real)/2,abs(b[l]))
        eig.extend([x-y,x+y])
    return np.array(sorted(eig))


def main():
    for n in range(3,31):
        C,O,H,T=predicted(n);ref,edges=direct(n)
        assert np.max(abs(C-ref))<2e-11,(n,'covariance')
        v=np.linalg.eigvalsh(C)
        f=fourier_eigenvalues(n,O,H,T)
        assert np.max(abs(v-f))<2e-10,(n,'spectrum')
        assert abs(v[0])<2e-10 and v[1]>1e-10,(n,'rank')
    for n in range(3,7):
        total,bc=brute(n)
        C,*_=predicted(n)
        assert np.max(abs(bc-C))<3e-12,(n,'enumeration',total)
        print('uniform spanning trees',n,total,'matched')
    limit=math.sqrt(3)/2
    for n in (80,160,320,640,1280):
        C,O,H,T=predicted_no_dense(n)
        v=fourier_eigenvalues(n,O,H,T)
        pos=v[v>1e-9]
        observed=(pos[-1]/pos[0])/n
        assert abs(observed-limit)<4/n, (n, observed,limit)
    print('All checks passed; asymptotic values supplement the analytic result.')


def predicted_no_dense(n):
    alpha=2-math.sqrt(3);s=1/(4*math.sqrt(3));d=np.arange(n)
    half=s*(alpha**d-alpha**(n-d))/(1+alpha**n)
    O=np.concatenate((half,-half));H=np.zeros(2*n);H[0]=1
    H-=1/(2*n)+2*O
    T=2*(O-np.roll(O,-1))
    return None,O,H,T

if __name__=='__main__':main()
