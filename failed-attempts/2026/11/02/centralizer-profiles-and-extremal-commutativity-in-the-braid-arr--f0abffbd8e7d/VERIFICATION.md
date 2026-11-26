---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The two products list the same nonempty cells; their row-first and column-first orders differ exactly when a pair of cells has reversed row and column indices. Thus each commuting partition is an arbitrary ordered partition inside each A_i, with the consecutive restrictions joined or kept separate independently at each interface. This yields the claimed factor and the multinomial composition multiplicities. The representation F_m = (1/2)∑_{r≥0} r^m/2^r gives strict log-convexity by Cauchy–Schwarz (the powers are not proportional on the positive support). Moving a unit from a larger part to a part at least two smaller lowers the product, and moving a unit from a part greater than one to a part at least as large raises it. This proves the precise balanced and concentrated equality cases, including trivial boundary compositions. The block generating function is T=(e^z−1)/(2−e^z), giving 1+T/(1−2T) and the Stirling expansion. The unique closest poles are log 2 and log(4/3), with residues −1/2 and −1/12 for the ordered Bell and commuting-pair series; taking the ratio of coefficients with the factorials gives the stated probability. The supplied Python checker is consistent with testing all pairs through n=5, not a proof of the asymptotic or extrema.

## originality

FAIL

An earlier distinct Resultary theorem already proves the same type-A centralizer profile, the composition-weighted distribution and the broader ordered commuting tuple count with the same cut bijection and corresponding asymptotic. Its r=2 specialization gives the semigroup interpretation claimed here, not merely the matching OEIS numbers. The fixed-k extremizers were not found stated there, but are a standard strict log-convexity consequence of the known profile; the probability limit just divides the earlier count by F_n².

## value

FAIL

The centralizer profile and commuting-pair interpretation are mathematically natural, but already established. Once the profile is known, the remaining probability and fixed-k extremes are respectively a quotient of known asymptotics and the standard balancing/concentration rule for a product of strictly log-convex terms. The frozen record identifies no additional invariant or question making either deduction a distinct valuable replacement claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
