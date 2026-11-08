"""Small-field checks of the quadratic-cone self-Fourier singular spectrum.

Requires Python 3 and NumPy. All Fourier matrices are constructed directly.
Checks finite examples only; the accompanying argument proves the general theorem.
"""
import itertools
import numpy as np


def quad_prime(x, p, m, typ):
    if typ == 'split':
        return sum(x[2*j]*x[2*j+1] for j in range(m)) % p
    base = sum(x[2*j]*x[2*j+1] for j in range(m-1))
    u, v = x[-2:]
    if p == 2:
        return (base+u*u+u*v+v*v) % p
    nonsquare = next(d for d in range(2,p) if pow(d,(p-1)//2,p)==p-1)
    return (base+u*u-nonsquare*v*v) % p


def predicted(q, m, typ):
    e = 1 if typ == 'split' else -1
    N = q**(2*m-1)+e*(q-1)*q**(m-1)
    P = (N-1)//(q-1)
    c = (q**(2*m)-1)//(q*q-1)
    b = P*(q-2)
    a = N-b-c
    assert a>0 and c>0 and a+b+c==N
    return N,a,b,c


def prime_check(p,m,typ):
    S = [x for x in itertools.product(range(p),repeat=2*m)
         if quad_prime(x,p,m,typ)==0]
    N,a,b,c = predicted(p,m,typ)
    assert len(S)==N
    B = np.array([[(quad_prime(tuple((u+v)%p for u,v in zip(x,y)),p,m,typ)
                    -quad_prime(x,p,m,typ)-quad_prime(y,p,m,typ))%p
                    for y in S] for x in S],dtype=int)
    F = np.exp(2j*np.pi*B/p)
    eigs = np.linalg.eigvalsh(F@F.conj().T)
    expected = [p**(2*m-2)]*c+[p**(2*m-1)]*b+[p**(2*m)]*a
    assert np.allclose(eigs,expected,atol=1e-8,rtol=1e-9)
    print('PASS prime',p,'dim',2*m,typ,'N',N,'multiplicities',c,b,a)


def f4mul(a,b):
    z=0
    for i in range(2):
        if (b>>i)&1: z^=a<<i
    if z&8: z^=12
    if z&4: z^=7
    return z


def f4sq(a): return f4mul(a,a)
def f4trace(a): return a^f4sq(a)
def quad4(x,typ):
    a,b,c,d=x
    if typ=='split': return f4mul(a,b)^f4mul(c,d)
    return f4mul(a,b)^f4sq(c)^f4mul(c,d)^f4mul(2,f4sq(d))


def extension_check(typ):
    S = [x for x in itertools.product(range(4),repeat=4) if quad4(x,typ)==0]
    N,a,b,c=predicted(4,2,typ)
    assert len(S)==N
    F=np.array([[1 if f4trace(quad4(tuple(u^v for u,v in zip(x,y)),typ)
                                      ^quad4(x,typ)^quad4(y,typ))==0 else -1
                 for y in S] for x in S], dtype=np.int64)
    vals=np.linalg.eigvalsh((F@F.T).astype(float))
    expected=[4**2]*c+[4**3]*b+[4**4]*a
    assert np.allclose(vals,expected,atol=1e-8,rtol=1e-9)
    print('PASS extension F4 dim4',typ,'N',N,'multiplicities',c,b,a)

if __name__=='__main__':
    for p,m in ((2,2),(2,3),(3,2),(5,2)):
        for typ in ('split','nonsplit'):
            prime_check(p,m,typ)
    for typ in ('split','nonsplit'):
        extension_check(typ)
    print('QUADRATIC_CONE_SELF_FOURIER_PASS 10_field_form_cases')
