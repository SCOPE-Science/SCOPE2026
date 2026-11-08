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

# Supplementary verification

The proof is an exact universal argument in the accompanying RESULT.md. The separate `ellipse_phase_checker.py` uses symbolic polynomial identities over rational \(a,b\) and numerical comparisons across small degrees to corroborate its critical formulas.

Run `python ellipse_phase_checker.py` with SymPy and NumPy installed. The expected output is exactly `ELLIPSE_PHASE_CHECK_PASS 64`.

The checker verifies (a) the recurrence generating the two extreme powers under the ellipse parametrization and the associated intensity identity, (b) real-linear rank of the sampled lifted profile forms at admissible equispaced grids, (c) recovery of full intensity by the displayed interpolation formula at additional unit-circle test points, and (d) actual polynomial ambiguities at the excluded half-shifts. Exact symbolic steps cover degrees \(1\) through \(6\) for two rational ellipses; floating-point comparisons cover degrees \(1\) through \(4\). Numerical accuracy does not prove injectivity or minimality in all dimensions. Rigidity in arbitrary degree is established by the rational-function dilation argument in RESULT.md. The only stability statement made is exact-data uniqueness, not a uniform numerical bound.

Independent mathematical audit has not been performed.
