"""Standalone finite tests for periods of order-k Fibonacci recurrences."""


def shift(state, modulus):
    return state[1:] + (sum(state) % modulus,)


def period_direct(k, r):
    modulus = 1 << r
    initial = (0,) * (k - 1) + (1,)
    state = initial
    for t in range(1, (k + 1) * (1 << (r - 1)) + 1):
        state = shift(state, modulus)
        if state == initial:
            return t
    raise AssertionError('period above predicted bound')


def mul_ring(a, b, k, modulus):
    # Reduce modulo X^k - X^(k-1) - ... - X - 1.
    c = [0] * (2 * k - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            c[i+j] += ai*bj
    for j in range(2*k-2, k-1, -1):
        v = c[j]
        for t in range(1, k+1):
            c[j-t] += v
    return tuple(x % modulus for x in c[:k])


def power_x(k, exponent, modulus):
    v = [0] * k
    v[0] = 1
    x = [0] * k
    x[1] = 1
    while exponent:
        if exponent & 1:
            v = mul_ring(v, x, k, modulus)
        exponent >>= 1
        if exponent:
            x = mul_ring(x, x, k, modulus)
    return tuple(v)


def main():
    tested = 0
    for k in range(2, 31):
        for r in range(1, 9):
            target = (k+1)*(1 << (r-1))
            assert period_direct(k, r) == target
            modulus = 1 << r
            one = (1,)+(0,)*(k-1)
            assert power_x(k, target, modulus) == one
            if r >= 2:
                assert power_x(k, target//2, modulus) != one
            if (k+1) % 2 == 0 and r == 1:
                assert power_x(k, (k+1)//2, modulus) != one
            # Check the base exponent is exactly k+1 modulo two.
            if r == 1:
                for t in range(1,k+1):
                    assert power_x(k,t,2) != one
            tested += 1
    for k, r in [(2,1),(2,4),(3,5),(4,6),(10,7),(30,8)]:
        print('order_k=%d modulus=%d minimal_period=%d' %
              (k, 2**r, period_direct(k, r)))
    print('PASS: %d exhaustive state-cycle checks, %d polynomial power checks' %
          (tested, 2*tested))
    print('This finite test is not a proof of the uniform theorem.')


if __name__ == '__main__':
    main()
