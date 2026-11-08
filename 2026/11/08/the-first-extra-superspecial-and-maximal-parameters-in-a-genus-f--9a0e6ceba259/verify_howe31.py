"""Exact Hasse-Witt gcd certificate for the genus-five Howe pencil.

No external dependencies: python3 verify_howe31.py.
"""
from math import comb


def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def add(a, b, p):
    return trim([((a[i] if i < len(a) else 0) +
                  (b[i] if i < len(b) else 0)) % p for i in range(max(len(a), len(b)))])


def mul(a, b, p):
    c = [0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j] = (c[i+j]+x*y)%p
    return trim(c)


def divmod_poly(a, b, p):
    a = trim(a); b = trim(b)
    if b == [0]:raise ZeroDivisionError
    q = [0]*max(1, len(a)-len(b)+1)
    r = a[:]
    while r != [0] and len(r) >= len(b):
        d = len(r)-len(b)
        v = r[-1]*pow(b[-1],-1,p)%p
        q[d] = v
        for i, bi in enumerate(b):r[d+i] = (r[d+i]-v*bi)%p
        r = trim(r)
    return trim(q),r


def monic(a, p):
    return trim([(x*pow(a[-1],-1,p))%p for x in a])


def gcd(a,b,p):
    while b != [0]:
        _,r = divmod_poly(a,b,p)
        a,b = b,r
    return monic(a,p)


def direct_coefficient(p,m):
    # f^e=(x^4-1)^e(x^4-a)^e. Set u=x^4.
    e=(p-1)//2
    c=[0]*(e+1)
    for i in range(e+1):
        j=m-i
        if 0<=j<=e:
            c[e-j]=(c[e-j] + comb(e,i)*comb(e,j)*(-1)**(2*e-i-j))%p
    return trim(c)


def recurrence_coefficient(p,m):
    # independently multiply (u^2-(1+a)u+a)^e in F_p[a,u].
    e=(p-1)//2
    basis=[[0],[0,(-1)%p],[1]]
    # coefficient u^0 = a; coefficient u^1=-(1+a); u^2=1
    basis=[[0,1],[-1%p,-1%p],[1]]
    f=[[1]]
    for _ in range(e):
        out=[[0] for _ in range(len(f)+2)]
        for i,old in enumerate(f):
            for j,coef in enumerate(basis):out[i+j]=add(out[i+j],mul(old,coef,p),p)
        f=out
    return f[m]


def run(p, expected):
    m=[(p*i-j)//4 for i,j in ((1,3),(2,2),(3,1))]
    assert all((p*i-j)%4==0 for i,j in ((1,3),(2,2),(3,1)))
    polys=[direct_coefficient(p,k) for k in m]
    assert polys==[recurrence_coefficient(p,k) for k in m]
    g=gcd(gcd(polys[0],polys[1],p),polys[2],p)
    target=[1]
    for root in expected:target=mul(target,[(-root)%p,1],p)
    assert g==target, (p,g,target)
    for root in expected:
        assert all(sum(c*pow(root,i,p) for i,c in enumerate(a))%p==0 for a in polys)
    assert all(sum(c*pow(root,i,p) for i,c in enumerate(g))%p==0 for root in expected)
    print(f'p={p}, positions={m}, degrees={[len(x)-1 for x in polys]}, '
          f'gcd_coeffs={g}, superspecial_parameters={expected}')
    return polys

if __name__=='__main__':
    a=run(7,[6])
    b=run(23,[22])
    c=run(31,[14,20,30])
    assert 14*20%31==1
    print('HOWE31_GCD_CERTIFICATE_PASS')
