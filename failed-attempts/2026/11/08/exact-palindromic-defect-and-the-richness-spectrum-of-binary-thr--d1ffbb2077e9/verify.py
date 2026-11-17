"""Independent finite checks for the three-one palindromic-defect theorem.

Run: python3 verify.py
Uses only the Python standard library. These checks do not replace the
all-length argument in RESULT.md.
"""
from collections import Counter
from itertools import combinations, product
from math import comb
from fractions import Fraction


def actual_defect(w):
    # Independent definition: enumerate distinct literal palindrome factors.
    palindromes = set()
    for center2 in range(2 * len(w) - 1):
        left = center2 // 2
        right = (center2 + 1) // 2
        while left >= 0 and right < len(w) and w[left] == w[right]:
            palindromes.add(w[left:right + 1])
            left -= 1
            right += 1
    return len(w) - len(palindromes)


def predicted_defect(a, b, c, d):
    return 0 if b == c else max(0, min(a, d) - max(b, c))


def palate_formula(a, b, c, d):
    z = max(a,b,c,d)
    one = 1 + max(min(a,b), min(b,c), min(c,d))
    if b == c:
        two = 1 + max(min(a,c), min(b,d))
        three = 1 + min(a,d)
    else:
        two = 2 + min(a,c) + min(b,d)
        three = 0
    return z + one + two + three


def coeff_h(max_k):
    # H(z) = 1 / ((1-z)(1-z^3)(1-z^4)).
    h = [0] * (max_k + 1)
    h[0] = 1
    for step in (1, 3, 4):
        for k in range(step,max_k+1):
            h[k] += h[k-step]
    return h


def count_r(n,r,h):
    k=n-6-2*r
    if k<0:return 0
    return 2*(h[k]+(h[k-1] if k>0 else 0))


def main():
    max_n=34
    h=coeff_h(max_n)
    tested=0
    for n in range(3,max_n+1):
        counts=Counter()
        for pos in combinations(range(n), 3):
            a=pos[0]
            b=pos[1]-pos[0]-1
            c=pos[2]-pos[1]-1
            d=n-pos[2]-1
            w='0'*a+'1'+'0'*b+'1'+'0'*c+'1'+'0'*d
            observed=actual_defect(w)
            assert observed == predicted_defect(a,b,c,d), (w,observed)
            assert n-observed == palate_formula(a,b,c,d), (w,'pal classes')
            counts[observed]+=1
            tested+=1
        assert sum(counts.values()) == comb(n,3)
        for r in range(1,n+1):
            assert counts[r] == count_r(n,r,h), (n,r,counts[r],count_r(n,r,h))
        if n>=8:
            assert max(counts)==(n-6)//2
        else:
            assert max(counts)==0
    # Independent finite verification of the max/min identity for long runs.
    for a,b,c,d in product(range(18), repeat=4):
        n=a+b+c+d+3
        assert n-palate_formula(a,b,c,d)==predicted_defect(a,b,c,d)
    # Check limiting density mass, first and second raw moments exactly.
    # Integration of t^k(1-2t)^2 from 0 to 1/2.
    def moment(k):
        return (Fraction(1,2)**(k+1)/Fraction(k+1)
                -4*Fraction(1,2)**(k+2)/Fraction(k+2)
                +4*Fraction(1,2)**(k+3)/Fraction(k+3))
    assert moment(0)==Fraction(1,6)
    assert moment(1)==Fraction(1,48)
    assert moment(2)==Fraction(1,240)
    assert moment(2)-moment(1)**2==Fraction(43,11520)
    print('VERIFY_OK',tested,'direct words; 18^4 algebra tuples; rational moments')


if __name__ == '__main__':
    main()
