#!/usr/bin/env python3
"""Reproduce the exact steady-state coherence-deficit identity using finite matrices."""
import numpy as np
import sympy as sp

def solution(n,t,rate,gamma,potential,exact=False):
    if exact:
        i=sp.I
        H=sp.zeros(n)
        for a in range(n):H[a,a]=potential[a]
        for a in range(n-1):H[a,a+1]=H[a+1,a]=t
        # Build basis of Hermitian matrices E_ii, E_ij+E_ji, i(E_ij-E_ji)
        B=[]
        for a in range(n):
            M=sp.zeros(n);M[a,a]=1;B.append(M)
        for a in range(n):
            for b in range(a+1,n):
                M=sp.zeros(n);M[a,b]=M[b,a]=1;B.append(M)
                M=sp.zeros(n);M[a,b]=sp.I;M[b,a]=-sp.I;B.append(M)
        def L(M):
            ans=i*(H*M-M*H)
            for a in range(n):
                for b in range(n):
                    if a!=b:ans[a,b]+=gamma*M[a,b]
                    if a in (0,n-1):ans[a,b]+=rate*M[a,b]/2
                    if b in (0,n-1):ans[a,b]+=rate*M[a,b]/2
            return ans
        def coord(M):
            vv=[sp.expand(M[a,a]) for a in range(n)]
            for a in range(n):
                for b in range(a+1,n):
                    vv.extend([sp.expand(sp.re(M[a,b])),sp.expand(sp.im(M[a,b]))])
            return sp.Matrix(vv)
        A=sp.Matrix.hstack(*[coord(L(M)) for M in B]);S=sp.zeros(n);S[0,0]=rate/2;S[n-1,n-1]=-rate/2
        xx=A.inv()*coord(S)
        X=sum([xx[k]*B[k] for k in range(n*n)],sp.zeros(n))
        return X
    H=np.diag(potential).astype(complex)
    for a in range(n-1):H[a,a+1]=H[a+1,a]=t
    P=np.zeros((n,n));P[0,0]=P[-1,-1]=1
    D=np.zeros((n*n,n*n),dtype=complex)
    # vec column-major: -i[H,X] in evolution, positive L=i[H,X].
    for a in range(n):
        for b in range(n):
            idx=a+n*b
            D[idx,idx]=gamma*(a!=b)+rate/2*((a in (0,n-1))+(b in (0,n-1)))
    Q=D+1j*(np.kron(np.eye(n),H)-np.kron(H.T,np.eye(n)))
    S=np.diag([rate/2]+[0]*(n-2)+[-rate/2]);x=np.linalg.solve(Q,S.reshape(-1,order='F')).reshape(n,n,order='F')
    return x

def check(X,t,rate,gamma,tol=1e-10):
    n=X.shape[0]
    j=float(2*t)*complex(X[0,1]).imag
    w=lambda a,b:gamma+(rate/2)*(int(a in (0,n-1))+int(b in (0,n-1)))
    R=sum(2*w(a,b)*(float(sp.re(X[a,b]))**2+(float(sp.im(X[a,b]))**2 if b>a+1 else 0)) for a in range(n) for b in range(a+1,n))
    j0=1/(2/rate+(gamma*(n-1)+rate)/(2*t*t))
    err=abs(R-j*(1-j/j0))
    assert err<tol,(err,n,j,j0,R)
    assert -tol < j <= j0+tol
    return j,j0,R,err

if __name__=='__main__':
    count=0
    for n in [2,3,4]:
        for rate,gamma,t,V in [(sp.Rational(2,3),sp.Rational(1,2),sp.Rational(3,2),0), (sp.Rational(1,2),sp.Rational(1,3),sp.Rational(2),1),(sp.Rational(3,2),sp.Rational(3,5),sp.Rational(1),2)]:
            # Three rational profiles, including zero and spatial gradient
            p=[sp.Rational(V)*a for a in range(n)]
            X=solution(n,t,rate,gamma,p,exact=True)
            res=check(X,t,rate,gamma,1e-13)
            j=2*t*sp.im(X[0,1])
            j0=1/(2/rate+(gamma*(n-1)+rate)/(2*t*t))
            E=sp.Integer(0)
            for a in range(n):
                for b in range(a+1,n):
                    w=gamma+(rate/2)*(int(a in (0,n-1))+int(b in (0,n-1)))
                    E+=2*w*(sp.re(X[a,b])**2+(sp.im(X[a,b])**2 if b>a+1 else 0))
            assert sp.simplify(E-j*(1-j/j0))==0
            assert sp.simplify(sp.im(X[0,1])-sp.im(X[n-2,n-1]))==0
            count+=1
    rg=np.random.default_rng(42841)
    for n in [2,3,4,5,6,7]:
        for k in range(20):
            rate=0.1+2*rg.random();gamma=0.05+2*rg.random();t=0.2+2*rg.random()
            p=rg.normal(size=n)*rg.random()*8
            X=solution(n,t,rate,gamma,p)
            check(X,t,rate,gamma,1e-8)
            count+=1
    print('PASS 9 exact rational identities and 120 randomized matrix diagnostics; total',count)
