"""Reproducible finite checks for colored-path one-point type extrema.

Run with Python 3.10+: python verify.py
"""
from itertools import product
from collections import Counter

COLORS = (1, 2, 3)
STATES = (0, 1, 2, 3)


def admissible(left, right, old_color):
    return not (left and right and left != right
                and left != old_color and right != old_color)


def direct_count(word):
    """Enumerate all four-state extensions, without using matrices."""
    n = len(word) + 1
    return sum(all(admissible(s[i], s[i+1], word[i]) for i in range(n-1))
               for s in product(STATES, repeat=n))


def transfer_count(word):
    """A separate dynamic-programming implementation."""
    v = [1, 1, 1, 1]
    for c in word:
        v = [sum(v[a] for a in STATES if admissible(a, b, c))
             for b in STATES]
    return sum(v)


def lower_word(e):
    return tuple(1 + (i % 3) for i in range(e))


def max_value(n):
    a, b = 4, 14
    if n == 1:
        return a
    for _ in range(3, n+1):
        a, b = b, 3*b + 2*a
    return b


def matrix_mult(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def mat_pow(a,k):
    z=[[int(i==j) for j in range(len(a))] for i in range(len(a))]
    while k:
        if k & 1:
            z=matrix_mult(z,a)
        a=matrix_mult(a,a)
        k>>=1
    return z


def cycle_matrix():
    t = [[[int(admissible(a,b,c)) for b in STATES] for a in STATES]
         for c in COLORS]
    return matrix_mult(matrix_mult(t[0],t[1]),t[2])


def check_cycle_characteristic():
    q = cycle_matrix()
    identity=[[int(i==j) for j in range(4)] for i in range(4)]
    b=identity
    coeff=[1]
    for k in range(1,5):
        b=matrix_mult(q,b)
        trace=sum(b[i][i] for i in range(4))
        assert trace % k == 0
        c=-trace//k
        coeff.append(c)
        b=[[b[i][j]+c*identity[i][j] for j in range(4)]
           for i in range(4)]
    assert coeff==[1,-42,-23,1,0],coeff


def lower_matrix_count(n):
    m=[]
    for c in COLORS:
        m.append([[int(admissible(a,b,c)) for b in STATES] for a in STATES])
    q=matrix_mult(matrix_mult(m[0],m[1]),m[2])
    e=n-1
    a=mat_pow(q,e//3)
    for i in range(e%3):
        a=matrix_mult(a,m[i])
    return sum(sum(row) for row in a)


def run():
    check_cycle_characteristic()
    checked_direct=0
    checked_words=0
    table=[]
    for n in range(1,12):
        minimum=None; maximum=None; minwords=[]; maxwords=[]
        for w in product(COLORS, repeat=n-1):
            t=transfer_count(w)
            if n<=6:
                assert direct_count(w)==t,(n,w,t)
                checked_direct+=1
            if minimum is None or t<minimum:
                minimum,minwords=t,[w]
            elif t==minimum:
                minwords.append(w)
            if maximum is None or t>maximum:
                maximum,maxwords=t,[w]
            elif t==maximum:
                maxwords.append(w)
            checked_words+=1
        assert maximum==max_value(n)
        assert minimum==lower_matrix_count(n)
        if n>=3:
            expected_min={tuple((p[i%3]) for i in range(n-1))
                          for p in product(COLORS,repeat=3) if len(set(p))==3}
            expected_max={(c,)*(n-1) for c in COLORS}
            assert set(minwords)==expected_min,(n,minwords)
            assert set(maxwords)==expected_max,(n,maxwords)
        else:
            assert minimum==maximum
        table.append((n,minimum,maximum,len(minwords),len(maxwords)))
    # Longer checks independent of exhaustive search over edge-colour assignments.
    for n in range(1,35):
        assert lower_matrix_count(n)==transfer_count(lower_word(n-1))
        assert max_value(n)==transfer_count((1,)*(n-1))
    print('n min max min_optimizers max_optimizers')
    for row in table:
        print(*row)
    print(f'DIRECT_ENUMERATIONS={checked_direct}')
    print(f'COLOR_WORDS={checked_words}')
    print('MATRIX_CHECKS=34')
    print('CYCLE_CHARACTERISTIC=x(x^3-42x^2-23x+1)')
    print('VERIFY_OK')

if __name__ == '__main__':
    run()
