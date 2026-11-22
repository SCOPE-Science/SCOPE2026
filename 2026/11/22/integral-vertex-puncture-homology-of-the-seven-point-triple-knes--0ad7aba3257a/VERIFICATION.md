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

Run `python3 MORSE_CHECK.py` with Python 3 supporting integer `bit_count`. It uses only the standard library and rebuilds every face and matching from explicit definitions. Compare stdout with `EXPECTED.txt` exactly, including a final newline.

The verifier checks all 35 graph vertices, all nonempty faces, all critical cells, disjointness of every matching pair, and the absence of directed cycles in the full discrete-Morse orientation. It does not calculate higher homotopy attaching maps, use numerical floating-point ranks, extrapolate to other graph parameters, or constitute an independent mathematical audit.
