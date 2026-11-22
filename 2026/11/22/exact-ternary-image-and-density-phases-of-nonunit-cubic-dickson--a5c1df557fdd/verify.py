"""Standalone direct tests for the cubic Dickson image cardinality theorem.

Run: python3 verify.py
"""

def unit_count(a, k):
    assert a % 3 != 0 and k >= 1
    if a % 3 == 2:
        return 3 if k == 1 else 3 ** (k - 1)
    return (3, 3, 5)[k - 1] if k <= 3 else 13 * 3 ** (k - 4)


def predicted(a, k):
    assert k >= 1
    if a % 3:
        return unit_count(a, k)
    if k == 1:
        return 3
    outer = 2 * 3 ** max(k - 2, 0)
    if k <= 3:
        return outer + 1
    if a % 9:
        return outer + (3 ** (k - 4) if (a // 3) % 3 == 1 else 3 ** (k - 3))
    return outer + predicted(a // 9, k - 3)


def direct_image(a, k):
    modulus = 3 ** k
    return {(x ** 3 - 3 * a * x) % modulus for x in range(modulus)}


def direct_cylinders(a, k):
    modulus = 3 ** k
    if a % 3:
        return None
    main = {y for y in range(modulus) if y % 9 in (1, 8)} if k >= 2 else {1, 2}
    if k <= 3:
        return main | {0}
    if a % 9:
        zero_modulus = 81 if (a // 3) % 3 == 1 else 27
        zero = {y for y in range(modulus) if y % zero_modulus == 0}
    else:
        reduced = direct_image(a // 9, k - 3)
        zero = {(27 * y) % modulus for y in reduced}
    return main | zero


def run():
    tests = 0
    cylinder_tests = 0
    for a in range(-90, 91):
        for k in range(1, 9):
            actual = direct_image(a, k)
            assert len(actual) == predicted(a, k), (a, k, len(actual), predicted(a, k))
            tests += 1
            if a % 3 == 0:
                expected = direct_cylinders(a, k)
                assert actual == expected, (a, k)
                cylinder_tests += 1
    for a in (0, 3, 6, 9, 18, 27, 54, 81):
        for k in (9, 10):
            actual = direct_image(a, k)
            assert len(actual) == predicted(a, k), (a, k)
            tests += 1
    print(f"PASS: {tests} direct prime-power counts and {cylinder_tests} full-set identities")


if __name__ == "__main__":
    run()
