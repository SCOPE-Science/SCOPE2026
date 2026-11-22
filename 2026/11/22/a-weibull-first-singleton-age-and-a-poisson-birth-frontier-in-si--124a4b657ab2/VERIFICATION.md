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

# Verification record

The attached standard-library `verify.py` enumerates every possible recursive-tree parent assignment and every independent Bernoulli site-retention subset for \(2\le n\le7\) at \(p=1/3,1/2,2/3\). It compares all singleton, pair, and triple isolation probabilities against the exact conditional-parent formula in the proof. Each one-point probability is separately checked against the product formula. It also compares the expected number of early singleton vertices at four large finite parameter/window choices with the proposed intensity integral. The total recorded output after direct execution is `PASS: 544 exact/finite/numerical comparisons`.

These tests are finite, so the proof of all-size and asymptotic statements is the analytic argument in `RESULT.md`. In particular, the Poisson point-process claim uses uniform fixed-order joint-probability factorization on positive compact age windows, a one-point bound at the origin, and the standard factorial-moment characterization. Limits exclude \(p=0\) and \(p=1\); no convergence-rate certification or independent audit is asserted.
