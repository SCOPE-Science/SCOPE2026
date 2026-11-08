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

Reproduce from the adjacent `verify.py` with Python 3.10+ and SymPy 1.12+:

```sh
python verify.py
```

The program prints `VERIFICATION_PASS`, confirms the exact two-species and three-species moments using two distinct finite computations (subset inclusion-exclusion and a first-step Markov recursion), checks the symbolic curvature coefficient and critical quartic coefficient, and isolates the unique threshold by exact rational sign tests together with the monotonicity bound in the proof. All scientific assertions require the displayed analytic arguments as well as the code checks. The primary probability model assumes fixed positive abundances, independent sampling and perfect detection. No independent audit or external certification is claimed.
