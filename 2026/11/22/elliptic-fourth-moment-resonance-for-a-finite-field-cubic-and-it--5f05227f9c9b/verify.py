"""Independent finite-field enumeration for the cubic-graph/tangent-line moment theorem.
Run: python3 verify.py. Requires only Python's standard library.
"""
from collections import Counter


class Field:
    def __init__(self, p, degree=1):
        self.p, self.degree = p, degree
        self.q = p ** degree
        self.d = None
        if degree == 2:
            self.d = next(x for x in range(2, p) if pow(x, (p - 1) // 2, p) == p - 1)
        assert degree in (1, 2)

    def add(self, x, y):
        p = self.p
        if self.degree == 1:
            return (x + y) % p
        return ((x % p + y % p) % p) + p * ((x // p + y // p) % p)

    def sub(self, x, y):
        p = self.p
        if self.degree == 1:
            return (x - y) % p
        return ((x % p - y % p) % p) + p * ((x // p - y // p) % p)

    def mul(self, x, y):
        p = self.p
        if self.degree == 1:
            return x * y % p
        a, b = x % p, x // p
        c, e = y % p, y // p
        return ((a * c + self.d * b * e) % p) + p * ((a * e + b * c) % p)

    def power(self, x, n):
        z = 1
        while n:
            if n & 1:
                z = self.mul(z, x)
            x = self.mul(x, x)
            n //= 2
        return z

    def inv(self, x):
        assert x != 0
        return self.power(x, self.q - 2)

    def chi(self, x):
        if not x:
            return 0
        return 1 if self.power(x, (self.q - 1)//2) == 1 else -1


def run_case(p, degree):
    f = Field(p, degree)
    q = f.q
    cube = [f.power(x, 3) for x in range(q)]
    C = {(x, cube[x]) for x in range(q)}
    L = {(x, 0) for x in range(q)}
    S = C | L
    assert len(S) == 2*q-1
    direct = Counter((f.add(x[0], y[0]), f.add(x[1], y[1])) for x in S for y in S)
    assert sum(direct.values()) == (2*q-1)**2
    actual = sum(v*v for v in direct.values())
    if p == 3:
        expected = 2*q**3 + 6*q*q - 12*q + 5
        for x in range(q):
            for y in range(q):
                v = (2*q-1 if (x,y)==(0,0) else (q if (x,y) in S else 2))
                assert direct[(x,y)] == v, (p,degree,x,y)
    else:
        c = f.chi(f.sub(0,3%p))
        g = 3 if q%3==1 else 1
        inv3 = f.inv(3)
        n = Counter(cube)
        T = sum(f.chi(f.mul(f.sub(f.mul(4%p,cube[u]),1),inv3)) for u in range(q))
        assert c == (1 if q%3==1 else -1)
        expected = (q**3 + 11*q*q - 21*q + 10
                    +2*(q-1)*(q-2)*(c+2*g)+4*(q-1)*T)
        if q%3==2:
            assert T == 0
            assert expected == q**3+13*q*q-27*q+14
        else:
            assert expected == q**3+25*q*q-63*q+38+4*(q-1)*T
        for x in range(q):
            for y in range(q):
                if x == 0:
                    v = (2*q-1 if y==0 else 2*n[y])
                elif y == 0:
                    v = q+1+c
                else:
                    z = f.mul(y, f.inv(cube[x]))
                    dz = f.mul(f.sub(f.mul(4%p,z),1),inv3)
                    v = 1 + f.chi(dz) + 2*n[z] - 2*(z==1)
                assert direct[(x,y)] == v, (p,degree,x,y,v,direct[(x,y)])
        if degree == 2:
            base = Field(p)
            T0 = sum(base.chi(base.mul(base.sub(base.mul(4%p,base.power(u,3)),1),base.inv(3))) for u in range(p))
            # E_ell: a_(p^2)=a_p^2-2p and T_q=-a_q.
            assert T == 2*p-T0*T0, (p,T,T0)
    assert actual == expected, (p,degree,actual,expected)
    return actual


def main():
    primes = (3,5,7,11,13,17,19,23,29,31,37,41,43,47)
    for p in primes:
        run_case(p,1)
    extension = (3,5,7,11)
    for p in extension:
        run_case(p,2)
    print('VERIFY_OK prime_cases=14 quadratic_extension_cases=4 exact_fibers=yes max_order=121')

if __name__=='__main__':
    main()
