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

# Reproduction and limits

The proof is in `RESULT.md`. Reproduce `verification_output.txt` with `python verify.py` using `requirements.txt` (SymPy 1.14.0 and mpmath 1.3.0).

The executable verifies exact symbolic Hermite endpoint identities and discriminant identities. It builds rational upper and lower bounds for \(e^{-z}\) using a truncated positive Taylor series for \(e^z\) and a geometric majorant for the remainder; it verifies every Bernstein coefficient on four subintervals is positive for the lower-bound cubic at \(z=19/5\), giving rigorous positivity on the entire interval. It also proves \(H_{39/10}(2/3)<0\) using an exact-rational upper enclosure, and shows that the wholly positive interpolant at \(z=7/2\) already has a positive interior slope. Finally it solves the double-root system at 80 decimal digits and numerically tests the small-positive-parameter root splitting. The packaged run reports 50 passing assertions.

The uniqueness of the critical parameter, multiplicity of its zero, exact two-root count above threshold, and square-root asymptotic for all sufficiently small perturbations are established analytically in the written proof, not inferred from the finite tests. The 80-digit root output is not a validated high-precision interval proof. The two rational bracket endpoints and the full global theorem are verified separately. Independent scientific review has not been performed.
