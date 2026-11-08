#!/usr/bin/env python3
"""Finite, independent tests for a claimed infinite-word greedy attractor rule."""


def word(length):
    """Powers-of-two indicator at one-based positive integers (zero-based indices)."""
    powers = {1 << k for k in range((length + 1).bit_length())}
    return ''.join('1' if (i + 1) in powers else '0' for i in range(length))


def covered_factors(prefix, marks):
    covered = set()
    n = len(prefix)
    for left in range(n):
        for right in range(left + 1, n + 1):
            if any(left <= m < right for m in marks):
                covered.add(prefix[left:right])
    return covered


def is_attractor(prefix, marks):
    covered = covered_factors(prefix, marks)
    n = len(prefix)
    return all(prefix[left:right] in covered
               for left in range(n) for right in range(left + 1, n + 1))


def predicted_marks(length):
    marks = [0] if length else []
    a = 1
    while 3*a <= length:
        marks.append(3*a - 1)
        a *= 2
    return marks


def verify_direct(length=128):
    w = word(length)
    marks = []
    for j in range(length):
        if not is_attractor(w[:j+1], marks):
            marks.append(j)
        assert is_attractor(w[:j+1], marks), (j, marks)
        assert marks == predicted_marks(j+1), (j, marks, predicted_marks(j+1))
    return len(marks)


def verify_by_new_suffix(length=800):
    w = word(length)
    marks = []
    last = -1
    for end in range(length):
        tail = w[last+1:end+1]
        if w.find(tail, 0, end) == -1:
            marks.append(end)
            last = end
        assert marks == predicted_marks(end+1), (end, marks, predicted_marks(end+1))
    return len(marks)


def verify_local_substitutions(scale=12):
    w = word(6*(1 << scale)+1)
    cnt = 0
    for k in range(scale+1):
        a = 1 << k
        for j in range(3*a, 6*a-1):
            tail = w[3*a:j+1]
            if j < 4*a-1:
                assert tail == w[a:a+len(tail)]
            else:
                assert tail == w[a:j-2*a+1]
            assert w.find(tail, 0, j) != -1
            cnt += 1
        fresh = '0'*(2*a)
        assert w[4*a:6*a] == fresh
        assert fresh not in w[:6*a-1]
        cnt += 1
    return cnt


if __name__ == '__main__':
    direct = verify_direct()
    suffix = verify_by_new_suffix()
    substitutions = verify_local_substitutions()
    print(f'VERIFY_OK direct_prefixes=128 selected_direct={direct} suffix_prefixes=800 selected_suffix={suffix} explicit_gap_checks={substitutions}')
