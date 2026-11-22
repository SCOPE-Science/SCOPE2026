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

## Analytic verification
The proof uses the exact unique \(\ell_p\) duality functional, two parameterized weighted Young inequalities with their equality conditions, direct half-line summation and unit geometric sequences. Its plateau argument is established with long constant blocks; nonattainment follows from strictness of the Young deficits for nonzero \(\ell_p\) vectors. The critical curvature is an exact differentiation of the closed-form formulas. The statements hold for every real coupling strength \(t\ge0\) and \(1<p<\infty\).

## Finite diagnostic
Run `python checker.py` from the same directory with NumPy installed. The expected output is `BOUNDARY_NUMERICAL_RADIUS_DIAGNOSTIC_OK 28860`. Every sampled vector is checked against the relevant exact bound, geometric vectors against analytic equality, and critical radii against their curvature. Finite tests cannot certify the universal theorem and are not a replacement for the proof.

## Scope and outstanding checks
The Hilbert specialization is already published. Bibliographic originality remains conditional on the inspected coverage; older unindexed variational literature may contain an implicit implication. Independent external audit has not been performed.
