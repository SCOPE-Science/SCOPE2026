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
Run `python3 verify.py` in the same directory as the paper. The script uses exact rational arithmetic and no third-party packages. It checked 50 pairs of graph-side sizes and 74,142 positive-valued proper coalitions, and additionally reconstructed coalitional matching numbers via an independent recursion for graphs with at most ten vertices. It checks efficiency, nonnegativity, exact first-stage ratio, the second-stage positive-gap threshold on core cases, and core/noncore boundaries. The proof, not the finite tests, establishes the theorem for every admissible pair of side sizes.

The prior-work comparison considered the October 2026 full-text definition and generic algorithm; the 1995 abstract confirms a generic earlier algorithm, but its full text was not inspected. No independent audit has been conducted.
