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

# Reproducibility of the finite classification

From a directory containing the two source files, run `g++ -O2 -std=c++17 verify_paley49.cpp -o verify_paley49 && ./verify_paley49` and then `python3 verify_paley49.py`. No third-party data, graph packages, online services, or numerical rounding are required. The C++ program reconstructs all 24 squares and every zero-containing queried support up to size five. The Python program uses the independent norm-character criterion, computes every zero-containing shattered four/five-support, partitions the five-supports into the two explicit symmetry orbits, and tests all fifth-vertex extensions from each shattered four-support.

Observed terminal markers: `EXHAUSTIVE_SQUARE_ENUMERATION_CHECKS_PASS` and `INDEPENDENT_NORM_ORBIT_CHECKS_PASS`. Program assertions cover the full accepted numbers; source-file byte hashes are recorded in the containing package. These are finite exhaustive verifications, not a general proof for other field orders or an external independent audit.
