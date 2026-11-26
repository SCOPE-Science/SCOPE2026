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

The three finite singular fibres with cubic parameter a cube root of unity split into the linear factors x+omega^j y+omega^(k-j) z, and the fourth is the coordinate triangle. Each of the nine base points lies on one line in each fibre. All 54 pairs of lines from distinct fibres meet at these base points; the twelve within-fibre side intersections remain ordinary nodes. Blowing up a base point produces four distinct line-to-exceptional crossings. This gives 21 rational vertices, with degrees four and five, 48 ordinary edges, and genus 28; connectivity and the valencies prove stability. For point-line incidence B and the block matrix H of four all-ones 3-by-3 blocks, the line block of the Laplacian is 6I-H. Schur complementation of the invertible block 4I over F_3 and F_7 gives 21I-3H-J, with ranks one and three respectively, hence full ranks ten and twelve. These and the matrix-tree order give ten elementary order-three and eight elementary order-seven factors. Working independently from the Hesse factor equations and point ratios I verified the characteristic polynomial, reduced determinant and Smith form with exact arithmetic. Raynaud's multidegree/intersection-matrix description for the stated regular split semistable smoothing gives this same group as the geometric component group, since multiplicities and node thicknesses are one. This is a conditional statement about the generic genus-28 Jacobian, not about the elliptic surface's elliptic-fibre Jacobian or existence of an embedded smoothing.

## originality

FAIL

The principal integral finding is covered by a distinct indexed result, 87b703a9169b. It states the identical 21-vertex 48-edge graph group explicitly as an underlying group not claimed as new, and supplies a direct determinant and exponent computation and the same exact Smith form. The two dates do not determine priority and the source's unspecified previous nonequivariant computation is not assigned to either work here. What is established is equivalent coverage, not who obtained it first. The conditional Néron interpretation is the standard graph theorem applied to exactly this group. The spectrum is not asserted to occur verbatim in the other record: it is an elementary consequence of its explicit point-line incidence and class-triangle description, and does not establish a distinct substantive remainder here.

## value

FAIL

The full graph critical group of the resolved boundary is a naturally motivated exact invariant, especially because retaining the ordinary nodes creates a seven-primary part that the Levi graph lacks. But that entire useful integral fact is already covered. The remaining exact spectrum is a short block calculation from the standard affine-plane incidence relations on the explicit indexed graph; it does not distinguish a new geometry or solve a separate motivated problem here. The conditional use of Raynaud's theorem and the alternate proof are useful exposition, not a distinct valuable finding on the submitted scope. No substantive repair is supported.

The dated certificate retains the supplied scientific assessment, sources and limitations.
