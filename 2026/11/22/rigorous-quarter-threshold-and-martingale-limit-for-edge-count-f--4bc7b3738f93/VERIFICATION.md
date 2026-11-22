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

The attached `checker.py` is self-contained and can be executed with `python checker.py` using Python's standard library. It performs exact rational enumeration of growing simple graphs through five vertices for the four parameter pairs \((p,r)\in\{(1/5,1/2),(1/4,1),(1/3,2/3),(3/5,1/3)\}\), compares the directly enumerated expectations and variance with the displayed closed recurrences, and checks probabilities and positivity. It also algebraically compares the certain-parent-link asymptotic coefficient with Equation (16) of Bhat et al. (2016) at four rational probabilities below \(1/4\). The run passed 2,248 exact assertions.

The checker does not establish asymptotic convergence for any \(n\to\infty\) claim. The analytic proof of that claim is in `RESULT.md`: recurrences for edge counts and degree-square sums, exact total variance, positive forcing, variation of constants, summability for \(2p+p^2<4p\), and \(L^2\)-martingale convergence. The 2016 variance-scale prediction for \(r=1\) is explicitly credited. No Gaussian limiting law is claimed.
