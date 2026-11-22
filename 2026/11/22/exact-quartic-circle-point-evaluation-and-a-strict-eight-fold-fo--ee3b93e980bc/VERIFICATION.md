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

## Reproducibility
Run `python3 checker.py` with SymPy installed. It verifies the exact polynomial, derivative and elimination identities, a Sturm real-root count, rational root bounds, the subresultant reconstruction and an exact three-tangent lower certificate. This checker was executed successfully.

The proof of global optimality relies on strict convexity of the complex \(L^4\) functional under fixed point evaluation, uniqueness under conjugation/reversal, and exact stationarity. Machine arithmetic is used to verify polynomial identities and rational signs, not to infer global optimality from finite samples.

## Limits
The statement concerns only polynomials of degree at most four. The decimal constant is an approximation to an explicitly specified algebraic number. The general 2026 contractivity preprint was not available for full-text inspection in this analysis; possible earlier equivalent results remain a bibliographic risk. Independent external audit has not been performed.
