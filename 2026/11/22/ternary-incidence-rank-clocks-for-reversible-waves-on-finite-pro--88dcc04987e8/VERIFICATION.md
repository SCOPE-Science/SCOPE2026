---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification of the characteristic-three projective-plane wave for plane orders divisible by three

Run `python3 verify_planes.py` (requires NumPy) or `python3 verify_affine.py` (standard library) from the package directory. Both programs include an exact calculation for the Desarguesian example of plane order \(3\), with \(v=13\) and ternary incidence rank \(7\). The homogeneous checker calculates modular ranks of the whole wave matrix. The affine checker iterates the two-level update on each basis vector using different incidence coordinates and modular elimination. At times \(1,2,3,4,6,12\) the recorded fixed-space dimensions are \(1,2,2,26,4,52\), respectively. Their other checked orders are comparisons outside the finding's scope.

This is a basis/rank computation, not enumeration of all states. The universal result follows from the proof in `RESULT.md`, in particular the square-zero identity on the sum-zero shores and the rank of the fourth-iterate defect. The finite calculations do not settle historical priority.
