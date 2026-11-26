---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Orthogonal distinct character rows give Parseval normalization. One coordinate-pair Walsh sum is 2(−1)^{αβ}, so the nonzero-frequency D-sum is −r(−1)^q/2 and the restricted Gram is ((r−1)I+S_E)/(2r). The triangle product on a rooted pair of differences is −(−1)^B. All four triangle products multiply to +1, and switching to normalize the edges at one root shows that triangle signs determine the class. Relabeling gives all-positive, exactly one negative edge, or all-negative representatives, according to 0, 2, or 4 negative triangles. In the one-negative-edge case the two pair differences give eigenvalues +1 and −1, and the pair-constant block [−1,2;2,1] gives ±√5. The two uniform-sign matrices give the other spectra. For the all-positive and all-negative types the nondegenerate symplectic equations give respectively n(n−1)(n/2)(n/4)/24 and n(n−1)(n/2−2)(n/4−3)/24 unordered masks; the remainder is the middle class. These classes are intrinsic to the triangle signs, so the root criteria are invariant. The retained lower frame bound is 1−λ_max(P_E); all-positive has strictly largest λ_max and all classes occur for n≥16. The only Gram singularity is at r=4 in the all-negative class, which does not impair the retained frame. The asserted m=2 and m=3 counts agree with exact substitution and the frozen outputs.

## originality

FAIL

The claimed distinguishing census is mechanically determined by known real equiangular Parseval frame parameters and regular two-graph structure, with already available universal four-vertex switching spectra and erasure bounds. This is implication evidence, not a claim to have found these exact all-m formulas in print. At m=2 the 60 regular simplices are explicitly documented in primary work.

## value

FAIL

Four-erasure stability of a natural frame is well motivated, but all identifying four-mask statistics here reduce to universal signed K4 matrices and two elementary incidence moments from already fixed frame parameters. No new family-specific invariant survives that reduction; the sharp worst bound is a specialization of a known general erasure result. A useful worked example is not a distinct scientific census at this threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
