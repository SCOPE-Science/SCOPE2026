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

# Mathematical verification

Execute `python3 checks/verify.py` from this package root using only Python 3 standard library. The executable reports 529 passing deterministic assertions on elementary Erlang-tail formulas, distinct-overlap logarithmic exponents, selected exact two-window exceedance formulas, asymptotic numerical scale checks, and combinatorial enumeration of nonoverlapping windows. The critical unbounded-\(n\) conclusion is not a computational claim: it follows from the common/exclusive Gamma split, an \(O(n^{-1}/\sqrt{\log n})\) bound for each overlapping distinct window pair, and mixed factorial-moment convergence. Each overlap block contributes at most one rare-pair factor, with independent disjoint-support blocks. Finally, exponential normalization differs from one by \(O_{\Pr}(n^{-1/2})\) and is multiplied by maxima of order \(O_{\Pr}(\log n)\).

The numerical quadrature uses midpoint partitioning at Gamma-shape-zero discontinuities, and its checks are approximate with stated tolerances. No amount of finite testing certifies the point-process limit, and no independent validation has occurred.
