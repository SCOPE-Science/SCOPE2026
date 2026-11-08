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

## Reproduction
From the complete package directory run `python3 verify.py`. It uses only the standard Python library, enumerates all \(409110\) permutations of sizes \(3\) through \(9\), checks the conditional probabilities for every \(k\) and \(i\), and compares covariance against the closed formula. It separately checks all stated probabilities and aggregate covariance for \(3\le n\le300\) with exact rational arithmetic.

## Result of actual execution
`OK: 1195 exact rational assertions; 409110 complete permutation objects; n=3..9, plus symbolic formulas checked for n=3..300`

## Proof boundaries
The computation is finite and cannot establish the all-size theorem. Its generality follows instead from the tagged-cycle sampling law, adjacent-label conjugation cancellation, and the four-case conditional first-image calculation given in RESULT.md. The variance and asymptotic step uses standard Eulerian/uniform-distribution formulas. No independent audit is claimed.
