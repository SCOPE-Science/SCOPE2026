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

# Reproducible finite verification

The package contains `check_chvatal.py` and `check_chvatal.cpp`, each independently implementing a full state-space computation for the same mathematically defined local update. Their recorded stdout files are `python_output.txt` and `cpp_output.txt`.

Run `python3 check_chvatal.py` and `g++ -std=c++17 -O2 check_chvatal.cpp -o check_chvatal && ./check_chvatal`.

Both enumerate exactly 4096 binary states for the original Chvátal graph and for each of its 24 edge deletions. Every state is assigned an eventual least period (checked to be one or two), entrance time, and terminal recurrent component. Python uses path chasing and independently determines all eight automorphisms; C++ uses indegree peeling and reverse propagation. The five single-edge-deletion classes occur with exact multiplicities 4,8,4,4,4.

The finite calculation is exhaustive for its stated twelve-vertex domain; it does not imply any untested network size or local rule. The source codes, not merely the captured output logs, are the proof artifacts. No independent audit has been performed.
