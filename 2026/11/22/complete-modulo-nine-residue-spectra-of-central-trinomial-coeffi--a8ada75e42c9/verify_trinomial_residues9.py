"""Exact independent checks of central-trinomial residue formulas modulo nine."""
from collections import Counter
from math import comb


def base3(n):
    if n == 0:
        return '0'
    digits=[]
    while n:
        digits.append(str(n % 3))
        n //= 3
    return ''.join(reversed(digits))


def digit_residue(n):
    word = base3(n)
    twos = [j for j, digit in enumerate(word) if digit == '2']
    if not twos:
        return (1 + 6 * sum(word[i:i+2] == '10' for i in range(len(word)-1))) % 9
    if len(twos) >= 2:
        return 0
    j = twos[0]
    preceding = word[j-1] if j else '0'
    if j == len(word)-1:
        return 3 if preceding == '0' else 6
    return 6 if preceding == '0' else 0


def predicted_counts(L):
    counts = [0] * 9
    for j in range((L+1)//2 + 1):
        if 2*j+1 <= L+1:
            counts[(1 + 6*j) % 9] += comb(L+1, 2*j+1)
    if L == 0:
        pass
    elif L == 1:
        counts[3] = 1
    else:
        counts[3] = 2**(L-2)
        counts[6] = (L+1) * 2**(L-2)
        counts[0] = 3**L - (L+6) * 2**(L-2)
    return counts


def main():
    bound = 3**8
    Tprev, Tcur = 1, 1
    actual = [1]
    for n in range(1, bound):
        actual.append(Tcur % 9)
        next_val = ((2*n + 1) * Tcur + 3*n*Tprev) // (n+1)
        assert ((2*n + 1)*Tcur + 3*n*Tprev) % (n+1) == 0
        Tprev, Tcur = Tcur, next_val
    assert len(actual) == bound
    for n, value in enumerate(actual):
        assert value == digit_residue(n), (n,value,digit_residue(n))
    for L in range(9):
        count = Counter(actual[:3**L])
        predicted = predicted_counts(L)
        assert [count.get(r,0) for r in range(9)] == predicted, (L,count,predicted)
    assert all(actual[n] in {0,1,3,4,6,7} for n in range(bound))
    print('VERIFY_OK exact_terms={} block_censuses=0..8 digit_formula=PASS'.format(bound))

if __name__ == '__main__':
    main()
