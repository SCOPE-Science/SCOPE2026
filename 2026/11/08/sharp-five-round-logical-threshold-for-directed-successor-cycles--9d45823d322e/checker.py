"""Exhaustive first-order rank profiles of directed successor cycles.

Computes exact Hintikka/back-and-forth signatures on every cycle C_n, n<=32.
This is a finite certificate; the accompanying proof handles n>=32 separately.
"""
from functools import lru_cache

class CanonicalTypes:
    def __init__(self):
        self.ids = {}
    def intern(self, record):
        ans = self.ids.get(record)
        if ans is None:
            ans = len(self.ids)
            self.ids[record] = ans
        return ans
    def profile(self, n, maximum_rank=5):
        @lru_cache(None)
        def rec(q, raw):
            if raw and raw[0]:
                # Rotations are automorphisms, and every orbit of a nonempty
                # ordered tuple contains exactly one tuple beginning at zero.
                shift = raw[0]
                return rec(q, tuple((i - shift) % n for i in raw))
            arity = len(raw)
            atoms = tuple((raw[i] == raw[j], (raw[i]+1) % n == raw[j])
                          for i in range(arity) for j in range(arity))
            if q == 0:
                return self.intern((arity, atoms, None))
            extensions = frozenset(rec(q-1, raw+(v,)) for v in range(n))
            return self.intern((arity, atoms, extensions))
        p = tuple(rec(q, ()) for q in range(1, maximum_rank+1))
        print(n, p[-1], 'states', rec.cache_info().currsize, flush=True)
        rec.cache_clear()
        return p

def direct_game(n,m,r):
    # Independent direct minimax EF recursion, intentionally not using types.
    @lru_cache(None)
    def wins(a,b,remaining):
        if any((a[i]==a[j]) != (b[i]==b[j]) or
               (((a[i]+1)%n==a[j]) != ((b[i]+1)%m==b[j]))
               for i in range(len(a)) for j in range(len(a))):
            return False
        if not remaining:
            return True
        for x in range(n):
            if not any(wins(a+(x,), b+(y,), remaining-1) for y in range(m)):
                return False
        for y in range(m):
            if not any(wins(a+(x,), b+(y,), remaining-1) for x in range(n)):
                return False
        return True
    return wins((),(),r)

def main():
    c = CanonicalTypes()
    groups = [{} for _ in range(5)]
    for n in range(1,33):
        p=c.profile(n)
        for j,code in enumerate(p):
            groups[j].setdefault(code,[]).append(n)
    expect = (2,4,7,11,19)
    for q in range(1,6):
        g=list(groups[q-1].values())
        print('rank',q,'classes',g,flush=True)
        assert g==[[n] for n in range(1,expect[q-1])] + [list(range(expect[q-1],33))], (q,g)
    for r in range(1,4):
        for n in range(1,8):
            for m in range(n,8):
                expect_win = (n==m and n<expect[r-1]) or (n>=expect[r-1] and m>=expect[r-1])
                assert direct_game(n,m,r)==expect_win, (n,m,r)
    print('DIRECT_GAME_CHECKS_OK',flush=True)
    print('ALL_CHECKS_OK',flush=True)

if __name__=='__main__': main()
