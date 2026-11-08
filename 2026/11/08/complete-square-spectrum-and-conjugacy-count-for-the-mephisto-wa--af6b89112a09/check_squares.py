#!/usr/bin/env python3
"""Finite diagnostics for a precise ordinary-power theorem in the Mephisto Waltz word.

Uses direct symbol comparisons as the reference implementation, independent of the
closed-form start tests and independent of the block-conjugacy count argument.
No finite test substitutes for the symbolic proof.
"""

def word(level):
    x = bytes([0])
    for _ in range(level):
        x = bytes(z for a in x for z in ((0,0,1) if a == 0 else (1,1,0)))
    return x


def is_power_three(n):
    if n < 1:
        return False
    while n % 3 == 0:
        n //= 3
    return n == 1


def square_expected(w, i, p):
    if not is_power_three(p):
        return False
    q, r = divmod(i, p)
    if r == 0:
        return w[q] == w[q+1]
    return w[q] == w[q+1] == w[q+2]


def cube_expected(w, i, p):
    return is_power_three(p) and i % p == 0 and w[i//p] == w[i//p+1] == w[i//p+2]


def main():
    w = word(9)  # 19,683 symbols
    n = len(w)
    square_trials = cube_trials = fourth_trials = 0
    positive_square_periods = set()
    for p in range(1, 601):
        run = 0
        for i in range(n-p-1, -1, -1):
            run = run + 1 if w[i] == w[i+p] else 0
            if i+2*p <= n:
                actual_sq = run >= p
                expected_sq = square_expected(w, i, p)
                assert actual_sq == expected_sq, ('square', p, i, actual_sq, expected_sq)
                square_trials += 1
                if actual_sq:
                    positive_square_periods.add(p)
            if i+3*p <= n:
                actual_cube = run >= 2*p
                expected_cube = cube_expected(w, i, p)
                assert actual_cube == expected_cube, ('cube', p, i, actual_cube, expected_cube)
                cube_trials += 1
            if i+4*p <= n:
                assert run < 3*p, ('fourth power', p, i)
                fourth_trials += 1
    assert positive_square_periods == {1,3,9,27,81,243}
    distinct_checks = 0
    for p in (1,3,9,27,81,243):
        forms = {w[i:i+2*p] for i in range(n-2*p+1)
                 if w[i:i+p] == w[i+p:i+2*p]}
        assert len(forms) == 2*p, (p,len(forms))
        distinct_checks += 1
    counting_checks = 0
    for k in range(5):
        p = 3**k
        for t in range(1, 6):
            m = p*(3**t)
            if m+3*p > n:
                continue
            sq = sum(w[i:i+p] == w[i+p:i+2*p] for i in range(m))
            cu = sum(w[i:i+p] == w[i+p:i+2*p] == w[i+2*p:i+3*p] for i in range(m))
            Q = (3**t + (-1)**t)//2
            T = (3**(t-1) - (-1)**(t-1))//2
            assert sq == Q+(p-1)*T, ('square counts',p,t,sq,Q+(p-1)*T)
            assert cu == T, ('cube counts',p,t,cu,T)
            counting_checks += 2
    print('VERIFY_OK', 'periods=1..600', 'word_length=',n,
          'square_checks=',square_trials, 'cube_checks=',cube_trials,
          'fourth_checks=',fourth_trials, 'distinct_counts=',distinct_checks,
          'finite_window_counts=',counting_checks)

if __name__ == '__main__':
    main()
