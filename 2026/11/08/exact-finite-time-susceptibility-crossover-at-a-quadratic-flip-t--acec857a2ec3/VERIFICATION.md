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

# Verification

The proof uses the exact identity for the second iterate and both the unperturbed and parameter-differentiated reciprocal-square recurrences. Their cumulative errors are \(O(\sqrt N)\) on \(N\)-long windows uniformly for bounded \(z\), and the excluded initial-layer response contributes at most \(O(\delta^2)\) after normalization. These analytic estimates, not the accompanying finite computations, establish the universal limits.

Run `python verify.py` with SymPy and mpmath. It checks the polynomial identities exactly, the critical integral and slope numerically at high precision, and finite-\(N\) susceptibility against the predicted crossover for a range of positive and negative scaled parameters. No proof of arbitrary-\(N\) behavior follows from finitely many tests, and no external independent scientific audit has occurred.
