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

For every nonnegative zero count \(N\le100\), `verify.py` lists all feasible triples satisfying \(2a+2b+c=N\), constructs the corresponding palindrome, and independently calculates its eight scattered-subsequence multiplicities using a dynamic programming recurrence. The resulting observations are grouped into full equivalence fibers and matched to the explicit partner map and the coefficient of the rational collision-pair generating function. Through \(N=18\), a separate literal three-position enumeration checks the dynamic counts. For \(N\le500\), two different coin-change coefficient calculations are compared.

Observed output (see `verify_output.txt`): 45,526 full eight-coordinate comparisons, 385 literal-triple checks, exact fiber and involution checks at all zero counts through 100, and generating-series coefficient checks through 500. The displayed length-14 pair was checked explicitly and is previously known. No arbitrary-length proof is inferred from finite computation: the proof is the algebraic argument in `RESULT.md`.

Self-review was completed on the proof and the finite checks. Independent audit: not yet performed.
