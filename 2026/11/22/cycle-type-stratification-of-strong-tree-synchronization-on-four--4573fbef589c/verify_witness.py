# Independent direct verification of the sharp commutative four-state witness.
# Run: python3 verify_witness.py
import json
from pathlib import Path
p = Path(__file__).resolve().parent
obj = json.loads((p/'witness.json').read_text(encoding='utf-8'))
Q = set(range(4))
f = obj['binary_table']
w = obj['unary']
assert sorted(w) == [0,1,2,3]
assert all(f[i][j] == f[j][i] for i in Q for j in Q)
mask = lambda S: sum(1 << i for i in S)
def app_w(S): return {w[i] for i in S}
def app_f(S,T): return {f[i][j] for i in S for j in T}
reached = {frozenset(Q)}
new_masks=[15]
term = {15: (frozenset(Q), 0)}
for h in range(1,12):
    nxt = set(reached)
    for S in reached:
        nxt.add(frozenset(app_w(S)))
        for T in reached:
            nxt.add(frozenset(app_f(S,T)))
    news = nxt - reached
    new_masks.extend(sorted(mask(S) for S in news))
    assert len(news) == 1 and (h == 11 or not any(len(S)==1 for S in nxt))
    reached = nxt
assert new_masks == obj['first_appearance_masks']
rec={0:Q}
for index, (op, *args) in enumerate(obj['term_recipes'], 1):
    if op=='w':rec[index]=app_w(rec[args[0]])
    else:rec[index]=app_f(rec[args[0]],rec[args[1]])
    assert mask(rec[index])==new_masks[index]
assert rec[11]=={0}
print('WITNESS_OK code=739 heights=0..11 masks=' + ','.join(map(str,new_masks)))
