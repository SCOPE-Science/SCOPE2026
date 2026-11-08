"""Exact finite verifier for majority-assignment lottery and cover statements.

Python 3 standard library only. Run beside cover_dual_certificates.json.gz.
All arithmetic below is integral; the compressed data contain nonnegative
rational dual certificates, not papers or external dependencies.
"""
import gzip
import itertools
import json
from pathlib import Path


def majority_matrix(profile):
    n = len(profile)
    allocations = list(itertools.permutations(range(n)))
    positions = [{house: i for i, house in enumerate(order)} for order in profile]
    m = [[0] * len(allocations) for _ in allocations]
    for i, a in enumerate(allocations):
        for j in range(i):
            b = allocations[j]
            margin = sum((positions[k][a[k]] < positions[k][b[k]]) -
                         (positions[k][a[k]] > positions[k][b[k]])
                         for k in range(n))
            m[i][j] = margin
            m[j][i] = -margin
    return allocations, m


def cover_masks(m):
    size = len(m)
    wins = [sum(1 << j for j in range(size) if m[i][j] > 0)
            for i in range(size)]
    losses = [sum(1 << j for j in range(size) if m[j][i] > 0)
              for i in range(size)]
    masks = {}
    for name in ('Bordes', 'Gillies', 'McKelvey'):
        covered = 0
        links = []
        for a in range(size):
            for b in range(size):
                if not ((wins[a] >> b) & 1):
                    continue
                bordes = (wins[b] & ~wins[a]) == 0
                gillies = (losses[a] & ~losses[b]) == 0
                if (name == 'Bordes' and bordes or
                    name == 'Gillies' and gillies or
                    name == 'McKelvey' and bordes and gillies):
                    covered |= 1 << b
                    links.append((a, b))
        masks[name] = (covered, links)
    return masks


def verify_certificates():
    with gzip.open(Path(__file__).with_name('cover_dual_certificates.json.gz'),
                   'rt', encoding='utf-8') as file:
        root = json.load(file)
    assert root['schema'] == 'majority_assignment_cover_dual_v1'
    for key, certificates in root['datasets'].items():
        n_str, variant = key.split('_', 1)
        n = int(n_str)
        perms = list(itertools.permutations(range(n)))
        checked = cover_cases = 0
        for pi in itertools.product(range(len(perms)), repeat=n - 1):
            profile = (perms[0],) + tuple(perms[i] for i in pi)
            allocations, m = majority_matrix(profile)
            covered, _ = cover_masks(m)[variant]
            denominator, sparse = certificates[checked]
            assert type(denominator) is int and denominator > 0
            coeff = [0] * len(perms)
            assert len(sparse) == len({entry[0] for entry in sparse})
            for idx, numerator in sparse:
                assert 0 <= idx < len(perms) and type(numerator) is int and numerator > 0
                coeff[idx] = numerator
            for target in range(len(perms)):
                payoff = sum(coeff[i] * m[i][target] for i in range(len(perms)))
                assert payoff >= denominator * ((covered >> target) & 1), (
                    key, pi, target, payoff, denominator)
            checked += 1
            cover_cases += bool(covered)
        assert checked == len(certificates) == root['counts'][key]['total']
        assert cover_cases == root['counts'][key]['with_covered']
        print('PASS', key, 'profiles', checked, 'covered_profiles', cover_cases)


def verify_examples():
    examples = [
        {'variant': 'Bordes',
         'profile': ((0, 1, 2, 3), (0, 1, 2, 3), (0, 1, 3, 2), (1, 2, 0, 3)),
         'lottery': [((0, 2, 3, 1), 1), ((2, 0, 1, 3), 1)],
         'denominator': 2,
         'coverer': (1, 0, 3, 2), 'covered': (2, 0, 1, 3)},
        {'variant': 'Gillies',
         'profile': ((0, 1, 2, 3), (0, 1, 2, 3), (0, 2, 1, 3), (1, 0, 3, 2)),
         'lottery': [((0, 2, 3, 1), 1), ((2, 3, 0, 1), 1), ((3, 0, 2, 1), 1)],
         'denominator': 3,
         'coverer': (0, 1, 2, 3), 'covered': (0, 2, 3, 1)}]
    for ex in examples:
        allocations, m = majority_matrix(ex['profile'])
        indices = {a: i for i, a in enumerate(allocations)}
        assert sum(weight for a, weight in ex['lottery']) == ex['denominator']
        for j in range(len(allocations)):
            assert sum(weight * m[indices[a]][j] for a, weight in ex['lottery']) >= 0
        masks = cover_masks(m)
        a, b = indices[ex['coverer']], indices[ex['covered']]
        assert (a, b) in masks[ex['variant']][1]
        assert (masks['McKelvey'][0] >> b) & 1 == 0
        assert any(a == ex['covered'] and weight > 0 for a, weight in ex['lottery'])
        print('PASS rational', ex['variant'], 'witness, winning covered assignment', ex['covered'])


if __name__ == '__main__':
    verify_certificates()
    verify_examples()
    print('ALL EXACT CHECKS PASS')
