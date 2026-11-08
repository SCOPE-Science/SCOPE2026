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

The self-contained `checker.py` uses only Python's standard library. Run `python checker.py` to verify exact-rational second-moment agreement between the Laplace-series formula and independently derived backward-generator moment boundary equations, check the derivative sign factor and critical-rate example, and exercise parameter cases. Its recorded execution passed 294 exact-rational cases; an independent high-precision evaluation of the full hyperbolic Laplace transform at three parameter choices gave second-moment differences below \(2\times10^{-9}\).

Mathematical completeness comes from the symbolic backward-generator derivation and the affine sign of the derivative numerator; numerical tests cannot establish the quantified global theorem. No external mathematical validation or independent audit has been performed.
