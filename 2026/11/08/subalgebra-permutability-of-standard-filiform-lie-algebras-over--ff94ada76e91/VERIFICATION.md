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

Execute `python verify.py` with Python 3, using no third-party packages. The script constructs the original Lie bracket on the full vector space and directly enumerates every vector subspace in reduced row-echelon form for the cases in `verify_output.txt`; it determines subalgebra closure and pairwise vector-sum closure without using the theorem's subalgebra classification. All nine test cases match the independently evaluated closed formulas, and the script emits `FILIFORM_SUBALGEBRA_PERMUTABILITY_DIRECT_PASS` and `ALL_CASES_PASS` on success. The full run's standard output is recorded verbatim in `verify_output.txt`.

The proof in `RESULT.md` covers every prime-power field and every integer dimension at least four; the finite checker tests prime fields only and does not verify the general infinite-dimensional claims by enumeration. Historical-priority and independent mathematical audits have not been performed.
