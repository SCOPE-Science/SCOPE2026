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

# Verification instructions and limits

The standalone `verify.py` uses Python 3 and standard-library `math` only. Run `python3 verify.py` in this directory. It checks all sixteen finite alphabet rectangles up to size four on each shore, all inclusion-minimal failure sizes and six pattern labels; tests direct lax-split semantics on all rectangular teams with both dimensions at most three; and tests the full two-fiber binary rectangle. The final printed line is `VERIFY_OK 16 alphabet pairs; all 2x2x2 team subsets; raw split semantics through 3x3`.

The proof is a general finite combinatorial argument, rather than an extrapolation from the tested sizes. It depends on the classical matching–vertex-cover theorem for bipartite graphs. There is no external formal proof assistant or independent mathematical audit. The underlying first public source date for the subject is 22 August 2025 (arXiv:2508.16146v1); the source has also appeared in CSL 2026.
