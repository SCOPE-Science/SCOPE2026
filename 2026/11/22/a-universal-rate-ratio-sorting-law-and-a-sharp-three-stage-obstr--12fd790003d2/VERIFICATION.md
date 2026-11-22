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

# Reproducibility and exact-proof scope

Run `python verify.py` from the extracted directory (Python standard library only). The deterministic test reports 46,171 passing assertions, including exact rational two- and three-transition results, stochastic numerical examples, and arbitrary-prefix/suffix interchange tests. No random data are required to reconstruct the closed forms; a fixed seed makes the auxiliary tests reproducible.

The infinite/all-parameter assertion is supported by the algebraic interchange identity and strict positivity of its factors, not by exhaustive finite tests. The three-transition result is a constructive nonexistence claim about a context-independent local pair-ordering preference; the exact fraction calculation is a complete proof of that example. No general biological performance claim or independent verification is asserted.
