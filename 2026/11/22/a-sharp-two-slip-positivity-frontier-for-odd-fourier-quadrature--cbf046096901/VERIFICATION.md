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

# Verification record

Run `python verify.py` using Python 3 and `mpmath`. The included recorded output reports 411 passed high-precision tests. The verifier independently inverts the Fourier moment matrix for odd sizes \(3\le n\le31\) at eight interior displacements each, checks coefficient and noise identities at 65 decimal digits, recomputes threshold roots and confirms the sign of every weight. Three additional large-grid thresholds are checked against the derived \(n^{-2}\) law.

The universal claims are analytic: the Dirichlet replacement formula is an exact identity; the convexity reduction proves which weights fail first; and monotonicity of simple sine ratios proves the unique crossing for every qualifying odd size and every real displacement in the domain. Finite tests cannot establish these universal statements independently. Independent audit and external formal verification have not been performed.
