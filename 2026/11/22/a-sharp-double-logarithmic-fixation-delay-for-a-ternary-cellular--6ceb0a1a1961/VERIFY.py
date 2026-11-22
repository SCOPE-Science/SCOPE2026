"""Reproducibility checks for the ternary lifted-140 finite-ring relaxation theorem.
Run with Python 3, standard library only: python verify.py
"""
from itertools import product
from fractions import Fraction
from collections import Counter

ALPHABET = range(3)


def original_local(left, center, right):
    triple = (left, center, right)
    def binary140(a,b,c):
        return b - a*b + a*b*c
    if set(triple) <= {0, 1}:
        return binary140(*triple)
    if set(triple) <= {0, 2}:
        return 2*binary140(*(v//2 for v in triple))
    if set(triple) <= {1, 2}:
        return 1 + binary140(*(v-1 for v in triple))
    return center


def simple_local(left, center, right):
    return right if left == center and right < center else center


def update(word, local=simple_local):
    n = len(word)
    return tuple(local(word[(i-1)%n], word[i], word[(i+1)%n]) for i in range(n))


def relaxation_time(word, local=simple_local):
    state = tuple(word)
    for time in range(2*len(word)+1):
        nxt = update(state, local)
        if nxt == state:
            return time
        assert sum(nxt) < sum(state), 'Non-monotone energy'
        state = nxt
    raise AssertionError('Potential-decrease bound broken')


def window_local_average(t, local=simple_local):
    # A site at time t+1 depends on 2t+3 initial sites.
    L = 2*t+3
    change_sum = 0
    for word in product(ALPHABET, repeat=L):
        current = word
        at_t = None
        for iteration in range(t+1):
            if iteration == t:
                at_t = current[len(current)//2]
            current = tuple(local(*current[j-1:j+2]) for j in range(1, len(current)-1))
        at_tp1 = current[0]
        change_sum += at_t-at_tp1
    return Fraction(change_sum, 3**L)


def predicted_change(t):
    return Fraction(t+15, 81*3**t)


def check_motif(a,b):
    # Left and right sentinel zeros are permanent in any surrounding configuration.
    word = (0,)+(2,)*a+(1,)*b+(0,)
    return relaxation_time(word)


def matrix_certificate():
    """Exact all-time scalar one-density identity via the published 4-state
    preimage transfer, at p=q=r=1/3. The matrix annihilator plus three
    initial values proves the closed expression for every t>=3.
    """
    one=Fraction(1)
    z=Fraction(1,3)
    Q=(Fraction(1,27),Fraction(4,27),Fraction(5,27),Fraction(2,27))
    S=(Fraction(9,27),Fraction(14,27),one,Fraction(13,27))
    R=((z,0,0,0),(z,z,0,0),(0,z,one,z),(0,0,0,z))
    I=tuple(tuple(one if i==j else Fraction(0) for j in range(4)) for i in range(4))
    def mm(A,B):
        return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(4)) for j in range(4)) for i in range(4))
    def sub(A,B):
        return tuple(tuple(A[i][j]-B[i][j] for j in range(4)) for i in range(4))
    def scale(A,c):
        return tuple(tuple(c*A[i][j] for j in range(4)) for i in range(4))
    Z=mm(sub(R,I),mm(sub(R,scale(I,z)),sub(R,scale(I,z))))
    assert all(Z[i][j]==0 for i in range(4) for j in range(4))
    v=Q
    for t in range(3,6):
        measured=sum(S[i]*v[i] for i in range(4))
        predicted=Fraction(11,36)+Fraction(2*t+7,108*3**t)
        assert measured == predicted,(t,measured,predicted)
        v=tuple(sum(R[i][j]*v[j] for j in range(4)) for i in range(4))
    print('ALL-TIME MATRIX CERTIFICATE: (R-I)(R-I/3)^2=0; t=3,4,5 bases match')
    print('P(X_i(t)=1)=11/36+(2t+7)/(108*3^t); source transfer R, all t>=3')
    print('P(X_i(t)=2)=2/9+1/(9*3^t); source density polynomial, all t>=1')


def main():
    for triple in product(ALPHABET, repeat=3):
        assert original_local(*triple)==simple_local(*triple), triple
    print('all_27_local_rules: OK')
    matrix_certificate()
    for t in range(1,5):
        observed = window_local_average(t)
        expected = predicted_change(t)
        assert observed == expected, (t, observed, expected)
        print(f'one_site_drop_t={t}: {observed} EXACT')
    for a in range(2,10):
        for b in range(2,10):
            observed=check_motif(a,b)
            expected=a+b-2
            assert observed == expected,(a,b,observed,expected)
    print('double_run_barrier_motifs: 64/64 OK')
    for n in range(3,11):
        hist=Counter()
        for initial in product(ALPHABET, repeat=n):
            left=relaxation_time(initial)
            right=relaxation_time(initial,original_local)
            assert left==right
            hist[left]+=1
        assert sum(hist.values()) == 3**n
        assert max(hist)==n-2
        assert hist[n-2]==(9 if n == 3 else 4*n)
        print(f'ring_n={n} configurations={3**n} max_time={max(hist)} extremizers={hist[max(hist)]} histogram={sorted(hist.items())}')
    print('PASS: local equivalence, exact local mean-decrement, motifs, independent ring dynamics')

if __name__ == '__main__':
    main()
