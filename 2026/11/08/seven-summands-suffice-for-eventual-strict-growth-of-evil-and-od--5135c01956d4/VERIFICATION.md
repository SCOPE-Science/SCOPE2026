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

# Verification scope and actual checks

The proof uses the uniform Gelfond Thue--Morse exponential-sum estimate at exponent \(\alpha=\log_4 3\), uniform Abel-summation bounds on \(T(\rho e^{i\theta})\), exact Parseval \(\int|T|^2=(1-\rho^2)^{-1}\), and weighted circle estimates. The coefficients of first differences are the exact binomial-signed expansions of \((1-z)F_\pm(z)^k\). The most restrictive term is \(O(N^{1+(k-2)\alpha})\), strictly below the main \(N^{k-2}\) for every \(k\ge7\). These are mathematically proved inequalities; no experimental extrapolation is used.

Run `python3 verification/verify.py` with Python 3.8+ to reproduce independent integer-arithmetic checks. Actual run yielded:

```text
VERIFY_OK exact_coefficient_equalities=2568 finite_window=320 last_nonincreases={('evil', 7): 25, ('odious', 7): 6, ('evil', 8): 22, ('odious', 8): 7, ('evil', 9): 16, ('odious', 9): 8, ('evil', 10): 16, ('odious', 10): 9} total_nonincreases=63
```

The tests cover degrees \(0\le n\le320\), \(k=7,8,9,10\), and both parity sets, separately compute ordered counts and signed polynomial coefficient identities. Positivity in \(40\le n\le320\) is finite evidence, not a certified infinite monotonicity threshold. No independent audit has been performed.
