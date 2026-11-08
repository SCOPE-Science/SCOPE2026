"""Finite verification of the two-row knowing-whether modal algebra.

Run: python3 support_checker.py
The construction enumerates all nonempty subsets of four column types.
"""
from itertools import combinations

TYPES=range(4)
STATES=[(s,t,r) for s in range(1,16) for t in TYPES if s & (1<<t) for r in range(2)]
IX={v:i for i,v in enumerate(STATES)}
assert len(STATES)==64
ROWS={(s,r):tuple(IX[s,t,r] for t in TYPES if s&(1<<t))
      for s in range(1,16) for r in range(2)}
COLS={(s,t):tuple(IX[s,t,r] for r in range(2))
      for s in range(1,16) for t in TYPES if s&(1<<t)}
U=set(range(64))

def H(X):
    """A world knows whether X in at least one of its two equivalence classes."""
    return frozenset(i for i,(s,t,r) in enumerate(STATES)
        if len({j in X for j in ROWS[s,r]})==1
        or len({j in X for j in COLS[s,t]})==1)

P=frozenset(i for i,(s,t,r) in enumerate(STATES) if (t>>r)&1)
K=H(P)
F=[P,K,H(K),H(P|K),H(P-K)]
signatures={i:''.join(str(int(i in x)) for x in F) for i in U}
blocks={b:frozenset(i for i in U if signatures[i]==b) for b in set(signatures.values())}
expected=['00001','00100','00101','01111','10010','10100','10110','11111']
assert sorted(blocks)==expected
assert {v:len(blocks[v]) for v in sorted(blocks)}==dict(zip(expected,[2,8,2,20,2,8,2,20]))
# Verify closure under the unary modality on all Boolean combinations of atoms.
labels=sorted(blocks)
closure_rows=[]
for m in range(256):
    X=frozenset().union(*(blocks[labels[j]] for j in range(8) if m&(1<<j)))
    Y=H(X)
    bits=[]
    for j in range(8):
        b=blocks[labels[j]]
        assert b<=Y or b.isdisjoint(Y), (m,labels[j])
        bits.append(int(b<=Y))
    closure_rows.append(sum(bit<<j for j,bit in enumerate(bits)))

# Each type is realizable with the claimed smallest number of distinct columns.
mincols={name:min(s.bit_count() for i,(s,t,r) in enumerate(STATES) if signatures[i]==name)
         for name in labels}
assert [mincols[v] for v in labels]==[2,2,3,1,2,2,3,1]
for m in range(1,5):
    occurring={signatures[i] for i,(s,t,r) in enumerate(STATES) if s.bit_count()<=m}
    assert len(occurring)==(2 if m==1 else 6 if m==2 else 8)
# Depth-one classes are exactly (p,H(p)) and depth-two signatures split them.
for m in range(1,5):
    available=[i for i,(s,t,r) in enumerate(STATES) if s.bit_count()<=m]
    pairs={(i in P,i in K) for i in available}
    assert len(pairs)==(2 if m==1 else 4)
# Verify H(P) is closed under complement of the argument and that depth one alone
# does not isolate all semantic types when there are at least two columns.
assert H(U-P)==K
assert len(set(signatures.values()))==8
from pathlib import Path
reference=Path(__file__).with_name('closure_table.tsv')
assert reference.read_text(encoding='utf-8') == ('input_mask_hex\toutput_mask_hex\n' + ''.join(f'{i:02x}\t{j:02x}\n' for i,j in enumerate(closure_rows)))
print('SUPPORT_ALGEBRA_OK 64 states, 8 atoms, 256 closure cases, depth 2, sizes 4/64/256')

if __name__=='__main__':
    pass
