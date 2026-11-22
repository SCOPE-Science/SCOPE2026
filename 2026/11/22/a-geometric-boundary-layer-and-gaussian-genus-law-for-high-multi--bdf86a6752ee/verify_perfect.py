#!/usr/bin/env python3
"""Standalone exact census verification for high-multiplicity perfect numerical semigroups."""
from collections import defaultdict
from itertools import product
import math

def words_hist(t):
    out = defaultdict(int)
    for bits in product((0, 1), repeat=t):
        if bits[-1] != 0: continue
        # 1=present, 0=gap
        if any(bits[i] == 0 and (i == 0 or bits[i-1] == 1) and (i == t-1 or bits[i+1] == 1) for i in range(t)):
            continue
        out[bits.count(0)] += 1
    return dict(out)

def rational_formula(F):
    out = defaultdict(int)
    out[(F+1, F)] = 1  # ordinary semigroup
    for t in range(2, (F-1)//2 + 1):
        for gap_count, ways in words_hist(t).items():
            out[(F-t, F-t-1+gap_count)] += ways
    return dict(out)

def independent_direct(F):
    out = defaultdict(int)
    for mask in range(1 << (F-1)):
        present = {0} | {i+1 for i in range(F-1) if mask >> i & 1}
        m = min(present-{0}) if present != {0} else F+1
        if 2*m <= F: continue
        if any(a+b <= F and a+b not in present for a in present for b in present):
            continue
        if any((i not in present) and (i-1 in present) and (i+1 in present or i==F)
                for i in range(1,F+1)):
            continue
        genus = F - (len(present)-1)
        out[(m,genus)] += 1
    return dict(out)

def test():
    cells = 0
    for F in range(3,19):
        x = rational_formula(F)
        y = independent_direct(F)
        assert x == y, (F,x,y)
        cells += sum(x.values())
        print(f'F={F:2d} count={sum(x.values()):5d} m_min={min(m for m,g in x):2d}')
    print('PASSED 16 exact independent all-subset semigroup censuses, total counted',cells)
    return True

if __name__=='__main__': test()

def coefficient_moments(max_t):
    # state: counts, first and second raw moments in number of missing symbols
    states = [(1,0,0),(0,0,0),(0,0,0)]
    ans = [(0,0,0)]
    def advance(src, add_zero):
        c,s,q=src
        return (c, s+add_zero*c, q+2*add_zero*s+add_zero*c)
    for t in range(1,max_t+1):
        nxt = [[0,0,0] for _ in range(3)]
        for st in range(3):
            for target,is_zero in ({0:[(0,0),(1,1)],1:[(2,1)],2:[(2,1),(0,0)]}[st]):
                triple=advance(states[st],is_zero)
                for j in range(3): nxt[target][j]+=triple[j]
        states=[tuple(x) for x in nxt]
        ans.append(states[2])
    return ans

def asymptotic_tests():
    import decimal
    from decimal import Decimal
    decimal.getcontext().prec=70
    rho=Decimal('0.5885044113373542')
    v=Decimal('0.2810976123429705')
    lam=Decimal('1.754877666246693')
    cm=coefficient_moments(550)
    for F in (41,101,201,401,1001):
        h=(F-1)//2
        n=1; total_g=F; total_g2=F*F
        weights={0:0}
        for t in range(2,h+1):
            c,s,q=cm[t]
            a=F-t-1
            n+=c;total_g+=a*c+s;total_g2+=a*a*c+2*a*s+q
            weights[h-t]=c
        N=Decimal(n); mean=Decimal(total_g)/N; variance=Decimal(total_g2)/N-mean*mean
        jzero=Decimal(weights[0])/N
        print(f'F={F} total={n} mu/F={mean/Decimal(F):.12f} variance/F={variance/Decimal(F):.12f} P(offset=0)={jzero:.12f}')
        if F>=401:
            assert abs(mean/Decimal(F) - (1+rho)/2)<Decimal('.005')
            assert abs(variance/Decimal(F)-v/2)<Decimal('.005')
            assert abs(jzero-(1-1/lam))<Decimal('.005')
    print('PASSED exact moment recurrence and convergence comparison')

if __name__=='__main__': asymptotic_tests()

def rational_series_test():
    # A(z,u) = u^2 z^2 / ((1-z)(1-uz)-u^2*z^3).
    # Coefficients satisfy A_t=(1+u)A_{t-1}-u A_{t-2}+u^2 A_{t-3},
    # with the sole inhomogeneous input A_2=u^2.
    polynomials = [{}, {}]
    for t in range(2,19):
        out = defaultdict(int)
        if t == 2: out[2] += 1
        for k,c in polynomials[t-1].items():
            out[k] += c
            out[k+1] += c
        for k,c in polynomials[t-2].items(): out[k+1] -= c
        if t>=3:
            for k,c in polynomials[t-3].items(): out[k+2] += c
        poly={k:v for k,v in out.items() if v}
        assert poly == words_hist(t), (t,poly,words_hist(t))
        polynomials.append(poly)
    assert [sum(p.values()) for p in polynomials[2:12]] == [1,2,3,5,9,16,28,49,86,151]
    print('PASSED 17 exact symbolic polynomial recurrences (through t=18)')

if __name__=='__main__': rational_series_test()
