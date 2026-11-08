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

# Verification instructions and scope

The proof of the clique-number theorem appears in `RESULT.md`. The critical externally established premise is the published Type-A characterization of exactly two common one-deletion descendants, as cited there.

Run `python checker.py` with Python 3 and NetworkX installed. The script uses independent direct descendant-ball comparisons, enumerates all maximal cliques in the stated small cases, verifies the alternate interval description of adjacency, checks a sharp lower-bound construction, and checks the one/two-pencil classification for every maximal clique and every possible base word in those cases.

Completed ranges: alphabet size 2, lengths 2 through 9; alphabet size 3, lengths 2 through 6; alphabet size 4, lengths 2 through 4. Every reported check passed. No claim is made that these finite computations establish the infinite theorem. The mathematical proof relies on exact interval comparisons and an independent literature premise, not an enumeration extrapolation.
