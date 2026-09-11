"""Bounded recovery test: single-modulus congruence sieve.
For each k with no integral point to XMAX, test moduli 3<=m<500:
reports moduli m (if any) for which x^3+k mod m is never a quadratic residue
(which would certify emptiness elementarily). Stdlib only."""
import json

KS = [10002,10003,10004,10005,10006,10007,10010,10011,10013,10014,10015,
      10016,10018,10019,10020,10021,10022,10023,10024,10026,10028,10029,
      10030,10031,10032]


def ruled_out_mod(k, m):
    sq = {pow(y, 2, m) for y in range(m)}
    for x in range(m):
        if (pow(x, 3, m) + k) % m in sq:
            return False
    return True


res = {}
for k in KS:
    res[str(k)] = [m for m in range(3, 500) if ruled_out_mod(k, m)]
print(json.dumps({"modulus_range": [3, 500], "obstructing_moduli": res}, indent=1))
print("curves with >=1 obstructing modulus: "
      + str(sum(1 for v in res.values() if v)) + " of " + str(len(res)))
