---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

A jump at s in ((j-1)/n,j/n] samples exactly the binomial upper tail from j. The beta CDF and monotone inverse King map identify the error as E|X_j-s| including the endpoint jump s=1. The canonical right-continuous Stieltjes measure has total mass in absolute variation equal to Var(f); Minkowski gives the matching upper bound and concentrating unit mass at jumps gives the lower bound. On each cell the error derivative is 2F_X(s)-1, strictly increasing; only one-sided endpoints enter, and each uniquely winning R endpoint is excluded in its own cell, so no norm attainment by a step or by any nonzero variation measure. Independently reproduced all 81 comparisons using exact integers on M=25200 and Q=25200·2^15. At i/M find the lower parameter as k/Q with k=floor(Q i²/M²) at n=1 and k=(isqrt(Q²+4n(n-1)i²(Q/M)²)-Q)//(2(n-1)) otherwise. Bound each increasing binomial CDF between tail numerators at k and min(k+1,Q); for a candidate p/M sum lower left nodes for F on [0,p/M], and 1 minus upper right nodes on [p/M,1]; reverse bounds for the upper sum. All comparisons have denominator MQ^n; minimum gap across the nine winning lower bounds versus strongest rival upper is >0.00023129 (n=9, rival R_{9,3}). Confirmed all three printed strict decimal enclosures; independent n=8 and n=9 intervals have endpoints approximately (0.1511675291,0.1512072132) and (0.1369558401,0.1369955238). Frozen CHECKER.py inspected, not executed; the replay algorithm above uses a different grid and exact square root. Finally inverse shift ≤1/n by rationalization, so beta CLT in the interior plus bounded scaled second moments gives convergence of mean absolute deviations. Mean shift is O(1/n) and scaled variance vanishes at endpoint subsequences. Subsequence compactness gives both the sharp asymptotic and all near-maximizing single-jump positions converging to 1/2.

## originality

PASS

The new mathematical target is the finite sharp norm profile for this prescribed nonlinear King time change, particularly the first switch from a boundary cell to a strictly interior cell and its directional nonattainment. The operator, basic distributional reductions, and leading Bernstein asymptotic transfer are not separately strong priority claims. Best-of-knowledge PASS for the complete King-specific comparison.

## value

PASS

The first strict change of the worst jump from a boundary to the right side of an interior lattice point is a natural cutoff for a standard operator, not an arbitrary degree sample. It answers which discontinuity its sharp norm measures, and rigorous nonattainment and eventual midpoint localization clarify how representative conventions and approximation degree affect that benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
