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

# Verification scope and reproducibility

The proof in `RESULT.md` establishes an all-parameter homotopy equivalence using elementary collapses, contiguous simplicial retractions, a homotopy pushout, and attached one-cells. Its key infinite steps are not inferred from finite enumeration.

Run `python verify_matching_deleted_bipartite.py` with Python 3.9+ and no third-party modules. The script independently enumerates the induced-degree face set and the facet-decomposition face set for all \(127\) triples with \(1\leq a,b\leq6\) and \(0\leq t\leq\min(a,b)\). For every triple with \(t\geq1\), it checks the prescribed free-edge/triangle pairs, the exact face remainder, and contiguity of the retraction onto matched indices. For \(t\geq2\), it also checks contiguity of the tetrahedral-core retraction. It then computes the complete mod-two Betti vector by exact finite-field elimination and compares it with the predicted integral homotopy type.

Expected first output line: `FACE_COLLAPSE_RETRACTION_AND_MOD2_CHECKS_PASS cases=127 a,b=1..6 t=0..min(a,b)`. The complete recorded output is `verification_output.txt`. The code contains no publication-priority oracle. Integer torsion-freeness and the homotopy type rely on the algebraic-topological argument, not on these mod-two checks. No external validation has been performed.
