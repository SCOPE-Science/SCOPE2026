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

# Verification and limits

Run `python3 verify.py` with Python 3 and its standard library only. The checker enumerates the complete no-`11` source language for each length from 2 through 18, totaling 17,706 inputs, and compares direct output-string deduplication against the lag-two transition count. It separately computes the weighted transfer-polynomial recurrence, checks the initial values, Fibonacci totals, sharp largest exponent, and coefficient counts through length 250. It completed with the exact terminal marker `VERIFY_OK`. An explicit extremizer construction was separately tested through length 80.

The all-length theorem does not follow from checking finitely many inputs: it follows from the collision lemma, Cayley--Hamilton recurrence, residue-class leading-coefficient induction and dominant-pole coefficient argument in `RESULT.md`. Verification does not independently review the proof, establish global novelty, or certify an optimal codebook. Independent mathematical audit has not been performed.
