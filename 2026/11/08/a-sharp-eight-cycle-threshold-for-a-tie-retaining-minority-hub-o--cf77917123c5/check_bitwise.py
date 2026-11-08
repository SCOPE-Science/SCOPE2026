#!/usr/bin/env python3
"""Exact exhaustive eight-cycle check on finite wheels, plus a symbolic witness."""

def update(state, n):
    mask = (1 << n) - 1
    hub = state & 1
    rim = state >> 1
    count = rim.bit_count()
    newhub = int(2 * count < n) if 2 * count != n else hub
    left = ((rim << 1) | (rim >> (n - 1))) & mask
    right = (rim >> 1) | ((rim & 1) << (n - 1))
    newrim = (left | right) if hub else (left & right)
    return (newrim << 1) | newhub

def period_eight(state, n):
    cur = state
    for _ in range(4):
        cur = update(cur, n)
    if cur == state:
        return False
    for _ in range(4):
        cur = update(cur, n)
    return cur == state

def witness(n):
    assert n >= 12 and n % 2 == 0
    initial_length = n // 2 - 4
    return (sum(1 << (i + 1) for i in range(initial_length))) | 1

if __name__ == '__main__':
    for n in range(3, 17):
        answer = sum(period_eight(x, n) for x in range(1 << (n + 1)))
        assert answer == 0 if n < 12 or (n % 2) else answer > 0
        if n == 12:
            assert answer == 288
        if n == 14:
            assert answer == 784
        if n == 16:
            assert answer == 1536
        print(f'n={n} eight_periodic_states={answer}')
    for n in range(12, 102, 2):
        x = witness(n)
        assert period_eight(x, n), n
        if n == 12:
            history = []
            for _ in range(8):
                history.append((x & 1, (x >> 1).bit_count()))
                x = update(x, n)
            assert history == [(1,2),(1,4),(1,6),(1,8),(0,10),(0,8),(0,6),(0,4)]
            print('witness_n12_history=' + repr(history))
    print('BITWISE_EXHAUSTIVE_AND_ALL_EVEN_WITNESSES_OK')
