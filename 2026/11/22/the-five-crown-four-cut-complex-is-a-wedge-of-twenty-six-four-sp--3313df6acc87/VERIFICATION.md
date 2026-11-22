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

# Verification record

Run `python verify.py` using Python 3. The resulting JSON should equal `verify-output.json` apart from harmless representation ordering; both are generated deterministically by the supplied source. Graph adjacency is built directly from ten labels, all disconnected quadruples are independently enumerated and classified, all 80 cut facets and 697 nonempty cut faces are generated, and the full Hasse orientation is topologically sorted to certify that the 335-pair matching is acyclic.

The cut vector is \((10,45,120,210,232,80)\), with one critical zero-cell and 26 critical four-cells. The independent Alexander-dual calculation checks the dual definition on all \(2^{10}\) subsets and a 325-face matching with 149 pairs, giving one critical vertex and 26 critical three-cells. Counts are exhaustive for this finite example; no infinite extrapolation or independent third-party validation is implied.
