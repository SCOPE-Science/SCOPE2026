---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Reconstructed the equivariant retraction and the nonabelian attaching words. The geometric diagonal is full in the center-coned triangulation; normalizing the complementary barycentric weights defines an equivariant strong deformation retract off the diagonal. A square coming from distinct incident edges loses exactly its common-end diagonal corner. Label the three retained corners q,r,s in consecutive order and its center c. The only center triangles are cqr and crs; collapse the free spokes cq and cs with their triangles, then remove c along cr. Center supports are disjoint and the C₃×S₂ action has trivial stabilizer on these ordered centers, so the same collapses descend. Equal-edge squares have their central vertex and two diagonal corners removed; disjoint-edge squares remain intact. Thus the quotient reduces to the stated deleted-product CW model. The cell representatives and count follow by indexing each two-cell by its increasing pair of right vertices, translating the first left vertex to a₀, and choosing one of two distinct other left vertices. The ordered square traversals are L_i⁺ R_{i,j} R_{j,i}⁻¹ (L_j⁻)⁻¹ and L_i⁻ R_{i,j} R_{j,i}⁻¹ (L_j⁺)⁻¹, not merely their signed edge multisets. The specified tree leaves A:y⁻¹x_j⁻¹ and B:x_i y⁻¹. Solve B for y and transfer the other attaching map by homotopy before cancellation; this is a presentation-complex move, not a free-face collapse of the original square pair. The resulting x_i x_j relations give x_j=x₁⁻¹ for j>1 and leave a circle with binomial(n−1,2) attaching maps of degree −2. At n≥3 one such cell makes RP²; the others now attach by nullhomotopic maps, giving the sphere wedge of the claimed rank. This also checks the n=3 boundary and integral consequences without inferring homotopy type from homology.

## originality

PASS

The n=3 cyclic quotient is known in the discretized model, and the coned-square triangulation and diagonal-complement method already appear in the full-symmetry disk work. Neither covers the all-n proper-subgroup quotient computation. The new content is the uniform proper-action orbit-cell and attaching-map reduction, especially the extra spheres for n≥4.

## value

PASS

This is a uniform integral homotopy classification for a natural nonfree symmetry of a standard configuration family. The quotient fundamental group remains of order two while the number of actual wedge-sphere summands grows quadratically. The integral attaching-map calculation detects more than rational symmetry invariants or the n=3 special case, and distinguishes this proper subgroup from the full-symmetry disk quotient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
