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

# Reproduction and limits

Run `python verification/verify.py` from the directory containing these files. The script is standalone and uses only the Python 3 standard library.

The recorded output in `verification/run_output.txt` was regenerated from the exact embedded verifier prior to packaging. It includes all eleven quotient conjugacy classes and ends with `ALL_VERIFY_OK`.

Checks reconstruct all \(12\) initial vertices, \(36\) edges, \(24\) faces, all \(216\) barycentric edges and \(144\) barycentric triangles, and exactly \(30\) subgroups and \(11\) conjugacy classes. For every quotient vertex the link was checked to be exactly one path or one circle, and for every boundary orbit the boundary graph was checked to be a union of simple circles. Every group element's effect on the signed integral fundamental cycle was verified. The complete finite group search has no untested subgroup parameter.

The inferred homeomorphism types additionally use the standard classification theorem for compact connected surfaces. Executable checks are not a substitute for that theorem. The assertion has not been independently audited; no result on all chessboard sizes or on row-and-column permutations is claimed.
