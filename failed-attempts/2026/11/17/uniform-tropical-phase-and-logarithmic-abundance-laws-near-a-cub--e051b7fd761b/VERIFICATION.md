---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The squared-coordinate equations conserve both the simplex sum and log H. Strict concavity gives a unique interior maximizer and compact regular level circles, and only the maximizer is stationary. Each vertex section has two transverse crossings at small h, from the strict log concavity of the one-variable section product and the opposite signs of the normal velocity near its ends. At the u-passage, v decreases and w increases at logarithmic rates bounded away from zero, making the integrated correction in (log v)'=-2a+2av+2(a+c)w bounded uniformly up to every intermediate time. Thus log v=-2a tau+O(1), log u=O(1), and log w=-L/a+2b tau+O(1) by the conserved product. At exit, v is bounded above AND below by fixed multiples of h^(1/b), because both u and w are bounded away from zero there. Cyclically this yields the other two affine paths and the stated passage lengths in original time. Outside the three vertex boxes, at sufficiently small h one coordinate is below any fixed sufficiently small eta<delta/2 while the two others are at least delta-eta; the growing edge coordinate then has derivative bounded below by a positive constant, giving O(1) travel times in their stated order. Log derivatives are globally bounded; cumulative phase breakpoints differ by O(1) in physical time, and the continuous reference path is Lipschitz across its corners. This gives the O(1/L) normalized phase error including transitions and endpoints. Coupling with the same uniform phase gives the stated Euclidean W1 bound; the three duration fractions are c/S, a/S, b/S and arclength on each edge projects to the listed atom or uniform law. The limitation calls the edge-supported measure two-dimensional; its support is the one-dimensional boundary of the planar triangle, and it is mutually singular with every finite-h law. This wording does not affect the theorem. Inspected the frozen verification notes and checker without executing the supplied code. Independent finite replay: python /workspace/review_evidence/2_reproduce.py, which integrates two log coordinates and reconstructs the third from H. Observed periods 27.631022548790 and 12.664218017506 and sampled errors 0.122042053 and 0.140716465; this corroborates normalization, not the limiting theorem. All constants are for fixed positive coefficients and a fixed small section parameter.

## originality

FAIL

The same-system November 8 period-tail result does not literally state the phase or W1 formulas, but its published proof already provides the uniform integrated defect, entry data, dwell times and connecting-time bounds that mechanically imply the full claimed result. In its u-box, the displayed equation for (log v)' and the whole-passage integral bound, applied to any prefix of that passage, yield log v(t)=-2a tau+O(1) uniformly. The prior's exact log H identity and log u=O(1) give the other two coordinates immediately. Cycle the same argument, use the prior O(1)-length connecting arcs and bounded log derivatives, and divide its breakpoints by L. This gives the same section-phased reference path and rate, not just the scalar period. The probability law is the pushforward of uniform phase along that very path, and the common-phase coupling transfers the supremum error to W1. No distinct surviving assertion is established by separating the law from the profile.

## value

PASS

A physical-time, phase-resolved law and coordinate abundance distribution on one near-boundary orbit are meaningful descriptive invariants, distinct in use from a scalar period tail over sampled initial energies. That usefulness does not make the routine extraction from the existing passage proof an original contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
