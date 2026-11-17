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

The constructive proof in `RESULT.md` establishes the theorem for every integer \(n\ge1\) and \(k\ge3\). Two independent, directly executable enumerators corroborate different aspects.

Compile and run `verify_direct.cpp` with a C++17 compiler using `g++ -O3 -std=c++17 verify_direct.cpp -o verify_direct && ./verify_direct`; compare stdout to `verify_direct.txt`. This directly enumerates all \(k^n\) configurations for \(k=3\), \(1\le n\le10\); \(k=4\), \(1\le n\le8\); and \(k=5\), \(1\le n\le7\). It reconstructs the graph update without the suffix combinatorial recurrence, and checks the entire first-extinction histogram.

Run `python3 verify_suffix.py`; compare stdout to `verify_suffix.txt`. This separately computes excitation-time traces of suffix extensions for \(3\le k\le7\), \(1\le n\le7\), and checks their complete active-burst polynomials. The program also checks that every excitation trace is a consecutive initial interval.

All specified checks passed. A finite set of exhaustive tests cannot certify unrestricted \(n\) and \(k\); that conclusion relies on the proof of the triangular bijection and refractory-decay count. These checks do not provide independent scientific validation.
