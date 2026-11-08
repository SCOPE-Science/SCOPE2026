"""Independent finite-algebra checks for Frobenius-height automorphisms.

Requires only Python 3's standard library.  Polynomial multiplication and
literal substitution are used for the exhaustive small cases.
"""
from itertools import product
from math import gcd

class Field:
    def __init__(self, q):
        assert q in (2, 3, 4)
        self.q = q
        self.p = 3 if q == 3 else 2
    def add(self, a, b):
        return (a + b) % 3 if self.q == 3 else a ^ b
    def neg(self, a):
        return (-a) % 3 if self.q == 3 else a
    def mul(self, a, b):
        if self.q != 4:
            return (a * b) % self.q
        v = 0
        for i in range(2):
            for j in range(2):
                if ((a >> i) & 1) and ((b >> j) & 1):
                    v ^= 1 << (i + j)
        if v & 8:
            v ^= 0b1110
        if v & 4:
            v ^= 0b111
        return v
    def pow(self, a, k):
        r = 1
        for _ in range(k):
            r = self.mul(r, a)
        return r
    def inv(self, a):
        assert a
        for b in range(1, self.q):
            if self.mul(a, b) == 1:
                return b
        raise AssertionError('nonfield')

class Ring:
    def __init__(self, q, heights):
        self.F = Field(q)
        self.hs = tuple(heights)
        self.rs = tuple(self.F.p**s for s in heights)
        self.mons = list(product(*(range(r) for r in self.rs)))
        self.where = {v:i for i,v in enumerate(self.mons)}
        self.N = len(self.mons)
        self.unit = self.monomial((0,)*len(heights))
        self.xs = [self.monomial(tuple(int(j == i) for j in range(len(heights)))) for i in range(len(heights))]
        self.soc = self.monomial(tuple(r-1 for r in self.rs))
        self.soc_idx = self.where[tuple(r-1 for r in self.rs)]
        self.mul_table = []
        for a in self.mons:
            self.mul_table.append([
                self.where.get(tuple(u+v for u,v in zip(a,b)), -1)
                if all(u+v<r for u,v,r in zip(a,b,self.rs)) else -1
                for b in self.mons])
    def monomial(self, mon):
        arr = [0]*self.N
        arr[self.where[mon]] = 1
        return tuple(arr)
    def mul(self, a, b):
        F = self.F
        c = [0]*self.N
        for i, x in enumerate(a):
            if not x: continue
            for j, y in enumerate(b):
                if not y: continue
                z = self.mul_table[i][j]
                if z>=0:
                    c[z] = F.add(c[z], F.mul(x,y))
        return tuple(c)
    def power(self, a, n):
        c = self.unit
        for _ in range(n):
            c = self.mul(c,a)
        return c
    def substitution_matrix(self, images):
        cols = []
        for mon in self.mons:
            c = self.unit
            for i, exponent in enumerate(mon):
                for _ in range(exponent):
                    c = self.mul(c, images[i])
            cols.append(c)
        return cols

def rank(cols, F):
    M = [list(row) for row in zip(*cols)]
    nr = len(M); nc = len(cols)
    row = 0
    for col in range(nc):
        at = next((i for i in range(row,nr) if M[i][col]),None)
        if at is None: continue
        M[row],M[at] = M[at],M[row]
        inverse = F.inv(M[row][col])
        M[row] = [F.mul(inverse,x) for x in M[row]]
        for j in range(nr):
            if j==row or not M[j][col]: continue
            coeff = M[j][col]
            M[j] = [F.add(x,F.neg(F.mul(coeff,y))) for x,y in zip(M[j],M[row])]
        row +=1
        if row==nr: break
    return row

def formula(q, heights):
    p = 3 if q==3 else 2
    D = p**sum(heights)
    groups = {h:heights.count(h) for h in set(heights)}
    K = [D - p**sum(max(v-h,0) for v in heights) for h in heights]
    gl = lambda n: __import__('math').prod(q**n-q**j for j in range(n))
    return q**(sum(K)-sum(v*v for v in groups.values())) * __import__('math').prod(gl(v) for v in groups.values())

def brute(q, heights):
    A = Ring(q,heights)
    d=len(heights); N=A.N
    choices=[]
    for h in heights:
        allowed=[]
        for coeffs in product(range(q),repeat=N-1):
            vec=(0,)+coeffs
            if A.power(vec, A.F.p**h) == (0,)*N:
                allowed.append(vec)
        choices.append(allowed)
    num=0; tangent_num=0; multipliers=set()
    for imgs in product(*choices):
        if A.substitution_matrix is None: raise AssertionError()
        tangent = [[imgs[i][A.where[tuple(int(z==j) for z in range(d))]] for i in range(d)] for j in range(d)]
        tcols = [tuple(tangent[j][i] for j in range(d)) for i in range(d)]
        if rank(tcols, A.F)==d:
            tangent_num +=1
        whole = A.substitution_matrix(imgs)
        if rank(whole,A.F) == N:
            assert rank(tcols,A.F)==d
            num+=1
            soc_image=A.substitution_matrix(imgs)[A.soc_idx]
            assert all((v==0) for i,v in enumerate(soc_image) if i!=A.soc_idx)
            multipliers.add(soc_image[A.soc_idx])
    assert num==tangent_num
    expected=formula(q,heights)
    assert num==expected,(q,heights,num,expected)
    e=2 if q==4 else 1
    g=gcd(e,*heights)
    expected_image=(q-1)//(A.F.p**g-1)
    assert len(multipliers)==expected_image,(q,heights,multipliers,expected_image)
    print(f'EXHAUSTIVE_OK field={q} heights={heights} images={[len(c) for c in choices]} automorphisms={num} socle_multiplier_count={len(multipliers)}')

if __name__=='__main__':
    for q,heights in ((2,(1,)),(2,(2,)),(2,(1,1)),(2,(1,2)),(3,(1,)),(4,(1,)),(4,(2,)),(4,(1,1))):
        brute(q, heights)
    print('VERIFY_OK')
