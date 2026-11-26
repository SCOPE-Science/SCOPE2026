---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The sample space is cyclic tours of the distinctly labeled arcs, with rotations but not binary complements identified. For s with different overlapping n-blocks, contracting their successive arcs into one distinguished arc is a bijection on the required tours. Outdegree remains two except at the middle vertex where it becomes one, so BEST has no extra factorial factors, even when endpoints coincide. If the balanced contracted graph disconnects, all vertices have positive degree and Euler-tour and arborescence counts are both zero. Equal overlapping n-blocks mean a constant s and are impossible on a tour. Subtracting the two arc Laplacian contributions and adding the shortcut gives (e_u−e_v)(e_v−e_w)^T, with both factors of sum zero; the determinant ratio with J added therefore uses only the inverse on the zero-sum subspace. Exact replacement of the m=n−1 initial symbols implies P^m=J, and for t<m an overlap fixes exactly one appended t-bit word, giving P^t(x,y)=2^(−t)H_t(x,y). This verifies the signs and all four terms in the formula, including wraparound, coincident vertices and n=2. The exact numerator can be obtained from a=1 by a←2a+δ_t for t=0,...,m−1, where δ_t is the signed four-indicator sum. Four direct comparisons and the accumulator cost O(n) bit operations per t and O(n) auxiliary bits overall. This is for the probability, not explicitly writing out the potentially exponentially long cycle count. As an independent corroboration, I anchored the binary cycle by its unique all-zero n-block, appended one bit at a time forbidding already seen n-blocks, kept only paths with 2^n visited blocks and last n−1 bits zero, then compared every cyclic window frequency by integer cross-multiplication. Orders 2–5 produced 1,2,16,2048 cycles with zero mismatches at each order. The frozen script was inspected, not run. The proof is for one prescribed window, not joint probabilities or general alphabets.

## originality

FAIL

The scoped contribution is the matrix-free four-overlap likelihood and the quadratic bit upper bound. The distinct indexed local-selector correlation record explicitly has the same shift-and-append kernel and the same one-contraction diagonal formula. Evaluating that entry by direct string comparisons with a dyadic accumulator already has the stated bit and space bounds. This is demonstrable mathematical coverage, not a judgment about calendar priority between the two 2026-11-22 UTC records.

## value

FAIL

Exact per-window probabilities are a natural and useful object. Nevertheless, the only proposed new gain is already achieved by the indexed singleton overlap entry using the same direct evaluation. The record makes that evaluation easier to find but contributes neither a new mathematical computation nor a stricter bound beyond the mechanically implied result. Treating the few small orders or the already-known total cycle count separately does not leave a substantive scientific finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
