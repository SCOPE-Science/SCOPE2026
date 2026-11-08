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

# Reproducibility and checks

The file `verify_moments.py` requires Python 3 and SymPy and carries out exact symbolic and finite-parametric checks. Execute `python verify_moments.py` from the extracted package directory. The Schur-character expansion and normalized coefficients are checked as rational identities in the two symbolic variables \(n,k\), independently of particular numerical dimensions. A rank-one Dirichlet specialization is also checked exactly. The program checks explicitly generated two-eigenvalue extremal witnesses through dimension 50, all rank phase signs through dimension 60, and exact Fibonacci/Lucas resonances. These finite loops do not certify the universal spectral lemma: the proof in RESULT.md supplies the essential all-dimensions argument.

A separate finite Haar-unitary experiment on six representative rank/dimension pairs produced fourth moments consistent with the analytic formula; such experiments are consistency checks, not proof. The status of independent audit is unperformed.
