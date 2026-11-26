---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Under the iid uniform simple null the centered upper-tail feature has the same squared empirical norm as the centered CDF. Integrating the upper-tail feature gives U−1/2, so Watson subtracts the orthogonal constant-function projection. In the product of two empirical quadratic statistics a covariance survives only for a shared diagonal label or an identical unordered off-diagonal pair; all one-label overlaps involving a degenerate pair vanish on conditioning. Hence each of the six moments is affine in 1/n. An independent exact integration of the defining statistics over the sorted-sample simplex verifies all six moments at n=1 and 2, which determines those two affine coefficients, and also at n=3 as a cross-check. This checks the finite-n terms, not just the Gaussian limit. Symbolic differentiation gives the stated positive derivatives of squared correlations and their positive gap for n≥2. The covariance share decreases from 29/35 to 10/13, not reaching 10/13. At n=1 Watson is deterministic and its correlation is undefined. The frozen check.py was inspected but not executed. Independent replay: python3 /workspace/checks/4.py (SymPy); output /workspace/checks/4.out.

## originality

PASS

Pass is for the evaluated exact mixed finite-sample laws of the characterization statistic against these classical statistics and the finite-n mean-mode share. The statistic, the contraction method, and the constant-mode definition of Watson are not new. The closest inspected statements concern the classical pair, marginal limiting cumulants/eigenstructure, marginal finite-sample skewness, or empirical power, none of which gives the mixed contractions. This is a bounded best-of-knowledge assessment.

## value

PASS

The initiating uniformity paper compares these particular tests, making their redundancy on the same observations a natural question. The exact formulas quantify a distinction not visible in marginal variances or power: the squared empirical mean accounts for more than 10/13 of the CvM cross-covariance at every n≥2, while Watson centering leaves a weaker but positive association. This is useful for reasoning about comparisons on one sample; it is not a joint calibration, a power guarantee, or a claim of independence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
