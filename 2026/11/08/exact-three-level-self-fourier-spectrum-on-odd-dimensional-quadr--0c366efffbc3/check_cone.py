"""Finite exact Gram identities and numerical spectra for odd quadratic cones.

Run: python check_cone.py
Uses Python 3 and NumPy. Finite checks are supporting evidence, not an infinite proof.
"""
import itertools
import math
import numpy as np


class Field:
    def __init__(self, order):
        if order == 9:
            self.q = 9
            self.p = 3
        else:
            assert order in (3, 5, 7, 11)
            self.q = order
            self.p = order

    def add(self, x, y):
        if self.q != 9:
            return (x+y) % self.p
        return ((x % 3+y % 3) % 3)+3*((x//3+y//3) % 3)

    def neg(self, x):
        return self.sub(0, x)

    def sub(self, x, y):
        if self.q != 9:
            return (x-y) % self.p
        return ((x % 3-y % 3) % 3)+3*((x//3-y//3) % 3)

    def mul(self, x, y):
        if self.q != 9:
            return x*y % self.p
        a,b = x % 3, x//3
        c,d = y % 3, y//3
        return (a*c+2*b*d) % 3 + 3*((a*d+b*c) % 3)

    def pow(self, x, n):
        y = 1
        for _ in range(n):
            y = self.mul(y, x)
        return y

    def eta(self, x):
        return 0 if x == 0 else (1 if self.pow(x,(self.q-1)//2) == 1 else -1)

    def trace(self, x):
        return 2*(x % 3) % 3 if self.q == 9 else x

    def char(self, x):
        return np.exp(2j*np.pi*self.trace(x)/self.p)


def verify(q, m, a, char_scale=1):
    F = Field(q)
    d = 2*m+1
    def polar(x,y):
        v = F.mul(F.mul(2, a), F.mul(x[-1], y[-1]))
        for j in range(m):
            v = F.add(v, F.add(F.mul(x[2*j], y[2*j+1]), F.mul(x[2*j+1], y[2*j])))
        return v
    def quad(x):
        v = F.mul(a,F.mul(x[-1],x[-1]))
        for j in range(m):
            v=F.add(v,F.mul(x[2*j],x[2*j+1]))
        return v
    cone = [v for v in itertools.product(range(q), repeat=d) if quad(v) == 0]
    n = len(cone)
    assert n == q**(2*m), (q,m,a,n)
    b = np.fromiter((polar(x,y) for x in cone for y in cone), dtype=np.int16, count=n*n).reshape(n,n)
    eta = np.array([F.eta(t) for t in range(q)])
    K = eta[b]
    R = np.zeros((n,n),dtype=np.int16)
    index={x:i for i,x in enumerate(cone)}
    for i,x in enumerate(cone):
        if not any(x):
            continue
        for t in range(1,q):
            y = tuple(F.mul(t,xi) for xi in x)
            R[i,index[y]]=F.eta(t)
    s = F.eta(F.neg(a))
    alpha=q**(2*m-1)*(q-1)
    beta=s*q**(m-1)*(q-1)**2
    assert np.array_equal(K@K,alpha*R+beta*K), f'quadratic kernel identity {q,m,a}'
    gram = q**(2*m)*np.eye(n,dtype=np.int64)+s*q**m*K
    H = np.array([F.char(F.mul(char_scale,int(t))) for t in b.ravel()]).reshape(n,n)
    assert np.max(abs(H.conj().T@H-gram)) < 1e-8*(n+1)
    P=(n-1)//(q-1)
    c=(n-1)//(q*q-1)
    sv=np.sort(np.linalg.svd(H, compute_uv=False))
    target=np.sort([q**(m+.5)]*c+[q**(m-.5)]*(P-c)+[float(q**m)]*(n-P))
    error=float(max(abs(sv-target)))
    assert error<1e-8*(n+1), (q,m,a,error)
    print(f'PASS q={q} m={m} a={a} char_scale={char_scale} size={n} max_singular_error={error:.2e}')


def main():
    cases=[(3,1,1,1),(3,1,2,2),(3,2,1,1),(5,1,1,1),(5,1,2,2),(5,2,1,1),
           (7,1,1,1),(7,1,3,3),(9,1,1,1),(9,1,4,4),(11,1,1,2)]
    for case in cases:
        verify(*case)
    print('ODD_QUADRATIC_CONE_SELF_FOURIER_PASS')

if __name__=='__main__':
    main()
