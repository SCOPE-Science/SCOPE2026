"""Independent deletion-shadow packing check using integer programming.

Requires SciPy; independently constructs a word-output incidence matrix,
without using the compatibility/clique search from verify_exact.py.
"""
import itertools
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import coo_matrix


def main():
    for n, claimed in [(7, 6), (8, 10), (9, 13)]:
        sources = [''.join(bits) for bits in itertools.product('01', repeat=n)
                   if '000' not in ''.join(bits) and '111' not in ''.join(bits)]
        outputs = sorted({s[:i] + s[i+1:] for s in sources for i in range(n)})
        loc = {w: i for i, w in enumerate(outputs)}
        rows, cols = [], []
        for col, s in enumerate(sources):
            for y in {s[:i] + s[i+1:] for i in range(n)}:
                rows.append(loc[y]); cols.append(col)
        A = coo_matrix((np.ones(len(rows)), (rows, cols)),
                       shape=(len(outputs), len(sources))).tocsr()
        result = milp(c=-np.ones(len(sources)),
                      integrality=np.ones(len(sources)),
                      bounds=Bounds(0, 1),
                      constraints=LinearConstraint(A, -np.inf, 1),
                      options={'mip_rel_gap': 0, 'time_limit': 60})
        assert result.status == 0, (n, result.message)
        solution = np.rint(result.x).astype(int)
        assert np.all(A @ solution <= 1)
        assert sum(solution) == claimed, (n, sum(solution))
        assert abs(result.mip_gap) < 1e-9
        print('n={}, sources={}, outputs={}, optimum={}'.format(
              n, len(sources), len(outputs), claimed))
    print('PASS: independent integer-optimization formulation')

if __name__ == '__main__':
    main()
