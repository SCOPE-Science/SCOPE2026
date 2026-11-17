"""Exact integer-polynomial and expected-value checks."""
from fractions import Fraction

def calc(m):
    # coefficient count via products: 1 + sum_{k=1}^m q^k prod_{i<k}(1+q^(2i))
    poly = {0:1}
    prefix = {0:1}
    for k in range(1,m+1):
        for deg,coef in prefix.items():
            poly[k+deg] = poly.get(k+deg,0) + coef
        prefix_next = prefix.copy()
        for deg,coef in prefix.items():
            prefix_next[deg+2*k] = prefix_next.get(deg+2*k,0)+coef
        prefix = prefix_next
    brute = {}
    for mask in range(1<<m):
        marked = [j for j in range(1,m+1) if mask & (1<<(j-1))]
        t = 0 if not marked else 2*sum(marked)-max(marked)
        brute[t] = brute.get(t,0)+1
    assert poly == brute
    mean = Fraction(sum(d*c for d,c in poly.items()),1<<m)
    assert mean == Fraction(m*m-m+2,2)-Fraction(1,1<<m)
    return poly,mean

if __name__ == '__main__':
    for m in range(1,18):
        p,mean = calc(m)
        if m<=6: print(f'm={m}, mean={mean}, counts={dict(sorted(p.items()))}')
        else: print(f'm={m}, mean={mean}, count={sum(p.values())}')
    print('POLYNOMIAL CHECKS PASS')
