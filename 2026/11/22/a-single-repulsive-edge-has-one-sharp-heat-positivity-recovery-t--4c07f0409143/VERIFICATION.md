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

The analytical proof in `RESULT.md` uses exact matrix block diagonalization, eigenvalue inequalities, a strictly convex derivative argument, convolution positivity for all times, Duhamel monotonicity and two matched limiting expansions. These are the complete correctness arguments for all integers \(m\ge2\) and allowed real \(a\).

`check_signed.py` (run with `python check_signed.py`, using NumPy, SciPy and SymPy) makes independent finite calculations on sizes \(m=2,3,4,7,12\), six stable antagonism fractions per size, 24 sampled positive times for each pair and exact symbolic matrix invariants. The supplied script completed 60,817 assertions. Its numerical tolerances and finite samples are explicitly **not** substitutes for proof of the continuum claims.

No independent mathematical audit or external certification was performed. Historical priority is not guaranteed by a finite literature search.
