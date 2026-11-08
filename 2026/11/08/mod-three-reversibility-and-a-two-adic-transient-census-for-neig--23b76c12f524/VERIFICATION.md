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

# Verification and reproducibility

Execute `python verify_linear.py` using Python 3.8 or newer. This constructs the \(2n\)-vertex open-neighbor ladder matrix directly and checks \(\dim\ker(A_n^t)=2\min(t,m)\) for singular ladders and zero nullity for reversible ladders. It verifies 525 distinct \((n,t)\) cases with \(2\le n\le84\). `linear_check.txt` contains the actual captured outcome.

Execute `python verify_labelled.py` with Python 3.8 or newer. This constructs neighbor lists independently and follows every binary configuration until it repeats, recording the first periodic-entry index. Its exhaustive cases are \(n=2,3,4,5,6\), totaling 5,456 configurations. `labelled_check.txt` records the observed histograms and pass result. Neither program uses external libraries.

The checker code is included complete and self-contained. These checks neither enumerate arbitrary \(n\) nor constitute the mathematical proof. For the infinite family and for arbitrary characteristic-two finite fields, rely on the tridiagonal recurrence, cyclicity, cubic-root valuation, dual-number change of variable and Fitting-decomposition counting steps in `RESULT.md`.

An independent external audit has not been performed.
