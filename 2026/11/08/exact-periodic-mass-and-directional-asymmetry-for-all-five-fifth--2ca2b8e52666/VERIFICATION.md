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

# Verification of the exact fifth-rotation classification

Run `python3 certificate5.py`. All first-return transitions are exact integers on the forty-cell partition and all omitted cycles are enumerated exhaustively. The induction uses the exact identity `a(7/8+u/8)=a(u)/8` on the tail, so no floating-point approximation or finite-orbit enumeration serves as an infinite proof. The rational test section only double-checks the induced maps at interior samples. The result has not received independent mathematical audit.
