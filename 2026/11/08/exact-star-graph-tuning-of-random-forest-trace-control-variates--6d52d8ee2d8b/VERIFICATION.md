---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

PASS: Partition of oriented rooted forests of K_(1,k) into hub-rooted versus hub-directed-to-one-rooted-leaf cases exhausts configurations; their independent Bernoulli leaf flags yield correct joint moments of R and C=tr(K^-1 S)-(k+1), with K^-1=I+L/q. The submitted formulas for Var R, Cov(R,C), Var C, alpha*=Cov/Var and residual variance follow. Var C>0 ensures unique minimizer; k=1 yields zero residual and k>=2 strict positive. Along k=Q^2,q=Q the exact moments imply alpha_opt->1/2, alpha_mean_degree->1 and variance ratios 1/2 vs 1. Independent exact rational enumeration checked k=1..7 and four q values, including boundaries; infinite assertion from analytic conditional moment identities.

## originality

PASS

PASS qualified: the primary Pilavci et al. 2022 work defines the identical random spanning-forest trace control statistic and practical mean-degree coefficient, and earlier work gives the abstract covariance/variance optimum, but the inspected full conference paper does not supply the all-q, all-k star covariance closed forms or the explicit asymptotic factor-two counterexample to mean-degree tuning. Resultary search found the submitted record, not a stronger star-specialized earlier theorem. Priority outside inspected materials remains possible.

## value

PASS

PASS: A heterogeneous star is a natural stress-test for a degree-average heuristic used in random-forest inverse-trace estimation. The sharp factor-two asymptotic comparison demonstrates an actual persistent variance gap for an identifiable algorithmic statistic, not a tiny gain or arbitrary numerical example; complete all-parameter optimization supplies a reusable benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
