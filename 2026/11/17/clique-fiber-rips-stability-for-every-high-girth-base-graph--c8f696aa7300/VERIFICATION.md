---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

PASS — Reconstructed full carrier cover using d_P((v,a),(w,b))=d_H(v,w)+[a≠b]. When a base projection has pair distance two its intermediate vertex is unique; an alternative center would force a short cycle length ≤6, so other projected vertices must lie in its closed star. Distinct off-fiber neighbor vertices have one common center and one color, making all faces with ≥2 such neighbors private to one star. Descending-dimension matching toggling (v,a) is therefore a sequence of genuine free-face pairs, not a homology-only matching. The residual edge-carrier union has every nonzero color dominated by color zero, permitting explicit final simplicial collapses. Difference in exact face counts gives m·2^(m−1)Σ_v(2^deg(v)−deg(v)−1)+|E|(2^(2m−1)−2^m)+|V|(2^(m−1)−1). Contracting all scale-one fiber simplices gives rank mE−V+1, and the fixed-color inclusion splits the map to scale-two rank E−V+1, hence a primitive free kernel rank (m−1)E. C6 is excluded and published cyclic example is nontrivial in degree 2. Verified proof normalization and equality at inclusive radius two, at trees and branching bases. The inspected verifier enumerates true shortest-path Rips faces and checks individual immediate cofaces in 22 small cases; this finite evidence is corroboration, not the infinite proof.

## originality

PASS

PASS — The width-two prism theorem has general high-girth bases but not fibers of width ≥3; the wide-clique high-girth Čech theorem uses the closed-neighborhood nerve and has extra 2-spheres, incompatible with the present Rips claim. The width-m clique-fiber cycle theorem covers C_n only and the sharp C6 obstruction but not branching bases. Adams et al. consider torus-grid Rips complexes, not arbitrary high-girth bases with complete fibers. These are statement/implication comparisons, not title comparisons. Best-of-knowledge originality of the m≥3 arbitrary-base collapse and primitive persistence splitting survives, subject to unindexed equivalent graph-product results.

## value

PASS

PASS — An explicit uniform collapse for all finite high-girth base graphs and arbitrary clique width resolves a natural stability question for graph-metric Rips filtrations. The exact elementary-collapse complexity, integral scale-one persistence and sharp six-cycle obstruction are independently useful; the contrast with the same product family’s Čech spheres isolates a meaningful structural distinction rather than a numerical gain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
