"""Independent exact mask-transfer count of cyclically supported colorings.

Run: python3 verify_transfer.py
The method does not assume a row-surjection classification or the claimed formula.
"""
from collections import defaultdict


def transfer(n):
    # Four bitsets: colors seen on each row and colors required to have
    # a same-row witness because the rung does not supply one.
    counts = {(0, 0, 0, 0): 1}
    for _ in range(n):
        nxt = defaultdict(int)
        for (seen_a, seen_b, req_a, req_b), amount in counts.items():
            for a in range(3):
                for b in range(3):
                    next_req_a = req_a | (0 if b == (a + 1) % 3 else 1 << ((a + 1) % 3))
                    next_req_b = req_b | (0 if a == (b + 1) % 3 else 1 << ((b + 1) % 3))
                    state = (seen_a | (1 << a), seen_b | (1 << b), next_req_a, next_req_b)
                    nxt[state] += amount
        counts = nxt
    return sum(c for (sa, sb, ra, rb), c in counts.items()
               if (sa & ra) == ra and (sb & rb) == rb)


def formula(n):
    return 9**n - 6 * 6**n + 15 * 4**n - 12 * 3**n + 3


def main():
    for n in range(1, 61):
        observed = transfer(n)
        expected = formula(n)
        assert observed == expected, (n, observed, expected)
    for n in (1, 2, 3, 4, 5, 6, 10, 20, 60):
        print(f"n={n} transfer={transfer(n)} formula={formula(n)}")
    print("PASS independent exact mask transfer, all lengths 1..60")


if __name__ == '__main__':
    main()
