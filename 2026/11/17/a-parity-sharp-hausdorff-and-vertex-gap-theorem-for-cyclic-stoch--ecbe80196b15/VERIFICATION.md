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

Run `python check_circulant.py` using Python 3. The first part requires no third-party packages. It exhaustively computes cyclic-displacement multiplicity vectors for all permutations of orders \(2\) through \(8\), compares the first two distinct squared-norm histogram levels with their formulas, and checks the modular relationship between repeated and absent offsets. It also directly verifies explicit maximizing and second-level constructions for all integers \(3\le n\le1000\).

When NumPy and SciPy are installed, the optional part makes 48 independent equality-constrained, box-constrained SLSQP minimizations over the cyclic-shift simplex at orders \(3\) through \(8\), using both permutation and interior bistochastic inputs. These compare against the orthogonal-projection formula; numerical tolerance is \(5\cdot10^{-6}\).

An observed successful check printed exact-order statistics \(n=2:(2,[4])\), \(n=3:(6,[3,9])\), \(n=4:(24,[6,8])\), \(n=5:(120,[5,9])\), \(n=6:(720,[8,10])\), \(n=7:(5040,[7,11])\), and \(n=8:(40320,[10,12])\), where the brackets list the least histogram square sums. All 998 construction orders passed, and the 48 optional numerical checks passed with worst absolute deviation below \(2.3\cdot10^{-7}\).

The proof of the all-order Hausdorff value, equality classification, and first discrete gap is analytic and does not depend on extrapolating the finite checks. No claim concerning other Schatten metrics or the second farthest distance over continuous nonvertex points is made. Independent mathematical audit has not been performed.
