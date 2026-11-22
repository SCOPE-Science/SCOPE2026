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

# Finite replay instructions

With Python 3.10 or later, run `python3 verify.py` in the directory containing `certificates.json`. It recomputes the complete set of `11`-avoiding words for every length 1 through 16, filters precisely the self-bordered words, tests all candidate pairs by string slicing and independently by integer masking, executes a complete colored maximum-clique search, verifies the matching witness codebooks, and rechecks the restricted Chee--Levenshtein marker family. The successful ending is `VERIFY_OK`.

The largest case contains 2584 source words, 410 unbordered candidates, a maximum clique of 42, and 308053 visited recursive nodes. Length 15 has maximum 30. No random seeds, external data, floating-point optimization, unverified oracle, or external certificate channel is involved. The proof of search completeness appears under **Proof** in RESULT.md and in the commented branch-and-bound implementation.

Limits: these are exact finite computations for the stated orders, not statements about all lengths. No independent audit was performed.
