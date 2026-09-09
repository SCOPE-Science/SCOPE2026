"""Independent verifier (stdlib only): replays widgets:
standards, per-witness chain steps (3-conn lambda tables, F7 models, MK5 verdicts),
and checks deletion/contraction reversal consistency. Prints VERIFY_OK or FAIL detail.
"""
import json, sys
sys.path.insert(0, '/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-433/output/artifacts')
from tool import (gf2_rank, mat_rank, delete1, contract1, contract_set, simplify,
                  is_simple, nbases, bases_set, conn_check, std_F7, std_MK5,
                  iso_to_std_F7, find_F7_model, mk5_search_stats)

ART = '/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-433/output/artifacts'

def check(cond, msg):
    if not cond:
        print("FAIL:", msg)
        sys.exit(1)

F7 = std_F7(); K5 = std_MK5()
check(mat_rank(F7) == 3 and len(F7[1]) == 7 and nbases(F7) == 28, "F7 standard")
check(mat_rank(K5) == 4 and len(K5[1]) == 10 and nbases(K5) == 125, "MK5 standard")
ok, _ = conn_check(F7); check(ok, "F7 3-connected")
check(find_F7_model(K5) is None, "MK5 must be F7-free (non-regular root)")

W = json.load(open(ART + '/witnesses.json'))
check(len(W) >= 3, "need >=3 witnesses")
ns = set()
for i, w in enumerate(W):
    chain = [(r, cols) for (r, cols) in w['chain_mats']]
    ops = w['ops']
    check(len(chain) == len(ops) + 1, f"W{i}: chain/ops length")
    M0 = chain[0]
    check(M0[0] == 3 and len(M0[1]) == 7 and iso_to_std_F7(M0) is not None,
          f"W{i}: M0 must be F7")
    for k in range(1, len(chain)):
        Mp, M = chain[k - 1], chain[k]
        op, e = ops[k - 1][0], ops[k - 1][1]
        check(e == len(Mp[1]), f"W{i} step {k}: new element must be last (e={e})")
        if op == 'ext':
            check(M[0] == Mp[0] and M[1][:e] == Mp[1] and len(M[1]) == e + 1,
                  f"W{i} step {k}: ext consistency")
            # reverse: delete e
            D = delete1(M, e)
            check(D[1] == Mp[1] and D[0] == Mp[0], f"W{i} step {k}: delete-reversal")
        elif op == 'coext':
            check(M[0] == Mp[0] + 1 and len(M[1]) == e + 1,
                  f"W{i} step {k}: coext consistency")
            # reverse: contract e, must recover Mp exactly
            Mc = contract1(M, e)
            check(Mc[1] == Mp[1] and Mc[0] == Mp[0],
                  f"W{i} step {k}: contract-reversal")
        else:
            check(False, f"W{i} step {k}: unknown op {op}")
        check(is_simple(M), f"W{i} M{k}: simplicity")
        okk, info = conn_check(M)
        check(okk, f"W{i} M{k}: 3-connected, info={info}")
        check(info['lambda_min_by_size'].get(1, 0) >= 1, f"W{i} M{k}: lambda1")
        check(info['lambda_min_by_size'].get(2, 0) >= 2, f"W{i} M{k}: lambda2")
        check(find_F7_model(M) is not None, f"W{i} M{k}: F7 model")
    top = chain[-1]
    check(mat_rank(top) == 7, f"W{i}: top rank 7")
    check(nbases(top) == w['nbases'], f"W{i}: nbases replay")
    st = mk5_search_stats(top)
    check(not st['found'], f"W{i}: MK5 minor found!")
    check(st['models_examined'] == w['mk5']['models_examined'], f"W{i}: mk5 count replay")
    check(st['max_bases_seen'] == w['mk5']['max_bases_seen'], f"W{i}: mk5 maxb replay")
    ns.add(len(top[1]))
check(len(ns) >= 2, "want >=2 distinct top sizes")

# per-element splitter-move census replay (minimality.json)
MN = json.load(open(ART + '/minimality.json'))
check(len(MN) == len(W), "minimality entries match witnesses")
for i, w in enumerate(W):
    M = (w['chain_mats'][-1][0], w['chain_mats'][-1][1])
    n = len(M[1])
    me = MN[i]
    check(me['n'] == n and me['seed'] == w['seed'], f"W{i}: minimality header")
    check(len(me['rows']) == n, f"W{i}: minimality row count")
    ngood = 0
    for row in me['rows']:
        e = row['e']
        D = delete1(M, e)
        okd, _ = conn_check(D)
        fd = find_F7_model(D) is not None
        check(row['del']['conn3'] == okd, f"W{i} e={e}: del conn replay")
        check(row['del']['F7'] == fd, f"W{i} e={e}: del F7 replay")
        check(row['del']['n'] == len(D[1]) and row['del']['rank'] == D[0],
              f"W{i} e={e}: del size replay")
        try:
            Mc = contract1(M, e)
            S, dropped = simplify(Mc)
            okc, _ = conn_check(S)
            fc = find_F7_model(S) is not None if len(S[1]) >= 7 else False
        except AssertionError:
            S, dropped, okc, fc = None, [], False, False
        check(row['con']['conn3'] == okc, f"W{i} e={e}: con conn replay")
        check(row['con']['F7'] == fc, f"W{i} e={e}: con F7 replay")
        if S is not None:
            check(row['con']['n'] == len(S[1]) and row['con']['rank'] == S[0],
                  f"W{i} e={e}: con size replay")
        if okd and fd:
            ngood += 1
        if okc and fc:
            ngood += 1
    check(me['n_good_moves'] == ngood, f"W{i}: good-move count replay")
    check(ngood >= 1, f"W{i}: each witness keeps >=1 splitter move")
print(f"MINIMALITY_OK: good moves per witness "
      f"{[(me['seed'], me['n_good_moves']) for me in MN]}")
print(f"VERIFY_OK: {len(W)} witnesses, top sizes {sorted(ns)}")
