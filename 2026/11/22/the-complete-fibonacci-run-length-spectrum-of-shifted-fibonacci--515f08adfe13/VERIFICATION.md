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

# Reproducibility and limits

Execute `python3 verify.py` from the same directory. The checker uses only Python standard-library integer arithmetic. It builds the semigroup by unbounded-generator coin-change dynamic programming for each \(5\le a\le24\), independently computes the Zeckendorf-digit count and the membership threshold, and scans the entire finite gap set to obtain lengths and multiplicities. It independently compares with the proposed closed formula and checks the Fibonacci word recursion.

The run passed 1,381,700 membership checks, 121,385 digit-word positions, and 46,365 gap blocks, including every relevant boundary for these 20 parameter values. Computation is finite and cannot establish the theorem at all indices; the infinite proof is the membership-word concatenation and its run-multiset recurrence as presented in `RESULT.md`. The published Apéry-set theorem is treated as a proven mathematical input, not a locally reconstructed independent result. The evidence supports self-review only; no independent mathematical audit has been performed.
