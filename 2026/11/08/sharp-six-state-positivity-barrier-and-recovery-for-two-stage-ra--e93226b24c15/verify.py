"""Check the three exact first-column witnesses for the unit-rate directed eight-cycle."""
from fractions import Fraction
import json
from pathlib import Path

table = json.loads(Path(__file__).with_name('certificate.json').read_text())['steps']
assert [row['h'] for row in table] == [2, 4, 20]
expected = {2: Fraction(11824, 2058973),
            4: Fraction(-5703833, 339145563),
            20: Fraction(127548251905668327, 1666416340218976267)}
for row in table:
    h, d, m = row['h'], row['denominator'], row['numerators']
    assert d > 0 and len(m) == 8 and sum(m) == d
    for j in range(8):
        # Apply 6I-4hQ+h^2Q^2 using cyclic backward differences on components.
        delta = m[(j-1) % 8]-m[j]
        delta_prev = m[(j-2) % 8]-m[(j-1) % 8]
        lhs = 6*m[j]-4*h*delta+h*h*(delta_prev-delta)
        rhs = d*(6*(j == 0)+2*h*((j == 1)-(j == 0)))
        assert lhs == rhs
    minimum = Fraction(min(m), d)
    assert minimum == expected[h]
    assert m[0] < 0 < min(m[1:]) if h == 4 else minimum > 0
    print(f'h={h}: minimum={minimum}')
print('PASS: exact cyclic equations, mass and all three sign witnesses')
