"""Independent finite-interval tests of the ray-unitization automorphism law."""
from itertools import product
from random import Random

def verify(p,m,c,l):
    # m arrows, m+1 vertices, basis 1,e_0,...,e_m,a_0,...,a_{m-1}.
    N=2*m+2
    one=0
    def E(i): return i+1
    def A(i): return m+2+i
    def mul_basis(i,j):
        if i==0: return {j:1}
        if j==0: return {i:1}
        if 1<=i<=m+1 and 1<=j<=m+1:
            return {i:1} if i==j else {}
        if 1<=i<=m+1 and j>=m+2:
            return {j:1} if i == (j-(m+2))+1 else {}
        if i>=m+2 and 1<=j<=m+1:
            return {i:1} if j == (i-(m+2))+2 else {}
        return {}
    def scalar(coeffs): return [v%p for v in coeffs]
    def plus(x,y): return [(a+b)%p for a,b in zip(x,y)]
    def mm(x,y):
        z=[0]*N
        for i,xi in enumerate(x):
            if xi:
                for j,yj in enumerate(y):
                    if yj:
                        for k,t in mul_basis(i,j).items(): z[k]=(z[k]+xi*yj*t)%p
        return z
    basis=[]
    for i in range(N):
        b=[0]*N;b[i]=1;basis.append(b)
    images=[]
    images.append(basis[0])
    for i in range(m+1):
        x=basis[E(i)].copy()
        if i>0:x[A(i-1)]=(x[A(i-1)]+c[i-1])%p
        if i<m:x[A(i)]=(x[A(i)]-c[i])%p
        images.append(x)
    for i in range(m):
        x=[0]*N; x[A(i)]=l[i]
        images.append(x)
    def phi(x):
        z=[0]*N
        for coeff,im in zip(x,images):
            z=plus(z,[(coeff*e)%p for e in im])
        return z
    for i in range(N):
        for j in range(N):
            assert phi(mm(basis[i],basis[j])) == mm(images[i],images[j]), (p,m,c,l,i,j)
    ci=[(-c[i]*pow(l[i],-1,p))%p for i in range(m)]
    li=[pow(l[i],-1,p) for i in range(m)]
    for i in range(m):
        assert (c[i]+l[i]*ci[i])%p==0
    inv=[]
    inv.append(basis[0])
    for i in range(m+1):
        x=basis[E(i)].copy()
        if i>0:x[A(i-1)]=(x[A(i-1)]+ci[i-1])%p
        if i<m:x[A(i)]=(x[A(i)]-ci[i])%p
        inv.append(x)
    for i in range(m):
        x=[0]*N;x[A(i)]=li[i];inv.append(x)
    def invphi(x):
        z=[0]*N
        for coeff,im in zip(x,inv):
            z=plus(z,[(coeff*e)%p for e in im])
        return z
    for b in basis:
        assert phi(invphi(b))==b and invphi(phi(b))==b
    # Construct inner implementer for finite parameters, with diagonal tail 1.
    d=[1]*(m+1)
    for i in range(m-1,-1,-1):d[i]=(l[i]*d[i+1])%p
    s=[(c[i]*d[i+1])%p for i in range(m)]
    u=basis[0].copy()
    for i in range(m+1):u[E(i)]=(d[i]-1)%p
    for i in range(m):u[A(i)]=s[i]
    # finite truncation diagonal d as 1+ sum (d_i-1)e_i; finite support on infinite ray.
    v=basis[0].copy()
    for i in range(m+1):v[E(i)]=(pow(d[i],-1,p)-1)%p
    for i in range(m):v[A(i)]=(-s[i]*pow(d[i],-1,p)*pow(d[i+1],-1,p))%p
    assert mm(u,v)==basis[0] and mm(v,u)==basis[0]
    for b in basis:
        assert mm(mm(u,b),v)==phi(b), ('inner fail',p,m,c,l)
    return True

def run():
    runs=0
    for p,m in ((2,4),(3,3),(5,2)):
        for c in product(range(p),repeat=m):
            for l in product(range(1,p),repeat=m):
                verify(p,m,c,l);runs+=1
    rng=Random(20261120)
    for p,m in ((5,8),(7,7),(11,6)):
        for _ in range(100):
            c=[rng.randrange(p) for i in range(m)]
            l=[rng.randrange(1,p) for i in range(m)]
            verify(p,m,c,l);runs+=1
    print(f'INFINITE_RAY_UNITIZATION_AUTOMORPHISMS_OK cases={runs}')
if __name__=='__main__':run()
