---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

Independent rate-one type processes couple exactly to discrete coupon labels; cover time C_N=max first arrival has exact max-exponential CDF and bounded centered fourth moment. For each threshold j, empirical Gamma(j,1) tail has uniform-in-time DKW error O(N^−1/2), and there are only O(√logN) distinct thresholds on a fixed x-window; the union-bound L² supremum is o(1/logN). The Poisson CDF derivative equals minus its boundary pmf, with uniform local CLT giving √logN times derivative→−φ(x); bounded max pmf and centered cover fourth moments promote linearization to L². Optional isometry of total-rate-N Poisson martingale gives E|(T_N/N)−C_N|²=H_N/N→0. The uniform functional remainder and Gumbel moment convergence imply joint law and covariance. Finite companion code was inspected but is not the asymptotic proof.

## originality

PASS

Ilienko 2026 Theorem 1 proves infinite-dimensional sibling limits only in product topology with coordinatewise fixed-r normalizations r!U_r/(logN)^r→Exp common amplitude, not for moving r≈logN or compact-supremum profiles; the distinct fixed-index limit does not imply the target functional law. Long 2026 studies fixed sibling indices and explicitly excludes growing indices. Resultary nearby 2026 fixed-index residual and terminal-singleton laws control different counts/scales. No exact prior compact-uniform moving-index Gumbel law was found, with residual risk from broad occupancy/empirical-process literature.

## value

PASS

The logN sibling-index window is the natural transition where a typical type has roughly as many occurrences as the queried album rank at main completion. A compact-uniform rank-one non-Gaussian fluctuation law and full limiting covariance kernel are useful quantitative structure beyond classical fixed-sibling limits.

The dated certificate retains the supplied scientific assessment, sources and limitations.
