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

Squaring (a,b) gives (a²+2b²,2ab); direct evaluation gives the twelve nonzero vectors on the three stated directions. Choose a linear basis taking those directions to horizontal, vertical and the positive diagonal. Any noncollinear triangle uses all three directions. For a horizontal edge from (0,0) to (a,0) with a≠0, the two common neighbors off the row are (0,−a) and (a,a), which are not adjacent; neither is adjacent to another point of that row. Thus every clique of size at least four is collinear, and the 50 horizontal edges account once each for two mixed triangles. The 15 five-point lines then give face vector (25,150,250,75,15). Distinct lines meet in at most one point; on each line simplex first remove the tetrahedron opposite a chosen vertex together with the simplex, then collapse the four remaining tetrahedra along their opposite triangles. This is a genuine reduction to a connected 2-complex of Euler characteristic 65. Independently of the supplied Tietze search, every clique-complex edge path is homotopic rel endpoints to horizontal and vertical unit steps: a diagonal displacement can be replaced by its horizontal-vertical detour using a triangle, and each line simplex permits replacing jumps by unit paths. The unit grid with each square split along the positive diagonal on R²/(5Z)² maps into the complex, and therefore surjects on fundamental groups. Its two generator loops lie in full row/column simplices, so both die. Hurewicz and homological Whitehead now give a wedge of 64 two-spheres. A nonidentity translation has vertex orbits of length five; its only setwise fixed simplices are the five parallel five-point line simplices when its direction is square. Each has positive orientation sign. Subtracting the H0 trace from the alternating chain trace gives 4 or −1; the identity gives 64. For a nontrivial additive character the sum s over the three square lines is 2 if its kernel is one of them, otherwise −3. Fourier inversion gives (13+s)/5 and trivial multiplicity 4, yielding the reported 4,3,2 classes of multiplicities.

## originality

FAIL

Both substantive claims in the Finding are exactly covered by a distinct same-day indexed finding on the same ordinary Paley-25 clique complex and its natural additive action, which also gives further quotient information. The ordinary ranks were already implied by the Latin-square theorem. The alternate Tietze computation is a different certificate of the same conclusion, not an independently stronger result claimed here. This is a failure of demonstrated distinctness, not an inference about which same-day record came first, external publication priority, or provenance.

## value

FAIL

The integral homotopy type and additive representation are meaningful refinements of ordinary homology for a natural graph. But this exact-instance release has no separate valuable mathematical claim once the matching wedge and full additive representation are credited. The computational certificate is an alternate verification of the same covered assertions, not a new classification, extension, or motivated unresolved invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
