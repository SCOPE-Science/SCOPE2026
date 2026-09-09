"""Emit detailed per-step bridging log for each witness chain (stdlib only)."""
import json, sys
sys.path.insert(0, '/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-433/output/artifacts')
from tool import (gf2_rank, mat_rank, delete1, contract1, is_simple, nbases,
                  conn_check, std_F7, iso_to_std_F7, find_F7_model,
                  mk5_search_stats, counting_MK5_note)

ART = '/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-433/output/artifacts'
W = json.load(open(ART + '/witnesses.json'))
log = []
for i, w in enumerate(W):
    chain = [(r, cols) for (r, cols) in w['chain_mats']]
    ops = w['ops']
    steps = []
    # forward step k: Mp -> M via op; record reverse-splitter row (M, e, kind, M-checks)
    for k in range(1, len(chain)):
        Mp, M = chain[k - 1], chain[k]
        op, e = ops[k - 1][0], ops[k - 1][1]
        ok, info = conn_check(M)
        fm = find_F7_model(M)
        row = {'step': k, 'forward_op': op, 'e': e,
               'n': len(M[1]), 'rank': M[0], 'nbases': nbases(M),
               'is_simple': is_simple(M),
               'lambda_min_by_size': {str(a): b for a, b in info['lambda_min_by_size'].items()},
               'nviol': info['nviol'],
               'F7_model': {'C': fm[0], 'S': fm[1], 'perm': fm[2]},
               'reverse_splitter': ('delete', e) if op == 'ext' else ('contract', e)}
        if len(M[1]) <= 13:
            row['MK5_counting'] = counting_MK5_note(M)
        steps.append(row)
    top = chain[-1]
    st = mk5_search_stats(top)
    log.append({'witness': i, 'seed': w['seed'], 'top_n': len(top[1]),
                'top_cols': top[1], 'top_nrows': top[0],
                'top_nbases': nbases(top),
                'top_MK5_exhaustive': {k: v for k, v in st.items() if k != 'witness'},
                'steps': steps})
json.dump(log, open(ART + '/bridgelog.json', 'w'))
print("witnesses:", len(log))
for e in log:
    print(f"W{e['witness']} seed={e['seed']} n={e['top_n']} bases={e['top_nbases']} "
          f"mk5models={e['top_MK5_exhaustive']['models_examined']} "
          f"maxb={e['top_MK5_exhaustive']['max_bases_seen']}")
    for s in e['steps']:
        print(f"  step{s['step']} {s['forward_op']} e={s['e']}: "
              f"n={s['n']} r={s['rank']} lam={s['lambda_min_by_size']} "
              f"F7(C={s['F7_model']['C']},S={s['F7_model']['S']})")
