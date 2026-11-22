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

# Reproduction

Run `python3 verify.py` using standard Python 3. The script constructs the truncated forbidden-subset polynomial from integer binomial coefficients, independently brute-forces all subsets for small profiles, and applies exact Stirling/Bernoulli/Newton inversion to independently generated profiles. It also exhaustively enumerates unordered tripartite profiles through order 39 and verifies the first collision and shore-padding witness.

The recorded output is:

`VERIFY_OK direct_profiles=184 reconstructed_profiles=1465 first_collision=13 witness_p3_p4=[250, 535] witness_p5=(822, 798)`

The general all-rank inverse rests on the formal-power-series proof in `RESULT.md`; finite verification does not certify every infinite instance. Historical novelty remains provisional, and no independent mathematical audit has been performed.
