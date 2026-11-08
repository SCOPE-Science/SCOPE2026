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

The finite verifier in `verify.py` was executed with Python 3 against its own source. It generated each literal binary necklace through length 15 by canonical cyclic rotation, deleted every possible input position, canonicalized each output rotation class, and computed the exact maximum. It checked the run upper bound on every source, explicit sharp constructions through length 300, and rotation invariance on additional samples.

Observed output: `VERIFY_OK necklace_classes=4807 exhaustive_n=1..15 witnesses_n=4..300`.

The proof of the universal statement is the cyclic-run classification and construction in `RESULT.md`, not an inference from finite testing. No externally independent proof audit has been performed. The result concerns exact-one-deletion support only.
