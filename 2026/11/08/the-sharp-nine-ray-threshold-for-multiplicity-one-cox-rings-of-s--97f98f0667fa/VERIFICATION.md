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

# Verification and scope

The self-contained `CHECK.py` uses only the Python standard library. Running `python CHECK.py` checks the displayed smooth nine-ray fan with exact determinant arithmetic, verifies the three selected rays form a complete fan, and confirms that their three cyclic intervals each contain two other rays. It evaluates 2,600 nonzero dual lattice vectors of coordinate size at most 25 and tests the congruence and degree obstruction in each case.

The exact observed output was:

```text
NINE_RAY_FAN_OK 9 TRIPLE_GAPS_OK INTEGER_TESTS_OK 2600
UNBOUNDED_IDEAL_CONTAINMENT_REQUIRES_THE_WRITTEN_CONGRUENCE_PROOF
```

The character congruence identity holds for **every** integer character by direct symbolic calculation; the finite enumeration is only a reproducible regression check. The universal eight-ray lower bound follows from the integral-character sparse-interval lemma and cyclic counting in `RESULT.md`, not from finite enumeration. The external Laface–Ugaglia 2026 Theorem 3 is explicitly used as an established mathematical premise. Independent validation is not claimed.
