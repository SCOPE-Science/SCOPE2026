"""Rebuild witnesses: pure-coextension tower F7=M0<M1<M2<M3<M4 (rank 7, n=11),
each step 3-connected + simple + F7-retaining; then optionally one extension step
to diversify sizes. All steps cross-checked with the FIXED conn_check. Stdlib."""
import random, json, sys
sys.path.insert(0, '/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-433/output/artifacts')
from tool import (gf2_rank, mat_rank, delete1, contract1, is_simple, nbases,
                  conn_check, std_F7, std_MK5, iso_to_std_F7, find_F7_model,
                  mk5_search_stats)

def coextend(M0, b):
    r, cols = M0
    newcols = [(c | ((((b >> j) & 1)) << r)) for j, c in enumerate(cols)]
    return (r + 1, newcols + [(1 << r)])

def coext_tower(seed):
    rng = random.Random(seed)
    chain = [std_F7()]
    ops = []
    M = std_F7()
    for _ in range(4):
        r, cols = M
        n = len(cols)
        for _ in range(500):
            b = rng.randrange(1, 1 << n)
            M2 = coextend(M, b)
            if not is_simple(M2):
                continue
            ok, _ = conn_check(M2)
            if not ok:
                continue
            if find_F7_model(M2) is None:
                continue
            break
        else:
            return None, None
        e = len(M2[1]) - 1
        chain.append(M2)
        ops.append(['coext', e, b])
        M = M2
    return chain, ops

if __name__ == '__main__':
    F7 = std_F7(); K5 = std_MK5()
    print("F7:", mat_rank(F7), len(F7[1]), nbases(F7), flush=True)
    print("MK5:", mat_rank(K5), len(K5[1]), nbases(K5), flush=True)
    towers = []
    s = 1000
    seen = set()
    while len(towers) < 3 and s < 1200:
        s += 1
        chain, ops = coext_tower(s)
        if chain is None:
            continue
        M = chain[-1]
        if mat_rank(M) != 7:
            continue
        key = tuple(sorted(M[1]))
        if key in seen:
            continue
        st = mk5_search_stats(M)
        if st['found']:
            print(f"seed {s}: MK5 present, skip", flush=True)
            continue
        seen.add(key)
        towers.append((chain, ops, st, s))
        print(f"TOWER n={len(M[1])} r=7 seed={s} bases={nbases(M)} "
              f"mk5models={st['models_examined']} maxb={st['max_bases_seen']} "
              f"lam={conn_check(M)[1]['lambda_min_by_size']}", flush=True)
    # one bigger witness: extend a tower top by one element (keep 3-conn + F7)
    big = None
    for (chain, ops, st, s) in towers:
        M = chain[-1]
        r, cols = M
        for v in range(1, 1 << r):
            if v in set(cols):
                continue
            M2 = (r, cols + [v])
            ok, _ = conn_check(M2)
            if not ok:
                continue
            if find_F7_model(M2) is None:
                continue
            st2 = mk5_search_stats(M2)
            if st2['found']:
                continue
            big = (chain + [M2], ops + [['ext', len(cols), v]], st2, s)
            print(f"BIG n={len(M2[1])} r=7 bases={nbases(M2)} "
                  f"mk5models={st2['models_examined']} maxb={st2['max_bases_seen']}",
                  flush=True)
            break
        if big is not None:
            break
    allw = towers + ([big] if big else [])
    out = []
    for (chain, ops, st, s) in allw:
        out.append({'chain_mats': [[m[0], m[1]] for m in chain],
                    'ops': ops, 'seed': s, 'n': len(chain[-1][1]),
                    'nbases': nbases(chain[-1]),
                    'mk5': {k: v for k, v in st.items()
                            if k in ('models_examined', 'rank4_10elt_minors',
                                     'max_bases_seen', 'found')}})
    ART = '/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-433/output/artifacts'
    json.dump(out, open(ART + '/witnesses.json', 'w'))
    print("saved", len(out))
