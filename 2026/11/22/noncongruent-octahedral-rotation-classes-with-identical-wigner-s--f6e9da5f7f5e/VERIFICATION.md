---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The two lists are full six-element conjugacy classes: proper signed coordinate permutations act transitively on the directed coordinate axes and on the unoriented edge axes. For both lists the absolute quaternion inner product is 0 inside each distinct matched pair and 1/2 across blocks, with 1 on the diagonal. This fixes the labeled relative-angle matrix. The signed lift spans differ (four via sums and differences for the quarter-turns, three for the edge half-turns), independent of lift sign. Every isometry of this round real projective space lifts to an orthogonal isometry of its spherical universal cover, so the ranks obstruct ambient congruence. Schur orthogonality for Haar probability yields the sample Gram chi_l/d after dividing evaluation by d. Its three eigenspaces are pair differences, block-constant configurations with zero total, and constants, giving the stated multiplicities and eigenvalues. At degrees 1, 2, 3 the unscaled extrema are (2,4), (2,8), (4,10) for d=3,5,7; at all degrees l>=4 each unscaled row has absolute off-diagonal sum at most 5, so the normalized extrema lie in [1-5/d,1+5/d], strictly inside [2/5,8/5]. This establishes full row rank, interpolation, uniqueness of the extreme degree, and the sharp condition number. With W positive diagonal, the weighted Gram shares the spectrum of G^(1/2) W G^(1/2); transitive group averaging replaces W by a scalar identity of the same trace. Rayleigh quotient convexity/concavity bounds the two extremes in the required directions. My integer reproduction independently generated the proper signed permutations, computed the two conjugacy classes and relative trace patterns, and checked six spectral power sums for each degree 1–6; Newton identities fix the corresponding finite eigenvalue multisets. The all-degree and all-weight decisions are analytic.

## originality

PASS

The supported distinction is the paired natural octahedral classes with identical central two-point data but different ambient projective ranks, together with their sharp common all-degree sampling behavior. The basic character and symmetry-averaging tools and the cuboctahedral line configuration on its own are not original contributions.

## value

PASS

These are canonical equal-size cube rotation classes, not arbitrary tuned point sets. They show exactly what even complete central pair measurements cannot distinguish in SO(3), while yielding a useful positive single-degree interpolation result with sharp bounds over every degree and a principled equal-weight optimum. The lift-rank obstruction makes the distinction geometric rather than a numerical coincidence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
