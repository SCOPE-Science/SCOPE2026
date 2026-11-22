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

# Reproduction and verification
Run `python verify_enriched_bipartite.py` with Python 3 and SymPy available. It must exit successfully with `ALL CHECKS PASSED` after enumerating the six listed bipartite sizes and their orbit-cell boundary complexes. It verifies exact integer composition of consecutive boundary maps and independent ranks over two prime fields, including the full part-exchange quotient for balanced sizes. It does not calculate Smith normal forms for all sizes or prove a uniform result by enumeration. The complete proof, including the integral homotopy type and the geometric quotient homotopy types, is in `RESULT.md`.

Independent mathematical audit has not been performed. No assessment of independent validation is asserted.
