#!/usr/bin/env python3
"""Direct finite-field checks for threefold convolution of two nonzero quadratic fibers.

The program checks direct ordered sums against character formulas over prime and
extension fields. The algebraic proof and the Hasse bound, not these finite tests,
justify the theorem over all finite fields.
"""

class Field:
    def __init__(self, prime, modulus=None):
        self.p = prime
        self.mod = modulus or [0, 1]
        self.n = len(self.mod) - 1
        self.q = prime ** self.n
        assert self.mod[-1] == 1
        self.add = [[self._add(a, b) for b in range(self.q)] for a in range(self.q)]
        self.neg = [self._neg(a) for a in range(self.q)]
        self.sub = [[self.add[a][self.neg[b]] for b in range(self.q)] for a in range(self.q)]
        self.mul = [[self._mul(a, b) for b in range(self.q)] for a in range(self.q)]
        self.inv = [0] * self.q
        for a in range(1, self.q):
            v = self.power(a, self.q - 2)
            assert self.mul[a][v] == 1
            self.inv[a] = v
        squares = {self.mul[a][a] for a in range(1, self.q)}
        self.chi = [0 if a == 0 else (1 if a in squares else -1) for a in range(self.q)]
        assert len(squares) == (self.q - 1) // 2
        self.one = 1
        self.two = self.add[1][1]
        self.four = self.mul[self.two][self.two]
        self.three = self.add[1][self.two]
        self.five = self.add[1][self.four]

    def _digits(self, a):
        return [(a // self.p ** i) % self.p for i in range(self.n)]

    def _encode(self, digits):
        return sum((v % self.p) * self.p ** i for i, v in enumerate(digits))

    def _add(self, a, b):
        ad, bd = self._digits(a), self._digits(b)
        return self._encode([(x+y) % self.p for x, y in zip(ad, bd)])

    def _neg(self, a):
        return self._encode([(-x) % self.p for x in self._digits(a)])

    def _mul(self, a, b):
        ad, bd = self._digits(a), self._digits(b)
        conv = [0]*(2*self.n-1)
        for i, u in enumerate(ad):
            for j, v in enumerate(bd):
                conv[i+j] += u*v
        for k in range(len(conv)-1, self.n-1, -1):
            v = conv[k] % self.p
            if v:
                for j in range(self.n):
                    conv[k-self.n+j] -= v*self.mod[j]
        return self._encode(conv[:self.n])

    def power(self, x, n):
        y = 1
        while n:
            if n & 1:
                y = self.mul[y][x]
            x = self.mul[x][x]
            n //= 2
        return y

    def times(self, *vals):
        ans = 1
        for v in vals: ans = self.mul[ans][v]
        return ans

    def plus(self, *vals):
        ans = 0
        for v in vals: ans = self.add[ans][v]
        return ans

    def integer(self, k):
        return k % self.p

    def shell(self, level):
        return [(x, self.mul[level][self.inv[x]]) for x in range(1, self.q)]

    def predicted(self, level, a, b):
        if a == 0 and b == 0:
            return 2 * (self.q - 1)
        if a == 0 or b == 0:
            return 2
        s = self.mul[a][b]
        d11 = self.times(s, self.sub[s][self.four])
        d22 = self.times(s, self.sub[s][self.times(self.four, level)])
        mid = self.plus(self.times(s, s), self.neg[self.times(self.two, s, self.plus(1,level))], self.times(self.sub[1][level], self.sub[1][level]))
        return 4 + self.chi[d11] + self.chi[d22] + 2*self.chi[mid]

    def exceptional(self, level):
        a = self.chi[self.neg[self.three]]
        b = self.chi[self.sub[1][self.times(self.four, level)]]
        c = self.chi[self.times(level, self.sub[level][self.four])]
        return a == b == c == -1

    def count_exceptional(self):
        return sum(self.exceptional(level) for level in range(2, self.q) if level != 1)

    def trace_sum(self):
        out = 0
        for u in range(self.q):
            a = self.sub[1][self.times(self.four, u)]
            b = self.times(u, self.sub[u][self.four])
            out += self.chi[self.mul[a][b]]
        return out


def check_field(F, do_full):
    q = F.q
    levels = list(range(2, q)) if do_full else [2, 3, q-1]
    targets = [(a,b) for a in range(q) for b in range(q)]
    predicted_count = F.count_exceptional()
    if q % 3 != 2:
        assert predicted_count == 0
    elif F.p == 5:
        assert predicted_count == (q-5)//4
    else:
        T = F.trace_sum()
        expected = (q - 5 + 2*F.chi[F.integer(-15)] + T)
        assert expected % 4 == 0 and predicted_count == expected // 4
    tested = 0
    tested_three = 0
    for level in levels:
        if level == 1 or level == 0: continue
        S = F.shell(1) + F.shell(level)
        assert len(S) == 2*(q-1) and len(set(S)) == len(S)
        Sset = set(S)
        # Count ordered pairs directly, without invoking the quadratic discriminant.
        direct = {(a,b):0 for (a,b) in targets}
        for x,y in S:
            for z,w in S:
                at = F.add[x][z]
                bt = F.add[y][w]
                direct[(at,bt)] += 1
        for a,b in targets:
            assert direct[(a,b)] == F.predicted(level,a,b), (q,level,a,b,direct[(a,b)],F.predicted(level,a,b))
        a = F.chi[F.neg[F.three]]
        b = F.chi[F.sub[1][F.times(F.four, level)]]
        c = F.chi[F.times(level, F.sub[level][F.four])]
        triple_origin = sum(direct[(F.neg[x], F.neg[y])] for x,y in S)
        assert triple_origin == (q-1)*(8+2*a+3*b+3*c)
        tested += len(targets)
        if do_full:
            # Threefold: compare the entire output support against the theorem.
            triples = {(a,b):0 for (a,b) in targets}
            for x,y in S:
                for a,b in targets:
                    u = F.sub[a][x]
                    v = F.sub[b][y]
                    triples[(a,b)] += direct[(u,v)]
            for a,b in targets:
                assert (triples[(a,b)] == 0) == (a == 0 and b == 0 and F.exceptional(level)), (q,level,a,b)
            tested_three += len(targets)
    print('field',q,'prime',F.p,'ratios',len(levels),'exceptional',predicted_count,
          'two_sum_fibers',tested,'three_sum_fibers',tested_three,'PASS')


def main():
    specs = [(3,None),(5,None),(7,None),(11,None),(13,None),(17,None),
             (19,None),(23,None),(29,None),(31,None),
             (3,[1,0,1]),(5,[2,0,1]),(7,[1,0,1]),
             (3,[1,2,0,1]),(5,[1,1,0,1])]
    total2 = total3 = 0
    for p,poly in specs:
        F=Field(p,poly)
        check_field(F, do_full=F.q<=17)
    print('All tested direct convolution fibers and exceptional-ratio counts passed.')

if __name__ == '__main__': main()
