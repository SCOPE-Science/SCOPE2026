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

# Verification scope
The companion `verify.py` uses only the Python 3 standard library. It independently generates every shortest path by breadth-first search, filters extendable subpaths, and tests the labelled forbidden-face condition for every vertex subset. It compares maximal-geodesic families, the maximal-face enumerator, and mod-two reduced homology.

Execution: `python3 verify.py`

Observed result: `VERIFY_OK profiles=102 masks=37656 maximal_geodesics=PASS minimal_transversals=PASS face_complex=PASS mod2_homology=PASS`.

The finite computation covers 102 parameter profiles and does not prove integral homotopy or the infinite family; the mathematical proof in `RESULT.md` establishes both. The package has undergone self-review only; no independent audit was performed.
