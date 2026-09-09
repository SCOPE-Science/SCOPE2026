"""Per-element splitter-move census for each witness top M (stdlib only).
For every e: deletion M\\e and simplified contraction si(M/e): record
(3-connected?, F7-retaining?). Saves minimality.json."""
import json, sys
sys.path.insert(0, '/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-433/output/artifacts')
from tool import (delete1, contract1, simplify, conn_check, find_F7_model)

ART = '/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-433/output/artifacts'
W = json.load(open(ART + '/witnesses.json'))
out = []
for i, w in enumerate(W):
    M = (w['chain_mats'][-1][0], w['chain_mats'][-1][1])
    n = len(M[1])
    rows = []
    good = []
    for e in range(n):
        D = delete1(M, e)
        okd, infd = conn_check(D)
        fd = find_F7_model(D) is not None
        try:
            Mc = contract1(M, e)
            S, dropped = simplify(Mc)
            okc, infc = conn_check(S)
            fc = find_F7_model(S) is not None if len(S[1]) >= 7 else False
        except AssertionError:
            S, dropped, okc, fc = None, [], False, False
            infc = {'lambda_min_by_size': {}, 'nviol': -1}
        rows.append({'e': e,
                     'del': {'n': len(D[1]), 'rank': D[0],
                             'conn3': okd, 'F7': fd,
                             'lam': {str(a): b for a, b in infd['lambda_min_by_size'].items()}},
                     'con': {'n': len(S[1]) if S else 0,
                             'rank': S[0] if S else -1,
                             'dropped_parallel': dropped,
                             'conn3': okc, 'F7': fc,
                             'lam': {str(a): b for a, b in infc['lambda_min_by_size'].items()}}})
        if okd and fd:
            good.append(['del', e])
        if okc and fc:
            good.append(['con', e])
    out.append({'witness': i, 'seed': w['seed'], 'n': n,
                'n_good_moves': len(good), 'good_moves': good, 'rows': rows})
json.dump(out, open(ART + '/minimality.json', 'w'))
for e in out:
    print(f"W{e['witness']} seed={e['seed']} n={e['n']}: good moves={e['n_good_moves']}")
print("saved minimality.json")
