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

Run \(\texttt{python3 verify.py}\) from the extracted package directory with Python 3 standard library. The program constructs finite one-card transition kernels directly from packet lengths, checks stochasticity, the entrywise lower bound and the published cosine eigenpairs, and compares large-finite spectral \(\chi^2\) values to the stated leading profile. The verifier is computational corroboration, not an infinite-dimensional or asymptotic proof. The analytical convergence relies on the exact cosine basis and the uniform low/bulk-mode estimate in RESULT.md. Mathematical and literature review are internal to this report; no independent audit has been performed.
