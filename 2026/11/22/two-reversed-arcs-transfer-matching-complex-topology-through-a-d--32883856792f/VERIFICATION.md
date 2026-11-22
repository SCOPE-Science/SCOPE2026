---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification of the two-reversal theorem

## Proof-level checks
The proof checks the only possible directed cycles by counting reversed arcs: no reverse arc implies acyclic; one reverse arc cannot return without a now-absent forward edge; two reverse arcs yield exactly one possible four-cycle, requiring both cross edges. The three-piece simplicial union is an identity at face level, not only a homotopy surrogate. The simplicial cofibration pushout yields a single suspension of a relative quotient, and the quotient of the matching complex by its cross-pair-avoiding subcomplex yields two more suspensions. For a graph with no residual edges, augmented \(\mathcal M(H)=\{\varnothing\}\) produces \(S^2\) and prevents the common empty-space shift error.

## Computational corroboration
`python3 multipath_two_reversal_check.py` was run with Python 3 and passed: all labeled bipartite graphs containing the prescribed two disjoint edges for part sizes 2×2, 2×3, 2×4, 3×2, 3×3 and 3×4; 45 seeded random larger bipartite graphs; and four complete-bipartite examples. Total 1,301 cases. This checker independently enumerates directed cycles, compares the full face sets and computes reduced mod-two homology with the augmented dimension −1 boundary. Finite tests do not prove the general result, integral equivalence, or the torsion of the seven-by-seven case.

## External integral input and scope
The integral torsion in degree five follows from the proved suspension and Jonsson's published \(H_2(\mathcal M(K_{5,5});\mathbb Z)\cong\mathbb Z/3\mathbb Z\) theorem (arXiv:1203.5644). No program or finite field calculation is offered as a replacement for that integral result. No independent audit has been performed.
