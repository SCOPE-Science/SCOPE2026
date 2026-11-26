---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Backward exponential integration of the stationary ODE splits the integral into independent Poisson intervals, including the stationary age, giving Beta(1,α) breaks independent of sphere directions. In Q_d−S=2∑_{i<j}P_iP_j(U_i·U_j), distinct pairs are conditionally orthogonal even if they share one index, and each inner product has second moment 1/d. Thus the conditional error is 2(S²−H₄)/d. The beta recursion gives E S=1/(α+1), E S²=(α+6)/D and E H₄=6/D for D=(α+1)(α+2)(α+3); these give every displayed variance and the common-weight L² limit. For finitely many directions normalize independent Gaussian rows and use the joint CLT for their centered coordinate products; the limiting covariance is the identity. The scaled omitted terms have uniformly vanishing conditional second moment 4∑_{i<j, j>m}P_i²P_j² as m→∞. Bounded convergence against weight-measurable bounded tests gives stable convergence. The mixing variance is positive almost surely but bounded by 4(1−P₁) (indeed it is O((1−P₁)²) near P₁=1); it can approach zero with positive probability, hence is not constant, and uniqueness of Laplace transforms rules out a single Gaussian. With M=max P_j, a size-biased mass has the first-break Beta law and a mass exceeding 1−δ for δ<1/2 is unique. Its chance of selection lies between 1−δ and 1, so P(M>1−δ)∼δ^α. The bounds M²≤S≤M²+(1−M)² and S≤M then trap 1−M at the S-edge threshold ε/2+O(ε²), giving 2^(−α) for squared radius and 1 for radius. These are limits in the stated order, not uniform in d. RESULT.md Steps 1–6 give analytic replay; frozen VERIFICATION.md and verify.py were inspected, not executed.

## originality

FAIL

The main random-radius and stable fluctuation assertions are demonstrably earlier in a distinct Resultary record, including the sharp finite-d L² error. The radial edge coefficient is not stated in that finding but is an elementary consequence of its limit representation and classical size-biased GEM data, as explained below; it does not validate the frozen theorem as an original finding.

## value

FAIL

The random-shell and stable-mixture phenomenon is meaningful but already covered. In isolation the new edge wording reports the leading asymptotic forced by a single size-biased beta mass and deterministic inequalities. It does not determine a finite-d turning-surface law, any crossover, or a separate mechanism; the routine consequence does not justify a repaired finding here.

The dated certificate retains the supplied scientific assessment, sources and limitations.
