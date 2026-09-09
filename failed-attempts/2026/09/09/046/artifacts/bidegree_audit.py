"""Bidegree legality + May-Ravenel monomial enumeration for lane-395 target.

Conventions (verified against Beaudry et al. 1909.13379 and Ravenel [Rav77]):
- ANSS: E_r^{s,t} => pi_{t-s}; stem = t-s. d_r: (s,t)->(s+r,t+r-1),
  so (stem,filt): (34,2)->(33,5) is Delta=(-1,+3): a d3. LEGAL.
- Good-complex (May-Ravenel E1) stems: |h_{j,0}|=2(2^j-1), |h_{j,1}|=2|h_{j,0}|,
  |v2|=6; stem contribution = internal - filtration(1 per h).
  h30:13, h40:29, h50:61, eh21/h21:11, h31:27, eh41/h41:59.
"""
from itertools import product

ST = {'h30':13,'h40':29,'h50':61,'h21':11,'h31':27,'h41':59}

def enum(filt, stem, m_min=0, m_max=8, gens=None):
    gens = gens or list(ST)
    sols = []
    def rec(i, nleft, s, combo):
        if i == len(gens):
            if nleft == 0 and (stem - s) % 6 == 0:
                m = (stem - s)//6
                if m_min <= m <= m_max:
                    sols.append((dict(combo), s, m))
            return
        for e in range(nleft+1):
            combo.append((gens[i], e))
            rec(i+1, nleft-e, s+ST[gens[i]]*e, combo)
            combo.pop()
    rec(0, filt, 0, [])
    return sols

if __name__ == '__main__':
    # d3 legality
    x, y = (34,2), (33,5)
    assert (y[0]-x[0], y[1]-x[1]) == (-1,3), "not a d3"
    print("d3 bidegree legal: Delta=(stem -1, filt +3)")
    print("(audit plan text '(-1,+2)' is a typo; admission review says (-1,+3), correct)")
    s34 = enum(2, 34)
    print(f"\nMay-Ravenel monomials at (stem34,filt2), m>=0: {len(s34)}")
    for c,s,m in s34: print("  ", c, f"stem0={s}", f"m={m}")
    s33 = enum(5, 33)
    print(f"\nMay-Ravenel monomials at (stem33,filt5), m>=0: {len(s33)}")
    for c,s,m in s33: print("  ", c, f"stem0={s}", f"m={m}")
    # localized at (34,2): allow m<0
    s34l = enum(2, 34, m_min=-3)
    print(f"\nMay-Ravenel monomials at (stem34,filt2), m>=-3: {len(s34l)}")
    for c,s,m in s34l: print("  ", c, f"stem0={s}", f"m={m}")
    # localized ANSS E2 inventory (Beaudry (8.5.3)): F2[v2^+-1] x E[h30,e21,h31,e41]
    print("\nLocalized ANSS E2 (8.5.3) basis stems: h30=13 e21=11 h31=27 e41=59 v2=6")
    print(" (34,2) localized: v2^-1 h30 h31 (40-6=34). (33,5): EMPTY (max exterior rank 4).")
