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

Under the fully specified continuous null the probability integral transform gives i.i.d. uniform observations. The centered L² summand has the published covariance: integrating its product above max(s,t) gives the cubic term and subtracting the outer product of the means gives −s(1−s)t(1−t). Its finite mean-square norm gives positive trace class. Fubini gives the stated rational-polynomial action. An independently written Fraction calculation, without executing the supplied verifier, reproduced the three Hilbert–Schmidt ingredients, H=109/8100, the q and r² of f=K^5 1, and all strict rational comparisons. In particular λ₁≥q and λ₂²≤H−q²<10^−4, so q>0.01 proves simplicity. On the spectral support the product (λ−λ₁)(λ−0.01) is nonnegative, including at λ=0; averaging gives (λ₁−q)(q−0.01)≤r² and the stated Temple enclosure. The single largest Gaussian-square term gives the log-tail lower bound; positivity and trace class give the finite exponential moment for 0<h<1/(2λ₁) and thus the matching Chernoff upper bound. The reciprocal constant in the finding is consistent with the certified interval.

## originality

PASS

The Gaussian covariance limit, eigenvalue formulation, and role of the largest eigenvalue in Bahadur analysis are prior work. The generic log-tail relationship and Rayleigh–Temple machinery are not new. The scientifically distinct claim is the narrow certified enclosure of the largest eigenvalue of this particular covariance, left unevaluated in the original paper. The separate exact same-statistic Resultary result computes mixed covariances and variances, not this spectral invariant.

## value

PASS

The statistic and its missing leading spectral weight are independently motivated by §6 of the original paper. Certifying the model-specific weight quantifies the null logarithmic tail and supplies the constant required for local Bahadur comparisons, with rigorous error control and without treating a finite-dimensional discretization as the infinite operator.

The dated certificate retains the supplied scientific assessment, sources and limitations.
