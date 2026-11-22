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

## Analytical checks

The derivation diagonalizes the positive star kernel on a two-dimensional hub/leaf-constant invariant subspace. The one-parameter substitution \(r=\sqrt{m(s+f)/(s+mf)}\) turns the Perron root into a rational function whose derivative has the exact sign \(s-S_m(r)\), with \(S'_m(r)>0\) throughout the allowed interval. This proves the unique turning point or strict monotonicity for all integers \(m\ge2\) and all stated real rates. A positive left Perron vector gives extinction convergence even at the exact capacity threshold; positive sub/supersolution iterations give a positive equilibrium above the threshold.

## Reproducible computations

With Python 3, NumPy and SymPy installed, extract `check.py` and execute `python3 check.py`. The script tests symbolic identities and the factorization, checks the exact rational seventeen-patch eigenvector certificate at the optimizing mobility, and performs 500 full-matrix comparisons. It also checks strict numerical brackets for the two exact threshold roots. It printed three PASS lines on the reviewed package's actual `check.py` path.

## Limits

Finite matrix calculations are consistency checks, not infinite-domain proof. The results concern deterministic fast-exploration dynamics with equal patch rates and a fixed neighbor-born exploration-feasibility function; they are not a stochastic nonextinction guarantee, a general-graph classification, or an experimental measurement. The mathematical and publication-priority assessments have not been independently audited.
