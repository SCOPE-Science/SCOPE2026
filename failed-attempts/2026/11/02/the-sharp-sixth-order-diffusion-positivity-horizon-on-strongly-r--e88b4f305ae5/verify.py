"""Reproducible exact checks for sixth-order Padé diffusion on strongly regular graphs.

Run with Python 3.9+ standard library: python verify.py
Finite checks supplement, but do not replace, the analytic proof.
"""
from fractions import Fraction as F
from itertools import combinations, product


def add(A,B):
    return [[A[i][j]+B[i][j] for j in range(len(A))] for i in range(len(A))]

def mul(A,B):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

def identity(n):
    return [[F(int(i==j)) for j in range(n)] for i in range(n)]

def scale(A,s):
    return [[s*x for x in row] for row in A]

def inverse(A):
    n=len(A)
    M=[row[:] + eye for row,eye in zip(A, identity(n))]
    for j in range(n):
        k=next(k for k in range(j,n) if M[k][j])
        M[j],M[k]=M[k],M[j]
        p=M[j][j]
        M[j]=[x/p for x in M[j]]
        for i in range(n):
            if i==j: continue
            p=M[i][j]
            if p: M[i]=[u-p*v for u,v in zip(M[i],M[j])]
    return [row[n:] for row in M]

def mat_r(L,z):
    n=len(L)
    X=scale(L,z)
    X2=mul(X,X); X3=mul(X2,X)
    D=add(add(add(scale(identity(n),F(120)),scale(X,F(60))),scale(X2,F(12))),X3)
    N=add(add(add(scale(identity(n),F(120)),scale(X,F(-60))),scale(X2,F(12))),scale(X3,F(-1)))
    return mul(inverse(D),N)

def r(z):return (120-60*z+12*z*z-z*z*z)/(120+60*z+12*z*z+z*z*z)

def g(z):return (1-r(z))/z

def make_graph(tag):
    if tag=='C4':
        n=4; edges=[(i,(i+1)%n) for i in range(n)]
    elif tag=='K3,3':
        n=6;edges=[(i,j) for i in range(3) for j in range(3,6)]
    elif tag=='Petersen':
        n=10; edges=[(i,(i+1)%5) for i in range(5)]+[(i,i+5) for i in range(5)]+[(i+5,5+(i+2)%5) for i in range(5)]
    elif tag.startswith('Rook'):
        m=int(tag[-1]);verts=list(product(range(m),repeat=2));n=len(verts)
        edges=[(i,j) for i in range(n) for j in range(i+1,n) if verts[i][0]==verts[j][0] or verts[i][1]==verts[j][1]]
    elif tag.startswith('Triangular'):
        m=int(tag[-1]);verts=list(combinations(range(m),2));n=len(verts)
        edges=[(i,j) for i in range(n) for j in range(i+1,n) if len(set(verts[i])&set(verts[j]))==1]
    else:raise ValueError(tag)
    A=[[F(0) for _ in range(n)] for _ in range(n)]
    for i,j in edges:A[i][j]=A[j][i]=F(1)
    return A

def polyadd(a,b):
    return [(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))]

def polymul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out

def polyscale(a,s):return [v*s for v in a]

def der(a):return [i*a[i] for i in range(1,len(a))]

def normalized(a):
    while a and a[-1]==0:a.pop()
    return a

def check_symbolics():
    N=[120,-60,12,-1];D=[120,60,12,1]
    # r'(z) * D(z)^2 = N'D-ND'
    lhs=polyadd(polymul(der(N),D),polyscale(polymul(N,der(D)),-1))
    assert normalized(lhs)==normalized(polyscale([600,0,-30,0,1],-24))
    # g(z) = 2(60+z^2)/D(z)
    G=[120,0,2]
    assert normalized(polyadd(D,polyscale(N,-1)))==normalized(polymul([0,1],G))
    lhs=polyadd(polymul(der(G),D),polyscale(polymul(G,der(D)),-1))
    assert normalized(lhs)==normalized(polyscale([3600,1200,120,0,1],-2))
    # Fourth-order [2/2] contrast on the four-cycle: opposite-vertex
    # numerator for the 0,2,2,4 spectrum is always positive.
    U=[12,-6,1];V=[12,6,1]
    sub=lambda a,c:[a[i]*(c**i) for i in range(len(a))]
    u2,u4=sub(U,2),sub(U,4)
    v2,v4=sub(V,2),sub(V,4)
    four=polyadd(polyadd(polymul(v2,v4),polyscale(polymul(u2,v4),-2)),polymul(u4,v2))
    assert normalized(four)==[0,0,576,576]
    return 4

