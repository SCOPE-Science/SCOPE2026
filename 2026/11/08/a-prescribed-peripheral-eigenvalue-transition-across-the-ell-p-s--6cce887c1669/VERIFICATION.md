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

The construction is explicit for every \(\rho>1\), with \(\kappa=(\rho-1)^{-1}\). The decisive proof checks are: (i) exponential spacing of the inserted offspring-two levels gives the exact logarithmic correction to \(\log_2 B_n\); (ii) levelwise Hölder provides the necessary eigenvalue test; (iii) the radial eigenfunction realizes every summable case, including the sharp harmonic-series boundary; (iv) the exact power norm yields the spectral radius; (v) disjoint sibling-subtree eigenvectors give infinite geometric multiplicity, forcing Fredholm-essential coverage.

`CHECKER.py` is Python-standard-library-only; run `python3 CHECKER.py` to check finite prefix accounting, norm growth bounds and rational critical-exponent comparisons. These finite checks are not used as proofs of infinite convergence, spectral radius or Fredholm properties. Every asymptotic claim is proved in the result text. Publication priority and independent audit have not been independently established.
