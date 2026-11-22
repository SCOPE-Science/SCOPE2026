#!/usr/bin/env python3
"""Exact, standalone verification of the marked Picard normal-form census.
Only Python 3 standard library is needed. No remote data and no heuristics.
"""
from collections import Counter, defaultdict
from itertools import product

P = 5
EXPECTED = {-3:10, -2:4, 0:12, 1:8, 3:20, 6:8,
            7:12, 9:16, 10:4, 12:4, 13:2}

def trim(poly):
    poly = [n % P for n in poly]
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly

def remainder(f, g):
    f, g = trim(f), trim(g)
    assert g != [0]
    while f != [0] and len(f) >= len(g):
        coefficient = f[-1] * pow(g[-1], -1, P) % P
        shift = len(f) - len(g)
        for i, t in enumerate(g):
            f[shift + i] = (f[shift + i] - coefficient * t) % P
        f = trim(f)
    return f

def gcd(f, g):
    while trim(g) != [0]:
        f, g = g, remainder(f, g)
    return trim(f)

# Two independent polynomial-basis presentations of the 25-element field.
# z^2=2; t^2=4*t+4 (irreducible t^2+t+1 over F5).
class F25:
    def __init__(self, z2constant, z2linear):
        self.const = z2constant
        self.linear = z2linear
    def plus(self, u, v):
        return (u%5+v%5)%5 + 5*((u//5+v//5)%5)
    def times(self, u, v):
        a,b = u%5,u//5
        c,d = v%5,v//5
        return (a*c+self.const*b*d)%5 + 5*((a*d+b*c+self.linear*b*d)%5)
    def power(self, u, n):
        ans=1
        while n:
            if n&1: ans=self.times(ans,u)
            u=self.times(u,u)
            n//=2
        return ans
    def evalquartic(self, x, a,b,c):
        x2=self.times(x,x)
        x4=self.times(x2,x2)
        return self.plus(self.plus(self.plus(x4,self.times(a,x2)),self.times(b,x)),c)
    def roots_cubed(self):
        return Counter(self.power(y,3) for y in range(25))
    def point_count(self, a,b,c):
        # Directly enumerate all y over the field by the precomputed cube fibers.
        fibers=self.roots_cubed()
        return 1+sum(fibers[self.evalquartic(x,a,b,c)] for x in range(25))
    def character_count(self, a,b,c):
        # Independent mathematical test: nonzero cubes are the roots of v^8=1.
        # Includes exactly one place at infinity.
        ans=1
        for x in range(25):
            v=self.evalquartic(x,a,b,c)
            ans += (1 if v==0 else (3 if self.power(v,8)==1 else 0))
        return ans

def is_squarefree(a,b,c):
    f=[c,b,a,0,1]
    derivative=[b,(2*a)%5,0,4]
    return len(gcd(f,derivative))==1

def discriminant(a,b,c):
    return (256*c**3 - 128*a*a*c*c + 144*a*b*b*c -27*b**4 +
            16*a**4*c -4*a**3*b*b)%5

def main():
    fields=(F25(2,0), F25(4,4))
    for F in fields:
        assert len(F.roots_cubed())==9
        assert sum(F.roots_cubed().values())==25
        assert {F.power(u,3) for u in range(25)}==set(F.roots_cubed())
        for v in range(25):
            assert F.roots_cubed()[v] == (1 if v==0 else (3 if F.power(v,8)==1 else 0))
    types=Counter()
    strata=Counter()
    parameters=defaultdict(list)
    squarefree=0
    for a,b,c in product(range(5),repeat=3):
        nonsingular=is_squarefree(a,b,c)
        assert nonsingular == (discriminant(a,b,c)!=0), (a,b,c)
        if not nonsingular:continue
        squarefree+=1
        n1=1+5 # Every element of F5 has a unique cube root.
        n2=fields[0].point_count(a,b,c)
        assert n2==fields[0].character_count(a,b,c)
        assert n2==fields[1].point_count(a,b,c)
        assert n2==fields[1].character_count(a,b,c)
        assert n1==6
        assert (n2-26)%2==0
        A=(n2-26)//2
        assert -15<=A<=15
        types[A]+=1
        parameters[A].append((a,b,c))
        # Rank-zero known locus is independently compared against the
        # p-adic Newton-polygon prediction from the exact zeta polynomial.
        rankzero=(c*c+a*a*c+a*b*b)%5==0
        assert rankzero==(A%5==0), (a,b,c,A)
        strata[(A,rankzero)]+=1
        # The candidate zeta polynomial is 1+A*T^2+5*A*T^4+125*T^6.
        # P(1) equals the rational Jacobian order and is positive.
        assert (126+6*A)>0
    assert squarefree==100
    assert dict(types)==EXPECTED, dict(types)
    assert sum(n for (a,rankzero),n in strata.items() if rankzero)==16
    assert sum(n for (a,rankzero),n in strata.items() if not rankzero)==84
    assert sum(types.values())==100
    print('PICARD_F5_11_WEIL_TYPES_VERIFIED smooth=100 singular=25 types=11 rank0=16 rank2=84')
    print('A N25 count rank')
    for A in sorted(types):
        print(A,26+2*A,types[A], 0 if A%5==0 else 2)

if __name__=='__main__':
    main()
