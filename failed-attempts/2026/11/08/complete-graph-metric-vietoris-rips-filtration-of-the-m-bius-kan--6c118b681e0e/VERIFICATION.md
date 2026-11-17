---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-08.md",
      "INDEPENDENT_AUDIT_2026-11-08.json"
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

On GP(8,3), independently rebuilt 16 vertices/24 edges, all shortest distances, and 249 augmented faces at graph radius two (f-vector 16,72,112,48 plus empty). Reconstructed the two actual 119-pair discrete-Morse matchings with 688 oriented Hasse covers and independently verified each matching is acyclic, critical cells nine 2-cells and two 3-cells, no 1-cells. Two 8-vertex bipartition-induced S3 crosspolytope cycles are independent in top integral homology because there are no 4-simplices; with exactly two critical 3-cells this forces zero Morse attaching degrees and integral wedge ∨9 S2 ∨2 S3. Radius3 has exactly 8 antipodal forbidden pairs, giving S7; first stage cycle rank9 and radius4 simplex. All intervals follow distinct degrees; proof reconstructs integral homotopy, not just mod-p ranks.

## originality

FAIL

An already published 2026-11-01 full theorem on this very Möbius–Kantor/GP(8,3) shortest-path vertex Rips filtration proves every asserted homotopy stage and complete integral barcode, and adds an integral H3 basis from two bipartition crosspolytope boundaries. Another 2026-11-02 theorem adds automorphism characters. Present claim is fully covered.

## value

FAIL

The mixed-dimensional Morse calculation is structurally attractive but it is already known for precisely this graph and metric, including integral H3 generators. As submitted, this is an exact known-table recomputation with no motivated new residual theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
