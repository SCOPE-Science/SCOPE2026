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

The standalone `verify.py` uses only the Python standard library. Run it from its directory with `python3 verify.py`; its reference output is `verification_output.txt`.

The program independently enumerates all vertex subsets, uses union–find to check for graph cycles, and computes reduced simplicial Betti numbers by reconstructing all mod-two boundary matrices. It checks every triple of integers \(2\le p\le q\le6\), \(0\le t\le p\), for 65 test instances, and independently checks relative three- and four-simplex counts. It processed 20,934 forest faces. A separate signed six-by-six block check directly reconstructs the three-missing-index boundary, locates a determinant-one five-by-five minor, and verifies its signed six-facet kernel relation. All checks passed.

These finite data are not exhaustive for arbitrary shore sizes. The integral all-parameter homotopy statement depends on the exact face classification, the primitive integral block argument, and the connecting-map basis in `RESULT.md`; no infinite computational certification or independent external assessment is claimed.
