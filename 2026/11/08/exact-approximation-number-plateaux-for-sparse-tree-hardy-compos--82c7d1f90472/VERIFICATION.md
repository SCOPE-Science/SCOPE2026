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

# Verification and limits

For the compact sparse tree-Hardy symbol specified in `RESULT.md`, the root term is rank one; each distinct input level yields exactly \(c_{m_j}\) independent coordinate copies with common contraction factor \(\delta_j\). Keeping the rank-one root and the largest \(k-1\) copied coordinate directions establishes \(a_{k+1}\le w_k\); taking the root and the largest \(k\) input coordinates establishes \(a_{k+1}\ge w_k\) by the rank-k kernel argument. The compactness criterion is \(\delta_j\to0\), equivalently \(n_j-m_j\to\infty\), because \(q>1\).

The exact checker `check_tree_approximations.py` uses only Python standard libraries and runs as `python3 check_tree_approximations.py`. Expected successful output: `TREE_SPARSE_COPY_EXACT_FINITE_OK 2166`. It tests 2,166 finite exact-rational identities/inequalities in several parameter configurations and a nonmonotone ordering example. No finite test establishes the infinite theorem; the explicit proof in `RESULT.md` provides the necessary quantifiers and endpoint reasoning.

No Hilbert singular-value formula, spectrum, entropy-number theorem, or result for general tree symbols is asserted. No independent audit has been performed.
