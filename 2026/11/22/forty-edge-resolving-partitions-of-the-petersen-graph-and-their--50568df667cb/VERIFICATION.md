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

# Verification of the finite edge-partition theorem

The two independent standalone implementations compute the complete vector of edge-resolving partition counts for block counts one through ten, the reduced three-block obstruction, all minimum block-size profiles and symmetry-orbit transitivity. The C++17 implementation constructs the pair-Kneser model directly. The Python implementation independently constructs the generalized Petersen model and uses breadth-first distances. They agree on every claimed number.

From the artifact directory, run `g++ -std=c++17 -O2 check_kneser.cpp -o check_kneser && ./check_kneser` and `python3 check_gp.py`. The exact expected text is in `check_kneser.out` and `check_gp.out` respectively. A failed assertion terminates either program without the corresponding success marker. No downloaded graph tables, network access, or third-party libraries are required.

The finite search covers all \(B_{10}=115975\) unordered vertex partitions, not a partial sample. The highest-order computation is a finite enumeration, not an infinite-family extrapolation. A directly displayed four-block witness permits human recomputation of all fifteen edge signatures. No external independent mathematical audit has been performed.
