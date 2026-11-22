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

The stand-alone `verify.py` uses only Python's standard library and requires no external datasets. Run `python3 verify.py`. It constructs direct maximal geodesics of the specified complete multipartite test graphs, exhaustively checks every edge subset, compares the transversal predicate to the per-block matching characterization, and compares complete degree distributions to the product formula. It also checks directly that all inclusion-minimal solutions have minimum size.

Observed `VERIFY_OK` on 2026-11-15 UTC. Profile checks: `(1,1)`, `(1,2)`, `(1,1,2)`, `(1,2,2)`, `(1,2,3)`, `(2,2)`, `(2,3)`, `(2,2,2)`, `(1,1,1,2)`. All 2-power edge-subsets of each listed graph were examined, up to 4096 subsets in the largest example. The general result is proved mathematically in RESULT.md and does not follow from finite tests alone. Independent mathematical audit has not been performed.
