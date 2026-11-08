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

## Direct checks
The standalone `verify.py` calculates the exact first-end and joint-end vacancy probabilities by the first-edge recursion through n=100; it compares the finite exponential sums and confirms covariance signs using `fractions.Fraction`. It separately exhausts all (n-1)! dimer edge-priority orders for n=3,...,9 and matches both probabilities exactly. The analytic inequality and asymptotic are proved in `RESULT.md`; these finite tests do not certify any untested n.

## Scope and limitations
Only the finite, free-boundary, unbiased lattice dimer process and its jammed state are covered. The original 1959 finite-line study and 1994 spatial pair-correlation article were not available in full text, so historical priority remains qualified. Independent audit was not performed.
