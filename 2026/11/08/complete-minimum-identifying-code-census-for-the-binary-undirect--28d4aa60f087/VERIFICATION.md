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

Run `g++ -std=c++17 -O2 count_cpp.cpp -o count_cpp`, `./count_cpp > enumerated_masks.txt`, `python3 independent_verify.py`, and `diff -u optima_58.txt enumerated_masks.txt` from the directory containing these files.

The exact graph is built from all 32 length-five words, with symmetric shift-adjacency and closed neighborhoods. C++ constructs and inclusion-minimizes all 528 nonempty identifying-set constraints to 161, exhaustively excludes any identifying set of size at most 11, enumerates all 58 identifying sets of size 12, and verifies the stated four-element symmetry action. Python independently uses direct string-overlap edge tests and a different include/exclude branching recursion on the unreduced constraints. The two enumerations give identical sets. `orbits_16.tsv` is checked against the raw optimal masks, and each final codebook is tested against all 32 exact identifying signatures.

Results from package replay: `CXX_SIZE_11=0`, `CXX_SIZE_12=58`, `CXX_ORBITS_SIZE2=3`, `CXX_ORBITS_SIZE4=13`, `INDEPENDENT_EXACT_11=0`, `INDEPENDENT_EXACT_12=58`, `INDEPENDENT_COMPLETE_OK`; the final file diff is empty.

Scientific scope: this is an exhaustive finite statement solely for undirected binary word length five with radius-one closed neighborhoods. No claim is made for unexamined graph parameters, or for historical priority beyond the inspected sources. Independent audit is not yet performed.
