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

# Verification details

Execute `python3 check.py` in the directory containing this document. The executable uses Python 3's standard library only. The test checks 472878 individual Fibonacci-factorial-derived coefficients at the largest height (\(L=5\), 972 rows), all lower levels, the exact three-state digit transition generated from nine ternary digit pairs, the two-by-two carry matrix, the polynomial recurrence through \(L=6\), zero counts, maximal counts and triangle totals. The observed output ends in `PASS: elementary Fibonacci valuations, all triangular fibers (L=0..5), digit transitions, rational recurrence (L=0..6).`

The mathematical proof in `RESULT.md`, not these finite experiments, establishes the generating function for arbitrary \(L\). A finite check cannot rule out a counterexample beyond its range, and the checker does not claim to test any alternative prime or all possible congruence residues. Independent audit has not been performed.
