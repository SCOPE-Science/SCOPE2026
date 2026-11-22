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

# Reproducibility and finite checks

Run `python3 verify.py` with Python 3.9 or later; it uses the standard library only. The script independently enumerates every undirected loopless labelled graph for each order one through seven by flipping edges along a Gray code, records its exact degree-one vertex set, and runs the full Walsh–Hadamard transform of the profile histogram. It compares all character values to the closed exact formula. It checks the full weight spectrum at order eight and checks the finite inequalities and spectral minimizers used in the written proof.

The executed script printed:

`PASS: 591 exact assertions; direct graph enumeration through n=7; full small-order spectrum through n=8; all-order bounds proved in RESULT.md`

The all-order positivity, strict ordering, sharp condition bound and asymptotic are proved with explicit inequalities in `RESULT.md`; numeric tests through finite orders are not presented as infinite certification. The historical priority search has bounded coverage, and no independent evaluation has been performed.
