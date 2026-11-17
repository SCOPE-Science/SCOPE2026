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

# Computational verification and proof boundary

The provided file `check_even_permutation_schatten.py` is a standalone checker. Execute `python check_even_permutation_schatten.py` with Python 3, NumPy and SciPy. It enumerates parity classes for each order \(3\le n\le8\), verifies that the exact trace \(n-2\) equality instances are precisely the \(\binom n2\) transpositions, checks the rational center formula and singular values at indices \(1, 3/2, 2, 3, 5,\infty\), and verifies the simplex off-diagonal certificate. Separate constrained numerical programs project one odd permutation matrix onto the full even-permutation hull for orders \(3,4,5\), confirming squared Frobenius distances \(2,4/3,1\).

The analytic proof in RESULT.md covers all \(n\ge4\) and all \(1\le p\le\infty\); the finite enumeration and numerical optimization are supplementary. Finite results do not certify literature priority, independent auditing, or theorems at untested orders. The Schatten endpoint projections are exhibited but not claimed to be unique. Historical-priority risk remains for uninspected older texts.
