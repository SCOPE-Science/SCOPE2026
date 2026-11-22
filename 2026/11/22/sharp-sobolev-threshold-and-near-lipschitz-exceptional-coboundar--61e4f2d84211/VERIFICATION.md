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

# Verification of the sharp Sobolev threshold and endpoint family

**Analytic checks.** The dyadic separation estimate controls the inverse-square divisor sum; Cauchy–Schwarz reconstructs a real continuous transfer when the Sobolev order exceeds one. At the endpoint, convergent identities give positive small divisors of order reciprocal to the frequencies; the transfer is square-integrable but has unbounded positive Fejér means. The difference of cosines has a uniform bound and a common signed small-increment lower bound, yielding matching two-sided moduli. The slow-block construction is square-summable yet not summable and beats any prescribed diverging nondecreasing gauge.

**Standalone finite checks.** Run `python verify_rotation.py` with Python 3 and `mpmath`. The code uses 85-digit working precision, exact Fibonacci identities, positive convergent errors, exact rational harmonic-sum proxies, and truncated modulus ratios at eight scales. Observed: `PASS: 186 finite checks`. The finite checks test only consistency of examples; no claimed infinite result is inferred from a finite computation.

**Scientific limits.** The theorem concerns bounded-type irrational circle rotations and real additive cohomology, not unbounded-type angles or circle-valued cocycles. General qualitative measurable noncontinuous examples are already known. Exact gauge bounds are asymptotic, and no effective constants are asserted for an arbitrary nonconstructively specified gauge. Historical priority is not an independent certification.
