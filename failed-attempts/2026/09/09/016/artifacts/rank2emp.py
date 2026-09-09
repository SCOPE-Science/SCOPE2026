"""rank2emp.py: rank>=2 via empirical torsion cosets.
tors(d,P0) = {delta(P0+Ti)/delta(P0)} — true torsion images, self-validated
(4 distinct + subgroup closure). Then <dP,dQ,tors> size 16 => rank>=2.
delta(P)=(sqf(x),sqf(x-9d)). All exact.
"""
import sys, math, itertools, json
sys.path.insert(0, '/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-310/output/artifacts')
from fractions import Fraction
from indep import sqf, sqfmul
from ecarith import add_pts, y2_of
from descent import rhs

def dl(d, Pt):
    return (sqf(Pt[0]), sqf(Pt[0] - 9*d))

def tors_emp(d, P0):
    T = [(Fraction(0), Fraction(0)), (Fraction(9*d), Fraction(0)), (Fraction(729*d), Fraction(0))]
    d0 = dl(d, P0)
    imgs = [((1, 1), (1, 1))]
    for Tk in T:
        S = add_pts(d, P0, Tk)
        assert S is not None, 'P0+Torsion = O?'
        dS = dl(d, S)
        imgs.append((sqfmul(dS[0], d0[0]), sqfmul(dS[1], d0[1])))
    keys = set((a[0], a[1], b[0], b[1]) for (a, b) in imgs)
    assert len(keys) == 4, f'torsion images not distinct: {imgs}'
    # closure
    for a, b in itertools.product(imgs, imgs):
        c = (sqfmul(a[0], b[0]), sqfmul(a[1], b[1]))
        k = (c[0][0], c[0][1], c[1][0], c[1][1])
        assert k in keys, f'not closed: {imgs}'
    return imgs

def cert_rank2_emp(d, P, Q):
    assert P[1]*P[1] == y2_of(d, P[0]) and Q[1]*Q[1] == y2_of(d, Q[0])
    t = tors_emp(d, P)
    dp, dq = dl(d, P), dl(d, Q)
    seen = set()
    for i, j in itertools.product((0, 1), (0, 1)):
        for tk in t:
            e1 = sqfmul(sqfmul(dp[0] if i else (1, 1), dq[0] if j else (1, 1)), tk[0])
            e2 = sqfmul(sqfmul(dp[1] if i else (1, 1), dq[1] if j else (1, 1)), tk[1])
            seen.add((e1[0], e1[1], e2[0], e2[1]))
    return (len(seen) == 16, len(seen))

def Ptof(d, xstr):
    x = Fraction(xstr)
    y2 = rhs(d, x)
    rn = math.isqrt(y2.numerator); rd = math.isqrt(y2.denominator)
    assert rn*rn == y2.numerator and rd*rd == y2.denominator and y2 > 0
    return (x, Fraction(rn, rd))

if __name__ == '__main__':
    cert = json.load(open('/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-310/output/artifacts/nontorsion.json'))
    out = {}
    for k, ents in cert.items():
        d = int(k)
        inf = [e for e in ents if e['infinite']]
        if len(inf) < 2:
            continue
        Pts = [Ptof(d, e['x']) for e in inf]
        hit = None
        for i, j in itertools.combinations(range(len(Pts)), 2):
            try:
                ok, n = cert_rank2_emp(d, Pts[i], Pts[j])
            except AssertionError as ex:
                ok, n = False, f'ERR {ex}'
            if ok:
                hit = (inf[i]['x'], inf[j]['x'])
                break
        out[k] = {'pair': list(hit) if hit else None, 'npts': len(inf)}
        print(k, 'RANK2' if hit else 'dep?', hit, flush=True)
    json.dump(out, open('/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-310/output/artifacts/rank2emp.json', 'w'), indent=0)
