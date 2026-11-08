---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and limits

Run `python3 artifacts/verify.py` in the extracted package. Python 3 standard library only; no network or data downloads are required. The checker enumerates exactly the nonempty connected-shore cuts for \(2\le p\le5\), \(p\le q\le8\), \(p+q\le11\), identifies each cut up to shore complement, computes all \(pq\times pq\) covariance entries with `Fraction`, and compares them against four analytic eigenspace actions. It checks the exact sign-change inequality for another 102 parameter profiles with \(2\le p\le18\). The reference replay reported:

`BICLIQUE_BOND_INERTIA_CHECKS_PASSED cases=19 vertices=5133 entries=6144 phases=102`

The count of entries includes all ordered pairs of edge coordinates. These finite experiments cannot certify the unbounded integer domain; the proof establishes this through exact shore-sign sums, invariant tensor subspaces, a strict positivity inequality, and induction. The probability space excludes zero incidence. The formula is not valid without adjustment for augmented bond polytopes that include the empty cut. Independent verification has not been performed.
