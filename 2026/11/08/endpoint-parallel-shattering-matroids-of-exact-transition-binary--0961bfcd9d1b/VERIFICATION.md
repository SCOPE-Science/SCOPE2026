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

# Verification and reproducibility

From the directory containing the standalone files, run `python check_exact_switches.py`. It uses only the Python standard library. It enumerates every binary word of length from two through eleven and all switch counts, then tests every possible coordinate support by direct trace enumeration against the claimed criterion. It also checks the complete coefficients and the class size. Finally, independent recursive version-space calculations compute the Littlestone dimension for lengths two through nine and check the proved lower and upper bounds. The captured stdout is in `check_output.txt`.

A successful replay prints `EXACT_SWITCH_SHATTERING_PASS` and reports 40,960 checked support instances. This is finite corroboration only. The unrestricted proof is given in `RESULT.md`, including parity restrictions, integer-interval completion, and the transition-block lower bound. No independent mathematical audit has been performed.
