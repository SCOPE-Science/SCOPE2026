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

# Verification of the finite probability law and asymptotics

Run `python verify.py` using a standard Python 3 interpreter. No nonstandard packages or network access are needed. `verify_output.txt` records a successful execution ending in `ALL_PASS 491`.

The checker independently constructs each clique–cycle graph, implements exact degree-minimum selection from every distinct sampled candidate subset, and performs exact clique completion. Memoized rational-state recursion checks the distribution of inserted edges against the closed-form hazard law for \(1\le h\le4\), \(3\le m\le6\), \(h+m\le8\), and the tested budgets. Full permutation enumeration supplies a separate validation for the uniform-order case. Other checks cover the exact expected-fill identity for \(333\) pairs \((h,m)\) and finite-size convergence diagnostics at three different sizes.

The crucial proof step that cannot be certified merely by finite code is the preservation of the cycle structure after a rim pivot and the completion to a clique after the first hub pivot. The proof also establishes the uniform asymptotic survival-product estimate and exact regular-variation tail. The code tests examples, not all graph sizes or the infinite-sample limits. No independent external mathematical audit was performed. The theorem concerns symbolic Cholesky fill, not measured numerical speed, floating-point stability, or all sparse graphs.
