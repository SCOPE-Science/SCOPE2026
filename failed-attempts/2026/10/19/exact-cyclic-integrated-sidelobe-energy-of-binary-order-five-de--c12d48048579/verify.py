"""Reproduce the exact cyclic autocorrelation-energy census of binary order-five de Bruijn cycles.

Only the Python standard library is required. Run from any directory with spectrum.csv
next to this file. The calculation is exact integer arithmetic.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path
import csv

N = 32


def via_edge_pairings():
    """Enumerate all local incoming-to-outgoing bijections of the 4-bit de Bruijn graph."""
    words = set()
    for pairing in range(1 << 16):
        successor = [0] * N
        for vertex in range(16):
            switch = (pairing >> vertex) & 1
            for incoming_high_bit in range(2):
                entering_edge = (incoming_high_bit << 4) | vertex
                leaving_edge = 2 * vertex + (incoming_high_bit ^ switch)
                successor[entering_edge] = leaving_edge
        path = [0]
        visited = {0}
        edge = successor[0]
        while edge not in visited:
            visited.add(edge)
            path.append(edge)
            edge = successor[edge]
        if edge == 0 and len(path) == N:
            word = ''.join(str(edge >> 4) for edge in path)
            assert len({(word + word)[i:i + 5] for i in range(N)}) == N
            words.add(word)
    return words


def via_eulerian_search():
    """Enumerate Euler circuits, always beginning with the unique edge 00000."""
    words = set()

    def extend(vertex, used_mask, route):
        if len(route) == N:
            if vertex == 0:
                word = ''.join(str(edge >> 4) for edge in route)
                assert word[:5] == '00000'
                words.add(word)
            return
        for label in (0, 1):
            edge = 2 * vertex + label
            if not ((used_mask >> edge) & 1):
                extend(edge & 15, used_mask | (1 << edge), route + [edge])

    extend(0, 1, [0])
    return words


def correlations_multiplication(word):
    sequence = [2 * int(letter) - 1 for letter in word]
    return tuple(sum(sequence[i] * sequence[(i + delay) % N]
                     for i in range(N)) for delay in range(N))


def correlations_intersection(word):
    """Independent identity R(delay) = 4*|S intersect (S-delay)| - 32."""
    positions = {i for i, letter in enumerate(word) if letter == '1'}
    assert len(positions) == N // 2
    return tuple(4 * sum((i + delay) % N in positions for i in positions) - N
                 for delay in range(N))


def rotate_normal_form(word):
    return min(word[i:] + word[:i] for i in range(N))


def symmetry_orbit(word):
    complement = ''.join('1' if c == '0' else '0' for c in word)
    return frozenset(map(rotate_normal_form,
                         [word, word[::-1], complement, complement[::-1]]))


def census():
    first = via_edge_pairings()
    second = via_eulerian_search()
    assert first == second and len(first) == 2048
    energy_histogram = Counter()
    peak_histogram = Counter()
    joint = Counter()
    energy_to_words = defaultdict(list)
    for word in sorted(first):
        direct = correlations_multiplication(word)
        overlap = correlations_intersection(word)
        assert direct == overlap
        assert direct[0] == N and direct[1:5] == (0, 0, 0, 0)
        assert all(direct[delay] == direct[N - delay] for delay in range(1, N))
        energy = sum(value * value for value in direct[1:])
        peak = max(map(abs, direct[1:]))
        energy_histogram[energy] += 1
        peak_histogram[peak] += 1
        joint[(energy, peak)] += 1
        energy_to_words[energy].append(word)

    assert sum(energy_histogram.values()) == 2048
    assert len(energy_histogram) == 47
    assert min(energy_histogram) == 192 and max(energy_histogram) == 1952
    assert all(energy % 32 == 0 for energy in energy_histogram)
    assert energy_histogram[192] == 12 and energy_histogram[1952] == 4
    assert peak_histogram == {4: 12, 8: 772, 12: 882, 16: 282, 20: 88, 24: 12}
    total_energy = sum(energy * count for energy, count in energy_histogram.items())
    average = Fraction(total_energy, 2048)
    variance = (Fraction(sum(energy * energy * count for energy, count in
                             energy_histogram.items()), 2048) - average * average)
    assert average == Fraction(2813, 4)
    assert variance == Fraction(1336631, 16)

    # Full orbit identification uses rotation, reversal and bit complementation.
    for energy, expected_orbits in ((192, 3), (1952, 1)):
        equivalence_classes = {symmetry_orbit(w) for w in energy_to_words[energy]}
        assert len(equivalence_classes) == expected_orbits
        assert all(len(o) == 4 for o in equivalence_classes)
        assert set().union(*equivalence_classes) == set(energy_to_words[energy])

    # Compare all actual pairs (energy, peak) with the published CSV certificate.
    file_path = Path(__file__).resolve().with_name('spectrum.csv')
    with file_path.open(encoding='utf-8', newline='') as source:
        records = list(csv.DictReader(source))
    assert len(records) == 47
    assert [int(record['energy']) for record in records] == sorted(energy_histogram)
    for record in records:
        energy = int(record['energy'])
        assert int(record['cycles']) == energy_histogram[energy]
        assert sum(int(record['peak_' + str(p)]) for p in peak_histogram) == energy_histogram[energy]
        for peak in peak_histogram:
            assert int(record['peak_' + str(peak)]) == joint[(energy, peak)]
    print('VERIFY_OK independent_complete_generators=2 local_pairings=65536 '
          'order5_cycles=2048 independent_correlation_methods=2 '
          'cyclic_correlation_values=65536 energy_levels=47 '
          'energy_min=192:12 energy_max=1952:4 '
          'minimizer_symmetry_orbits=3 maximizer_symmetry_orbits=1 '
          'mean=2813/4 variance=1336631/16')


if __name__ == '__main__':
    census()
