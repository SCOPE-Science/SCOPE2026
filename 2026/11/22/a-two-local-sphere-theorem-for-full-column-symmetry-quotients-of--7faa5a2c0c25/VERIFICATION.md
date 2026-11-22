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

Exact reproducible checks: `python3 verify.py` enumerates every orbit of nested nonempty faces, not a sample of labelled faces, for widths 4, 5 and 6. It constructs all quotient mod-two boundary matrices, verifies consecutive boundaries compose to zero, and performs exact bit-vector elimination. All three quotient complexes have mod-two Betti vector `(1,0,0,0,0,1)` in degrees 0 through 5. The generator confirms that column-type orbit-cell models cease changing at width six; the proof explains why this stabilization holds for every later width.

The code does not calculate integral odd-primary torsion or the full integral homotopy type. Simple connectivity and the two-local Whitehead step are mathematical consequences proved in RESULT.md, not replaced by finite experiments.
