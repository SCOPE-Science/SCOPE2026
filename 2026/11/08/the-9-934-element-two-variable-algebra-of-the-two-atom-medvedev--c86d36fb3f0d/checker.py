"""Reproduce the two-variable equivalence count for the three-world fork.
Only the standard Python library is required. No external proof software.
"""
from itertools import combinations, product

# A color is the two-bit truth assignment to (p,q): 0,1,2,3.
# Types 0..3 are maximal worlds. Other types are roots (color, set of leaf colors).
types = [('leaf', a, (a,)) for a in range(4)]
for a in range(4):
    allowed = [b for b in range(4) if (a & b) == a]
    for k in (1, 2):
        for leaves in combinations(allowed, k):
            if leaves != (a,):
                types.append(('root', a, leaves))
assert len(types) == 17

# Explicit small family of witness formulas, in documented order.
def I(x, y): return ('imp', x, y)
def O(x, y): return ('or', x, y)
def neg(x): return I(x, 0)
p, q = 'p', 'q'
formulas = [
    I(p,q), I(q,p), I(I(p,q),q), I(p,neg(q)), I(I(q,p),p),
    neg(I(p,neg(q))), I(neg(neg(p)),p), I(neg(neg(q)),q),
    I(I(p,neg(q)),O(p,q)), I(p,O(neg(q),q)), I(q,O(neg(p),p)),
]
# Certificates are 17-bit truth vectors: bit i corresponds to type i.
expected_masks = [
    0x1936d, 0x06adb, 0x1ec1e, 0x005b7, 0x1f42e, 0x0a048,
    0x177af, 0x1cf9f, 0x1f84e, 0x19fff, 0x07fff,
]

def on_type(e, a, leaves, root):
    if e == 0: return False
    if e == 1: return True
    if e == 'p': return bool(a & 1)
    if e == 'q': return bool(a & 2)
    op, x, y = e
    if op == 'or':
        return on_type(x, a, leaves, root) or on_type(y, a, leaves, root)
    if op != 'imp': raise ValueError(op)
    if on_type(x, a, leaves, root) and not on_type(y, a, leaves, root):
        return False
    if root:
        return all(not on_type(x, b, (b,), False) or
                   on_type(y, b, (b,), False) for b in leaves)
    return True

masks = [sum(1 << i for i, (kind, a, leaves) in enumerate(types)
             if on_type(e, a, leaves, kind == 'root')) for e in formulas]
assert masks == expected_masks

# Independently evaluate the same formulas on the actual three-world frame
# under all 5^2=25 upward-persistent valuations.
upsets = [0, 2, 4, 6, 7]  # bit 0=root, bit 1=first leaf, bit 2=second leaf
successors = [7, 2, 4]

def on_frame(e, u, v):
    if e == 0: return 0
    if e == 1: return 7
    if e == 'p': return u
    if e == 'q': return v
    op, x, y = e
    xx, yy = on_frame(x, u, v), on_frame(y, u, v)
    if op == 'or': return xx | yy
    if op != 'imp': raise ValueError(op)
    return sum(1 << i for i, s in enumerate(successors)
               if not ((xx & s) & ~(yy & s)))

observed = set()
for u, v in product(upsets, repeat=2):
    leafcols = [(int(bool(u & (1 << i))) +
                 2 * int(bool(v & (1 << i)))) for i in (1, 2)]
    rootcol = int(bool(u & 1)) + 2 * int(bool(v & 1))
    S = tuple(sorted(set(leafcols)))
    root_type = ('root', rootcol, S)
    if S == (rootcol,): root_type = ('leaf', rootcol, (rootcol,))
    j = types.index(root_type)
    observed.add(j)
    for k, f in enumerate(formulas):
        actual = on_frame(f, u, v)
        assert bool(actual & 1) == bool(masks[k] & (1 << j))
        for i, color in enumerate(leafcols, 1):
            assert bool(actual & (1 << i)) == bool(masks[k] & (1 << color))
assert len(observed) == 17

# Every formula is persistent along root-to-leaf arrows. The witness family
# separates every other directed pair of types, proving that there are no
# additional definability constraints beyond persistence.
order = {(i, i) for i in range(17)}
order |= {(i, b) for i in range(4, 17) for b in types[i][2]}
assert len(order) == 38
for x in range(17):
    for y in range(17):
        if (x, y) not in order:
            assert any(mask & (1 << x) and not mask & (1 << y)
                       for mask in masks), (x, y)
# Explicit principal-upset formulas are conjunctions of selected witnesses.
for x in range(17):
    principal = sum(1 << y for y in range(17) if (x, y) in order)
    selected = []
    for y in range(17):
        if (x, y) not in order:
            selected.append(next(mask for mask in masks
                                 if mask & (1 << x) and not mask & (1 << y)))
    truth = (1 << 17) - 1
    for mask in selected:
        truth &= mask
    assert truth == principal

# Sum over subsets L of the four leaf types. A root type may be selected iff
# all leaf types above it are selected; the eligible roots are independent.
contributions = []
all_upsets = set()
for L in range(16):
    eligible = [i for i in range(4, 17)
                if all(L & (1 << b) for b in types[i][2])]
    contributions.append(1 << len(eligible))
    for sub in range(1 << len(eligible)):
        bitset = L | sum(1 << i for k, i in enumerate(eligible)
                         if sub & (1 << k))
        all_upsets.add(bitset)
assert sum(contributions) == len(all_upsets) == 9934
print('MEDVEDEV_M2_TWO_VARIABLE_9934_OK',len(observed),'types',
      len(order),'comparabilities',len(all_upsets),'inequivalent formulas')
