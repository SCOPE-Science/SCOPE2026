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

Nonzero H2 forces a composable pair; with three acyclic objects this gives a chain. The nerve has 3 vertices, m=a+b+c edges and ab triangles, so m=ab+1+2g. The link graph Γ at the sink has b+c vertices, ab edges and an edge-label map to the remaining graph Y with a parallel arrows. To verify the disconnected-domain step, collapse spanning trees in Y and in each component of Γ, first homotoping the link map to be constant on the latter trees at the common basepoint of the quotient of Y. Homotopy invariance of the mapping cone now gives q spokes from that basepoint to the common apex, one per Γ component, and 2-cells attached along the corresponding loops in Y; the paths up and down the same spoke cancel up to attaching-map homotopy. Collapsing one spoke leaves a wedge of q−1 free circles. Their H¹ classes lie in the radical of the degree-one cup form, incompatible with integral Poincaré duality, so q=1. Then β1(Γ)=ab−(b+c)+1=a−2g and the cone sequence injects H2 into H1(Γ); hence a≥2g+1, and reversing arrows gives b≥2g+1. For r=2g+1, the table has r(r−1) long arrows. The unique-use long edges collapse with their triangles, leaving A_j=(f_j,g_j,h_j) and B_j=(f_{j+1},g_j,h_{j−1}). Each edge appears once of each sign; in the three links alternating the two matchings advances indices by ±1 or ±2, so all links are single circles since r is odd. The core is a closed connected orientable surface with χ=3−r=2−2g, realizing both adjacent bounds. Two objects cannot support H2, but the arrow minimum is conditional on three objects.

## originality

PASS

Best of current knowledge, the supported distinct contribution is the sharp uniform lower bound on both adjacent Hom sizes, and hence the minimum total arrow count. The existence of a three-object model, the topology of the reduced cyclic complex and the upper construction are not claimed as independent novelty in this assessment. The closest indexed surface result has strong upper-construction overlap but its available statement does not constrain all three-object competitors.

## value

PASS

The distinction from a bare existence theorem is substantive: at the fewest possible objects, the exact surface genus forces a quadratic total arrow budget and independent lower bounds on both adjacent Hom sets. The use of the surface cup-product pairing to rule out compression provides a meaningful obstruction, with a matching geometric realization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
