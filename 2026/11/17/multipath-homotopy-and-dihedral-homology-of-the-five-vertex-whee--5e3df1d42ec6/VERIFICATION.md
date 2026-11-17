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

# Reproduction

Use the exact files `verify_wheel.py` and `verification_output.txt` in this package. Run `python3 verify_wheel.py`; the script uses only Python 3 standard-library modules. It reconstructs the complete complex, verifies the 704 incidence DAG, checks the integer Morse differential and full rational group characters, and checks mod-two boundary ranks from scratch. The recorded output should end in `WHEEL_MULTIPATH_EXACT_PASS`.

The graph is finite (5 original vertices, 16 arcs). The proof is an exhaustive finite certificate plus the stated standard topological implications; its group-action conclusion is over rational coefficients. Checks of arbitrary larger wheels, all orientations, or an integral equivariant splitting have not been performed. The report is not an independent audit.
