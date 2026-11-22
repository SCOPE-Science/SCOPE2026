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

## Analytic verification

The proof reduces every permutation to a sum of independently assigned incremental scores \(h(x_j)\), establishes strict single-peakedness, and proves strict decrease of \(h(x)/h(cx)\) using a hyperbolic-function derivative inequality. All parameter boundaries in the theorem are explicitly quantified; the equalities at each transition compare neighboring blocks and preserve both optimal choices.

## Reproducible diagnostics

`python checker.py` ran successfully under Python 3, without external dependencies. It recorded 6089 passed assertions, including exhaustive finite combination comparisons for \(2\le n\le9\), deterministic sensitivity/retention parameter draws, checks on every block transition, and the golden-ratio special case. The displayed demonstration for initial load \(8\) gives expected sums \(4.241880690637\) and \(3.990255637369\) for the optimal and front-loaded arrangements, respectively. These finite diagnostics cannot certify all real parameters; the mathematical proof is the basis for those claims.

## Limits

No empirical calibration, biological optimality of observed movement, field validation, or independent audit was performed. Literature priority is provisional due to incomplete access to some related original papers and possible broader scheduling equivalences.
