---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

Diagonal entries give D_n=sup_k nr_k|1-r_ke^{iφ}|^n. Uniform log|1-re^{iφ}|=-br+O(r²) and exponential tails yield D_n=b^{-1}max_k(br_k)e^{-br_k}+O(1/n); the error bound follows from n²r³exp(-cnr)=O(1/n). The resolvent Ritt bound uses 1-|1-re^{iφ}|≥cr for 0<r≤r_1<2b. For y_j=bnr_j≥1>y_{j+1}, unimodality reduces the scalar max exactly to two adjacent modes. The crossing y=L(q_j)=log(1/q_j)/(1-q_j) gives the liminf, while n≈1/(br_j) gives limsup 1/(eb). For q=0 a geometric-mean time gives a zero trough; for q=1 both neighbors approach one. O(1/n) consecutive-step variation makes the whole cluster set an interval, not merely its endpoints. Monotonicity of L and h gives inverse uniqueness. Explicit summable ray sequences and scaling verify all-Schatten realizability; arbitrary smallness is for a fixed p, not uniform in p. No finite tests substitute for these all-n steps.

## originality

PASS

Prior Ritt growth and subsequence-of-time-index results are adjacent but the exact spatial gap-ratio/entire-cluster-set inverse is a distinct quantified statement; plausible uninspected full texts remain a priority risk.

## value

PASS

The exact inverse observable recovers asymptotic eigenvalue separation from long-time operator norm data; it distinguishes normal Ritt contractions invisible to generic uniform Ritt bounds. The entire cluster interval and arbitrarily small Schatten perturbations supply a mathematically motivated sharp boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
