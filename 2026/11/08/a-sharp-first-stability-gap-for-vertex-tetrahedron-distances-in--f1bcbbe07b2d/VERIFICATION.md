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

# Verification instructions and reproducible limits

Execute `python verify.py` with a standard Python 3.10+ interpreter. No third-party software, downloaded datasets, floating-point arithmetic, or external proof assistant is used. The code reconstructs all 1,365 fixed-origin candidate tetrahedra from the 15 nonzero Boolean four-vectors. Exact Gaussian elimination finds 940 full-rank four-simplices. Each Euclidean distance is the minimum over exact feasible orthogonal projections onto the 15 nonempty faces. The checker asserts the unique first level \(1/4\), 28 second-level cases at \(1/3\), no intervening value, and the three second-level orbit representatives and sizes 12, 12, 4 under the fixed-marked-vertex coordinate permutation action. Multiplying by 16 reconstructs the global 448 cases and orbit sizes 192, 192, 64. A fresh execution completed successfully.

For the finite domain, exhaustive enumeration with exact rational arithmetic is a complete proof if the face projection lemma and symmetry reduction given in RESULT.md are accepted. It does not establish a statement for more than four coordinates or for lattice entries outside \(\{0,1\}\). Historical-priority comparison is provisional. Independent mathematical validation has not been performed.
