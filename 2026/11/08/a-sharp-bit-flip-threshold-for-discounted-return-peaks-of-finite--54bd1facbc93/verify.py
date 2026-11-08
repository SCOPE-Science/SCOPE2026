"""Finite exact cross-check of a bit-flip-perturbed cat map's return resolvent.
Uses only Python's standard library. This code checks finite examples, not the infinite modulus theorem.
"""
from fractions import Fraction as Q
from itertools import product

A=((1,1),(1,2))

def graph(n,e):
    pts=list(product(range(n),repeat=2))
    ix={p:i for i,p in enumerate(pts)}
    v=(n//2,0)
    P=[[Q(0) for j in pts] for i in pts]
    for i,(a,b) in enumerate(pts):
        u=((a+b)%n,(a+2*b)%n)
        w=((u[0]+v[0])%n,u[1])
        P[i][ix[u]]+=1-e
        P[i][ix[w]]+=e
    return pts,P

def resolvent_diagonal(n,e,alpha):
    pts,P=graph(n,e)
    k=len(pts)
    # Invert I-alpha P by exact Gauss-Jordan arithmetic.
    A0=[[Q(i==j)-alpha*P[i][j] for j in range(k)]+[Q(i==j) for j in range(k)] for i in range(k)]
    for col in range(k):
        pivot=next(i for i in range(col,k) if A0[i][col])
        A0[col],A0[pivot]=A0[pivot],A0[col]
        f=A0[col][col]
        A0[col]=[a/f for a in A0[col]]
        for row in range(k):
            if row==col:continue
            f=A0[row][col]
            if f:A0[row]=[b-f*a for a,b in zip(A0[col],A0[row])]
    return {pt:A0[i][k+i] for i,pt in enumerate(pts)}

def check():
    count=0
    for N in [2,4]:
        star=(N//2,N//2)
        for e in [Q(0),Q(1,4),Q(1,2),Q(3,4),Q(1)]:
            for alpha in [Q(1,3),Q(3,4)]:
                diag=resolvent_diagonal(N,e,alpha)
                mx=max(diag.values())
                winners={x for x,y in diag.items() if y==mx}
                targets={(0,0)} if e<Q(1,2) else ({(0,0),star} if e==Q(1,2) else {star})
                assert winners==targets, (N,e,alpha,winners,targets)
                gap=alpha*abs(1-2*e)
                if e!=Q(1,2):
                    peak=next(iter(targets))
                    assert all(diag[peak]-v>=gap for x,v in diag.items() if x!=peak)
                else:
                    assert all(diag[(0,0)]-v>=alpha/2 for x,v in diag.items() if x not in targets)
                # Exact translation duality: subtract the alternative affine fixed point.
                twin=resolvent_diagonal(N,1-e,alpha)
                assert all(diag[x]==twin[((x[0]-star[0])%N,(x[1]-star[1])%N)] for x in diag)
                count+=1
                if N==2:
                    q=alpha
                    det=1-q**3*(1-2*e)**2
                    assert diag[(0,0)]-diag[(1,1)]==q*(1+q)*(1-2*e)/det
                    assert diag[(0,0)]-diag[(1,0)]==q*(1-e)*(1-q*(2*e-1))/det
    # Independently check positive Fourier coefficients of step kernels at selected resolution.
    from cmath import exp,pi
    for N in [2,4,8,16]:
        for e in [Q(0),Q(1,3),Q(49,100)]:
            for k,l in product(range(N),repeat=2):
                ch=exp(2j*pi*k*(N//2)/N)
                val=(1-float(e))+float(e)*ch
                assert abs(val.imag)<1e-12 and val.real>0
    print(f'VERIFY_OK exact_resolvents={count} symbolic_N2_identities={10} Fourier_tests={4*3} gap_bounds=1 affine_duality=1')

if __name__=='__main__':check()
