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

From the extracted package directory, execute `python3 verify.py`. This implements the original derangement recurrence modulo increasing powers of three, enumerates one full period, and tests every attainable-residue cardinality against the theorem for exponents one through eight. It also verifies local derivative values and the critical-point valuation congruences using independently differentiated falling-factorial sums at finite precision. All arithmetic uses Python integers and the standard library.

The computed cases provide evidence for the infinite theorem, not an exhaustive proof at all moduli. Completeness rests on the analytic interpolation, Hensel lifting, square-coordinate change, exact intersection, and measure arguments in RESULT.md.
