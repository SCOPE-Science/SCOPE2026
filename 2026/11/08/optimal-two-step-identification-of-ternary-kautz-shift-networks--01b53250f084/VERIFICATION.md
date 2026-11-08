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

The proof is mathematical and all-length; `VERIFY.py` is a separate finite cross-check, not an infinite certificate. Run with `python3 VERIFY.py` (Python 3 standard library only). The program enumerates graph vertices, directed predecessor balls and signatures; checks the claimed sensor count, coverage, separation and decoding for every vertex at lengths 3 through 11; checks sibling difference conditions through length 7; and exhibits the indistinguishable radius-two balls at length 2. Its required ending is `VERIFY_OK`. There is no claim of machine checking beyond these finite lengths.
