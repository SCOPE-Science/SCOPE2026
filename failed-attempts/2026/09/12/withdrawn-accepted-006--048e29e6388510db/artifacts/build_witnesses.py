"""Build exact witnessed 4-rank table (final).
r4 = 1 iff 4 | h_ordinary. Witnesses (all verified by integer substitution):
- r4=1, N=+1 (5 fields): (x,y) with x^2-Dy^2 in {+-4p,+-4q}  (unramified C4-generator norms).
- r4=1, N=-1 (8 fields): (x,y) with x^2-Dy^2 = -4p^2 or -4q^2 (square-of-generator norms;
  every one found with y>0; listed with smallest y).
- r4=0, leg=-1 (46 fields): Legendre log (p/q)=-1.
- r4=0, leg=+1 (22 fields): unit-norm cert (N=+1) + rho h+=4 log.
Writes witnessed_table.json.
"""
import json, math, os
HERE = os.path.dirname(os.path.abspath(__file__))
rows = json.load(open(os.path.join(HERE, "census.json")))
norms = {c["D"]: c for c in json.load(open(os.path.join(HERE, "norms_cert.json")))}

def find_all(D, t, ymax):
    sols = []
    for y in range(0, ymax + 1):
        v = D * y * y + t
        if v < 0:
            continue
        x = math.isqrt(v)
        if x * x == v and (x & 1) == (y & 1):
            sols.append([x, y])
    return sols

YMAX = 400000
table = []
for r in rows:
    D, p, q = r["D"], r["p"], r["q"]
    N = norms[D]["N"]
    hplus = r["hplus"]
    h = hplus if N == -1 else hplus // 2
    assert h == r["h"] and h % 2 == 0, (D,)
    r4 = 1 if h % 4 == 0 else 0
    assert r4 == r["r4"], (D,)
    leg = r["leg"]
    entry = dict(p=p, q=q, D=D, leg_pq=leg, redei_rank=0 if leg == 1 else 1,
                 period=r["period"], N=N, hplus=hplus, h=h, r4=r4)
    if r4 == 1:
        assert leg == 1, (D,)
        if N == 1:
            cands = [("4p", 4 * p), ("-4p", -4 * p), ("4q", 4 * q), ("-4q", -4 * q)]
        else:
            cands = [("-4p2", -4 * p * p), ("4p2", 4 * p * p),
                     ("-4q2", -4 * q * q), ("4q2", 4 * q * q)]
        wit = {}
        for name, t in cands:
            s = [z for z in find_all(D, t, YMAX) if z[1] > 0]
            if s:
                s.sort(key=lambda z: (z[1], z[0]))
                wit[name] = dict(t=t, sol=s[0])
        assert wit, (D, "no norm witness found")
        # prefer square witnesses (-4p2 etc.) for N=-1, generator norms for N=+1
        entry["witness"] = dict(kind="norm_solution", hits=wit)
    else:
        if leg == -1:
            entry["witness"] = dict(kind="legendre_obstruction", note="(p/q)=-1 so Redei rank 1")
        else:
            assert N == 1 and h % 4 != 0, (D,)
            entry["witness"] = dict(kind="unit_norm_obstruction",
                                    note="Redei rank 0 but N(eps)=+1; rho ordinary h=2 (h+=%d), so no C4" % hplus)
    table.append(entry)

json.dump(table, open(os.path.join(HERE, "witnessed_table.json"), "w"))
n1 = sum(1 for e in table if e["r4"] == 1)
print("fields:", len(table), " r4=1:", n1, " r4=0:", len(table) - n1)
from collections import Counter
print(Counter((e["leg_pq"], e["N"], e["r4"]) for e in table))
for e in table:
    if e["r4"] == 1:
        print("r4=1:", e["p"], e["q"], e["D"], "N=", e["N"], "h=", e["h"],
              {k: v["sol"] for k, v in e["witness"]["hits"].items()})
print("WITNESSED_TABLE_OK")
