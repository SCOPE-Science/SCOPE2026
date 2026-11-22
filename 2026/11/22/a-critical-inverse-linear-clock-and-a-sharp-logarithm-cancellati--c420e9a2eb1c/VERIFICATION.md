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

Run `python checker.py` using Python 3 with the SymPy package available. The checker explicitly verifies the polynomial-rational identity for the decreasing weighted sum, the positive left center eigenvector, the second-order center/slaving coefficients, the cubic drift coefficient and the reciprocal logarithmic coefficient. It also performs finite diagnostics at four positive gain values, including the cancellation gain.

Actual execution returned `Exact symbolic identities: PASS` and `Finite diagnostics: PASS`. The diagnostic tests used 200,000 iterations for each parameter and agreed with the predicted reciprocal rates. These finite computations are not exhaustive and do not prove global convergence or asymptotics. The full mathematical proof is in `RESULT.md`; its core is a strict Lyapunov identity, primitive stochastic spectral gap, second-order stable slaving with controlled remainder, and a summable reciprocal-increment expansion.

The statement is restricted to every fixed \(b>0\) with strictly positive history on the critical surface \(a=b+1\). Uniformity as \(b\downarrow0\), signed initial conditions and off-critical parameters were not established. An independent audit was not performed.
