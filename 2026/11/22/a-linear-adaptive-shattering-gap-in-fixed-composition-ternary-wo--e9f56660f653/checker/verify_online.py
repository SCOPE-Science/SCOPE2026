"""Verify a depth-three binary membership decision tree on ternary fixed-content words."""
import json
from itertools import permutations
from pathlib import Path

BASE = Path(__file__).resolve().parent
T = json.loads((BASE / 'depth3_tree.json').read_text(encoding='utf-8'))
H = {''.join(w) for w in permutations('AABC')}
assert len(H) == 12

def validate(node, version, depth, binary_prefix=''):
    if isinstance(node, str):
        assert depth == 3, (depth, binary_prefix)
        assert node in H and node in version, (node, binary_prefix)
        return [node]
    assert depth < 3
    i = node['position'] - 1
    c = node['color']
    assert 0 <= i < 4 and c in 'ABC'
    no = {w for w in version if w[i] != c}
    yes = {w for w in version if w[i] == c}
    assert no and yes
    return (validate(node['no'], no, depth + 1, binary_prefix + '0') +
            validate(node['yes'], yes, depth + 1, binary_prefix + '1'))

leaves = validate(T, H, 0)
assert len(leaves) == 8 and len(set(leaves)) == 8
assert len(H) < 16  # Information bound excludes depth four.
print('TERNARY_FIXED_CONTENT_DEPTH3_PASS 12 hypotheses 8 certified leaves')
print('BASE_VC_2_LITTLESTONE_3')
