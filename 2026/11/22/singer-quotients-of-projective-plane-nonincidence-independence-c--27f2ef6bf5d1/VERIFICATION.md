---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility

Execute `python3 verify.py` with Python 3, using no external packages. The success marker is `SINGER_NONINCIDENCE_QUOTIENT_CHECKS_OK`.

The verification tests all differences in specified cyclic plane difference sets for orders two, three and four, all point-pair incidences in the resulting models, and the equivariant star-tree edges. It does not enumerate all possible difference sets. It also constructs the order-two quotient cellular chain after stellar subdivision at the two fixed-shore barycenters and checks the chain identities and the chain reduction by exact elementary integer pivots. The reduced complex certifies integral homology with one degree-zero and two degree-two generators and no other homology. The matrix operations do not certify geometric cell collapses, simple connectivity, or the wedge homotopy type.

The infinite proof in `RESULT.md` uses an explicit equivariant contraction on a union of stars, an equivariant suspension, relative linewise simplicial collapses, and an integral group-ring chain basis change. The finite matrix checks neither replace these arguments nor establish the integral Singer lattice for arbitrary orders.
