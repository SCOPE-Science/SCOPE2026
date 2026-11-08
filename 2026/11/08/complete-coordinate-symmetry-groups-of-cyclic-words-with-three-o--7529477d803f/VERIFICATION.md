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

The exact theorem covers positive integer run lengths, at least three distinct run letters, and lengths at least the primitive period. The argument in `RESULT.md` recovers the actual congruence blocks from the full factor set; reconstructs the cyclic graph from co-occurrences in translates of a nontrivial run interval; excludes reflection using the cyclic order of at least three distinct labels; and counts the multiplicity-preserving rotations. These are the critical infinite proof steps.

Reproduction: place `verify.py` in the working directory and run `python3 verify.py`. The successful output is `VERIFY_OK configurations=382; two-colour boundary=8 versus 4`. The checker enumerates all coordinate permutations for each of 382 test cases and constructs the true factor orbit directly. Its exhaustive scope is bounded by length eight. These tests do not certify all infinitely many lengths or run parameters.

The independent audit channel is not performed. No formal proof-assistant certification is claimed. The literature comparison remains subject to possibly unindexed equivalent results.
