"""Exact verification of the possible tangent multipliers on polygonal edges."""
from fractions import Fraction

matrices = {
    'Q1': ((1, -1), (1, -1)),
    'Q2': ((-1, -1), (1, -1)),
    'Q3': ((-1, -1), (1, 1)),
    'Q4': ((1, -1), (1, 1)),
}
directions = {'horizontal': (1, 0), 'vertical': (0, 1),
              'ascending': (1, 1), 'descending': (1, -1)}
zero_pairs = {('Q1', 'ascending'), ('Q3', 'descending')}
seen = 0
for quadrant, A in matrices.items():
    for label, v in directions.items():
        w = (A[0][0] * v[0] + A[0][1] * v[1],
             A[1][0] * v[0] + A[1][1] * v[1])
        squared_ratio = Fraction(w[0] ** 2 + w[1] ** 2,
                                 v[0] ** 2 + v[1] ** 2)
        is_plateau = (quadrant, label) in zero_pairs
        assert (squared_ratio == 0) == is_plateau, (quadrant, label)
        if not is_plateau:
            assert squared_ratio in (2, 4), (quadrant, label, squared_ratio)
        print(f'{quadrant:2} {label:10} squared arclength ratio = {squared_ratio}')
        seen += 1
assert seen == 16
assert Fraction(3, 4) < 1 # BV four-step contraction coefficient: 3 / (sqrt(2)**4)
print('PASS: all 16 matrix-direction identities, two plateaus, nonzero length ratios 2 or 4.')
