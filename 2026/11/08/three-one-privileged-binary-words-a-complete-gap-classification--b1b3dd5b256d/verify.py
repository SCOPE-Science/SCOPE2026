"""Independent finite checks for fixed-weight-three privileged binary words.

Python 3.10+. This does not establish the unrestricted theorem; that is
proved by the exhaustive border-type argument in the accompanying text.
"""
from functools import lru_cache
from itertools import combinations
from math import comb
from random import Random

@lru_cache(None)
def direct_privileged(w: str) -> bool:
    if len(w) <= 1:
        return True
    for k in range(1, len(w)):
        b = w[:k]
        if b != w[-k:] or not direct_privileged(b):
            continue
        if sum(w.startswith(b, j) for j in range(len(w)-k+1)) == 2:
            return True
    return False

def three_gap_predicate(a: int, b: int, c: int, d: int) -> bool:
    return a == d and (a > max(b,c) or (b == c and b >= a))

def nonpal_partitions(n: int) -> int:
    m = n-8
    if m < 0:
        return 0
    return 2*sum(1 for x in range(m//2+1)
                 for y in range(m//3+1)
                 if (m-2*x-3*y) >= 0 and (m-2*x-3*y)%4 == 0)

def count_predicted(n: int) -> int:
    return ((n-1)//2 if n%2 else 0) + nonpal_partitions(n)

def word_from_gaps(a,b,c,d):
    return '0'*a+'1'+'0'*b+'1'+'0'*c+'1'+'0'*d

def run():
    trials = 0
    for n in range(3,33):
        ct = npl = 0
        for p,q,r in combinations(range(n),3):
            a,b,c,d = p,q-p-1,r-q-1,n-r-1
            w = word_from_gaps(a,b,c,d)
            direct = direct_privileged(w)
            predicted = three_gap_predicate(a,b,c,d)
            assert direct == predicted, (n, (a,b,c,d), direct, predicted)
            trials += 1
            if direct:
                ct += 1
                if w != w[::-1]: npl += 1
        assert ct == count_predicted(n), (n,ct,count_predicted(n))
        assert npl == nonpal_partitions(n), (n,npl,nonpal_partitions(n))
    # Separate random samples with far larger gap lengths, not a proof.
    rng = Random(12010)
    for _ in range(3000):
        a,b,c,d = (rng.randrange(0,90) for _ in range(4))
        w = word_from_gaps(a,b,c,d)
        assert direct_privileged(w) == three_gap_predicate(a,b,c,d)
    # Fundamental two-one border lemma used by the proof.
    for n in range(2,25):
        for p,q in combinations(range(n),2):
            a,b,c=p,q-p-1,n-q-1
            w='0'*a+'1'+'0'*b+'1'+'0'*c
            assert direct_privileged(w) == (a==c)
    # Dynamic-programming coefficient computation from the proposed GF.
    dp=[0]*701
    dp[0]=1
    for part in (2,3,4):
        for s in range(part,len(dp)):
            dp[s]+=dp[s-part]
    for n in range(3,701):
        assert nonpal_partitions(n) == (2*dp[n-8] if n>=8 else 0)
    print('VERIFY_OK')
    print('three-one exhaustive word tests:',trials)
    print('independent long-word samples:',3000)
    print('two-one lemma exhaustive up to length:',24)
    print('generating function coefficients checked through length:',700)
    print('length 8-20 predicted totals:',[count_predicted(n) for n in range(8,21)])

if __name__ == '__main__':
    run()
