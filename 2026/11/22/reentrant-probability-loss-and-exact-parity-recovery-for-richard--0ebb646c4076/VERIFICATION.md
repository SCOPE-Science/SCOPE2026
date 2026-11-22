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

# Verification and scientific limits

The independent source-level construction in `verify.py` uses rational \(2\times2\) matrix inversion to form the two backward-Euler resolvents, multiplies each into the active extrapolation step, then checks powers against the analytical stationary-projector formula. This avoids using the claimed rational stationary formula to *construct* the update matrix. Running `python3 verify.py` produced `PASS`, with 3,360 exact rational matrix-power comparisons and row-sum, parity and positivity checks. Separate deterministic numerical brackets checked the unique scalar extremum, crossing positions, and square-root cusp.

The proof, not the finite tests, establishes universal quantifiers over every positive pair of transition rates, every positive step and every integer number of repetitions. Independent audit has not been performed. Generic equal-input algebra and active Richardson stability functions are known and explicitly attributed, and the historical priority of the new sharp specialization is not independently certified. No symbolic solver, third-party package, external hidden data, or time-limited computation is required to replay the verifier.
