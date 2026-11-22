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

# Verification of the rank-one matrix anti–Rota–Baxter census

The package contains the complete standalone `verify.py`, requiring Python 3.11 or later and no external dependencies. Run `python verify.py` from the extracted package directory. This checker compares the original, bilinear anti–Rota–Baxter identity on all matrix units (rather than assuming the normal-form reduction), then verifies the resulting distinct operator counts.

Successful recorded execution printed:

```
EXHAUSTIVE 2 2 nonzero= 15 squarezero_image= 3 idempotent_image= 12 R2_nonzero= 0 idempotent_operator= 0
EXHAUSTIVE 2 3 nonzero= 112 squarezero_image= 8 idempotent_image= 104 R2_nonzero= 78 idempotent_operator= 39
EXHAUSTIVE 2 5 nonzero= 24 squarezero_image= 24 idempotent_image= 0 R2_nonzero= 0 idempotent_operator= 0
DIRECT_ALL_CANONICAL 3 2 total= 651 squarezero_image= 315 idempotent_image= 336
ANTI_ROTA_BAXTER_MATRIX_VERIFIED
```

The three dimension-two cases exhaust all matrix pairs and quotient duplicate linear operators. Dimension three checks the defining identity for every canonical normal-form factor pair; this does not exhaust all possible factor pairs outside the classification. In particular, the verification does not replace the general symbolic proof or resolve historical priority. No independent audit has been performed.
