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

# Verification of the stated theorem

The proof derives the infinite statement analytically from the established truncated-cycle functional limit, a marked-Poisson process, exact change-of-variables factorization, a beta-moment asymptotic, and a Laplace--Stieltjes Tauberian theorem. These critical steps and their domains appear in `RESULT.md`.

The independent finite-state checker `check.py` runs directly with Python, SymPy and SciPy. It uses an exact rational recursion for the first twelve growing permutations at \(\theta=1\) and cutoffs \(k=1,2,3\), rather than sampling paths, and tests consistency of finite means and second moments. It also symbolically checks the service-survival polynomial identities for \(1\leq k\leq8\), numerically tests complete moment-product sequences for three parameter values, and checks the closed derangement variance. Its completed run had **101 successful assertions**; for \(k=1\), the limiting variance printed was \(0.09720887469821693\ldots\).

The finite recurrence and numerical quadrature support correctness but neither certify an infinite-dimensional convergence nor establish historical novelty. The limits use the previously published functional convergence, and no independent audit or external verification has been performed. Reproduce using `python check.py` from the directory containing the standalone artifact.
