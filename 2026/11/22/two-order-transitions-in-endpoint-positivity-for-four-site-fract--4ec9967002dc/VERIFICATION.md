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

# Verification evidence and limits

The proof derives the exact spectral-projector coefficients and uses the elementary extended-Chebyshev zero-count lemma for four exponentials. It verifies the boundary powers \(\alpha=1\) and \(\alpha=2\) using explicit matrix powers and shows a strict negative intermediate-time witness for every \(\alpha\ge2\). The near-critical asymptotic constants are coefficients of analytic two-parameter expansions and are not inferred from extrapolating samples.

To rerun the supplementary check, use Python 3 with SymPy and mpmath installed and execute `python check.py` alongside the other included files. The checker validates exact spectral-projector identities and selected 60-digit numerical examples. Such examples do not prove the claims for all real parameters; the written analytic proof supplies that coverage. No independent validation is represented.
