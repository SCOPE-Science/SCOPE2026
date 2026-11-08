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
# Reproducibility

Use the accompanying standard-library Python 3 program `verify.py` and run `python3 verify.py` in the extracted package directory. A successful run must finish with `ALL_VERIFY_OK`. The expected output, recorded from the supplied program, is embedded in `verify_output.txt`.

The program independently enumerates graph perfect matchings for \(n=4,6,8,10,12,14\), and exhaustively enumerates **all faces** for \(n=4,6,8,10\). For those four widths it separately enumerates independent sets of the forbidden-pair graph and compares complete face sets, and calculates every group-element signed reduced Lefschetz trace directly from the action on simplicial faces. For all six widths it enumerates the reflection edge-orbits, constructs the quotient incompatibility graph, checks the false-twin deletions and path of triangles, and checks the two generator rotation traces. A full face enumeration is **not** claimed for the two largest widths. The complete finite calculations are not an infinite proof: the universal orbit partition and alternating-cover cancellation are given in `RESULT.md`, and the homology concentration is an explicit published input. No external auditor or independent validation is claimed.
