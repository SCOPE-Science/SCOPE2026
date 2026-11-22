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

To reproduce the checks, run `python3 check.py` beside this document. Python's standard library suffices. Exact rational arithmetic verifies the four cubic corner derivatives and their coefficients, the maxima \(U(1/3)=4/27\) and \(W(2/3)=-4/27\), and all selector-column norms for \(2\le n\le9\) and five scales. An independent numerical total-variation routine splits cubic polynomials at stationary points and checks explicit attaining input pairs through 29 sites, randomized rational pairs, and loss of individual variation preservation beyond the sharp scale interval.

Expected final output line: `ALL_MINMOD_HERMITE_BV_CERTIFICATES_PASS`.

The exact all-dimensional theorem is established by the proof in RESULT.md; the finite checks are supplementary and do not certify every real input or every dimension by enumeration. Full-text comparison with some older publisher literature remains incomplete. Independent audit was not performed.
