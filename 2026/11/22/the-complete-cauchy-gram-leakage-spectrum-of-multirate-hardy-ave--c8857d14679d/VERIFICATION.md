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

# Verification notes

The claim is proved algebraically and analytically in `RESULT.md`. The critical computations are the shifted-Jacobi Rodrigues beta-integrals, the cancellation of Gamma prefactors in the low/high factors, and both Cauchy–Gram power-sum limits. Those are explicit steps in the proof rather than inferred from numerical sampling.

For a supplementary reproducibility check, execute `python checker.py` with Python 3. It directly evaluates two finite-section Gram matrices via log-Gamma arithmetic. Tested cutoffs \(n=5,20,80,300,1000\) all returned two positive singular values approaching the exact limits \(1/5\) and \(1/30\); in particular at \(n=300\) the values were approximately \(0.1999999990\) and \(0.0333333328\). Large-tail truncation and floating-point rounding limit this check; they do not affect the analytical proof. All assumptions and conclusions use a non-probability-normalized weight \(x^\beta\,dx\), and no boundary rate or infinitely many channels are asserted. Independent mathematical review is not performed.
