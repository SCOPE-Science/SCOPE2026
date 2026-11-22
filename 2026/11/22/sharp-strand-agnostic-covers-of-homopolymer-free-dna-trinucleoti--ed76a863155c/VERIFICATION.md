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

Run `python3 verify_dp.py`, then compile and run `verify_dfs.cpp` with a C++17 compiler. The Python code constructs the 36-edge directed overlap graph, determines the 18 reverse-complement classes and eight quotient vertices, checks the degree-parity obstruction and both explicit witnesses, and uses exact integer recurrence counting. The independent C++ implementation performs depth-first traversal without memoization and checks every admissible optimal-structure trail through twenty windows. Its direct search examines 3,221,436 recursion nodes.

The verified numerical outputs are 57,984 distinct labeled shortest linear hosts; 289,920 rooted closed trails; 14,496 circular hosts up to rotation. Structural parity rules exclude any shorter complete host and prove which two orbit classes may be repeated; witness scans attain the bounds. The checks do not imply any higher-order or other-alphabet classification, nor any empirical biological binding property. They are finite verification, not independent expert audit.
