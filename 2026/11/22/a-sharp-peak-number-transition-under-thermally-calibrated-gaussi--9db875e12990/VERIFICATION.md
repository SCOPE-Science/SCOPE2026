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

The included self-contained `checker.py` uses only Python 3 standard-library modules. Running `python3 checker.py` checks six resetting-to-trap ratios \(a>1\), numerical existence and uniqueness of the threshold, strict decrease of the derivative-sign kernel, examples on both sides of the phase boundary, one-mode cases for \(a\le1\), the exact \(a=2\) critical equation, the beta moments, and convergence to the coefficient three in the near-critical mode opening. A clean execution passed 59 assertions; the numerical root for \(a=2\) was approximately \(1.256431207267\) using midpoint quadrature.

The exact integral identity, monotonicity, existence of the unique root, all-region mode classification and quartic transition are established analytically in RESULT.md. The finite quadrature mesh cannot establish them on its own. No experimental, independent expert, or independent scientific audit is claimed. The result requires equilibrium-width reset Gaussians and equal packet weights; these assumptions must not be silently dropped.
