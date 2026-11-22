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

Deleting rung {0,n} leaves 2n-cycle, n-1 vertical rungs and two twisted seam edges. For even n any perfect matching uses either zero or two seams: an exactly-one-seam matching forces one crossing horizontal edge at each column cut, giving incompatible alternating row parity. The zero-seam and both-seam facet families A and B are cones on forced edge pairs. Their facetwise intersection equals T_(n-3), the straight 2-by-(n-3) ladder perfect-matching complex, by explicit outer-column extension/replacement. T_1 is one vertex and T_m for odd m has an inductive union of two cones with intersection T_(m-2), hence is contractible. Consequently A union B is contractible for every even n>=4 (CW homotopy pushout). Independent graph-edge perfect-matching enumeration for n=4,6,8,10 reproduced total counts 4,10,26,68; all matchings had exactly 0 or 2 seam edges and divided evenly between cones. Finite enumeration is diagnostic only. The proof does NOT assert arbitrary all-size simplicial collapsibility.

## originality

PASS

Agarwal–Basak arXiv:2608.30601v2 Section 5.1 and Theorem 21 fully classify INTACT Möbius ladder perfect-matching complexes, giving two spheres for even width. Their complete 19-page primary text was obtained and read through authorized Oxford access and does not classify a deleted rung. Chandrakar–Singh proves odd straight-ladder contractibility (used as a lemma), but not the defective Möbius seam-state decomposition. The related published rim-edge-deletion theorem deletes a perimeter edge and yields a sphere for even n, and a rung-fault independence-complex result treats a different simplicial complex; neither covers this claim.

## value

PASS

A minimal, natural graph defect destroys both homotopy generators of a highly symmetric perfect-matching complex uniformly in all even widths. The exact two-cone gluing and odd-ladder intersection reveal a structural topological phase change beyond recomputing intact-ladder Betti numbers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
