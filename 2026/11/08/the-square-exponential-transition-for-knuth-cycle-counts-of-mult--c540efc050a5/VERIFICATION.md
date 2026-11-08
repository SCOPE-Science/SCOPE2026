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

# Reproducibility and proof boundaries

Run `python3 verify.py` from a directory containing the embedded `verify.py`; the program is self-contained and requires only Python's standard library. The observed replay output is `PASS 347 exact and diagnostic assertions`.

Exact rational checks cover all pairs of initial successes and failures on an enumerated finite grid, their binomial-word representation, exact mean and variance, and convolution identities for several small multiset profiles. Numerical diagnostics check geometric Laplace-product moments and the three endpoint-weight scalings. An additional exact-large-integer test of \(n_j=2^{j^2}\) compares the normalized mean and variance to \(4/3\) and \(16/15\). These are finite validations of input formulas and asymptotic predictions, **not** substitutes for the displayed infinite-limit proof.

The proof's essential infinite steps are: exact increment independence (Stark), a tail-controlled exponential increment limit, a discrete endpoint Laplace estimate, Lyapunov's condition below the critical exponent, and uniform \(L^r\) control of the geometric tail at the critical exponent. Historical originality is provisional. No external independent audit has been performed.
