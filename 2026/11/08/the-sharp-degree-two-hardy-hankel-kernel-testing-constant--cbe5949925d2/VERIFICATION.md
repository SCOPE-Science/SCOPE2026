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

Run `python3 check_quadratic_hankel.py` using Python 3 standard library only. The checker performs exact formal polynomial arithmetic over \(\mathbb Q\) for the global lower certificate and over \(\mathbb Q(\sqrt6)\) for the sharpness identity, checks the exact radius square, then makes finite numerical spot checks of the normalization and kernel inequalities. In the packaged execution it printed `QUADRATIC_HANKEL_EXACT_CHECK_OK 2006 checks`.

The algebraically exact polynomial identities can be compared directly to §Proof in RESULT.md. They establish all-parameter inequalities **when combined with** the displayed analytic matrix and kernel reductions and the exact positivity arguments. The optional numerical samples alone do not prove an infinite quantified claim. The result has not received independent mathematical audit or external priority verification.
