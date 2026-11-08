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

# Reproduction

Run `python3 verify.py` with Python 3 and no third-party packages. The exact-rational checker prints `EXACT_VERIFY_OK` and regime counts for 1,462 parameter instances if all checks succeed. Its complete test range is \(1\le a\le12\), \(2\le b\le120\), together with selected much larger \(a,b\) pairs, including squared thresholds and high-imbalance tails.

It checks transition probabilities, row sums, symmetry, no forbidden transitions, zero internal eigenvalues, the quotient characteristic coefficients, exact candidate spectral norms (squared in radical regimes), and the sign of each threshold. The verifier does not exhaust infinitely many graphs or conduct numerical approximations as proof.

# Mathematical verification

The proof reduces the unrestricted convex optimization to two block-constant spectral dimensions. The critical identities are \(\lambda_-+\lambda_+=(a+1)x+(a+b)w\), \(\lambda_-\lambda_+=Na xw\), and the sharp test-vector bound \(\lambda_-\le aN(x+bw)/D\). For \(b\le a^2\), the missing-column norm lower bound is attained; for \(b>a^2\), minimizing the norm at each fixed \(w\) locates the capacity boundary and the concavity argument distinguishes the remaining regimes. All boundaries and nonnegativity constraints are stated and proved in `RESULT.md`.

# Limits

Finite checks cannot replace the analytic infinite-parameter proof. The constructed optimum need not be unique. No independent audit was performed.
