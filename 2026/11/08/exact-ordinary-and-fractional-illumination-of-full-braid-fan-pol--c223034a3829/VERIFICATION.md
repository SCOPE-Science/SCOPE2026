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

# Reproduction and limits

Run `python3 braid_illumination_verifier.py` from the directory containing this file and the script. Actual output after execution was `BRAID_FAN_ILLUMINATION_EXACT_OK 1258632`.

The test enumerates all indexed vertices for \(2\le n\le8\), checks generic partial-sum incidence and explicit optimal partitions, checks selected nongeneric directions against the sharp ceiling, and separately constructs vertices and active subset facets of nonsymmetrically weighted complete-graph zonotopes for \(2\le n\le6\). All checks use exact integer arithmetic; randomized cases use a fixed deterministic seed.

No finite test certifies all dimensions, all real deformations, or every direction; those quantifiers are handled by the algebraic fan and cycle-minimum proof in `RESULT.md`. Only self-review has been performed. Independent auditing is unperformed.
