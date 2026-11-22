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

The included `steiner_rectangle_check.py` is standalone and replays exact SymPy integration of the two fiber cases, simplification to the claimed formula, the square reduction and the sharp derivative calculation. It also performs numerical integration independently by intersection of rotated rectangle edges with horizontal fibers. Recorded output: `PASS: 89 exact identities and independently integrated numerical assertions`.

The mathematical proof covers all positive rectangle half-side lengths and all unoriented axes via an analytic first-branch calculation, symmetry, and continuity; numerical tests alone would not establish these quantifiers. It does not verify an external independent audit, nor exhaustively certify priority across inaccessible publications. Requires Python, SymPy and SciPy.
