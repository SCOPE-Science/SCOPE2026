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

# Reproduction and limitations

Place `CHECKER.py` alongside `DP_CERTIFICATE.json` and run `python3 CHECKER.py`. Both files are included with the mathematical result.

The verifier evaluates all \(128\) remaining-good states, checks \(448\) alternative actions, and independently traverses all \(13{,}700\) possible ordered game histories (including \(5040\) terminal paths) using integer arithmetic, the published full valuation matrix, and a fixed smallest-label continuation tie rule. It checks all prescribed state actions, allocation masks, payoff values, unique subset utilities, equilibrium path and strict EF1 violation. The expected terminal message begins with `PASS: 128 dynamic-program states and 448 state actions;`.

The lower bound for at most \(6\) goods is a direct proof from the equilibrium unilateral-deviation condition; the finite program does not purport to enumerate all possible valuations. The witness establishes the existence of a non-EF1 SPNE, not uniqueness of equilibrium or the failure of every SPNE.

No independent scientific audit has been performed.
