---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

# Independent mathematical audit

## correctness

FAIL

The main inference is false. BMZ Theorem 3.1 is stated for elementary abelian groups, not only cyclic prime-order groups, and does not require the action on the sphere to be free. In its Step (1), ‘fixed-point free’ concerns the whole-group fixed set. Each involution indeed has two cycles, so its fixed sphere is S⁰, but the full V4 fixed space is the diagonal intersected with its orthogonal complement, hence zero. More directly, the Borel sphere bundle over BV4 has mod-2 transgression d₃ of the sphere generator equal to its Euler class xy(x+y), nonzero: the representation is the sum of the three nontrivial real characters. The record's own w₃ falsifies the asserted breakdown. Its restrictions to the order-two subgroups do vanish, and for the rank-two subgroup fixed bundle the proposed e² is zero by dimension, but neither fact obstructs the whole-group step. For the source of a proposed map, 3-acyclicity gives the claimed degree cutoff via the edge map, not membership of x³y³; index functoriality is indeed in the stated direction. Independently of the equivariant argument, the affine target cell as stated follows from simultaneous medians: for unit normal n each block's median projected coordinate mℓ(n) is continuous and odd, so the two differences with block 0 vanish together by Borsuk–Ulam on S². In each ordered seven-point block take the median as a singleton and match the three lower to the three upper points by different colors. Hall holds because a monochromatic subset of color c has at least 3 minus the number of upper points of color c neighbors, at least its size by the class cap, while a multicolor subset sees all upper points. Ties can be ordered arbitrarily. The common median plane meets all singleton and paired convex hulls. Thus the frozen open-cell remark is not correct for the stated affine parameters either.

## originality

FAIL

There is no distinct transgression obstruction: the existing BMZ theorem and the usual Euler calculation give the opposite result for this step. The remaining fixed-set and index calculations are direct consequences of the standard representation and index facts. The neighboring prime-power statements below were not treated as equivalent when their hypotheses differ.

## value

FAIL

The alleged barrier would have mattered for a prime-power extension but does not exist. The surviving observations are immediate cycle counts, chessboard join arithmetic, and index functoriality without an independent obstacle or needed certificate for this cell; the affine target has a simple common-median proof. There is no substantive surviving repaired finding in these data.

The dated certificate retains the supplied scientific assessment, sources and limitations.
