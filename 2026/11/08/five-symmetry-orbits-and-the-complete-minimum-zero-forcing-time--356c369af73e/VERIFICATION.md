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

# Reproducibility and verification

The two standalone programs embedded with this result require Python 3 (standard library only) and a C++17 compiler, respectively.

Run `python3 verify_prism_python.py` and `g++ -O2 -std=c++17 verify_prism_cpp.cpp -o verify_prism_cpp && ./verify_prism_cpp` from a directory containing the extracted source files.

The Python script constructs the cyclic-prism adjacency lists directly, tries every four-vertex subset for each \(5\le n\le18\), tests the exact dihedral-plus-ring-swap orbits, and verifies the complete time distribution. It prints `PYTHON_EXHAUSTIVE_PASS` on success. The C++17 program independently constructs adjacency bit masks and enumerates every four-vertex subset for \(5\le n\le25\), then checks the explicit arrival-time vectors up through \(n=300\) via a separate vertex-array implementation. It prints `CPP_EXHAUSTIVE_AND_ARRIVAL_PASS` on success.

These checks were run from the complete extracted delivered package files. All bounded-range checks passed, and both expected markers were observed. Exhaustion of finitely many small orders does not establish a theorem for every integer order; the RESULT proof supplies the symbolic classification. No independent external audit was performed.
