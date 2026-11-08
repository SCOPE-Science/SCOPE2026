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

# Verification

Run `python3 verify.py` with the Python standard library. The code uses exact rational arithmetic, reconstructs both labeled graphs and all reachable informed subsets for up to eleven leaves, solves first-step expectations from the absorbing state backward, and compares them to the product-based analytic formulas (20 individual graph expectations). It also checks thirteen instances of the exact polynomial identity, the four boundary values, signs through fourteen leaves, and the positivity starting-point properties.

Expected initial output: `PASS: 13 exact product identities, 20 independently computed labeled-state expectations, four boundary fractions, signs, polynomial and asymptotic checks`.

The finite independent comparison is not an exhaustive proof for arbitrary graph sizes. The complete all-size argument appears in RESULT.md, based on independent Poisson thinning, conditional exponential waiting times, a beta-integral product, and the explicit positivity of \(P(m)\) for \(m\ge6\). The asymptotic check follows from \(F_m\le1/(m-1)\), not from a numerical limit.

Scientific limits: one initially informed leaf adjacent to the new edge; independent unit-rate Poisson calls; expected full broadcast time only. No external audit is asserted.
