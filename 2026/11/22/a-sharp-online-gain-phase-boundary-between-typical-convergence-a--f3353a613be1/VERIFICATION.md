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

The proof is given in `RESULT.md`. The standard-library artifact `artifacts/verify_online_scaling.py` was executed as a self-contained exact-rational checker. It tests four two-curvature laws, reconstructs all four independent sample-pair affine maps, checks first/second-moment identities and stationary covariance equations, and checks the exact prospective multiplier and example \(b=10\), \(\eta=1/225\).

For the example, the exact computed prospective factor is \(18225/17024\), with stationary gain variance \(8181/1029952\), and the population-target factor is \(81/121\). Rational endpoint tests bracket the unique admissibility curvature threshold between \(7.739\) and \(7.740\). The code also checks 512 finite gradient/gain steps for strict interiority and nonzero state, but those finite checks are not a proof of a general infinite-time statement. The proof of the almost-sure assertion uses a stationary coupling, bounded Lipschitz truncated logarithms and Jensen's inequality, not simulation.

Independent mathematical audit has not been performed. The prospective squared multiplier must not be read as the growth factor of the actual squared-state expectation; that stronger question is not resolved here.
