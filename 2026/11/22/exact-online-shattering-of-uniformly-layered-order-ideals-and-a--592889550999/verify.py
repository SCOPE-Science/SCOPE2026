#!/usr/bin/env python3
"""Exact independent tests for online ranks of uniform-level ideal classes.
Scientific code: no external dependencies.
"""
from functools import lru_cache

@lru_cache(None)
def compressed_rank(seq):
    seq = tuple(q for q in seq if q > 0)
    if not seq:
        return 0
    answer = 0
    for j, w in enumerate(seq):
        left = tuple(v for v in seq[:j] + (w-1,) if v)
        right = tuple(v for v in (w-1,) + seq[j+1:] if v)
        answer = max(answer, 1 + min(compressed_rank(left), compressed_rank(right)))
    return answer


def concrete_rank(width, height):
    # Enumerate the actual lower ideals, encoded as subsets of w*h points.
    concepts = [0]
    for level in range(height):
        forced_lower = (1 << (width * level)) - 1
        for within in range(1, 1 << width):
            concepts.append(forced_lower | (within << (width * level)))
    assert len(set(concepts)) == len(concepts) == 1 + height * ((1 << width) - 1)
    bit_columns = tuple(sum(1 << i for i, ideal in enumerate(concepts)
                            if ideal & (1 << x)) for x in range(width * height))
    @lru_cache(None)
    def solve(remaining):
        r = 0
        for col in bit_columns:
            yes, no = remaining & col, remaining & ~col
            if yes and no:
                r = max(r, 1 + min(solve(yes), solve(no)))
        return r
    result = solve((1 << len(concepts)) - 1)
    return result, len(concepts), solve.cache_info().currsize


def main():
    brute_cases = 0
    direct_states = 0
    for w in range(1, 5):
        for h in range(1, 8):
            observed, count, states = concrete_rank(w, h)
            expected = w - 1 + (h + 1).bit_length() - 1
            assert observed == compressed_rank((w,) * h) == expected, (w, h, observed, expected)
            assert count == 1 + h * (2**w - 1)
            direct_states += states
            brute_cases += 1
    extra_cases = 0
    for w in range(1, 6):
        for h in range(1, 32):
            assert compressed_rank((w,) * h) == w - 1 + (h + 1).bit_length()-1
            extra_cases += 1
    for w in range(2, 6):
        for h in range(1, 5):
            n = 1 + h * (2**w-1)
            rank = compressed_rank((w,) * h)
            assert n.bit_length()-1 == rank
        h = 5
        n = 1+h*(2**w-1)
        assert n.bit_length()-1 == compressed_rank((w,)*h) + 1
    print('UNIFORM_WEAK_ORDER_LDIM_PASS', brute_cases, 'independent literal cases',
          direct_states, 'version states', extra_cases, 'abstract cases',
          'first_entropy_gap_height_5')

if __name__ == '__main__':
    main()
