---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The binomial average of the focal geometric marginal return gives the stated gain. For every size n>=3 the second derivative of its gain term is a positive prefactor times (delta_n-1)^2 times a strictly positive power of 1+(delta_n-1)x. Thus either G''>0 everywhere or G is affine. The nonconstant affine case gives at most one root; the constant-zero gain gives an interval of stationary points with no isolated or asymptotically stable one. Strict convexity gives at most two roots; when there are two, signs are +,-,+ and only the lower crossing attracts from both sides. A minimum tangency is one-sided, not asymptotically stable. The strict signs at 0, 1/4 and 1 in the exact three-size example are as stated, so it exhibits two interior roots with the stated stability. The example shows attainment with three sizes, not that three are necessary.

## originality

FAIL

The arbitrary-finite-order no-go is a direct corollary of the published convex-gain result of Peña and Nöldeke. Apply their Lemma 2 to a point-mass size distribution separately for each n and to the convex sequence d_k^(n)=b_n delta_n^k/n-c: its second difference is (b_n/n) delta_n^k(delta_n-1)^2>=0. Each corresponding expected gain is convex by the lemma. Positive averaging now allows completely independent sequences at the different sizes, with no shared-sequence hypothesis needed at that last step. The equilibrium bound then follows from their convex-gain root argument, or strict convexity/affine degeneracy and the scalar phase line. Two-order sharpness was already shown by Llabrés et al.; adding a third positive size at sufficiently small weight preserves the strict +,-,+ sign witnesses. The particular rational data check out but do not supply a non-implied sharpness statement. This is a coverage finding, not a failure caused by access limits.

## value

FAIL

Whether richer random-size mixtures can yield more coexistence states is a legitimate modeling question, but this record does not resolve a substantive gap beyond the known convex-gain closure argument. The derivative/endpoint criterion is the usual horizontal-level test for a strict convex polynomial, and adding a third size preserves existing two-root behavior by continuity. The particular rational parameters are one illustration of that already guaranteed possibility, not an independently motivated exact instance or new threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
