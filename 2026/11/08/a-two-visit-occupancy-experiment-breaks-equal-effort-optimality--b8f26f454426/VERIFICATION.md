---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

An independent information derivation separates the Bernoulli event of any detection from the history conditional on a positive result. Write k=exp(-lambda T), alpha=1-k, q=1-psi alpha, and S=sum_j t_j^2/(exp(lambda t_j)-1). The any-detection contribution is the rank-one outer product of (alpha, psi T k), divided by psi alpha q. The positive-history conditional score involves only lambda and is orthogonal to the Bernoulli score. In the fully occupied subexperiment its information J satisfies S=T^2 k/alpha+alpha J; thus in the mixture the extra lambda-lambda entry is psi alpha J. This yields det I=(alpha S-T^2 k)/q exactly. Both positive-duration visits give J>0 because P(11)/P(10)=exp(lambda t_2)-1 has nonzero derivative; endpoints give determinant zero by continuity. At fixed budget only f(x)+f(theta-x) matters. Its small-budget strict concavity follows from f''(0)=-1 and continuity, with symmetry giving the unique equal split. At 10 log 2, exact operations on powers of 2 reduce the two scaled numerators to 715639/455168 and 775/512 (gain 3333/56896, about 3.8701%). The sign of f' is the sign of 2(1-exp(-u))-u, whose strictly decreasing derivative after its sole critical point gives the unique positive root a_*. For long budgets the competitor (a_*,theta-a_*) approaches f(a_*); unbounded shorter legs would make both f terms vanish, and every limit point of the bounded shorter legs must equal a_*. Finally f(a_*)=a_*(2-a_*), and direct simplification at equality gives (theta^2/2)(exp(-theta/2)-exp(-theta)), yielding both determinant limits for fixed interior psi and fixed lambda.

## originality

PASS

The supported distinct finding is the fixed-budget geometry for two positive binary visits, with unknown prevalence and one shared Poisson rate and no false positives: exact prevalence separation in the split criterion, strict small-budget symmetry, finite counterexample to equal allocation, and the universal normalized short leg. Joint design and occupancy likelihoods are antecedents rather than novelty claims. The strongest inaccessible comparisons remain explicit limitations, not inferred mismatches.

## value

PASS

Balancing two visits is a natural design default. This fixed-effort benchmark proves when that default works at small budgets, shows a concrete finite failure independent of prevalence, and gives a principled long-budget allocation with exponentially higher determinant than the balanced split. The mathematical motivation is the change in optimal design and its asymptotic efficiency, not the small size of the single finite witness gain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
