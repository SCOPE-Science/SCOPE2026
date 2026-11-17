---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For every ω>0, the basis 1, C(t)=cos(ωt)−sin(ω)/ω, S(t)=sin(ωt) is orthogonal under average dt/2 with strictly positive Gram norms 1,A,B, and its evaluation functional has exact squared norm K(ω)=1+(cosω−s)²/A+sin²ω/B. Equality at fixed ω occurs only for the scalar Riesz representer. With t=2ω the odd contribution <3 is equivalent to t(2+cos t)−3sin t>0, proved by derivative for 0<t<3 and a coarse bound after 3. The centered even contribution <5 is equivalent to F(t)=t²(4−cos t)+9t sin t−24(1−cos t)>0: the degree-eight alternating Taylor expansion with decreasing tail and its explicit positive degree-3 polynomial controls 0<t≤6, and 3t²−9t−48>0 for t≥6. Thus 1+5+3=9 is never attained for positive gap. The ω→0 Taylor limits give 5 and 3, hence sharpness through the degree-two Legendre kernel. Independent Gram inversions at seven distinct gaps and inspection of exact-series code corroborate, not replace, the global inequalities.

## originality

PASS

Originality survives against real-frequency k-sparse extrapolation and exponential-sum Nikolskii inequalities: those primary theorems give general nonsharp coefficients rather than the exact all-ω formula, strictness, and unique kernel for this three-tone space. The confluent Legendre polynomial lower bound does not prove a uniform positive-gap upper bound.

## value

PASS

The exact sharp endpoint leverage for clustered Fourier tones is a naturally needed conditioning and evaluation invariant of sparse exponential interpolation. The analysis supplies all positive real frequency gaps, the universal optimal constant and unique gapwise extremizers; it resolves a genuine uniform-versus-confluent issue rather than merely calculating a Gram matrix at one chosen frequency.

The dated certificate retains the supplied scientific assessment, sources and limitations.
