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

# Verification notes
The proof in RESULT.md establishes the infinite assertions; no finite enumeration is used as an infinite certificate. Run `python3 CHECK.py` using only the Python standard library. Its exact rational arithmetic checks the first five blocks of each of four representative nontrivial intervals, verifies the rounding brackets, and tests finite convergent examples, including endpoint densities. This confirms arithmetic examples but does not assert exhaustive verification of arbitrary real interval endpoints.

Source comparisons were performed against the publicly accessible full text of the 2026 countable-dynamics paper and the 2016/2018 Ellis-semigroup preprint, plus the authors' omega-limit paper and Sigmund's published abstract. The latter full text was not accessed; a priority risk remains for equivalent sparse-run historical constructions.
