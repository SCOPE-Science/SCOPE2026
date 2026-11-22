"""Direct construction and finite consistency checks for the path-shortcut theorem.

Requires NumPy. The analytic and variational proofs are in RESULT.md.
"""
import math
import numpy as np


def path(n):
    L = np.zeros((n,n), dtype=float)
    for i in range(n-1):
        L[i,i] += 1
        L[i+1,i+1] += 1
        L[i,i+1] -= 1
        L[i+1,i] -= 1
    return L


def augment(L,i,j):
    b=np.zeros(L.shape[0]);b[i]=1;b[j]=-1
    return L+np.outer(b,b)


def evs(L,i,j):
    return np.linalg.eigvalsh(augment(L,i,j))


checks=0
for n in range(9,35):
    L=path(n)
    E=evs(L,0,n-1)
    lam=2-2*math.cos(2*math.pi/n)
    assert abs(E[1]-lam)<5e-10 and abs(E[2]-lam)<5e-10
    # All nonedges: exact degree/tr(L^2) short-time leading coefficient.
    for i in range(n):
        for j in range(i+2,n):
            A=augment(L,i,j)
            di=int(round(L[i,i]));dj=int(round(L[j,j]))
            assert abs(float(np.trace(A@A))-(6*n-4+2*(di+dj)))<2e-8
            checks+=1
    F=evs(L,1,n-2)
    assert abs(F[1]-lam)<5e-10 and F[2]>lam+1e-8
    theta=2*math.pi/n
    # Shifted anti resolvent for chord at (2,n-1); explicitly fold the matrix.
    U=np.zeros((n,n//2))
    for j in range(n//2):
        U[j,j]=1/math.sqrt(2)
        U[n-1-j,j]=-1/math.sqrt(2)
    b=np.zeros(n);b[1]=1;b[n-2]=-1
    C=U.T@(L-lam*np.eye(n))@U
    g=(U.T@b)@np.linalg.solve(C,U.T@b)
    assert abs(g+math.sin(3*theta)/math.sin(theta))<5e-8
    checks+=4
    for t in [0.02,0.1]:
        h0=sum(math.exp(-t*v) for v in E)
        # The strict small-time global minimizer may need t smaller for large n.
        assert h0<sum(math.exp(-t*v) for v in F)
        checks+=1
    for t in [15/lam,20/lam]:
        h0=sum(math.exp(-t*v) for v in E)
        h1=sum(math.exp(-t*v) for v in F)
        # At these times the split eigenvalue contribution is exponentially small.
        assert h1 < h0
        checks+=1

# Critical integer n=8: the interior edge has double second eigenvalue.
L=path(8)
a=evs(L,1,6)
assert abs(a[1]-a[2])<1e-9
checks+=1

# The asymptotic second positive mode approaches the free-boundary profile.
for n in [30,45,60,90,120]:
    L=path(n)
    target=2*math.pi/n
    values=[]
    for i in range(n//4):
        E=evs(L,i,n-1-i)
        values.append((E[2],i))
        checks+=1
    best=max(values)[1]
    assert abs(best/n-1/6)<0.055
    checks+=1

print('VERIFY_OK',checks,'finite numeric/integer consistency checks')
