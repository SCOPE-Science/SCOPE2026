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

# Reproducibility and limits

The analytical argument and its normalizations are given in `RESULT.md`. Run the local checker using `python verify_gaussian_norm.py` with Python 3.10+, SymPy 1.14+ and mpmath 1.3+. It checks symbolic Taylor and saddle identities and numerically integrates the exact defining Gaussian norm in 15 cases, at \(n=80,160,320\) for \(c=0.4,1,1.3,2,4\). The expected message begins `SUPEROSCILLATION_NORM_VERIFY_PASS 5 symbolic-identities=6`. The representative ratio at \(n=320\) is 0.999479837 for \(c=0.4\), 1.01283151 at \(c=1\), 1.01772685 for \(c=1.3\), 1.00170694 for \(c=2\), and 1.00002883 for \(c=4\).

These finite checks are not a proof of asymptotic behavior, uniqueness, or originality. The entire \(n\)-parameter theorem follows analytically from dominated convergence and the two-saddle Laplace argument. No full parameter-uniform error bound has been established near \(c=1\). The cited source with arXiv ID 2306.03963 was accessible at the abstract level only; that limitation remains relevant to historical priority. Independent mathematical audit has not been performed.
