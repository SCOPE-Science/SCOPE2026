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

## Reproduction

Run `python3 proof/check_even_arcs.py`. The program generates complete even-cardinality arc sets for all even cycle sizes from four through eighteen, enumerates all query supports of sizes one through four, and compares each actual trace family with the theorem's face criterion. It also computes binary ranks of triangle-to-edge boundary matrices through fourteen vertices. Exact finite outputs are recorded in `proof/python_results.txt`.

Separately run `g++ -O2 -std=c++17 proof/check_even_arcs.cpp -o check_even_arcs && ./check_even_arcs`. This code independently enumerates hypothesis masks and traces for every support through size four for even cycle sizes four through twenty. Its output is in `proof/cpp_results.txt`.

The enumerations verify finite cases only. The characterization at arbitrary even order follows from the explicit interval-extension construction, and the integral homotopy type from disk fillings of all omitted triangular faces, elementary homology, and the homological Whitehead theorem. A mod-two rank check cannot by itself prove integral torsion-freeness or simple connectivity.
