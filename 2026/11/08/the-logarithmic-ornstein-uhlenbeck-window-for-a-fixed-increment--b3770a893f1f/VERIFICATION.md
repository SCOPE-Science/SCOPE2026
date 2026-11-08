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

Run `python3 check.py` in the directory containing this file and `RESULT.md`. The checker uses only the Python standard library and prints `PASS 206 exact/algebraic/asymptotic checks` on success. It enumerates exact finite-state urn distributions through seven updates for four parameter choices, verifies the conditional innovation variance symbolically using rational probabilities, and checks second-moment convergence under near-critical horizon-dependent probabilities.

# Analytical verification boundary

This finite test suite does not establish a process limit. The proof of the infinite claim is in `RESULT.md`: bounded martingale innovations, a uniform second-moment estimate, predictable quadratic-variation convergence on a logarithmic clock, the martingale functional central limit theorem, and gamma-product approximations yield the continuous Gaussian limit. The underlying invariance theorem is a standard external result and is cited as methodology rather than independently certified.

# Limits

No theorem is claimed for unequal random total increments or for parameter sequences outside the displayed \(1/\log N\) window. Historical priority requires independent expert assessment.
