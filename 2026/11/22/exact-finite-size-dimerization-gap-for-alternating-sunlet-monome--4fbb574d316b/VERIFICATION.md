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

The proof derives the weighted matching polynomial through the cycle-phase determinant and an exact two-step Chebyshev trace. The distinct-root argument, ordered band boundaries, and finite-size gap equation are algebraic identities for all stated lengths and positive weights.

`verify.py` performs independent vertex-mask matching enumeration, exact polynomial comparison for twelve parameter instances (including rational weights), exact magnetic determinants in two cases, and numerical gap checks for six additional lengths. Run with `python verify.py` and SymPy installed. These finite tests supplement rather than replace the proof. Historical-priority checks are not exhaustive; the full Mandal (2008) article was not available for inspection.
