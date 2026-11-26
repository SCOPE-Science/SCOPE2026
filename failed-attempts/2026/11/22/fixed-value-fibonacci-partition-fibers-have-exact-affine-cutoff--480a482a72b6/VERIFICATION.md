---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Independently recovered the two-state rule by complementing subsets. For a positive residual m whose greatest Zeckendorf index is j, set U=R(m), W_t=R(f_t−2−m) with R of negative arguments zero, and V=W_{j+1}. Then W_j=0; for t≥j+2, complement within the terms through f_{t−1} to count f_{t−1}+m, and split by whether f_{t−1} is included. The contribution including it is U; complementing the remaining case within the terms through f_{t−2} gives W_{t−2}. Thus W_t=U+W_{t−2}. Prepending f_i for i−j≥2 changes the pair to (U+W_{i−1},W_{i−1}); on a row (q,A−q) this gives exactly the two gap transitions. At a lone index j the pair is (floor((j+1)/2),floor((j+1)/2)−1), by the same complement split with empty residual. The state starts at (1,1), explaining the terminal formula. The second coordinate never decreases; once A>k, only q=k, any number of gap-2 extensions, and terminal index 1 or 2 can succeed. This tail is z/(1−z); before capping the first coordinate strictly increases and the allowed gap and stopping exponent bounds give the stated k-dependent polynomial degree bound. The cutoff operation adds one summation and the zero contribution when k=1. The gap 2k gives a positive infinite ray, ensuring a positive eventual coefficient, and Fibonacci bracketing gives the logarithmic law. A fresh exact subset-sum DP, `/workspace/branches/c30a8bd4-2ec4-4384-b365-15bf483114c3/check_k12.py`, checked every n<f₂₅=121393 without executing the frozen verifier. Differences of successive band counts give the seven coefficients at exponents 11,12,13,14,15,23,24 as 8,16,8,4,4,2,2, and C₁₂(24)=506. The exact recursion, not that finite check, justifies the infinite tail; the coefficient sum and first moment are 44 and 594.

## originality

FAIL

Weinstein's Theorems 3.8 and 5.1 are material prior coverage, omitted by the submitted comparison. They classify each fixed-value fiber and explicitly give stabilization at i≥2k with a computable band count. With the same indexing and the unique-representation endpoints removed/added, this implies the rational denominator, eventual affine and logarithmic laws, positivity, and a strictly better numerator degree bound. Weinstein's table gives the precise k=12 eventual band count. The finite numerator coefficients are a direct enumeration of the already classified fiber, and the alternative gap recursion does not establish a distinct substantive output at this scope.

## value

FAIL

A fixed-value census and effective linear-onset guarantee are natural questions, but the submitted mathematical outputs are covered by an earlier stronger stabilization theorem. The residual differences are a re-expression of the known band law, a different evaluation procedure with a weaker stated degree bound and no established computational advantage, and a routine finite prefix computation at k=12. These do not give a sufficiently motivated distinct surviving result for a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
