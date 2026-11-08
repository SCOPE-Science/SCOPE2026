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

# Reproduction and limits

From a directory containing the four standalone artifacts, run `python3 verify.py`. GNU `g++` with C++17 support and SymPy are needed. The script independently computes the full matching polynomial using a vertex-deletion recursion; compiles `morse_certificate.cpp`; checks its complete reversed-Hasse DAG topological sort; compares the replayed oriented integral Morse boundary to `morse_boundary.txt` byte-for-byte; verifies the 34 unit Smith invariant factors over the integers; and checks Euler characteristic. The run matches `verification_output.txt`. No finite-field calculation is substituted for integral homotopy proof.

The computation enumerates precisely 1,157,484 faces, including the empty face, and checks 8,344,008 codimension-one incidences. Integer overflow checks protect the integral accumulation. The proof uses the established discrete-Morse homotopy theorem and homotopy classification of attaching maps in the specific adjacent dimensions. Independent audit is not performed.
