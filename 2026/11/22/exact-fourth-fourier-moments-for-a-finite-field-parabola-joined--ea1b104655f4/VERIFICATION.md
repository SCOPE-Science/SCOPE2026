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

Completing the square by the affine parabola-preserving shear sends a nonvertical line to height Delta/4, and parabolic translation sends a vertical line to x=0; affine bijections preserve equality of two-term sums. Reconstructed the horizontal convolution by subtracting the shared points: it is N-2C+D, where C is the sum of translates of the parabola by the intersection points and D is supported on v=2c. The key mixed character sum over (u,v) equals q chi(c), by the two-root character identity after comparing v=c and v=u^2/2. At secant height 1, the C curves meet once, and the D weights at u=0, +2, -2 are q-2, q-3, q-3; these points remain distinct even in characteristic three. For a vertical line the mixed parabola/line convolution is identically one, and both intersection corrections at the origin give the listed vertical tuple. Expanding the six terms recovers the four polynomials. Orthogonality with the stated unitary normalization gives q^-2 E. For extension with output counting measure, the fourth-power expansion is bounded by q^2 E/|S|^4 on the unit input ball and input 1 attains equality. Separate exact difference-multiplicity counts for 342 configurations reproduced all polynomial evaluations (all lines for q=3,5,7,9 and samples in eleven larger fields, including q=27 and 81).

## originality

PASS

The supported distinct result is the exact four-case ordered-energy evaluation for a full parabola and an arbitrary affine line. The generic Fourier and extension identities are prior; neither those identities nor a parabola-only bound supplies the mixed terms, especially the dependence on intersection correction and chi(-1).

## value

PASS

The full parabola plus one line is a natural mixed support, and its fourth moment gives an exact baseline across all affine placements. In particular, vertical and tangent lines contribute differently despite equal intersection size, and the tangent, secant and exterior expressions retain quadratic-character dependence. The explicit evaluations determine a sharp extension norm rather than merely reasserting its known reduction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
