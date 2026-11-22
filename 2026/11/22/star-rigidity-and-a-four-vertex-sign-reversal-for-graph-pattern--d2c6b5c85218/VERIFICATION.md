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

# Reproducibility

Run `python3 verify_spai.py` from the directory containing the embedded source. No additional Python packages are required. The exact checker independently constructs graph-pattern least-squares normal equations using `fractions.Fraction` and direct elimination, compares their solutions with the theorem's local formulas, and verifies the rational path example and robust weighted-tree embeddings. The checker reports 13,257 successful exact-rational assertion groups.

Mathematical scope: finite connected simple weighted trees, \(w_e>0\) and \(\mu>0\); the right Frobenius residual is minimized without an extra symmetry or sign constraint. The paper proof, not the finite checker, establishes the universal statements. Scientific priority remains conditional on the available published-literature comparison. No independent audit has been performed.
