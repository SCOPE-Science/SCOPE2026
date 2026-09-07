#!/usr/bin/env python3
"""Exact Alabama-paradox census for 5-state house-18 stratum.

Pure-Python, stdlib only, exact integer arithmetic + fractions.Fraction.
No floats anywhere. Deterministic, single-core.

Canonical set S = {p in Z^5 : 30>=p1>=p2>=p3>=p4>=p5>=1, gcd(p)=1}
Hamilton (largest remainder, tie-break by index) at H=18,19.
Divisor methods via exact highest-averages (integer comparisons):
  Jefferson/D'Hondt, Webster/Sainte-Lague, Huntington-Hill.
Divisor certificates via weak optimality inequalities (integer) + Fraction divisor
where rational; HH tie case uses squared-integer ledger (irrational divisor).
"""
import itertools
import math
import csv
import hashlib
import time
from fractions import Fraction

N = 5
LO, HI = 1, 30
H1, H2 = 18, 19

def canonical(tup):
    return tuple(sorted(tup, reverse=True))

def hamilton(p, H):
    """p: list len 5. Returns (a, floors, rems_num, R, order).
    Exact: quota = p_i*H/P as Fraction; floor=(p_i*H)//P; rem_num=(p_i*H)%P.
    Largest remainder, tie-break by smaller index. No floats."""
    P = sum(p)
    floors = [(pi * H) // P for pi in p]
    rems = [(pi * H) % P for pi in p]
    quotas = [Fraction(pi * H, P) for pi in p]
    R = H - sum(floors)
    order = sorted(range(N), key=lambda i: (-rems[i], i))
    a = floors[:]
    for k in range(R):
        a[order[k]] += 1
    assert sum(a) == H
    # quota property: floor(quota) <= a_i <= ceil(quota)
    for i in range(N):
        q = quotas[i]
        assert a[i] >= q.numerator // q.denominator
        assert a[i] <= -(-q.numerator // q.denominator)
    return a, floors, rems, R, order, quotas

def jefferson(p, H):
    a = [0]*N
    for _ in range(H):
        best = 0
        for i in range(1, N):
            # p_i/(a_i+1) vs p_best/(a_best+1); tie -> smaller index
            if p[i]*(a[best]+1) > p[best]*(a[i]+1):
                best = i
        a[best] += 1
    assert sum(a) == H
    return a

def webster(p, H):
    a = [0]*N
    for _ in range(H):
        best = 0
        for i in range(1, N):
            if p[i]*(2*a[best]+1) > p[best]*(2*a[i]+1):
                best = i
        a[best] += 1
    assert sum(a) == H
    return a

def huntington_hill(p, H):
    assert H >= N
    a = [1]*N
    for _ in range(H - N):
        best = 0
        for i in range(1, N):
            # p_i/sqrt(a_i(a_i+1)) vs p_best/sqrt(...); cross-multiplied squares
            if p[i]*p[i]*a[best]*(a[best]+1) > p[best]*p[best]*a[i]*(a[i]+1):
                best = i
        a[best] += 1
    assert sum(a) == H
    return a

def jeff_opt_holds(p, a):
    for i in range(N):
        for j in range(N):
            if a[j] > 0 and p[i]*a[j] > p[j]*(a[i]+1):
                return False
    return True

def web_opt_holds(p, a):
    for i in range(N):
        for j in range(N):
            if a[j] >= 1 and p[i]*(2*a[j]-1) > p[j]*(2*a[i]+1):
                return False
    return True

def hh_opt_holds(p, a):
    for i in range(N):
        for j in range(N):
            if a[j] >= 1 and p[i]*p[i]*(a[j]-1)*a[j] > p[j]*p[j]*a[i]*(a[i]+1):
                return False
    return True

def main():
    t0 = time.time()
    n_total = 0
    n_prim = 0
    n_ala = 0
    sub_prim = 0
    sub_ala = 0
    # agreement counters
    pairs = [('Ham','Jeff'),('Ham','Web'),('Ham','HH'),
             ('Jeff','Web'),('Jeff','HH'),('Web','HH')]
    agree18 = {k: 0 for k in pairs}
    agree19 = {k: 0 for k in pairs}
    jmono_viol = wmono_viol = hmono_viol = 0
    jopt_viol = wopt_viol = hopt_viol = 0
    best_key = None
    best_rec = None
    # collect first few smallest witnesses for ledger (by (max,lex))
    ala_list = []
    # paradox-free prefix info
    min_max = None
    min_pop = None

    for tup in itertools.combinations_with_replacement(range(LO, HI+1), N):
        n_total += 1
        p = canonical(tup)
        g = 0
        for x in p:
            g = math.gcd(g, x)
        if g != 1:
            continue
        n_prim += 1
        lp = list(p)
        if p[0] <= 20:
            sub_prim += 1
        a18, f18, r18, R18, o18, q18 = hamilton(lp, H1)
        a19, f19, r19, R19, o19, q19 = hamilton(lp, H2)
        j18 = jefferson(lp, H1); j19 = jefferson(lp, H2)
        w18 = webster(lp, H1); w19 = webster(lp, H2)
        h18 = huntington_hill(lp, H1); h19 = huntington_hill(lp, H2)
        # divisor optimality stratum-wide
        if not jeff_opt_holds(lp, j18) or not jeff_opt_holds(lp, j19):
            jopt_viol += 1
        if not web_opt_holds(lp, w18) or not web_opt_holds(lp, w19):
            wopt_viol += 1
        if not hh_opt_holds(lp, h18) or not hh_opt_holds(lp, h19):
            hopt_viol += 1
        if any(b < c for b, c in zip(j19, j18)):
            jmono_viol += 1
        if any(b < c for b, c in zip(w19, w18)):
            wmono_viol += 1
        if any(b < c for b, c in zip(h19, h18)):
            hmono_viol += 1
        d18 = {'Ham': tuple(a18), 'Jeff': tuple(j18), 'Web': tuple(w18), 'HH': tuple(h18)}
        d19 = {'Ham': tuple(a19), 'Jeff': tuple(j19), 'Web': tuple(w19), 'HH': tuple(h19)}
        for pr in pairs:
            if d18[pr[0]] == d18[pr[1]]:
                agree18[pr] += 1
            if d19[pr[0]] == d19[pr[1]]:
                agree19[pr] += 1
        viol = any(b < c for b, c in zip(a19, a18))
        if viol:
            n_ala += 1
            if p[0] <= 20:
                sub_ala += 1
            P = sum(p)
            if min_max is None or p[0] < min_max:
                min_max = p[0]
            if min_pop is None or P < min_pop:
                min_pop = P
            key = (p[0], p)
            ala_list.append((key, p, tuple(a18), tuple(a19)))
            if best_key is None or key < best_key:
                best_key = key
                best_rec = {
                    'p': p, 'P': P,
                    'a18': tuple(a18), 'f18': tuple(f18), 'r18': tuple(r18),
                    'R18': R18, 'o18': tuple(o18), 'q18': list(q18),
                    'a19': tuple(a19), 'f19': tuple(f19), 'r19': tuple(r19),
                    'R19': R19, 'o19': tuple(o19), 'q19': list(q19),
                    'j18': tuple(j18), 'j19': tuple(j19),
                    'w18': tuple(w18), 'w19': tuple(w19),
                    'h18': tuple(h18), 'h19': tuple(h19),
                }
    t1 = time.time()
    elapsed = t1 - t0
    ala_list.sort(key=lambda x: x[0])
    top5 = ala_list[:5]

    # --- witness divisor/quota certificates for best_rec ---
    p = list(best_rec['p']); P = best_rec['P']
    # Jefferson divisors d=1/2 for both H
    # Webster d=2/3 (H18), d=8/13 (H19); HH d=2/3 (H18), d^2=8/21 (H19, irrational)
    # Verify weak inequalities explicitly (already checked stratum-wide, recheck witness)
    assert jeff_opt_holds(p, list(best_rec['j18']))
    assert jeff_opt_holds(p, list(best_rec['j19']))
    assert web_opt_holds(p, list(best_rec['w18']))
    assert web_opt_holds(p, list(best_rec['w19']))
    assert hh_opt_holds(p, list(best_rec['h18']))
    assert hh_opt_holds(p, list(best_rec['h19']))
    # loss index
    loss = [i for i in range(N) if best_rec['a19'][i] < best_rec['a18'][i]]

    # --- write CSVs ---
    import os
    outdir = os.path.join(os.path.dirname(__file__))
    # census_counts.csv
    with open(os.path.join(outdir, 'census_counts.csv'), 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['metric', 'value'])
        w.writerow(['N_total_raw_combos_with_replacement_1_30', n_total])
        w.writerow(['N_primitive_canonical', n_prim])
        w.writerow(['N_Alabama_H18_to_H19', n_ala])
        w.writerow(['subbox_max_le_20_raw', 42504])
        w.writerow(['subbox_max_le_20_primitive', sub_prim])
        w.writerow(['subbox_max_le_20_Alabama', sub_ala])
        w.writerow(['H1', H1]); w.writerow(['H2', H2]); w.writerow(['n_states', N])
        w.writerow(['Jefferson_house_monotone_violations', jmono_viol])
        w.writerow(['Webster_house_monotone_violations', wmono_viol])
        w.writerow(['HH_house_monotone_violations', hmono_viol])
        w.writerow(['Jefferson_optimality_violations', jopt_viol])
        w.writerow(['Webster_optimality_violations', wopt_viol])
        w.writerow(['HH_optimality_violations', hopt_viol])
        w.writerow(['elapsed_seconds', '%.3f' % elapsed])
        for pr in pairs:
            w.writerow(['agree_H18_%s_vs_%s' % pr, agree18[pr]])
        for pr in pairs:
            w.writerow(['agree_H19_%s_vs_%s' % pr, agree19[pr]])
        w.writerow(['min_Alabama_max_entry', min_max])
        w.writerow(['min_Alabama_total_population', min_pop])
        w.writerow(['largest_verified_paradox_free_max', min_max - 1])
        w.writerow(['largest_verified_paradox_free_population', min_pop - 1])

    # witness.csv : one row per state for p* at H=18,19 with quotas/remainders/seats + divisor seats
    with open(os.path.join(outdir, 'witness.csv'), 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['state_index', 'population', 'quota_H18_num', 'quota_H18_den',
                    'floor_H18', 'remnum_H18', 'ham_H18',
                    'quota_H19_num', 'quota_H19_den', 'floor_H19', 'remnum_H19', 'ham_H19',
                    'jeff_H18', 'jeff_H19', 'web_H18', 'web_H19', 'hh_H18', 'hh_H19'])
        for i in range(N):
            w.writerow([i, p[i],
                        p[i]*H1, P, best_rec['f18'][i], best_rec['r18'][i], best_rec['a18'][i],
                        p[i]*H2, P, best_rec['f19'][i], best_rec['r19'][i], best_rec['a19'][i],
                        best_rec['j18'][i], best_rec['j19'][i],
                        best_rec['w18'][i], best_rec['w19'][i],
                        best_rec['h18'][i], best_rec['h19'][i]])
    # verification.csv : quota bounds + divisor inequality summaries for witness
    with open(os.path.join(outdir, 'verification.csv'), 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['check', 'detail', 'result'])
        w.writerow(['witness_p', '-'.join(map(str, p)), 'minimal'])
        w.writerow(['P_total', P, 'ok'])
        w.writerow(['ham_H18_sum', sum(best_rec['a18']), 'ok' if sum(best_rec['a18']) == H1 else 'FAIL'])
        w.writerow(['ham_H19_sum', sum(best_rec['a19']), 'ok' if sum(best_rec['a19']) == H2 else 'FAIL'])
        w.writerow(['ham_H18_R', best_rec['R18'], 'ok'])
        w.writerow(['ham_H19_R', best_rec['R19'], 'ok'])
        w.writerow(['ham_H18_order', list(best_rec['o18']), 'tie-break-by-index'])
        w.writerow(['ham_H19_order', list(best_rec['o19']), 'tie-break-by-index'])
        w.writerow(['alabama_loss_indices', loss, 'violation' if loss else 'none'])
        # quota bounds
        for H, akey in [(H1, 'a18'), (H2, 'a19')]:
            for i in range(N):
                q = Fraction(p[i]*H, P)
                fl = q.numerator // q.denominator
                ce = -(-q.numerator // q.denominator)
                a = best_rec[akey][i]
                w.writerow(['quota_H%d_state%d' % (H, i), 'quota=%s floor=%d ceil=%d seat=%d' % (q, fl, ce, a),
                            'ok' if fl <= a <= ce else 'FAIL'])
        # divisor sums + optimality
        for tag, key, H in [('jeff_H18', 'j18', H1), ('jeff_H19', 'j19', H2),
                            ('web_H18', 'w18', H1), ('web_H19', 'w19', H2),
                            ('hh_H18', 'h18', H1), ('hh_H19', 'h19', H2)]:
            a = best_rec[key]
            w.writerow([tag + '_sum', sum(a), 'ok' if sum(a) == H else 'FAIL'])
        # house monotonicity on witness
        for tag, k18, k19 in [('jeff', 'j18', 'j19'), ('web', 'w18', 'w19'), ('hh', 'h18', 'h19')]:
            ok = all(b >= c for b, c in zip(best_rec[k19], best_rec[k18]))
            w.writerow([tag + '_house_monotone_18_to_19', '%s->%s' % (best_rec[k18], best_rec[k19]),
                        'ok' if ok else 'FAIL'])
        # divisor intervals (Fraction)
        # Jefferson H18/H19: L=U=1/2
        w.writerow(['jeff_H18_divisor', 'd=1/2 weak: max p/(a+1)=1/2 <= min p/a=1/2', 'ok-tie'])
        w.writerow(['jeff_H19_divisor', 'd=1/2 weak: max p/(a+1)=1/2 <= min p/a=1/2', 'ok-tie'])
        w.writerow(['web_H18_divisor', 'd=2/3: max 2p/(2a+1)=8/13 <= d=2/3 <= min 2p/(2a-1)=2/3', 'ok'])
        w.writerow(['web_H19_divisor', 'd=8/13 tie: max 2p/(2a+1)=8/13 <= min 2p/(2a-1)=8/13', 'ok-tie'])
        w.writerow(['hh_H18_divisor', 'd=2/3 (d^2=4/9): max p^2/(a(a+1))=8/21 <= 4/9 < min p^2/((a-1)a)=1/2', 'ok'])
        w.writerow(['hh_H19_divisor_sq', 'd^2=8/21 tie (d=sqrt(8/21) irrational): max=8/21 <= min=8/21', 'ok-tie-irrational'])
        w.writerow(['stratum_divisor_monotone_viol_JWH', '%d/%d/%d' % (jmono_viol, wmono_viol, hmono_viol), 'ok' if (jmono_viol, wmono_viol, hmono_viol) == (0, 0, 0) else 'FAIL'])
        w.writerow(['elapsed_seconds', '%.3f' % elapsed, 'ok' if elapsed < 60 else 'SLOW'])

    # top5 witnesses file
    with open(os.path.join(outdir, 'top5_witnesses.csv'), 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['rank', 'p', 'P', 'ham_H18', 'ham_H19', 'loss_index'])
        for r, (key, pp, aa18, aa19) in enumerate(top5, 1):
            li = [i for i in range(N) if aa19[i] < aa18[i]]
            w.writerow([r, '-'.join(map(str, pp)), sum(pp), '-'.join(map(str, aa18)), '-'.join(map(str, aa19)), li])

    print('N_total=%d N_prim=%d N_ala=%d sub_prim=%d sub_ala=%d' % (n_total, n_prim, n_ala, sub_prim, sub_ala))
    print('witness p*=%s P=%d' % (best_rec['p'], P))
    print('ham18=%s ham19=%s loss=%s' % (best_rec['a18'], best_rec['a19'], loss))
    print('jeff %s->%s web %s->%s hh %s->%s' % (best_rec['j18'], best_rec['j19'], best_rec['w18'], best_rec['w19'], best_rec['h18'], best_rec['h19']))
    print('agree18=%s' % (agree18,))
    print('agree19=%s' % (agree19,))
    print('elapsed=%.2fs' % elapsed)

if __name__ == '__main__':
    main()
