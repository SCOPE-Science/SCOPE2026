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

# Computational verification and limits

Run `python3 verify.py` using Python 3.10 or later. The file is complete and uses only the standard library. It reconstructs exactly all feasible colored cycle-independent-set vertices and, in odd cycles, all feasible half-integral vertices. All coordinates are multiplied by two so each pairwise squared distance is computed as an integer without floating-point error. In sixteen direct cases with \(4\le m\le9\), \(1\le a\le3\), and at most 1,500 vertices each, the script checked 973,988 unordered exact squared distances and compared their maximum and multiplicity with the asserted formulas. A separate independent-set overlap enumeration gives 111 additional parameter checks over \(4\le m\le22\) and \(1\le a\le5\).

The software tests mathematical consequences; it cannot prove the infinite classification or global historical novelty. The all-parameter proof is in `RESULT.md`. The earlier full-text sources used to establish distinctions concern an Ehrhart theorem and a minimum-sphere theorem, not the stated Euclidean pair enumeration. The proof and finite computations have received self-review only; independent audit is not performed.
