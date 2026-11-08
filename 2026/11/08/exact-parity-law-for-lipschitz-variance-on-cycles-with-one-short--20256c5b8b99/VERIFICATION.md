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
# Reproducible verification

Run `python3 verify.py` from the extracted file directory, using Python 3 and no third-party packages. The script enumerates the vertices of the weighted cycle increment section, computes centered variance by exact fractions, and checks the closed forms for orders three to ten with four rational edge lengths. It also checks reflection distance-kernel inequalities for orders three through thirty. Its expected final marker is `ALL_ONE_SHORT_EDGE_CYCLE_TESTS_OK`.

The main proof, not finite enumeration, establishes the all-order, all-real-parameter statement. The critical circular rearrangement argument is supplied in `RESULT.md`; the code does not certify the infinitely many instances of that argument. The literature comparison supports a self-review, not an independent priority guarantee. No independent audit has been performed.
