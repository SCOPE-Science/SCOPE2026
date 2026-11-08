"""Numerical independent checks of biclique trapping formulas; Python standard library only.

Run: python verify.py
The all-size theorem is proved in RESULT.md; these are finite-matrix checks.
"""
import math


def mean_formula(m, n, j, k, g, source):
    if m < 2 or n < 2 or j <= 0 or k <= 0 or g <= 0:
        raise ValueError('Outside finite-gamma domain')
    a = m - 1
    N = m + n
    C = N / k + (N - 1) * k / (4 * j * j * n)
    if source == 'B':
        return C + a * (N - 2) / (2*g+k) + (n - 1)/g + (N-1)*g/(2*j*j*n)
    if source == 'A':
        return C + (a-1)*(N-2)/(2*g+k) + (a-1)/g + N*g/(2*j*j*n)
    raise ValueError('Bad source')


def gaussian(A, rhs):
    # Complex Gaussian elimination with column pivot selection.
    n=len(rhs)
    a=[list(row)+[rhs[i]] for i,row in enumerate(A)]
    for k in range(n):
        pivot=max(range(k,n),key=lambda i:abs(a[i][k]))
        if abs(a[pivot][k])<1.e-12:
            raise ArithmeticError('Singular linear system')
        a[k],a[pivot]=a[pivot],a[k]
        v=a[k][k]
        for j in range(k,n+1): a[k][j] /= v
        for i in range(k+1,n):
            f=a[i][k]
            if f == 0: continue
            for j in range(k+1,n+1): a[i][j] -= f*a[k][j]
            a[i][k]=0j
    x=[0j]*n
    for i in range(n-1,-1,-1):
        x[i]=a[i][n]-sum(a[i][j]*x[j] for j in range(i+1,n))
    return x


def direct_liouvillian_mean(m,n,j,k,g,source):
    # Assemble the UNREDUCED generator in the computational density-matrix basis.
    N=m+n
    size=N*N
    H=[[0.0]*N for _ in range(N)]
    for i in range(m):
        for p in range(m,N):
            H[i][p]=H[p][i]=j
    M=[[0j]*size for _ in range(size)]
    for a in range(N):
        for b in range(N):
            r=a+N*b
            M[r][r]=g*(a != b)+(k/2)*((a == 0)+(b == 0))
            # M = -L, L rho = -i(H rho - rho H) - dephasing - sink.
            for c in range(N):
                M[r][c+N*b] += 1j*H[a][c]
                M[r][a+N*c] -= 1j*H[c][b]
    src=1 if source=='A' else m
    rhs=[0j]*size
    rhs[src+N*src]=1
    x=gaussian(M,rhs)
    return sum(x[i+N*i] for i in range(N))


def coeff(m,n,j,k,source):
    a=m-1; N=m+n
    if source=='A': return (a-1)*(N-2),a-1,N/(2*j*j*n)
    return a*(N-2),n-1,(N-1)/(2*j*j*n)


def derivative(m,n,j,k,g,source):
    A,B,D=coeff(m,n,j,k,source)
    if g==0 and B>0:return float('-inf')
    return D-2*A/(2*g+k)**2-(B/g**2 if B else 0.0)


def best_gamma(m,n,j,k,source):
    A,B,D=coeff(m,n,j,k,source)
    if B==0 and D>=2*A/(k*k):return 0.0
    lo,hi=0.,1.
    while derivative(m,n,j,k,hi,source)<0: hi*=2
    for _ in range(100):
        mid=(lo+hi)/2
        if derivative(m,n,j,k,mid,source)<0:lo=mid
        else:hi=mid
    return (lo+hi)/2


def main():
    total=0
    for m in range(2,5):
        for n in range(2,5):
            for j,k,g in [(1.,.6,.2),(.7,2.,1.3),(1.1,1.7,3.)]:
                for source in ['A','B']:
                    actual=direct_liouvillian_mean(m,n,j,k,g,source)
                    target=mean_formula(m,n,j,k,g,source)
                    assert abs(actual-target)<2e-7*max(1,abs(target)), (m,n,j,k,g,source,actual,target)
                    total+=1
    for m in range(2,6):
        for n in range(2,8):
            for s in ['A','B']:
                star=best_gamma(m,n,1.4,1.8,s)
                if m==2 and s=='A':
                    assert star==0
                else:
                    assert star>0
                    assert abs(derivative(m,n,1.4,1.8,star,s))<1e-8
                    t0=mean_formula(m,n,1.4,1.8,star,s)
                    for f in [0.7,1.4]:
                        assert t0<mean_formula(m,n,1.4,1.8,star*f,s)
                total+=1
    a=3; J=1.4; K=1.9; b=40000
    mb=a+1
    for s,v in [('A',math.sqrt(a-1)),('B',math.sqrt(a+2))]:
        opt=best_gamma(mb,b,J,K,s)
        assert abs(opt/(J*math.sqrt(b))-v)<.02
        N=mb+b
        C=N/K+(N-1)*K/(4*J*J*b)
        excess=(mean_formula(mb,b,J,K,opt,s)-C)/math.sqrt(b)
        assert abs(excess-v/J)<.02
        total+=2
    print('PASS: %d full-matrix, convexity and asymptotic checks' % total)

if __name__=='__main__':main()
