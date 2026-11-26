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

Gaussian convolution and the positive tilt give m(a)/m₀=Eν[q^β], with 0<β≤1 and positive tilted mass below 1. The even Gram block has determinant (1−q²)²+η(2+q⁴)+η²>0; the outer numerator is strictly positive and the center numerator is m₀(η−H(q)). The derivative H′/(4q³) is strictly decreasing from +∞ to (Eνβ−1)/2<0. Local differentiation is bounded uniformly in β on compact positive q-intervals, so no moment of the target scale is needed. Because H(0)=−1 and H(1)=0, the unique stationary point is a positive maximum, and each level gives precisely the stated count of crossing spacings, with their order reversed by q=e^(−a²/(2ℓ²)). Pointwise H(q)<2q−1−q⁴, maximized at 2^(−1/3); already evaluating at that q for single Gaussian targets as s/ℓ→∞ proves sharpness. At the stationarity point H″=4q_*²(E_*β−3)<0, where E_* tilts by (1+β)q_*^β. Taylor expansion and the nonzero derivative of spacing in q give the stated fold. The exact proof is sufficient; the finite checker was inspected, not executed.

## originality

PASS

The supported distinct result is the global spacing diagram under a fixed Gaussian kernel for arbitrary centered Gaussian scale-mixture targets: one maximum, sharp universal nugget and nondegenerate fold. The pointwise sign reduction is shared and is expressly not claimed as original.

## value

PASS

For a whole target family without moment restrictions, the result determines both an exact universally sufficient nugget and the only possible nonpositivity window at smaller noise. These are useful global properties not furnished by the pointwise Gram solve, and the fold quantifies how the window closes. No accuracy improvement or positivity of realized noisy outputs is inferred.

The dated certificate retains the supplied scientific assessment, sources and limitations.
