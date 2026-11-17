---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

PASS: Dual Lipschitz unit ball is {s: Σs_i=0, |s_i|<=1 for m unit edges, |s_(m+1)|<=p}. At a vertex at most one coordinate is slack. The parity p≡m (mod2) excludes slack ordinary coordinates at t=p; wall vertices consist precisely of feasible m-sign vectors. Fully tight vertices count 2*C(m,(m−p)/2) and give nonsimplicial facets with m+1 molecule vertices. Counting slack indices at t=p±ε yields F−=F+(m+p−2)C and F+=F+(m−p)C. Independent exact Fraction active-set enumeration verified all count types in six pairs, including m=4 p=2 (30,14,22), m=5 p=3 (60,30,40). Finite cases are corroboration.

## originality

FAIL

FAIL: The earlier stronger primary published mathematical finding covers the claimed exact theorem and all substantive consequences. The current wall formula and facet stratification are direct specializations of the previously derived complete vertex partition; the remaining asymmetric excess formulas are one-line binomial evaluations of the prior formula. O fails.

## value

FAIL

FAIL: A November 2 published theorem already enumerates the complete facet count for every positive real special-edge length t and all cycle orders, including every integer resonance and nonsimplicial facet size. The proposed wall valley and its asymmetric jumps are direct substitution/evaluation of this stronger exact t-formula, not a new motivated independent result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
