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

# Reproducibility and verification

Install dependencies with `python -m pip install -r requirements.txt` and execute `python verify.py` in a directory containing these files. The script runs symbolic determinant/descent identities, an independent rational enumeration of uniformly sampled subsets, and finite numerical eigenvalue checks across a range of dimensions and batch-size mixtures. The actual invocation passed 2241 assertions; complete output is in `verify_output.txt`.

The proof in `RESULT.md` does not rely on exhaustive search in an unbounded parameter family. It constructs the exact covariance transfer, proves the determinant factorization and a general Lyapunov no-reentry lemma, and minimizes the pair-incidence moment by an integer convexity inequality. These supply the infinite-domain results. Finite enumeration and floating-point checks cannot independently certify the general theorem or its historical originality.

The cited primary text and previously published mathematical statements were examined for relevant implication comparisons. One close four-coordinate publication was accessible only as a title and summary, and priority therefore remains provisional. There is no independent audit.
