# Exhaustive solver-free verifier: iterates ALL 29700 refined cells
# (10 maximal triples x minimal sets of size 3,4 x F in M x witness maps),
# rebuilds each cell's row system, and asserts every combo is decided by
# exactly one stored certificate in maincerts.json:
#  - "strong": exact rational dual bound certificate with bound >= 3;
#  - direct "branches" leaf: exact rational dual bound certificate with
#    bound > 2 (integer rounding gives W >= 3 since W is integer-valued
#    on integer points);
#  - "infeasible" or infeasible branch leaf: exact Farkas ray in
#    U/V/cert format.
# No LP solver is used anywhere in this file (Fraction arithmetic only).
import os
from fractions import Fraction
import json
from itertools import combinations, product
from rowsutil import rows, J, check_bound, check_infeas

_HERE = os.path.dirname(os.path.abspath(__file__))
main = json.load(open(os.path.join(_HERE, "maincerts.json")))
strong = {}
for s in main["strong"]:
    key = (tuple(s["M"]), tuple(s["A"]), s["F"],
           tuple(sorted((int(k), v) for k, v in J(s["wm"]).items())),
           tuple(sorted((int(k), v) for k, v in J(s["wn"]).items())))
    strong[key] = s
infeas = {}
for s in main.get("infeasible", []):
    key = (tuple(s["M"]), tuple(s["A"]), s["F"],
           tuple(sorted((int(k), v) for k, v in J(s["wm"]).items())),
           tuple(sorted((int(k), v) for k, v in J(s["wn"]).items())))
    infeas[key] = s
branch = {}
for b in main["branches"]:
    M, A, F, wm, wn = b["cell"]
    key = (tuple(M), tuple(A), F,
           tuple(sorted((int(k), v) for k, v in J(wm).items())),
           tuple(sorted((int(k), v) for k, v in J(wn).items())))
    branch[key] = b

n_strong = n_infeas = n_branch = 0
total = 0
for M in combinations(range(1, 6), 3):
    for r in (3, 4):
        for A in combinations(range(1, 6), r):
            e = 1 + len(A)
            nonmax = [q for q in range(1, 6) if q not in M]
            nonmin = [j for j in range(1, 6) if j not in A]
            for F in M:
                for wmt in product(M, repeat=len(nonmax)):
                    for wnt in product(A, repeat=len(nonmin)):
                        total += 1
                        wm = dict(zip(nonmax, wmt))
                        wn = dict(zip(nonmin, wnt))
                        key = (tuple(M), tuple(A), F,
                               tuple(sorted(wm.items())),
                               tuple(sorted(wn.items())))
                        o, oc, R = rows(tuple(M), tuple(A), F, wm, wn, e, [])
                        if key in strong:
                            s = strong[key]
                            check_bound(o, oc, R, s["U"], s["V"], Fraction(3, 1))
                            n_strong += 1
                        elif key in infeas:
                            check_infeas(R, infeas[key]["cert"])
                            n_infeas += 1
                        elif key in branch:
                            b = branch[key]
                            assert b["leaves"], "empty leaves for %r" % (key,)
                            for lf in b["leaves"]:
                                ex = [tuple(x) for x in lf["extra"]]
                                o2, oc2, R2 = rows(tuple(M), tuple(A), F, wm, wn, e, ex)
                                if lf["status"] == "bound":
                                    check_bound(o2, oc2, R2, lf["U"], lf["V"], Fraction(21, 10))
                                else:
                                    assert lf["status"] == "infeasible", lf["status"]
                                    check_infeas(R2, lf["cert"])
                            n_branch += 1
                        else:
                            raise AssertionError("combo undecided: %r" % (key,))
assert total == 29700, total
assert n_strong + n_infeas + n_branch == 29700, (n_strong, n_infeas, n_branch)
print("exhaustive enumeration verified: total=%d strong=%d infeasible=%d branched=%d"
      % (total, n_strong, n_infeas, n_branch))
