"""Finite-field checks for Nijenhuis operators on split square-zero local algebras.
Usage: python verify.py
All test fields here are prime; the mathematical proof covers arbitrary finite fields.
"""
from itertools import product
from collections import Counter


def mul(a,b,q,n):
    return tuple(sum(a[i*n+k]*b[k*n+j] for k in range(n))%q for i in range(n) for j in range(n))


def vec(a,v,q,n):
    return tuple(sum(a[i*n+j]*v[j] for j in range(n))%q for i in range(n))


def inv(a,q,n):
    m=[[a[i*n+j]%q for j in range(n)]+[int(i==j) for j in range(n)] for i in range(n)]
    for j in range(n):
        p=next((i for i in range(j,n) if m[i][j]),None)
        if p is None:return None
        m[j],m[p]=m[p],m[j]
        z=pow(m[j][j],-1,q)
        m[j]=[(x*z)%q for x in m[j]]
        for i in range(n):
            if i!=j:
                z=m[i][j]
                m[i]=[(x-z*y)%q for x,y in zip(m[i],m[j])]
    return tuple(m[i][n+j] for i in range(n) for j in range(n))


def nij_identity_raw(p,q,n):
    d=n+1
    e=[tuple(int(i==j) for i in range(d)) for j in range(d)]
    def act(x):return tuple(sum(p[i*d+j]*x[j] for j in range(d))%q for i in range(d))
    def product(x,y):return (x[0]*y[0]%q,)+tuple((x[0]*y[j]+y[0]*x[j])%q for j in range(1,d))
    for x in e:
        for y in e:
            nx,ny=act(x),act(y)
            z=product(nx,y);u=product(x,ny);v=act(product(x,y))
            r=tuple((z[i]+u[i]-v[i])%q for i in range(d))
            if product(nx,ny)!=act(r):return False
    return True


def raw_test(q,n):
    d=n+1;raw=0;normal=0
    for p in product(range(q),repeat=d*d):
        ok=nij_identity_raw(p,q,n)
        scalar=p[0]
        f=tuple(p[j] for j in range(1,d))
        w=tuple(p[i*d] for i in range(1,d))
        t=tuple(p[i*d+j] for i in range(1,d) for j in range(1,d))
        special=not any(f) and vec(t,w,q,n)==tuple(scalar*x%q for x in w)
        assert ok==special,(q,n,p)
        raw+=ok; normal+=special
    exp=q*(q**(n*n)+(q**n-1)*q**(n*n-n))
    assert raw==normal==exp,(q,n,raw,normal,exp)
    print(f'RAW q={q} n={n} {raw} exact operators, normal form verified')


def classes(q,n):
    mat=list(product(range(q),repeat=n*n))
    invert=[(a,z) for a in mat if (z:=inv(a,q,n)) is not None]
    orbit_count=0; visited=set(); number=0
    for lam in range(q):
        for t in mat:
            for w in product(range(q),repeat=n):
                if vec(t,w,q,n)!=tuple(lam*x%q for x in w):continue
                number+=1
                key=(lam,t,w)
                if key in visited:continue
                orbit_count+=1
                orbit={(lam,mul(mul(g,t,q,n),gi,q,n),vec(g,w,q,n)) for g,gi in invert}
                assert key in orbit
                visited.update(orbit)
    assert len(visited)==number
    exp=q*(q**(n*n)+(q**n-1)*q**(n*n-n))
    assert exp==number
    print(f'ORBITS q={q} n={n} {number} operators, {orbit_count} classes')
    return orbit_count


def expected_orbits(q,n):
    # [t^k] prod_{j>=1}(1-qt^j)^(-1): enumerate multiplicities of j.
    k=[0]*(n+1);k[0]=1
    for j in range(1,n+1):
        # multiply by (1-qt^j)^(-1) via ascending coin-like recurrence
        for a in range(j,n+1):k[a]+=q*k[a-j]
    return q*sum(k),k


def main():
    for q,n in [(2,1),(3,1),(2,2),(3,2)]:raw_test(q,n)
    for q,n in [(2,1),(3,1),(2,2),(3,2),(2,3)]:
        observed=classes(q,n)
        exp,k=expected_orbits(q,n)
        assert observed==exp,(q,n,observed,exp,k)
    print('VERIFY_OK')
if __name__=='__main__':main()
