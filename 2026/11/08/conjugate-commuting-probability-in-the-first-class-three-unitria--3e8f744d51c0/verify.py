#!/usr/bin/env python3
"""Exhaustive independent finite-field checks for a conjugate-commuting-pair law."""
from itertools import product

class Field:
    def __init__(self, q):
        assert q in (2, 3, 4)
        self.q = q
    def add(self, x, y):
        return x ^ y if self.q == 4 else (x + y) % self.q
    def neg(self, x):
        return x if self.q == 4 else (-x) % self.q
    def sub(self, x, y):
        return self.add(x, self.neg(y))
    def mul(self, x, y):
        if self.q != 4:
            return x * y % self.q
        z = 0
        for i in range(2):
            for j in range(2):
                if (x >> i) & 1 and (y >> j) & 1:
                    z ^= 1 << (i + j)
        if z & 8: z ^= 0b1110  # x^3=x(x+1)=x^2+x
        if z & 4: z ^= 0b111  # x^2=x+1
        return z


def mul_group(x, y, F):
    a,b,c,d,e,f = x
    A,B,C,D,E,H = y
    p, s = F.add, F.mul
    return (p(a,A),p(b,B),p(c,C),p(p(d,D),s(a,B)),
            p(p(e,E),s(b,C)),p(p(p(f,H),s(a,E)),s(d,C)))


def inverse_group(x,F):
    a,b,c,d,e,f=x
    p,m,n=F.add,F.mul,F.neg
    return (n(a),n(b),n(c),p(m(a,b),n(d)),p(m(b,c),n(e)),
            p(p(n(f),m(a,e)),p(m(d,c),n(m(m(a,b),c)))))


def independent_brute_q2():
    F=Field(2)
    elems=list(product(range(2),repeat=6))
    gens=[(a,b,c,0,0,0) for a,b,c in product(range(2),repeat=3)]
    n=0
    for x in elems:
        for y in elems:
            ok=False
            for h in gens:
                hyh=mul_group(mul_group(h,y,F),inverse_group(h,F),F)
                if mul_group(x,hyh,F)==mul_group(hyh,x,F):
                    ok=True
                    break
            n+=ok
    return n


def check_field(q):
    F=Field(q)
    el=tuple(range(q))
    triples=list(product(el,repeat=3))
    p,m,s,n=F.add,F.mul,F.sub,F.neg
    favorable=commuting=primary=fullcase=partialcase=0
    for a,b,c in triples:
        for A,B,C in triples:
            if s(m(a,B),m(A,b)) != 0 or s(m(b,C),m(B,c)) != 0: continue
            primary+=1
            # Enumerate all actual changes in the (1,3),(2,4) entries
            # produced by conjugating the second matrix.
            reachable=set()
            for u,v,w in triples:
                dd=s(m(A,v),m(u,B))
                ee=s(m(B,w),m(v,C))
                reachable.add(s(m(a,ee),m(c,dd)))
            if len(reachable)==q: fullcase+=1
            else:
                assert reachable=={0}; partialcase+=1
            for d,e,D,E in product(el,repeat=4):
                K=s(p(m(a,E),m(d,C)),p(m(A,e),m(D,c)))
                commuting += K == 0
                favorable += n(K) in reachable
    expected_fav=q**3*(2*q**5-3*q**4+3*q**3+2*q**2-4*q+1)
    expected_com=q**5*(2*q**2+q-2)
    assert favorable == expected_fav, (q, favorable, expected_fav)
    assert commuting == expected_com, (q, commuting, expected_com)
    assert primary == fullcase+partialcase
    assert (fullcase,partialcase) == ((q*q-1)*(q-1)*(2*q-1), (q-1)*(q+1)*(3*q-1)+q*q)
    print(f'q={q}: primary={primary}, full={fullcase}, partial={partialcase}, '
          f'favorable_pairs={favorable*q*q}, commuting_pairs={commuting*q*q}: PASS')

if __name__=='__main__':
    for q in (2,3,4):check_field(q)
    assert independent_brute_q2()==2**5*(2*2**5-3*2**4+3*2**3+2*2**2-4*2+1)
    print('q=2: independently enumerated literal group multiplication and conjugation: PASS')
    print('ALL_UT4_CONJUGATE_COMMUTING_CHECKS_PASS')
