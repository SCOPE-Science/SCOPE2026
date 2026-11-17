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

# Reproducibility and scope

Run `python3 verify.py` from the same directory as this document. The verifier uses only the Python standard library and computes exact integer squared-distance grades, so it has no floating-point threshold ambiguity. It enumerates all nonempty simplices on eight vertices, reduces simplicial boundaries over the two-element field to compute persistent intervals, and independently recomputes mod-two Betti numbers at each critical stage. It compares the outputs against the formulas for all ordered triples of integer squared side lengths from one through twelve, including equalities and \(C=A+B\).

The expected output is in `verify_output.txt`: 364 parameter triples, 2564 critical-stage checks, and the terminal marker `VERIFY_OK`. The source and output are supplied separately and must be compared against actual execution; the recorded output alone is not proof. The general correctness argument is the combinatorial face classification and integral cube-face boundary calculation in RESULT.md. These finite tests do not verify arbitrary real side lengths by enumeration.

Independent audit: not performed. No external validation is asserted.
