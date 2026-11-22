#!/usr/bin/env python3
"""Exact small-instance checks for the complete-split two-leader spectral theorem.

Run with python3 verify.py; uses only the Python standard library. Finite tests
corroborate the independent infinite-domain majorization proof.
"""
from fractions import Fraction as Q
from math import sqrt


def laplacian(p,q):
    n=p+q
    M=[[Q(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            if i<p or j<p:
                M[i][i]+=1;M[j][j]+=1
                M[i][j]-=1;M[j][i]-=1
    return M


def inverse(A):
    n=len(A)
    E=[[Q(A[i][j]) for j in range(n)]+[Q(i==j) for j in range(n)] for i in range(n)]
    for j in range(n):
        k=next(k for k in range(j,n) if E[k][j])
        E[j],E[k]=E[k],E[j]
        d=E[j][j]
        E[j]=[v/d for v in E[j]]
        for i in range(n):
            if i!=j:
                c=E[i][j]
                if c:
                    E[i]=[E[i][k]-c*E[j][k] for k in range(2*n)]
    return [v[n:] for v in E]


def matmul(A,B):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def exact_trace_power(p,q,a,r):
    leaders=list(range(a))+list(range(p,p+2-a))
    idx=[i for i in range(p+q) if i not in leaders]
    L=laplacian(p,q)
    A=[[L[i][j] for j in idx] for i in idx]
    B=inverse(A)
    P=B
    for _ in range(r-1):P=matmul(P,B)
    return sum(P[i][i] for i in range(len(P)))


def spectral_formula(p,q,a,r):
    N=p+q;u=p-a;v=q-2+a
    if not u:return Q(v,p**r)
    if not v:return Q(u-1,N**r)+Q(1,(N-u)**r)
    d=2*p+a*(q-2+a)
    # For integral r, the power sums of reciprocal block eigenvalues are rational.
    if r==1:block=Q(N+a,d)
    elif r==2:block=Q((N+a)**2-2*d,d*d)
    elif r==3:block=Q((N+a)**3-3*d*(N+a),d**3)
    else:raise ValueError('Integral r=1,2,3 only')
    return Q(u-1,N**r)+Q(v-1,p**r)+block


def recip_eigs(p,q,a):
    N=p+q;u=p-a;v=q-2+a
    if u==0:return [1./p]*v
    if v==0:return [1./N]*(u-1)+[1./(N-u)]
    trace=N+a;d=2*p+a*(q-2+a)
    lamlo=(trace-sqrt(trace*trace-4*d))/2
    lamhi=(trace+sqrt(trace*trace-4*d))/2
    return [1./N]*(u-1)+[1./p]*(v-1)+[1./lamlo,1./lamhi]


def expected(p,q,r):
    if q==2:return {0}
    if (p,q)==(2,3):return {0} if r==1 else {2}
    if r==1 and p==2:return {1,2}
    if r==1 and (p,q)==(3,3):return {0,2}
    return {2}


def main():
    exact=0;optima=0;major=0
    for p in range(2,8):
        for q in range(2,9):
            for r in (1,2,3):
                vals=[exact_trace_power(p,q,a,r) for a in range(3)]
                for a in range(3):
                    assert vals[a]==spectral_formula(p,q,a,r),(p,q,a,r)
                    exact+=1
                minimum=min(vals)
                winners={a for a in range(3) if vals[a]==minimum}
                assert winners==expected(p,q,r),(p,q,r,winners,expected(p,q,r))
                optima+=1
    for p in range(2,31):
        for q in range(2,31):
            target=0 if q==2 else 2
            if (p,q)==(2,3):continue
            x=sorted(recip_eigs(p,q,target),reverse=True)
            for a in range(3):
                if a==target:continue
                y=sorted(recip_eigs(p,q,a),reverse=True)
                sx=sy=0.0
                for xx,yy in zip(x,y):
                    sx+=xx;sy+=yy
                    assert sx<=sy+2e-10,(p,q,a,sx,sy)
                    major+=1
    def f(r):return 2**r+2**(-r)+(2./5)**r-3
    assert f(1)<0<f(2)
    lo,hi=1.,2.
    for _ in range(80):
        mid=(lo+hi)/2
        if f(mid)>0:hi=mid
        else:lo=mid
    rho=(lo+hi)/2
    assert abs(rho-1.1293316509672375)<1e-12
    print(f'PASS: {exact} exact matrix-to-spectrum identities, {optima} exhaustive orbit minimizer comparisons, {major} reciprocal-spectrum prefix comparisons.')
    print(f'Exceptional spectral-order transition rho = {rho:.15f}.')
    print('Finite diagnostics only; the unrestricted theorem uses analytic weak majorization.')

if __name__=='__main__':main()
