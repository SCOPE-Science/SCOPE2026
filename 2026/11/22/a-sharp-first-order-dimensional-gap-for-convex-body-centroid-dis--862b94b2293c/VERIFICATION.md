---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The sharp constant is correctly imported from the affine variational formula with exponent m=n-2. The objective is variance divided by mean, so reflection strictly improves increasing profiles. Integrating (t²w)' and using -w'≥sw proves F_m(s)≤2/s, which keeps all large-m maximizers in a fixed compact interval. Independently, with A=e^s−1 and B=A−s the limiting objective simplifies to 1/s+1/A−s/B; its derivative gives the displayed numerator with denominator s²A²B² and the opposite sign. The Taylor coefficients vanish through order 7, are negative in orders 8–13, and are positive starting at 14 by the stated induction (the cubic in that induction becomes h³+24h²+155h+264 at k=14+h). Therefore the derivative of P(s)/s^13 is positive on s>0 and the unique positive zero is nondegenerate. The uniform C² expansion of the affine-power weights gives strict concavity near that zero and a displacement O(m^-1) of the sole eventual scalar maximizer; stationarity then leaves the displayed first-order correction in its value. Independent replay: python3 /workspace/centroid_independent_certificate.py, using exact rational geometric and alternating Taylor tails rather than the supplied moment enclosure, verified the signs at 2.353317385 and 2.353317386 and obtained 0.038267059667≤C≤0.038267062326. This certifies positivity, not an explicit finite-dimensional threshold. Uniqueness refers to the normalized affine profile, not a convex body.

## originality

PASS

The sharp inequality, variational constant, limit and approximate optimizing argument are prior. The inspected results do not give the explicit positive first-order gap with quadratic-order remainder or the continuous and eventual scalar optimizer uniqueness proved here. This is a bounded comparison, not a claim of universal priority.

## value

PASS

Quantifies the dimensional deficit of a natural sharp geometric bound, beyond a known limiting value. The positive exact coefficient distinguishes a genuine 1/n gap from faster convergence, and the nondegenerate unique profile controls how the optimizing affine shape approaches its limit. This does not claim new extremizing bodies or a bound for every small dimension.

The dated certificate retains the supplied scientific assessment, sources and limitations.
