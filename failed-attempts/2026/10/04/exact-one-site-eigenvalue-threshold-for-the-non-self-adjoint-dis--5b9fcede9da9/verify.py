#!/usr/bin/env python3
import cmath, math


def matmul(A,B):
    return [[sum(A[i][r]*B[r][j] for r in range(2)) for j in range(2)] for i in range(2)]

def matvec(A,x):
    return [A[i][0]*x[0]+A[i][1]*x[1] for i in range(2)]

def adj(A):
    return [[A[j][i].conjugate() for j in range(2)] for i in range(2)]

def inner(x,y):
    return sum(x[i].conjugate()*y[i] for i in range(2))

def normv(x):
    return math.sqrt(max(0.0, inner(x,x).real))

def scale(c,x):
    return [c*z for z in x]

def add_outer(A,c,u,v):
    for i in range(2):
        for j in range(2):
            A[i][j] += c*u[i]*v[j].conjugate()

def spectral_norm_and_right_vector(A):
    H=matmul(adj(A),A)
    a=H[0][0].real; d=H[1][1].real; b=H[0][1]
    disc=math.sqrt(max(0.0,(a-d)*(a-d)+4*abs(b)**2))
    mu=(a+d+disc)/2
    sigma=math.sqrt(max(0.0,mu))
    if abs(b)>1e-14 or abs(mu-a)>1e-14:
        v=[b, mu-a]
    else:
        v=[1+0j,0j] if a>=d else [0j,1+0j]
    nv=normv(v)
    v=[z/nv for z in v]
    return sigma,v

def choose_k(lam,m):
    s=m*m+2-lam*lam
    disc=cmath.sqrt(s*s-4)
    roots=[(s+disc)/2,(s-disc)/2]
    roots.sort(key=abs)
    if not (abs(roots[0])<1+1e-12):
        raise AssertionError('no root in unit disk')
    return roots[0]

def T0(lam,m,k):
    den=1/k-k
    return [[(lam-m)/den,(1-k)/den],[(1-k)/den,(lam+m)/den]]

def T1(lam,m,k):
    den=1/k-k
    return [[k*(lam-m)/den,k*(1-k)/den],[k*(1-1/k)/den,k*(lam+m)/den]]

def orth(u):
    return [-u[1].conjugate(),u[0].conjugate()]

def construct_V(A,Q):
    sigma,x=spectral_norm_and_right_vector(A)
    y=matvec(A,x)
    assert abs(normv(y)-sigma)<1e-10
    e1=[z/sigma for z in y]
    e2=orth(e1)
    f1=[-z for z in x]
    f2=orth(f1)
    V=[[0j,0j],[0j,0j]]
    add_outer(V,1/sigma,f1,e1)
    add_outer(V,Q,f2,e2)
    return sigma,x,y,V

def det2(A):
    return A[0][0]*A[1][1]-A[0][1]*A[1][0]

def eyeplus(A):
    return [[1+A[0][0],A[0][1]],[A[1][0],1+A[1][1]]]

def maxerr(x,y):
    return max(abs(x[i]-y[i]) for i in range(2))

cases=[(0.5,3+0.4j),(0.0,2.7+0.3j),(1.2,-3.4+0.7j),(0.2,0.4+1.8j)]
for m,lam in cases:
    k=choose_k(lam,m)
    A=T0(lam,m,k)
    sigma,_=spectral_norm_and_right_vector(A)
    Q=1.7/sigma
    sigma,x,y,V=construct_V(A,Q)
    Vy=matvec(V,y)
    assert maxerr(Vy,[-z for z in x])<2e-10
    nV,_=spectral_norm_and_right_vector(V)
    assert abs(nV-Q)<2e-10
    VA=matmul(V,A)
    assert abs(det2(eyeplus(VA)))<2e-9
    # Any witness must obey Q >= 1/||T0||; here the construction attains arbitrary Q above threshold.
    assert Q+1e-12 >= 1/sigma

# Find a point where the off-diagonal resolvent block dominates. On the improved-boundary
# normalization Q=1/||T1||, the theorem predicts that no one-site perturbation can attain it.
m=0.125
found=False
for r in (0.2,0.35,0.5,0.7,0.85):
    for j in range(1,24):
        th=2*math.pi*j/25
        k=r*cmath.exp(1j*th)
        s=k+1/k
        lam2=m*m+2-s
        for lam in (cmath.sqrt(lam2),-cmath.sqrt(lam2)):
            A=T0(lam,m,k); B=T1(lam,m,k)
            n0,_=spectral_norm_and_right_vector(A)
            n1,_=spectral_norm_and_right_vector(B)
            if n1>n0*(1+1e-5):
                Q=1/n1
                assert Q*n0 < 1-1e-6
                found=True
                break
        if found: break
    if found: break
assert found
print('VERIFY_OK cases=%d off_diagonal_obstruction=1' % len(cases))
