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

# Exact arithmetic verification

Use `python3 verify_ie.py` and compile `verify_direct.cpp` with `g++ -std=c++17 -O2 verify_direct.cpp -o verify_direct && ./verify_direct` in this directory. Both commands were executed successfully on the actual packaged source files before delivery.

`verify_ie.py` starts from the inclusion-exclusion formula over all ten triangles of the labelled five-vertex complete graph and enumerates every one of the 1024 frequency masks. It tests the 34 representative-orbit rows of `orbit_table.tsv`, all 120 relabellings, the three zero orbits, Parseval, and the sharp Fourier range-projection norm.

`verify_direct.cpp` independently enumerates every graph on three, four, five and six vertices and builds the triangle-free truth table. A direct Walsh–Hadamard transform checks the full 21-level signed spectrum, 150 five-vertex zeros, support-size distribution, exact rank, spectral gap, Parseval, and the 7924/1024 projection norm. All arithmetic is integral.

The two programs' coefficient methods are independent, but their validation and present scientific review are not an external mathematical audit. In particular, exhaustive verification applies only to the finite sizes listed. Historical priority is only supported by bounded literature comparison.
