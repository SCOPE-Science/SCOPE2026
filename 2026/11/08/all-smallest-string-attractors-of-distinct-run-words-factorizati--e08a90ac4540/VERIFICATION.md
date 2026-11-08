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

# Verification protocol

Run `python3 verify.py` with Python 3 using the bundled standalone checker. The script enumerates every distinct contiguous factor and every occurrence, compares a selection's definition-level attractor status with the theorem's local boundary condition, and compares its count against the product formula. Its finite test domain consists of 339 run-length vectors with 2–5 runs, run lengths 1–3, and total length at most 12; it checks 6,786 selections. An additional 54 run-length-composition sums are compared with the closed coefficient formula (2–7 runs, word lengths from the number of runs through eight greater). The observed result was `PASS parameter vectors=339; direct minima=6786; global generating-function coefficients=54`.

The general theorem rests on the explicit lower bound, boundary uniqueness/sufficiency, endpoint-or-interior classification, and formal generating-function algebra in `RESULT.md`. Finite tests cannot establish correctness for all parameter values. No external independent audit has been conducted.
