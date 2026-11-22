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

# Reproducibility and limits

Run `python3 verify_nonlocal_wheel.py` with Python 3. The program has no third-party dependencies and prints `VERIFY_OK` only if all integer assertions pass.

For each circumference from 7 through 16 inclusive, the verifier constructs graph distances of the wheel and tests every rim mask for nonlocal and ordinary resolving status, both with and without the hub. There are exactly 130,944 such rim masks. It independently checks equivalence to the cyclic-gap criterion, full polynomial coefficients obtained from the rational transfer expression, and the minimum-base formulas.

For circumferences 17 through 220, it also checks the exact integer generating-function recurrence, binomial coefficient formula at the minimum, five congruence-class expressions, and absence of lower-degree terms.

The correctness of the infinite-family claim is proved in `RESULT.md` via the distance-signature characterization, formal cyclic transfer identity, binomial extraction and analytic location of the dominant pole. These finite checks do not establish the theorem outside the verified range by themselves. No independent mathematical audit has been performed.
