#!/usr/bin/env python3
"""Finite, exact-integer checks for the Fibonacci partition minimum theorem.

These checks verify examples, not the unrestricted mathematical proof.
"""

def check(max_m=21):
    fib = [0, 1, 1]
    for _ in range(3, max_m + 3):
        fib.append(fib[-1] + fib[-2])
    bound = fib[max_m] + fib[max_m - 1]
    counts = [0] * (bound + 1)
    counts[0] = 1
    # Enumerate by multiplying (1+z**F_i), each weight used at most once.
    for weight in fib[2:]:
        if weight > bound:
            break
        for n in range(bound, weight - 1, -1):
            counts[n] += counts[n - weight]
    tested = 0
    singleton_checks = 0
    for n in range(bound + 1):
        if counts[n] == 1:
            assert n in {fib[i] - 1 for i in range(2, max_m + 3)}, n
        singleton_checks += 1
    reflection = 0
    for k in range(5, max_m + 1):
        for t in range(fib[k - 1] - 1):
            assert counts[fib[k] + t] == counts[t] + counts[fib[k - 1] - 2 - t]
            reflection += 1
    for m in range(7, max_m + 1):
        actual_min = 10**30
        argmin = []
        for H in range(1, fib[m - 1]):
            value = counts[fib[m] + H]
            if value < actual_min:
                actual_min, argmin = value, [H]
            elif value == actual_min:
                argmin.append(H)
            j = max(i for i in range(2, m)
                    if (i - m) % 2 and fib[i] - 1 <= H)
            predicted = (m - j + 1) // 2
            extremizers = [t for t in (fib[j] - 1, fib[j + 1] - 1)
                          if 1 <= t <= H]
            assert actual_min == predicted, (m, H, j, actual_min, predicted)
            assert argmin == extremizers, (m, H, j, argmin, extremizers)
            tested += 1
    print("VERIFY_OK max_m=%d H_tests=%d reflection_tests=%d singleton_checks=%d exact_integer=yes"
          % (max_m, tested, reflection, singleton_checks))


if __name__ == '__main__':
    check()
