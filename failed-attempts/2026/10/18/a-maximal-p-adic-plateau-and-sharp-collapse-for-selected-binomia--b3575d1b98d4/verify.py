"""Exact finite checks of the prime-power-minus-one selected-binomial theorem.

No symbolic packages or randomness are required. This checks valuations using
Legendre's factorial formula, independently of the digit-sum proof.
"""


def vp_factorial(n, p):
    total = 0
    while n:
        n //= p
        total += n
    return total


def vp_binomial(n, k, p):
    return vp_factorial(n, p) - vp_factorial(k, p) - vp_factorial(n-k, p)


def main():
    cases = [(2, r) for r in range(2, 8)] + [(3, r) for r in range(2, 5)] + [(5, r) for r in range(2, 4)] + [(7, r) for r in range(2, 4)]
    total_coefs = 0
    for p, r in cases:
        b = p**r
        m = b-1
        for q in range(2, b+2):
            n = m*q
            valuations = [vp_binomial(n, m*d, p) for d in range(1, q)]
            total_coefs += len(valuations)
            expected = r if q<=b else 0
            actual = min(valuations)
            assert actual == expected, (p,r,q,actual,expected)
            if q<=b:
                assert all(v>=r for v in valuations), (p,r,q)
                assert valuations[0] == r, (p,r,q,'first coefficient')
            else:
                assert valuations[0] == 0, (p,r,q,'first failure')
        print(f'p={p}, r={r}, m={m}: all q=2..{b} have gcd valuation {r}; q={b+1} has valuation 0')
    print(f'PASS {len(cases)} parameter pairs, {total_coefs} selected binomial valuations')


if __name__ == '__main__':
    main()
