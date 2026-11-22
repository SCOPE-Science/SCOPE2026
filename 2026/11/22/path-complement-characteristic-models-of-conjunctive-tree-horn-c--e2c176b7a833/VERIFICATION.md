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

# Reproducibility

Run `python verify.py` with Python 3.9 or later. The script has no third-party dependencies and uses Prüfer codes to generate all labelled trees with orders one through seven, rooting every tree at vertex zero. It tests closed sets by the exact rule semantics and separately enumerates their meet-irreducibles from the finite inclusion poset, then compares with ancestor-to-leaf path complements. It tests the extremal inequalities as well.

Observed output concludes with:

`VERIFY_OK tree_instances=18249 subset_tests=2238526 maximizers=66`

Each count is an actually executed check. The finite enumeration is not the proof of the infinite theorem. The all-size argument is explicit in RESULT.md, including the unique-cover lemma, closedness under omitted paths, size polynomial and extremal equality conditions.

The scientific literature comparison relies on inspected HTML or abstracts and semantic search, not on a certified complete historical corpus. No independent validation has taken place.
