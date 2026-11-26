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

Character orthogonality gives the real kernel q⁻ᵈ(N−q dist_H(x,y)) independently of the finite abelian group structure. Within-axis differences have eigenvalue q before scaling; axis-constant functions with zero center and zero sum across axes have eigenvalue q². In the remaining orthonormal center/all-leaf basis the unscaled off-diagonal is √L(N−q) with L=d(q−1); the diagonal entries are N and T−N. Direct expansion gives trace T and determinant q². Since T>q²+1, the positive radial roots straddle the two contrast eigenvalues, with μ_+>q² and μ_−<1. To rule out a unit concentration eigenvalue, write the Fourier transform of a ball-supported function as a constant plus a sum of one-coordinate functions. Fixing nontrivial characters in two other coordinates forces each one-coordinate function constant if the transform vanishes outside F; its mean is zero, so all vanish, then the initial constant vanishes too. The radial eigenvector equation gives the center/leaf ratio (the off-diagonal is positive, so μ_+>N and neither coordinate vanishes). The next eigenspace yields the sharp projection-defect coefficient. The condition number follows from μ_+μ_−=q², and expansion of T gives both separate asymptotic regimes.

## originality

FAIL

The 2026-10-11 q-ary Hamming-shell record does not print the ball spectrum, but its exact first-band shell blocks at k=1, with the same explicitly supplied radial basis, give it by adding the center evaluation. The two contrast blocks are unchanged because their functions vanish at the center. In the radial block the two evaluations are (1,b0) and (1,b1), where b0=−√L and b1=b0+q/√L. The center and shell have weights 1 and L before scaling, so the unscaled frequency-side radial block is the sum of their two weighted outer products. Its trace is T, and its determinant is L(b1−b0)²=q². On the spatial side the evaluation rows (1,b0) and √L(1,b1) have Gram off-diagonal √L(N−q) and center diagonal N, giving exactly the stated ratio, sharp gap and condition number. The first band consists of constants and all mean-zero functions of one coordinate, so relabeling the alphabet fixing the center identifies cyclic and arbitrary abelian cases as concentration operators, not just as a conjectural analogy. This is positive prior-implication evidence. The later full-ball catalog hit independently matches the cyclic specialization; it is not used to infer earlier priority.

## value

FAIL

The conditioning of a spatial/spectral ball minor is a natural use case and the exact endpoint information is useful. Here, however, the radius-one restriction is exactly the already diagonalized first-band shell operator with a single evaluation in its known two-dimensional radial sector. The spectral and stability answers are mechanically implied by that block data; relabeling the alphabet is an operator equivalence and adds no independent exact invariant. No distinct valuable remainder warrants a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
