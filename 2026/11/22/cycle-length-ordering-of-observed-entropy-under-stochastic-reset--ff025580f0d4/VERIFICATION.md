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

Regeneration gives stationarity from the mixture of walks since the last reset, and coupling at the first reset gives uniqueness. The line resolvent satisfies the stated second-order recurrence; z(q+q^(-1))=2 and 1−zq=d normalize its absolutely summable solution. Projecting modulo n sums the two geometric image tails and gives the stated neighbor occupation. For every n>=3 the two neighbors of zero are distinct, and only their rows merge one hop with reset; the positive loss per such row is (γ+a)H_2(γ/(γ+a)). Subtraction from the line leaves the exact factor (1+q²)q^(n−1)/(1−q^n); the ratio of consecutive positive deficit factors is strictly below one at fixed 0<γ<1. For finite n, γ/d=(1−q)/(1+q) gives π_n(1)=1/n+O_n(sqrt(γ)) as γ tends to zero; on the line the neighbor mass is O(sqrt(γ)). Both B−log 2 and Δ equal γ log(1/γ)+O(γ), yielding an interior maximum for every size, including the continuous endpoint extension of the line formula. Comparing at a finite-cycle maximizer yields strict order of maxima, pointwise convergence evaluated at a limiting maximizer yields convergence of maxima, and strict collision loss plus compactness gives M_infinity<log 3. There is no stationary probability law on the unreset line at γ=0; its endpoint value is a continuous extension, not a stationarity assertion there. Reviewer-authored `python3 /workspace/independent_reproduction.py entropy` (Python 3.12.3) propagated the unreset walk for 420 reset ages and directly computed merged-destination row entropies in 72 finite examples. Omitted mass is at most (10/11)^420, and the largest absolute discrepancy from the formula was 1.33e−15. The proof, not the sampled rates, establishes the strict continuum result.

## originality

PASS

The reset resolvent and merged-action collision formula are known. The regular-graph entropy envelope already implies an implicit cycle entropy, a strict line upper bound, and convergence of cycle entropies and maxima. The distinct contribution is the exact positive size-dependent deficit evaluated by resumming the periodic images, its leading constant, and strict successive-size and successive-maxima comparisons. No checked prior theorem was shown to cover that remaining quantitative hierarchy.

## value

PASS

Cycles are the finite connected simple two-regular geometries. Their exact observed-entropy error relative to the line quantifies size effects with degree and local action probabilities fixed. The full reset-rate ordering and exponential prefactor provide a benchmark not supplied by an upper envelope or a numerical comparison, and the optimized hierarchy uses the order without claiming a unique best rate. The narrow value lies in that finite-size comparison rather than in a new theory of resetting entropy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
