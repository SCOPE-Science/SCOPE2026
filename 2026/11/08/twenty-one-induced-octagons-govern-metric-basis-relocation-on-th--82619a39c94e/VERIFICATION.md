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

# Finite verification and limits

The graph is fully specified in the accompanying sources; no external data are required. Both programs ran from their accompanying source files and produced the included output files. The Python checker tests all 1,001 four-element sets, all 2,002 five-element sets, and all 3,003 eight-element sets; it verifies 168 resolving five-sets, 21 induced octagons, and precisely eight admissible word rotations per octagon with no overlap between octagons. It then compares all 14,028 unordered state pairs for one-token moves and performs breadth-first searches from all 168 states. The C++17 checker performs the same complete state and graph census using bitmasks and explicit 91-pair resolution constraints, without calling the Python implementation. The C++ checker independently verifies that the vertex unions of the 21 slide components are exactly the 21 induced octagons.

Run the commands in the verification section of RESULT.md from the artifact root. Reference standard outputs are in `verification/python_output.txt` and `verification/cpp_output.txt`. The verified assertions establish the finite exact classifications. They do not test a larger projective plane, and no claim of external or independent scholarly certification is made.
