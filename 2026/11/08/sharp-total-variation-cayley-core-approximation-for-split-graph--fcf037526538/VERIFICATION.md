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

# Reproducible checks

Run `python verify.py` in an environment with Python 3 and SymPy. The standalone script enumerates every tree of each labeled split graph with \(2\le a\le4\), \(1\le b\le3\), using an independent union-find tree test, and compares the entire exact histogram of \((K,\deg_B-1)\) with the multinomial formula. It separately computes the multivariate spanning-tree Laplacian determinant for all nine parameter pairs, verifies exact zero-defect counts, and enumerates Cayley trees from Prüfer sequences for \(2\le a\le7\) to verify all two-point distance counts.

Observed replay: `VERIFY_OK exact tree enumeration, multivariate determinants, and pair-distance laws`. The enumerated split-graph spanning-tree counts range from 3 to 5488 over these parameter pairs, with zero-defect counts matching the closed formula including impossible boundary cases.

The proof of all-parameter identities is in the algebraic determinant, contraction bijection, logarithmic estimate, factorial moments and rooted-forest calculation. Neither finite enumeration nor numerical convergence tests establish the infinite limits on their own.
