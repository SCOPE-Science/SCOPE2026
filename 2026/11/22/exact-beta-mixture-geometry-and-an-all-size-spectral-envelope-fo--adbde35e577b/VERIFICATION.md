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

# Reproducibility and scope of verification

The accompanying `verify.py` is a Python 3 standard-library program. Run it with `python3 verify.py`. It computes exact rational hitting probabilities from the Markov first-step recurrence and independently from the published finite binomial-difference expression. It also checks all feasible signs of finite differences through order eight for \(2\le k\le13\) and \(n\le46\), plus exact strict second- and third-order Hankel determinant inequalities. The executed run returned `PASS: 4416 exact rational assertions; k=2..13; n<=46; r<=8`.

The infinite beta-mixture, complete monotonicity for every order, and all-index bound are established analytically in `RESULT.md`, using the published reciprocal-harmonic moment density and the finite-difference formula. The checker does not constitute an exhaustive proof over all indices, and the full infinite digamma-root series is not approximated by a finite list to assert its value. The digamma first-root decimal is supplementary to the root's unique interval definition.

Independent mathematical audit: not performed.
