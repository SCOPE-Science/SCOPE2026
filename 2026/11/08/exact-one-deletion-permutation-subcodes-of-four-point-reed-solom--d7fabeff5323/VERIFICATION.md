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

The finite certificate is reproducible by running `python3 checker.py` and compiling `certificate.cpp` with a standard C++17 compiler using `-O2 -Wall -Wextra`. Both tools independently obtain progression/non-progression packing maxima \(6/7\) and maximizing-family counts \(14/2\). The Python program also constructs all \(49\) Reed–Solomon words for each of two representative evaluation sets, checks every pair of channel output sets, and verifies all maximizing constructions. The C++ program inspects all \(2^{21}+2^{14}\) possible triple subsets with exact incidence masks. These provide a finite exhaustive argument for \(\mathbb F_7\), not a general-field theorem.

Self-review: passed. Independent audit: not yet performed.
