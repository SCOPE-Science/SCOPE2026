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

# Reproduction and verification

The all-size proof is given in `RESULT.md`. Reproduction requires Python 3 and only standard-library modules; execute `python3 verify.py` in the same directory. The verifier exhaustively enumerates the \(2!+3!+4!+5!+6!+7!+8!=46{,}232\) permutations of sizes two through eight, calculates exact joint probabilities for each record/excedance position pair, and checks every entry against the stated formula using rational arithmetic. It further tests exact row/column/global consequences for sizes up to one hundred. The run produced the final line `PASS: 640 exact checks; analytic proof needed for all n`.

A finite enumeration does not establish the infinite family of identities; the critical analytic steps are the conditional exchangeability calculation, the hockey-stick summation, and the monotonicity of the reciprocal-binomial sum. None requires computer algebra or unprovided third-party data. No independent audit has been performed.
