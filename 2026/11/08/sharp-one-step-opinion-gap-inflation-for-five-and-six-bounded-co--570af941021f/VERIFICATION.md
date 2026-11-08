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

# Exact verification

Run `python3 verify.py` with standard Python 3. The script independently reconstructs each binary contact-mask vertex, evaluates all permitted neighbor means with `fractions.Fraction`, and asserts the exact bound for \(n=2,3,4,5,6\). It reports 1, 2, 8, 55, and 549 weak-feasible graph masks, with 2, 12, 78, 616, and 6150 corresponding exact vertex-gap comparisons. It also checks every initial spacing vector in a four-value rational grid for each size and tests both explicit witnesses.

The general infinite-domain component is the mathematical proof that the closed-cell constraint matrix is totally unimodular with integral vertices, and that every strict-contact cell has the stated closure. The finite program is exhaustive for those vertices but does not, without that theorem, prove a bound on a continuum. No assessment by an independent reviewer is represented here.
