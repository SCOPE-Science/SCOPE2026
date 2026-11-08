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

# Reproducible scientific checks

Run `python verify.py` with Python 3.9 or later; no third-party libraries are required. The code independently enumerates pairs of lower and upper Wythoff values, checks a separate membership-convolution implementation, and evaluates the three-arc phase law using exact integer membership and floating-point phase approximations only for asymptotic numerical comparisons. It verifies the initial OEIS values and compares empirical moments with their analytically derived targets. Finite tests provide no proof of infinite identities, uniqueness, or historical originality.

The proof's infinite checks are (i) exact Beatty membership and complementarity; (ii) geometric interval equivalence; (iii) convergent-denominator block discrepancy for the golden rotation; (iv) pushforward of Lebesgue measure under the piecewise-linear profile; and (v) bounded-variation discrepancy control of all one-Lipschitz observables. The full range of \(n\) and all test functions in the theorem are covered by those arguments, not by code. Independent mathematical audit has not been performed.
