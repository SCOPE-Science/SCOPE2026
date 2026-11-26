"""Independent verification of genus-refined word formulas for reflexive ideals."""
from math import comb
from collections import Counter

def rational_coeffs(h, maximum):
    # Expand the derived rational generating function by coefficient recurrence.
    # F(z,u)=(1-uz+(uz)^h)/((1-z)(1-uz)-u^h z^(h+1))
    # polynomial in u, represented as Counter r->coefficient.
    out = [Counter() for _ in range(maximum + 1)]
    for n in range(maximum + 1):
        numerator = Counter({0: int(n == 0)})
        if n == 1: numerator[1] = -1
        if n == h: numerator[h] += 1
        coeffs = Counter(numerator)
        if n >= 1:
            for r, v in out[n-1].items(): coeffs[r] += v; coeffs[r+1] += v
        if n >= 2:
            for r, v in out[n-2].items(): coeffs[r+1] -= v
        if n >= h + 1:
            for r, v in out[n-h-1].items(): coeffs[r+h] += v
        out[n] = Counter({r:v for r,v in coeffs.items() if v})
    return out

def direct_word_count(n,h):
    ans = Counter()
    for word in range(1 << n):
        run = 0
        admissible = True
        for i in range(n):
            if word >> i & 1:
                if 0 < run < h: admissible = False
                run = 0
            else: run += 1
        if 0 < run < h: admissible = False
        if admissible: ans[n-word.bit_count()] += 1
    return ans

def closed(n,h,r):
    if r == 0: return 1
    return sum(comb(r-j*h+j-1,j-1)*comb(n-r+1,j)
               for j in range(1,r//h+1) if 0 <= j <= n-r+1)

for h in range(1,9):
    formal = rational_coeffs(h,16)
    for n in range(17):
        brute = direct_word_count(n,h)
        explicit = Counter({r:closed(n,h,r) for r in range(n+1) if closed(n,h,r)})
        assert brute == explicit == formal[n], (h,n,brute,explicit,formal[n])
print('All binary-word/genus identities verified for h=1..8 and n=0..16.')
print('Selected reflexive-ideal counts (m,h):', {(m,h):1+sum(direct_word_count(m-1,h).values()) for m,h in [(6,2),(7,3),(8,2),(8,3),(8,4)]})
print('VERIFY_OK')