def graph_params(A):
    n=len(A)
    k=sum(A[0]); assert 0<k<n-1
    assert all(sum(row)==k for row in A)
    c1=set();c0=set()
    for i in range(n):
        for j in range(i+1,n):
            common=sum(A[i][t]*A[j][t] for t in range(n))
            (c1 if A[i][j] else c0).add(common)
    assert len(c1)==len(c0)==1
    lam=c1.pop();mu=c0.pop();assert mu>0
    assert (n-k-1)*mu==k*(k-lam-1)
    return n,k,lam,mu

def spectral_params(n,k,lam,mu):
    # For the integral-spectrum test graphs, Laplacian roots solve
    # t^2-(2k-lam+mu)t+mu*n=0.
    s=2*k-lam+mu;p=mu*n
    roots=[i for i in range(1,2*int(k)+2) if i*i-s*i+p==0]
    assert len(roots)==2, (n,k,lam,mu,roots)
    a,b=sorted(roots)
    delta=b-a
    ma=F(b*(n-1)-n*k,delta);mb=F(n*k-a*(n-1),delta)
    assert ma>0 and mb>0 and ma+mb==n-1
    return a,b,ma,mb

def spectral_entry(i,j,A,n,k,a,b,ma,mb,z):
    ra=r(a*z);rb=r(b*z)
    if i==j:return (F(1)+ma*ra+mb*rb)/n
    # Subtraction-free formula for nonedge, plus positive edge correction.
    base=F(a*b, n*(b-a))*z*(g(a*z)-g(b*z))
    if A[i][j]:return base+(ra-rb)/(b-a)
    return base


def main():
    identities=check_symbolics()
    comparisons=0;off_signs=0;threshold_brackets=0;rowsums=0
    tags=['C4','K3,3','Petersen','Rook3','Rook4','Triangular5']
    vals=[F(1,5),F(1),F(2),F(5),F(11)]
    records=[]
    for tag in tags:
        A=make_graph(tag)
        n,k,lam,mu=graph_params(A)
        a,b,ma,mb=spectral_params(n,k,lam,mu)
        L=[[F(k) if i==j else -A[i][j] for j in range(n)] for i in range(n)]
        for z in vals:
            P=mat_r(L,z)
            for i in range(n):
                assert sum(P[i])==1
                rowsums+=1
                for j in range(n):
                    assert P[i][j]==spectral_entry(i,j,A,n,k,a,b,ma,mb,z),(tag,z,i,j)
                    comparisons+=1
                    if i!=j:
                        assert P[i][j]>0
                        off_signs+=1
        f=lambda z:F(1)+ma*r(a*z)+mb*r(b*z)
        # Exact rational bracket, not a floating root-finder certificate.
        lo=F(0);hi=F(1)
        while f(hi)>0:hi*=2
        for _ in range(40):
            mid=(lo+hi)/2
            if f(mid)>0:lo=mid
            else:hi=mid
        assert f(lo)>0 and f(hi)<=0 and (hi-lo)<F(1,100000)
        threshold_brackets+=1
        records.append((tag,str((n,k,lam,mu)),str((a,b,ma,mb)),f'{float((lo+hi)/2):.12f}'))
    # Direct fourth-order contrast on Petersen at unit-conductance z=4.
    r22=lambda t:F(12-6*t+t*t,12+6*t+t*t)
    contrast=F(3-5*r22(8)+2*r22(20),30)+(r22(8)-r22(20))/3
    assert contrast==-F(36,4123)
    print('PETERSEN_FOURTH_ORDER_EDGE',contrast)
    print('EXACT_IDENTITIES',identities)
    print('FULL_MATRIX_ENTRIES',comparisons)
    print('STRICT_OFFDIAGONAL_CHECKS',off_signs)
    print('STOCHASTIC_ROWS',rowsums)
    print('EXACT_ROOT_BRACKETS',threshold_brackets)
    for line in records:print('CASE',*line)
    print('VERIFY_OK')

if __name__=='__main__':main()
