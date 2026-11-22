"""Exact finite checks for top nilpotency of a product in a triangular nilradical."""
from fractions import Fraction
from itertools import product

def formula(n, q):
    assert n >= 3 and q >= 2
    s = Fraction((q-1)**2, q**2)
    if n & 1:
        return s ** ((n-1)//2)
    N = (n-2)//2
    f = 1-s
    eta = 1 - Fraction(q*q, (2*q-1)**2)
    inner = sum((N-d)*s**(N+d-1) for d in range(1, N))
    return 2*s**N-s**(2*N)+Fraction(q-1,q)*f*f*(inner+N*s**(N-1)*eta)

def small_direct(n,q):
    """Enumerate first two bands and calculate top power by multiplication paths."""
    p=n-1;w=n-2; hit=0;tot=0
    for v in product(range(q),repeat=2*p):
        a=[0]+list(v[:p]);b=[0]+list(v[p:]);
        t={i:(a[i]*b[i+1])%q for i in range(1,n-1)}
        if n%2:
            m=(n-1)//2;good=1
            for j in range(m):good=good*t[1+2*j]%q
            hit+=q**(2*w)*bool(good);tot+=q**(2*w);continue
        N=(n-2)//2
        l=r=1
        for j in range(1,N+1): l=l*t[2*j-1]%q;r=r*t[2*j]%q
        if l or r:
            hit+=q**(2*w);tot+=q**(2*w);continue
        for z in product(range(q),repeat=2*w):
            a2=[0]+list(z[:w]);b2=[0]+list(z[w:])
            u={i:(a[i]*b2[i+1]+a2[i]*b[i+2])%q for i in range(1,n-2)}
            corner=0
            for j in range(1,N+1):
                coeff=1
                for h in range(1,j):coeff=coeff*t[2*h-1]%q
                for h in range(j+1,N+1):coeff=coeff*t[2*h]%q
                corner=(corner+coeff*u[2*j-1])%q
            hit+=bool(corner);tot+=1
    return Fraction(hit,tot)

def conditional(n,q):
    """Different enumeration: top-corner linear-form rank, no second bands."""
    assert n%2==0
    N=(n-2)//2; hit=0
    for v in product(range(q),repeat=2*(n-1)):
        a=[0]+list(v[:n-1]);b=[0]+list(v[n-1:])
        t={i:a[i]*b[i+1]%q for i in range(1,n-1)}
        u=w=1
        for j in range(1,N+1):u=u*t[2*j-1]%q;w=w*t[2*j]%q
        if u or w:hit+=q;continue
        nonzero=False
        for j in range(1,N+1):
            c=1
            for h in range(1,j):c=c*t[2*h-1]%q
            for h in range(j+1,N+1):c=c*t[2*h]%q
            if c and (a[2*j-1] or b[2*j+1]):nonzero=True
        hit+=q-1 if nonzero else 0
    return Fraction(hit,q**(2*(n-1)+1))

if __name__=='__main__':
    for n,q in [(3,2),(4,2),(4,3),(6,2)]:
        got=small_direct(n,q)
        want=formula(n,q)
        assert got == want, (n,q,got,want)
        print(f'DIRECT n={n} q={q} probability={got} OK')
    for n,q in [(4,2),(4,3),(6,2),(6,3),(8,2)]:
        got=conditional(n,q);want=formula(n,q)
        assert got == want, (n,q,got,want)
        print(f'LINEAR-FORM n={n} q={q} probability={got} OK')
    print('ALL_CHECKS_PASSED')
