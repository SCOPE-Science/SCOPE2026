"""Independent finite checks for Boolean--chain Heyting materializer formulas.

Usage: python verify.py
No third-party packages are required.
"""
from collections import Counter
from math import comb


def check(n, k):
    B = 1 << n
    N = B + k
    # Integer labels 0,...,B-1 represent subsets. B,...,B+k-1
    # represent the new ordered levels above the Boolean top.
    elements = range(N)

    def below(a, b):
        if a < B and b < B:
            return a & b == a
        if a < B <= b:
            return True
        if b < B <= a:
            return False
        return a <= b

    def join(a, b):
        if a < B and b < B:
            return a | b
        return max(a, b)

    def meet(a, b):
        if a < B and b < B:
            return a & b
        return min(a, b)

    # Compute Heyting implication by the defining adjunction rather
    # than any case distinction used in the mathematical proof.
    implication = {}
    for a in elements:
        for b in elements:
            eligible = [c for c in elements if below(meet(c, a), b)]
            maximum = [c for c in eligible if all(below(d, c) for d in eligible)]
            assert len(maximum) == 1, (n, k, a, b, maximum)
            implication[a, b] = maximum[0]
            assert all((below(meet(c, a), b) == below(c, maximum[0])) for c in elements)

    materializers = {a: frozenset(b for b in elements if
                           implication[a, b] == join(implication[a, 0], b))
                    for a in elements}
    failure = N * N - sum(map(len, materializers.values()))
    predicted = 3**n - 2**n + (2**n - 1)*(k-1) + k*(k-1)//2
    assert failure == predicted, (n, k, failure, predicted)
    assert materializers[0] == materializers[N-1] == frozenset(elements)

    for a in elements:
        if a == 0:
            predicted_set = frozenset(elements)
            predicted_size = N
        elif a < B:
            predicted_set = frozenset(
                b for b in elements if b == N-1 or
                (b < B and (b & a) != a)
            )
            predicted_size = B + 1 - 2**(n - a.bit_count())
        else:
            predicted_set = frozenset(b for b in elements if b < a or b == N-1)
            predicted_size = B + (a-B+1)
        assert materializers[a] == predicted_set
        assert len(materializers[a]) == predicted_size

    # The nonzero elements are order-isomorphic to distinct materializers.
    for a in range(1, N):
        for b in range(1, N):
            assert (below(a, b) == (materializers[a] <= materializers[b]))

    multiplicity = Counter(map(len, materializers.values()))
    predicted_multiplicity = Counter()
    predicted_multiplicity[N] += 1  # Bottom element.
    for r in range(1, n+1):
        predicted_multiplicity[B+1-2**(n-r)] += comb(n, r)
    for i in range(1, k+1):
        predicted_multiplicity[B+i] += 1
    assert multiplicity == predicted_multiplicity
    return N, failure


def main():
    count = 0
    total_pairs = 0
    for n in range(1, 6):
        for k in range(1, 6):
            N, failures = check(n, k)
            count += 1
            total_pairs += N*N
    print(f'VERIFY_OK exhaustive_parameter_pairs={count} evaluated_input_pairs={total_pairs}')


if __name__ == '__main__':
    main()
