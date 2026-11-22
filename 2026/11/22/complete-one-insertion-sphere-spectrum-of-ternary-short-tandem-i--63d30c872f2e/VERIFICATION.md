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

Run `python3 verify_insertion.py` with Python 3 and no third-party packages. The program counts legal one-symbol inserted output words directly over the ternary alphabet, independently evaluates the difference-sign run formula and the composition-polynomial coefficients, then compares both counts and full support for each length \(3\le n\le12\). It separately checks the sharp minimum/maximum and their labeled multiplicities.

This verification enumerates finite test lengths only; the proof for all \(n\ge3\) is in RESULT.md. The proof's critical fact is that a legal interior insertion replaces one ternary difference sign by two copies of its opposite, and its only possible new alternating triples occur beside that pair. All relevant logical cases are enumerated in the proof. No external correctness or priority audit has been performed.
