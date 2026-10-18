---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Dolgachev-Laface-Persson-Urzua identify the 9 base points with AG(2,3) and each conic with the complement of one of 12 affine lines. Thus conic incidence automorphisms are affine-plane collineations AGL(2,3) of size 9*48=432. Parallel affine lines yield complementary block intersection3 (12 pairs), skew directions yield intersection4 (54 pairs), so the 4 classes of 3 conics are intrinsic. Action on four directions factors through GL(2,3)/{+/-I}=PGL(2,3)=S4 with kernel F3^2 rt {+/-I} order18. Corollary 4.2 of the source identifies projective Halphen automorphisms G18 and every projective arrangement stabilizer lifts via 9 unique 8-fold points; the construction gives the reverse containment. Finite incidence/GL calculations independently replayed; group equality uses prior geometry, not enumeration alone. Only nondegenerate complex family is claimed.

## originality

FAIL

FAIL. Strong prior coverage by Kohel-Roulleau-Sarti, A special configuration of 12 conics and generalized Kummer surfaces, Proposition 37 pp21-22, explicitly builds AGL_2(F3)=G432, states its surjection to S4 with kernel G18, and explains precisely which G18 symmetries are geometrically realizable; Dolgachev et al Corollary4.2 already gives the projective G18 group and same affine-plane conic incidence coding. The particular present S4 action is on four incidence-recoverable fiber triples rather than K3 lattice discriminant, but that difference follows routinely by taking the four directions of AG(2,3) already used for the same 12 conics. Re-labeling an explicitly previously known exact 432/18/S4 sequence is not a new classification. The prior K3 action is a different ambient object, noted accurately, but supplies a dominating equivalent group statement together with exactly the geometry needed for this corollary.

## value

FAIL

FAIL for distinct contribution. The specific 24-fold gap, group orders and exact quotient were already established for the same conic configuration in primary geometric/lattice analyses; reading the four parallel classes from pair-intersection sizes 3 versus4 is a one-line elementary affine-plane deduction. It offers a neat explanation, but no motivated new invariant or mathematical gap beyond the existing structural sequence to justify a separately valuable theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
