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
# Verification

Run `python3 verify_surjection.py` using Python 3, with no third-party dependencies.

The verifier enumerates **every** candidate query support for eight pairs `(n,q)`: `(2,2)`, `(3,2)`, `(3,3)`, `(4,2)`, `(4,3)`, `(4,4)`, `(5,2)`, `(5,3)`. It computes graph-incidence traces by enumerating all onto maps, checks the proposed shattering criterion, independently computes Stirling face counts, and checks facet size and count. Total examined: **104,272** candidate supports, including supports with more than one queried edge per row; **1,442** were shattered. Fifteen explicit exchange counterexamples across `3<=q<=5` and `q<=n<=8` were also checked (including the q=n boundary, as finite corroboration only).

Expected completion marker: `SURJECTION_SUPPORT_CLASSIFICATION_PASS 8 104272 1442 nonmatroid_witness_pairs 15`.

Finite enumeration cannot establish the unrestricted result; the complete proof in `RESULT.md` supplies quantifiers and critical Hall-completion reasoning. The executable never accesses external services or unprovided files. Independent external mathematical validation has not been performed.
